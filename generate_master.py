import os

import pandas as pd

seasons = [f"{season}-{season + 1}" for season in range(16, 26)]
fpl_files = [os.path.join("FPL", f"{season}.csv") for season in seasons[::-1]]
datasource_files = ["FBRef.csv", "Understat.csv", "Transfermarkt.csv", "Whoscored.csv"]
files = fpl_files + datasource_files
name_columns = ["first_name", "second_name", "web_name"]

master = pd.read_csv(files[0], index_col="code")
for file in files[1:]:
    df = pd.read_csv(file, index_col="code")
    master = master.combine_first(df)

master = master.sort_index()
master_names = master[name_columns]
col_order = name_columns + seasons + ["fbref", "understat", "transfermarkt", "whoscored"]

master = master[col_order]
for col in seasons + ["understat", "transfermarkt", "whoscored"]:
    master[col] = master[col].astype("Int64")
master.to_csv("Master.csv", encoding="utf-8-sig")

for file in datasource_files:
    df = pd.read_csv(file).set_index("code")
    df.update(master_names)
    df.to_csv(file, encoding="utf-8-sig")
