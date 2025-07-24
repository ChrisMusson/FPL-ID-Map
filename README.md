# ID Map

An ID map between Opta (code column in Master.csv), FPL, FBRef, Understat, Transfermarkt, and FotMob. To load the latest CSV, you can do something like

```python
import pandas as pd

url = "https://raw.githubusercontent.com/ChrisMusson/FPL-ID-Map/refs/heads/main/Master.csv"
df = pd.read_csv(url)
```