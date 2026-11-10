import json, os, datetime
d = os.path.join(os.path.dirname(__file__), "..", "data")
emb = {n: open(os.path.join(d, n + ".csv")).read() for n in ("videos", "history", "influencers")}
open(os.path.join(d, "embedded.js"), "w").write("window.EMBEDDED=" + json.dumps(emb) + ";window.UPDATED=" + json.dumps(datetime.date.today().strftime("%d %b %Y")) + ";")
print("embedded.js refreshed")
