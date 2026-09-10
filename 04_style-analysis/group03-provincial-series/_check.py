import re, glob, os
base = os.path.dirname(os.path.abspath(__file__))
names = ["增冲鼓楼","崇圣寺三塔","张掖大佛寺","莫高窟九层楼","苏公塔"]
for nm in names:
    files = glob.glob(os.path.join(base, f"*{nm}*.html"))
    if not files:
        print("MISSING", nm); continue
    f = files[0]
    txt = open(f, encoding="utf-8").read()
    ps = re.findall(r"<p[^>]*>(.*?)</p>", txt, re.S)
    counts = []
    for p in ps:
        t = re.sub(r"<[^>]+>", "", p)
        t = t.replace("\n","").replace(" ","").replace("\t","")
        counts.append(len(t))
    total = sum(counts)
    print(f"{nm} | 段数={len(ps)} | 各段={counts} | 总={total}")
