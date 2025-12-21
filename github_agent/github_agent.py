import os

from agency_swarm import Agent
from agency_swarm.mcp import MCPServerOAuth


github = MCPServerOAuth(
    url=os.getenv("GITHUB_MCP_URL", "http://localhost:8001/mcp"),
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


