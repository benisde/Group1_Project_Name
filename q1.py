import pandas as pd
import numpy as np
from pathlib import Path

def char1():
    # what this function is doing
    df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
    df.plot()