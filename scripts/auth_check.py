import sys, json
s = sys.stdin.read()
try:
    d = json.loads(s)
    print("is_error=", d.get("is_error"), "status=", d.get("api_error_status"),
          "cost=", d.get("total_cost_usd"), "result=", str(d.get("result"))[:120])
except Exception:
    print(s[:300])
