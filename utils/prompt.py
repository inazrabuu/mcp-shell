import json
import re

def extract_tool_call(text):
  match = re.search(r"USE_TOOL\s+({.*})", text)
  if match:
    try:
      return json.loads(match.group(1))
    except json.JSONDecodeError:
      print("Invalid JSON in tool call.")

  return None