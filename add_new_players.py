import csv
import os

import requests


def append_new_to_existing(filepath, new):
    with open(filepath, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(new)


with open(os.path.join("FBRef.csv"), "r", encoding="utf-8") as f:
    data = [row for row in csv.reader(f)][1:]
    old_codes = set([int(row[0]) for row in data])

with requests.Session() as s:
    url = "https://fantasy.premierleague.com/api/bootstrap-static/"
    players = s.get(url).json()["elements"]

data = [["code", "first_name", "second_name", "web_name", "24-25"]]
for p in players:
    data.append([p["code"], p["first_name"], p["second_name"], p["web_name"], p["id"]])
data = [data[0]] + sorted(data[1:], key=lambda x: x[-1])

with open(os.path.join("FPL", "24-25.csv"), "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

new_players = [x[:-1] + [None] for x in data[1:] if int(x[0]) not in old_codes]
for file in ["FBRef.csv", "Understat.csv", "Transfermarkt.csv"]:
    append_new_to_existing(file, new_players)
