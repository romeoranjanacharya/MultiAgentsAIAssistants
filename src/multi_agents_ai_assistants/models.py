"""Shared models for the multi-agent workflow."""

from dataclasses import dataclass, field


@dataclass
class ResearchResult:
    topic: str
    findings: list[str] = field(default_factory=list)


@dataclass
class DocumentResult:
    title: str
    content: str
