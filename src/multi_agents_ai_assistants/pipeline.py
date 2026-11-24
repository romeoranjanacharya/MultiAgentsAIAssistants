"""Coordinate the research and writing agents."""

from .agents import ResearchAgent, WritingAgent
from .models import DocumentResult


class AgentPipeline:
    """Run research, then pass the result to a writing agent."""

    def __init__(self, research_agent: ResearchAgent, writing_agent: WritingAgent):
        self.research_agent = research_agent
        self.writing_agent = writing_agent

    def run(self, topic: str) -> DocumentResult:
        research = self.research_agent.research(topic)
        return self.writing_agent.write(research)
