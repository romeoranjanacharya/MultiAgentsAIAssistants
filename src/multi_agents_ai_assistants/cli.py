"""Command-line interface for the starter multi-agent workflow."""

import argparse

from .agents import StarterResearchAgent, StarterWritingAgent
from .pipeline import AgentPipeline


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Run a research-and-writing multi-agent workflow"
    )
    parser.add_argument("topic", help="Topic for the agents to process")
    args = parser.parse_args(argv)

    pipeline = AgentPipeline(StarterResearchAgent(), StarterWritingAgent())
    print(pipeline.run(args.topic).content)
    return 0
