import os

import pandas as pd

seasons = [f"{season}-{season+1}" for season in range(16, 25)]
fpl_files = [os.path.join("FPL", f"{season}.csv") for season in seasons[::-1]]
files = fpl_files + ["FBRef.csv", "Understat.csv", "Transfermarkt.csv"]

master = pd.read_csv(files[0], index_col="code")
for file in files[1:]:
    df = pd.read_csv(file, index_col="code")
    master = master.combine_first(df)

master = master.sort_values(by="code")
col_order = (
    ["first_name", "second_name", "web_name"]
    + seasons
    + ["fbref", "understat", "transfermarkt"]
)

master = master[col_order]
for col in seasons + ["understat", "transfermarkt"]:
    master[col] = master[col].astype("Int64")
master.to_csv("Master.csv", encoding="utf-8")
