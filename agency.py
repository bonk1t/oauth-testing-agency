import logging

from dotenv import load_dotenv
from agency_swarm import Agency

from github_agent import GITHUB_MCP_URL, GITHUB_MCP_URL_SOURCE, github_agent

logger = logging.getLogger(__name__)

load_dotenv()

# do not remove this method, it is used in the main.py file to deploy the agency (it has to be a method)
def create_agency(load_threads_callback=None):
    logger.info("Resolved GITHUB_MCP_URL (%s): %s", GITHUB_MCP_URL_SOURCE, GITHUB_MCP_URL)

    agency = Agency(
        github_agent,
        name="OAuthAgency",
        shared_instructions="shared_instructions.md",
        load_threads_callback=load_threads_callback,
        oauth_token_path="./data/oauth-tokens",
    )

    return agency

if __name__ == "__main__":
    agency = create_agency()

    # run in terminal
    agency.terminal_demo()
