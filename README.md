# MCP Shell

A simple shell / skeleton for developing an MCP application. Used openai wrapper to interact with the LLM API, makes it compatible to use with another openai based LLM provider / aggregator (eg. Openrouting, Deepseek). Feel free to use and make modification to it.

Use FastAPI for the server and serve with uvicorn.

## How To Use
- clone this repo
- `cd` to the cloned directory
- ```pip install -r requirements.txt```
- `mv .env.example .env` and set your `API_KEY`
- start the server ```uvicorn server.server:app --reload```