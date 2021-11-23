import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
Path='C:/MIT线上/PBL/earthquake prediction/week5/all catalogs.xlsx'
Path=Path.strip('\u202a')
macro=pd.read_excel(Path,index_col='Y/M/D')
print(macro)

macro.plot(y='MAGNITUDE')
plt.show()
