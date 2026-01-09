import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("data.csv")
profile = ProfileReport(df, title= "Profiling Report")
profile.to_file("report.html")