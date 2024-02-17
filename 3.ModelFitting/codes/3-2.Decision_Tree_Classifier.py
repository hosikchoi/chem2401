# 데이터셋 scv 파일을 같은 경로상의 디렉터리에 두고 실행해주세요.



# 라이브러리 불러오기
import pandas as pd
#1. pandas: 데이터를 빠르고 강력하게, 그리고 유연하고 쉽게 다룰 수 있게 해주는 데이터 분석, 증강 도구입니다.
#    - <https://pandas.pydata.org/docs/user_guide/index.html>

import numpy as np
#2. numpy: 파이썬에서 수치 계산을 빠르게 수행할 수 있게 해주는 도구입니다.
#    - <https://numpy.org/doc/stable/>

import matplotlib.pyplot as plt
#3. matplolib: 정적, 애니메이션, 또는 상호작용형 시각화를 생성하기 위한 포괄적인 도구입니다.
#    - <https://matplotlib.org/stable/users/index>

import sklearn
#4. scikit-learn: 데이터 분석을 위한, 쉽고 효율적인 여러 도구를 제공합니다.
#    - <https://scikit-learn.org/stable/user_guide.html>



df = pd.read_csv('tox21_train.csv')
# 이 주피터파일과 같은 디렉터리에 존재하는 'tox21_dataset.csv' 파일을 읽어와 df에 저장합니다.





X = df.iloc[:, :-1]
# 독립 변수를 X에 저장합니다. 독립 변수는 'NR-AR' 열을 제외한 나머지 열입니다.

y = df.iloc[:, -1]
# 종속 변수를 y에 저장합니다. 종속 변수는 'NR-AR' 열입니다.



from sklearn.tree import DecisionTreeClassifier
# decision tree classifier를 사용하기 위한 라이브러리를 불러옵니다.

# 결정 트리 모델을 생성합니다.
model = DecisionTreeClassifier(max_depth=3, random_state=42)
# 결정 트리 모델을 생성하고, 모델을 model에 저장합니다.
model.fit(X, y)
# 모델을 학습시킵니다.



# 중요도 순으로 정렬
importances = pd.Series(data=model.feature_importances_, index=X.columns)
# 모델의 특성 중요도를 importances에 저장합니다.
importances_sorted = importances.sort_values()
# importances를 중요도 순으로 정렬합니다.

# 상위 10개 특성만 선택
importances_top10 = importances_sorted[-10:]
# 중요도가 높은 상위 10개의 특성을 importances_top10에 저장합니다.

plt.figure(figsize=(8, 6))
# 그래프의 크기를 설정합니다.
plt.barh(importances_top10.index, importances_top10.values)
# 가로 막대 그래프를 그립니다.
plt.xlabel('Importance')
# x축의 라벨을 설정합니다.
plt.ylabel('Features')
# y축의 라벨을 설정합니다.
plt.show()
# 그래프를 출력합니다.



from sklearn.decomposition import PCA
# PCA를 사용하기 위한 라이브러리를 불러옵니다.
from sklearn.metrics import confusion_matrix
# confusion matrix를 사용하기 위한 라이브러리를 불러옵니다.



# PCA를 사용하여 피처를 2개로 줄이기
pca = PCA(n_components=2)
# PCA를 생성하고, 2개의 주성분을 사용하도록 설정합니다.
X_pca = pca.fit_transform(X)
# PCA를 사용하여 X를 변환합니다.



# 결정 트리 모델 학습
model_pca = DecisionTreeClassifier(max_depth=3, random_state=42)
# 결정 트리 모델을 생성하고, 모델을 model_pca에 저장합니다.
model_pca.fit(X_pca, y)
# 모델을 학습시킵니다.



# 결정 경계 시각화
x1s = np.linspace(X_pca[:, 0].min()-0.5, X_pca[:, 0].max()+0.5, 100)
# x1s: X_pca의 첫 번째 열의 최솟값에서 0.5를 뺀 값부터 최댓값에서 0.5를 더한 값까지 100개의 구간으로 나눈 배열
x2s = np.linspace(X_pca[:, 1].min()-0.5, X_pca[:, 1].max()+0.5, 100)
# x2s: X_pca의 두 번째 열의 최솟값에서 0.5를 뺀 값부터 최댓값에서 0.5를 더한 값까지 100개의 구간으로 나눈 배열
x1, x2 = np.meshgrid(x1s, x2s)
# x1, x2: x1s와 x2s를 격자로 나눈 배열
X_new = np.c_[x1.ravel(), x2.ravel()]
# X_new: x1과 x2를 1차원 배열로 변환한 후, 열로 합친 배열
y_pred = model_pca.predict(X_new).reshape(x1.shape)
# y_pred: X_new를 사용하여 예측한 후, x1의 모양으로 변환한 배열



plt.contourf(x1, x2, y_pred, alpha=0.3)
# x1, x2, y_pred를 사용하여 등고선을 그립니다.
plt.scatter(X_pca[:, 0][y==0], X_pca[:, 1][y==0], color='blue', alpha=0.1)
# y가 0인 행을 파란색으로 점으로 표시합니다.
plt.scatter(X_pca[:, 0][y==1], X_pca[:, 1][y==1], color='red', alpha=0.1)
# y가 1인 행을 빨간색으로 점으로 표시합니다.
plt.show()
# 시각화를 출력합니다.


# 테스트 데이터를 학습한 모델로 분류한 결과를 혼동 행렬로 나타냅니다. 


df_test = pd.read_csv('tox21_test.csv')
# 이 주피터파일과 같은 디렉터리에 존재하는 'tox21_test.csv' 파일을 읽어와 df에 저장합니다.
X_test = df_test.iloc[:, :-1]
# 독립 변수를 X에 저장합니다. 독립 변수는 'NR-AR' 열을 제외한 나머지 열입니다.
y_test = df_test.iloc[:, -1]
# 종속 변수를 y에 저장합니다. 종속 변수는 'NR-AR' 열입니다.




# 혼동 행렬
from sklearn.metrics import confusion_matrix
# 혼동 행렬을 계산하기 위한 라이브러리를 불러옵니다.

print(confusion_matrix(y_test, model.predict(X_test)))
# 테스트 데이터의 혼동 행렬을 출력합니다.