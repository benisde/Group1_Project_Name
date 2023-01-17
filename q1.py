import pandas as pd
import numpy as np
from pathlib import Path

def chart2():
    # what this function is doing
    #df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
    #df.plot()

    vehicle_df = pd.read_csv("./resources/vrdb_60days_daily.csv")
    return vehicle_df.head()
