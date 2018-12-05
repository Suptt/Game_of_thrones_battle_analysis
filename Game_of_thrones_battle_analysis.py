# 请先运行此代码块，以确保在可视化中可以显示中文
#!rm -rf ~/.cache/matplotlib/fontList.json
#!wget http://d.xiazaiziti.com/en_fonts/fonts/s/SimHei.ttf -O /opt/conda/lib/python3.6/site-packages/matplotlib/mpl-data/fonts/ttf/SimHei.ttf
import matplotlib.pyplot as plt 

#plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
#plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

# TO DO: load pacakges
import pandas as pd

# TO DO: load the dataset
in_file = 'battles.csv'
full_data = pd.read_csv(in_file)

# TO DO: check the dataset general info
full_data.info()

# TO DO: clean the data (optional: only there are problems)

full_data['attacker_king']=full_data['attacker_king'].fillna('9999')
full_data=full_data.drop(full_data[full_data.attacker_king=='9999'].index.tolist())
full_data['attacker_king'].isnull().value_counts()

full_data['defender_king']=full_data['defender_king'].fillna('9999')
full_data=full_data.drop(full_data[full_data.defender_king=='9999'].index.tolist())
full_data['defender_king'].isnull().value_counts()

full_data['attacker_outcome']=full_data['attacker_outcome'].fillna('no')
full_data=full_data.drop(full_data[full_data.attacker_outcome=='no'].index.tolist())
full_data['attacker_outcome'].isnull().value_counts()

mean=full_data['attacker_size'].mean()
full_data['attacker_size'].fillna(mean,inplace=True)

mean=full_data['defender_size'].mean()
full_data['defender_size'].fillna(mean,inplace=True)

x=[6,7,8]
full_data.drop(full_data.columns[x], axis=1, inplace=True)

y=[7,8,9]
full_data.drop(full_data.columns[y], axis=1, inplace=True)

full_data['attacker_outcome'] = full_data['attacker_outcome'].map({'win': 10, 'loss': 1, 'draw': 5})
full_data.head(3)

full_data['region'].hist(xlabelsize=50,ylabelsize=30,figsize=(50,20));
#针对第一个问题，结果显示The Riverlands发生的战争次数最多。

full_data['battle_type'].hist(xlabelsize=50,ylabelsize=70,figsize=(50,20));
#针对第二个问题，结果显示pitched battle使用的次数最多。

# In exploratory data analysis, please make sure of using statistics and visualizations
full_data['data']=full_data['attacker_size']/full_data['defender_size']
full_data.plot(x='data',y='attacker_outcome',kind='scatter');
#针对第三个问题，可以从图上看出，进攻方和防守方的兵力比例与战争的结果相关性不大。