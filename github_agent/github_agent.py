import os

from agency_swarm import Agent
from agency_swarm.mcp import MCPServerOAuth

GITHUB_MCP_URL = os.getenv("GITHUB_MCP_URL", "http://localhost:8001/mcp")
GITHUB_MCP_URL_SOURCE = "env" if os.getenv("GITHUB_MCP_URL") else "default"

github = MCPServerOAuth(
    url=GITHUB_MCP_URL,
    name="github",
    scopes=["repo", "user"],
)

github_agent = Agent(
    name="GitHubAgent",
    description="Helps with GitHub repositories using OAuth-enabled MCP tools.",
    instructions="./instructions.md",
    files_folder="./files",
    tools_folder="./tools",
    mcp_servers=[github],
    model="gpt-5.2",
)

