import os
from dotenv import load_dotenv

# .env 로드 (adk web/cli를 안 쓰고, 순수 python 실행 시 편의용)
load_dotenv(override=False)


# 모델 상수 (튜토리얼 기본값)
MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash"

# (옵션) LiteLLM 모델 별칭
MODEL_GPT_4O = "openai/gpt-4.1"
MODEL_CLAUDE_SONNET = "anthropic/claude-sonnet-4-20250514"
