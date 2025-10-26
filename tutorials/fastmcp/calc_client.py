import asyncio
from fastmcp import Client

async def calculate():
    client = Client("/home/tyk/ai_tools/@mcp.py")
    async with client:
        result = await client.call_tool("add", {"a": 999, "b": 999})
        print(f"999 + 999 = {result}")

asyncio.run(calculate())
