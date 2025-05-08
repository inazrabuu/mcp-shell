import requests

def call_mcp_tools(tool_name, input_data):
  url = f"http://localhost:8000/tools/{tool_name}/call"
  response = requests.post(url, json=input_data)

  if response.status_code == 200:
    return response.json()
  else:
    raise Exception(f"MCP error: {response.status_code}: {response.text}")