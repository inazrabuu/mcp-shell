import os
from dotenv import load_dotenv
from utils.prompt import extract_tool_call as etc
import client as mcpc
import openai

load_dotenv()

c = openai.OpenAI(base_url=os.getenv('OPENROUTER_BASE_URL'), api_key=os.getenv('OPENROUTER_API_KEY'))

def send_to_llm(messages):
  response = c.chat.completions.create(
    model=os.getenv("LLM"),
    messages=messages,
    temperature=0.2
  )

  return response.choices[0].message.content

def get_available_tools():
  tools = "Available Tools: \n"
  available_tools = mcpc.available_tools()
  for i, t in enumerate(available_tools['tools']):
    tools += f"""
{i + 1}. {t['name']}
- Description: {t['description']}
- Input: {t['input_schema']}

"""
    
  return tools

def main():
  available_tools = get_available_tools()

  messages = [{
    'role': 'system',
    'content': f"""
You can use tools by saying: USE_TOOL {{"name": ..., "input_schema": {{...}}

{available_tools}

Rules:
- Only use a tool if the user's question can be solved using the tool
- Respond normally when no tool is relevant!
"""
  }]

  while True:
    user_input = input("User: ")
    messages.append({
      'role': 'user',
      'content': user_input
    })

    llm_response = send_to_llm(messages)

    tool_call = etc(llm_response)
    if tool_call:
      messages.pop()
      result = mcpc.call_mcp_tools(tool_call['name'], tool_call['input_schema'])
      print(f"[Tool Result] => {result}")
      messages.append({
        'role': 'user',
        'content': f"Tool Result: {result}"
      })

      final_response = send_to_llm(messages)
      print(f"LLM (final): {final_response}")
    else:
      print(f"LLM: {llm_response}")

    messages.pop()

if __name__ == '__main__':
  main()