# MultiAgentsAIAssistants
A Python starter project for a research-and-writing multi-agent workflow. The included agents share a simple interface and can be used independently or composed in a pipeline.

## Project layout

```text
src/multi_agents_ai_assistants/
  agents.py      # Research and writing agent implementations
  pipeline.py    # Coordinates the agents
  cli.py         # Command-line interface
  models.py      # Shared workflow data models
  __main__.py    # python -m entry point
tests/
  test_pipeline.py
