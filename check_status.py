from lxml import html
import sqlite3
import re
from datetime import datetime
db = sqlite3.connect("production.db")
cur = db.cursor()
parsed_html = html.parse("http://status.earthlost.de")
ship_dict = {}
for p in parsed_html.xpath("//b"):
    if p.text.startswith("Gesamt:"):
        key = p.getparent().getprevious().text.replace(" ", "_").replace("-", "_")
        ship_dict[key] = []
        for t in p.getparent().itertext():
            ship_dict[key].append([s.strip() if n != 1 else int(s.strip().replace(".", "")) for n, s in enumerate(re.split('- |:', t))])
for k, v_list in ship_dict.iteritems():
    for v in v_list:
        try:
            cur.execute("insert into " + k + "(id, tag, count, create_date)  values(?, ?, ?, ?)", (None, v[0], v[1], datetime.now()))
        except sqlite3.OperationalError:  # Better ask for forgiveness, then for permission!
            cur.execute("create table " + k + "(id primary key, tag, count, create_date)")
            cur.execute("insert into " + k + "(id, tag, count, create_date)  values(?, ?, ?, ?)", (None, v[0], v[1], datetime.now()))
cur.close()
db.commit()
db.close()
