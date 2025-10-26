from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm  # Step 2에서만 필요
from .config import MODEL_GEMINI_2_0_FLASH, MODEL_GPT_4O, MODEL_CLAUDE_SONNET
from .tools import get_weather, get_weather_stateful, say_hello, say_goodbye

# Step 1: 단일 날씨 에이전트
def make_weather_agent_basic():
    return Agent(
        name="weather_agent_v1",
        model=MODEL_GEMINI_2_0_FLASH,
        description="Provides weather information for a city.",
        instruction=(
            "You are a helpful weather assistant. Use the 'get_weather' tool for city weather requests. "
            "Carefully read the tool's dictionary output."
        ),
        tools=[get_weather],
    )

# Step 2 (옵션): 다른 모델(LiteLLM) 버전
def make_weather_agent_gpt():
    return Agent(
        name="weather_agent_gpt",
        model=LiteLlm(model=MODEL_GPT_4O),
        description="Weather agent using GPT.",
        instruction="Use 'get_weather'. Output clear Korean or English as appropriate.",
        tools=[get_weather],
    )

def make_weather_agent_claude():
    return Agent(
        name="weather_agent_claude",
        model=LiteLlm(model=MODEL_CLAUDE_SONNET),
        description="Weather agent using Claude Sonnet.",
        instruction="Use 'get_weather'.",
        tools=[get_weather],
    )

# Step 3: 팀 구성(인사/작별 하위 에이전트 + 루트)
def make_greeting_agent():
    return Agent(
        model=MODEL_GEMINI_2_0_FLASH,
        name="greeting_agent",
        instruction="Your ONLY task is to greet the user using 'say_hello'.",
        description="Handles simple greetings via 'say_hello'.",
        tools=[say_hello],
    )

def make_farewell_agent():
    return Agent(
        model=MODEL_GEMINI_2_0_FLASH,
        name="farewell_agent",
        instruction="Your ONLY task is to say goodbye using 'say_goodbye'.",
        description="Handles simple farewells via 'say_goodbye'.",
        tools=[say_goodbye],
    )

def make_root_agent_v2_with_subagents():
    greeting = make_greeting_agent()
    farewell = make_farewell_agent()
    return Agent(
        name="weather_agent_v2",
        model=MODEL_GEMINI_2_0_FLASH,
        description="Coordinator: weather + delegates greetings & farewells.",
        instruction=(
            "Provide weather via 'get_weather'. "
            "Delegate greetings to 'greeting_agent' and farewells to 'farewell_agent'. "
            "Handle only weather, greetings, and farewells."
        ),
        tools=[get_weather],
        sub_agents=[greeting, farewell],
    )

# Step 4: state + output_key
def make_root_agent_v4_stateful():
    greeting = make_greeting_agent()
    farewell = make_farewell_agent()
    return Agent(
        name="weather_agent_v4_stateful",
        model=MODEL_GEMINI_2_0_FLASH,
        description="State-aware main agent.",
        instruction=(
            "Provide weather using 'get_weather_stateful' (respect user's temperature unit in state). "
            "Delegate greetings/farewells appropriately."
        ),
        tools=[get_weather_stateful],
        sub_agents=[greeting, farewell],
        output_key="last_weather_report",
    )
