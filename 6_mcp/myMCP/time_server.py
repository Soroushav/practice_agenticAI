from datetime import datetime
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="time_server")

@mcp.tool()
async def get_time():
    """
        give the current time of the user
    """
    current_time = datetime.now().strftime("%H:%M:%S")
    return current_time


if __name__ == '__main__':
    mcp.run(transport='stdio')