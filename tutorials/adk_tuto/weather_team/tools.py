from typing import Dict
from google.adk.tools.tool_context import ToolContext

def get_weather(city: str) -> Dict:
    """특정 도시의 날씨 리포트를 반환(모의 데이터).
    Args:
      city (str): 도시 이름
    Returns:
      dict: {"status": "success", "report": "..."} 또는 {"status": "error", "error_message": "..."}
    """
    db = {
        "new york": ("New York", "sunny", 25),   # °C
        "london":   ("London", "cloudy", 15),
        "tokyo":    ("Tokyo", "light rain", 18),
    }
    key = city.strip().lower()
    if key in db:
        name, cond, t = db[key]
        return {"status":"success", "report": f"The weather in {name} is {cond} with a temperature of {t}°C."}
    return {"status":"error", "error_message": f"Sorry, I don't have weather information for '{city}'."}

# Step 4: state-aware 버전(섭씨/화씨 선호 반영 + state 기록)
def get_weather_stateful(city: str, tool_context: ToolContext) -> Dict:
    """세션 state에 저장된 온도 단위 선호를 반영해 리포트 생성, 마지막 조회 도시를 state에 기록."""
    unit = tool_context.state.get("user_preference_temperature_unit", "Celsius")
    base = get_weather(city)
    if base.get("status") != "success":
        return base

    # mock 리포트 문장 재구성
    report = base["report"]
    # 단순 파싱(데모 용)
    import re
    m = re.search(r"temperature of (\d+)°C", report)
    if m:
        c = int(m.group(1))
        if unit.lower().startswith("f"):
            f = round(c * 9/5 + 32)
            report = report.replace(f"{c}°C", f"{f}°F")
    tool_context.state["last_city_checked_stateful"] = city
    return {"status":"success", "report": report}

# Step 3: 인사/작별 도구
def say_hello(name: str = "") -> Dict:
    msg = f"Hello{', ' + name if name else ''}! 👋"
    return {"status": "success", "report": msg}

def say_goodbye() -> Dict:
    return {"status": "success", "report": "Goodbye! 👋"}
