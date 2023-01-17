import q1 
import pandas as pd
import numpy as np
from pathlib import Path

def bar():
    vehicle_df = pd.read_csv("./resources/vrdb_60days_daily.csv")
    vehicle_df.head()
    vehicle_df = vehicle_df[["RECALL_NUMBER_NUM", "MAKE_NAME_NM","MODEL_NAME_NM"]]
    vehicle_df = vehicle_df.groupby(["MAKE_NAME_NM","MODEL_NAME_NM"]).count()
    vehicle_df = vehicle_df.sort_values(by="RECALL_NUMBER_NUM")

    vehicle_df.plot(figsize=(20, 4))

    return vehicle_df.tail(20)


# Filtering 
#vehicle_df.drop(vehicle_df[vehicle_df.RECALL_NUMBER_NUM == 18].index, inplace=True)
#vehicle_df.tail(20)