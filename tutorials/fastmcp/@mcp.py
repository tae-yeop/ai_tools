from fastmcp import FastMCP

mcp = FastMCP("Simple Calculator MCP Server")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@mcp.tool
def subtract(a: int, b: int) -> int:
    """Subtract the second number from the first."""
    return a - b

if __name__ == "__main__":
    mcp.run()
