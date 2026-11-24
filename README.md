# MultiAgentsAIAssistants

A Python starter project for a research-and-writing multi-agent workflow. The sample agents run locally without API keys or third-party runtime dependencies. Replace the starter implementations with your preferred research and language-model providers as you build the application.

## Requirements

- Python 3.10 or newer

## Install from the repository root

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

On Windows, activate with `.venv\\Scripts\\activate`.

> If you are using a dev container or Codespace, first `cd` to the cloned repository root (the directory containing `pyproject.toml`), then run the install command.

## Run

```bash
python -m multi_agents_ai_assistants "How do multi-agent AI systems coordinate?"
```

Or, after installation:

```bash
multi-agents-ai-assistants "How do multi-agent AI systems coordinate?"
```

## Test

```bash
python -m unittest discover -s tests -v
```
