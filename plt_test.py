import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# 绘制简单的线图

# plt.plot([1, 3, 5], [4, 8, 10])
# plt.show()


# x = np.linspace(-np.pi * 2, np.pi * 2, 100)  # x 轴的定义为 -3.14 ~ 3.14 中间间隔100个元素
# plt.figure(1, dpi=50)  # 绘图精度
# for i in range(1, 5):  # 画四条线
#     plt.plot(x, np.sin(x / i))
# plt.show()

# plt.figure(1, dpi=50)  # 绘图精度
# data = [1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 4]
# plt.hist(data)
# plt.show()

# x = np.arange(1, 10)
# y = x
# fig = plt.figure()
# plt.scatter(x, y, c='r', marker='o')  # c='r' => color : red, marker='o' => 圆形
# plt.show()


iris = pd.read_csv("./iris_training.csv")
print(iris.head())

# 绘制散点图
# iris.plot(kind='scatter', x='120', y='4')  # 不美观
# plt.show()

sns.set(style='white', color_codes=True)
# sns.jointplot(x='120', y='4', data=iris, size=5)

# sns.FacetGrid(iris, hue='virginica', size=5).map(plt.scatter, '120', '4').add_legend()
sns.FacetGrid(iris, hue='virginica', size=5).map(plt.scatter, 'setosa', 'versicolor').add_legend()
sns.distplot(iris['120'])
plt.show()
