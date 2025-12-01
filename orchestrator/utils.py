import json
import re
import ast

def parse_gemini_response(resp: str):
    resp = resp.strip()
    try:
        return json.loads(resp)
    except:
        match = re.search(r'(\{.*\}|\[.*\])', resp, re.S)
        if match:
            try:
                return json.loads(match.group(1))
            except:
                pass
        try:
            return ast.literal_eval(resp)
        except:
            return {"error": "Failed to parse Gemini response", "raw": resp}
