import requests

base_url = 'http://localhost:8000'

def call_mcp_tools(tool_name, input_data):
  url = f"{base_url}/tools/{tool_name}/call"
  response = requests.post(url, json=input_data)

  if response.status_code == 200:
    return response.json()
  else:
    raise Exception(f"MCP error: {response.status_code}: {response.text}")
  
def available_tools():
  response = requests.get(f"{base_url}/tools")

  return response.json()