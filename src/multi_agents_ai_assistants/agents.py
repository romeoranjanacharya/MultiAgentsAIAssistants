"""Research and writing agent interfaces with runnable starter implementations."""

from abc import ABC, abstractmethod

from .models import DocumentResult, ResearchResult


class ResearchAgent(ABC):
    """An agent that gathers findings for a topic."""

    @abstractmethod
    def research(self, topic: str) -> ResearchResult:
        raise NotImplementedError


class WritingAgent(ABC):
    """An agent that turns research findings into a document."""

    @abstractmethod
    def write(self, research: ResearchResult) -> DocumentResult:
        raise NotImplementedError


class StarterResearchAgent(ResearchAgent):
    """Produce a simple research outline without external services."""

    def research(self, topic: str) -> ResearchResult:
        topic = topic.strip()
        if not topic:
            raise ValueError("A research topic is required")
        return ResearchResult(topic, [
            f"Define the scope of the topic: {topic}",
            "Identify the main concepts and relationships",
            "Summarize important benefits, risks, and open questions",
        ])


class StarterWritingAgent(WritingAgent):
    """Turn research findings into a Markdown document."""

    def write(self, research: ResearchResult) -> DocumentResult:
        findings = "\n".join(f"- {finding}" for finding in research.findings)
        content = (
            f"# {research.topic}\n\n## Research outline\n\n{findings}\n\n"
            "## Summary\n\n"
            "This document is a starting point for further research and drafting.\n"
        )
        return DocumentResult(research.topic, content)
