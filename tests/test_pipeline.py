import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from multi_agents_ai_assistants.agents import StarterResearchAgent, StarterWritingAgent
from multi_agents_ai_assistants.pipeline import AgentPipeline


class AgentPipelineTests(unittest.TestCase):
    def test_pipeline_creates_a_document(self) -> None:
        pipeline = AgentPipeline(StarterResearchAgent(), StarterWritingAgent())
        document = pipeline.run("Multi-agent systems")
        self.assertEqual(document.title, "Multi-agent systems")
        self.assertIn("## Research outline", document.content)
        self.assertIn("Identify the main concepts", document.content)

    def test_empty_topic_is_rejected(self) -> None:
        pipeline = AgentPipeline(StarterResearchAgent(), StarterWritingAgent())
        with self.assertRaisesRegex(ValueError, "topic is required"):
            pipeline.run("   ")


if __name__ == "__main__":
    unittest.main()
