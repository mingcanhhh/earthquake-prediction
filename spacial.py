import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
Path='C:/MIT线上/PBL/earthquake prediction/week5/all catalogs.xlsx'
Path=Path.strip('\u202a')
macro=pd.read_excel(Path)
datas=macro[['LAT','LON']]

sns.regplot(x='LAT',y='LON',data=datas)
plt.show()
