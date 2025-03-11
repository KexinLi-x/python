#导入库
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#读取数据
df=pd.read_csv(r"C:\\Users\\lkx\\Desktop\\世界杯\\WorldCupsSummary.csv",encoding='gbk')
df.head()


# 简单的数据清洗
# 删除所有包含缺失值的行（默认行为）
df_cleaned = df.dropna()
# 删除所有包含缺失值的列
df_cleaned_col = df.dropna(axis=1)


# 计算每个国家赢得世界杯的次数
winner_counts = df['Winner'].value_counts()
print("每个国家赢得世界杯的次数：")
print(winner_counts)


# 计算每个国家进入前四名的次数
top4_counts = pd.concat([df['Winner'], df['Second'], df['Third'], df['Fourth']]).value_counts()
print("每个国家进入前四名的次数：")
print(top4_counts)


# 设置Seaborn风格
sns.set(style="whitegrid",font_scale=1.2, palette="pastel")#指定图表样式为 “白色背景 + 灰色网格线”


# 可视化每个国家赢得世界杯的次数
plt.figure(figsize=(10, 6))#调整画布大小
winner_counts.plot(kind='bar', color='skyblue')
plt.title('The number of times each country has won the World Cup')
plt.xlabel('Country')
plt.ylabel('Times')
plt.xticks(rotation=45, ha="right", fontsize=12)  # 旋转国家名称，避免重叠,right是水平对齐
plt.yticks(fontsize=12)
plt.tight_layout()  # 自动调整子图间距,防止标签被截断
plt.legend()
plt.show()


# 可视化每个国家进入前四名的次数
plt.figure(figsize=(12, 8))
top4_counts.plot(kind='bar', color='lightpink')
plt.title('The number of times each country has reached the top four')
plt.xlabel('Country')
plt.ylabel('Times')
plt.xticks(rotation=45, ha="right", fontsize=12)  # 旋转国家名称，避免重叠
plt.tight_layout()  # 自动调整子图间距
plt.legend()
plt.show()


# 计算每个大洲赢得世界杯的次数
continent_winner_counts = df['WinnerContinent'].value_counts()
print("每个大洲赢得世界杯的次数：")
print(continent_winner_counts)


# 可视化每个大洲赢得世界杯的次数
plt.figure(figsize=(8, 5))
continent_winner_counts.plot(kind='bar', color='green')
plt.title('Tne number of times each continent has won the World Cup')
plt.xlabel('Continent')
plt.ylabel('Times')
plt.tight_layout()  # 自动调整子图间距
plt.xticks(rotation=45, ha="right", fontsize=12)
plt.legend()
plt.show()


# 保存每个国家赢得世界杯的次数到CSV文件
winner_counts.to_csv('winner_counts.csv')


# 保存每个国家进入前四名的次数到CSV文件
top4_counts.to_csv('top4_counts.csv')

