# 导入相关包
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm
import re
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
import os
from scipy import stats

# 读入前面处理好的virmach结构化的数据
df = pd.read_csv("./hei2019.csv", sep="\t")
df.locate = df.locate.str.split(",", n=1, expand=True)[1]
df.replace('^\s+', '', regex=True, inplace=True)


# 由于vps位置为category类型，不能直接用于机器学习，这里替换为对应数字

df.locate = df.locate.replace('CA', 1).replace('NY', 2).replace(
    'GA', 3).replace('NJ', 4).replace('TX', 5).replace('WA', 6).replace('IL', 7)

# 查看数据
df.head().append(df.tail())


# sklearn的线性回归模型部分
regressor = LinearRegression()
X = df.iloc[:, 1:].values
y = df.iloc[:, 0].values
# 训练集测试集1:2划分
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=1/3, random_state=0)

# 模型训练
print("开始训练～")
regressor.fit(X_train, y_train)

# 使用训练好的模型进行预测
y_pred = regressor.predict(X_test)

print("训练完成？")
print("模型评估")

test_set_rmse = (np.sqrt(mean_squared_error(y_test, y_pred)))
test_set_r2 = r2_score(y_test, y_pred)
print(test_set_rmse)
# 8.5790882402413
print(test_set_r2)
# 0.878882928666751

print("模型参数")
print(regressor.intercept_)
# 7.599458793118405
print(regressor.coef_)
# [ 2.44111567e-01  2.46369652e-01  5.93846195e+00 -6.07453703e+00 2.12034498e-03  6.35691925e-04]
