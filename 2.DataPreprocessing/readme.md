# 머신러닝 워크플로우 (Machine Learning Workflow)

## Workflow  
> 1) 데이터 수집 2) 탐색적 데이터 분석(EDA) 3) 데이터 전처리 4) 모델링 및 훈련 5) 모델 성능 평가 6) 배포
> 
![image](https://github.com/user-attachments/assets/d260ba30-1453-42b5-9ae4-b569e637ddfb)  
출처: https://wikidocs.net/31947

본 교재에서는 수집된 데이터를 이용하기 때문에, `1)데이터 수집`, `6) 배포`를 제외한 `2)EDA`, `3)데이터 전처리`, `4)모델링`, `5)모델 성능 평가`를 위주로 설명하겠습니다.    



## 1) 데이터 수집  

머신 러닝을 하기 위해서는 기계에 학습시켜야 할 데이터가 필요합니다. 
~자연어 처리의 경우, 자연어 데이터를 말뭉치 또는 코퍼스(corpus)라고 부르는데 코퍼스의 의미를 풀이하면, 조사나 연구 목적에 의해서 특정 도메인으로부터 수집된 텍스트 집합을 말합니다. 텍스트 데이터의 파일 형식은 txt 파일, csv 파일, xml 파일 등 다양하며 그 출처도 음성 데이터, 웹 수집기를 통해 수집된 데이터, 영화 리뷰 등 다양합니다.~



## 2) 탐색적 데이터 분석 (Exploratory Data Analysis, EDA)  

데이터가 수집되었다면, 데이터를 점검하고 탐색하는 단계입니다. 데이터의 구조, 노이즈 데이터, 머신 러닝 적용을 위해서 데이터를 어떻게 정재해야하는지 등을 파악해야합니다. 이 단계를 **탐색적 데이터 분석(Exploratory Data Analysis, EDA)** 라고 합니다. 이는 독립 변수, 종속 변수, 변수의 데이터 타입, 변수의 분포, 요약통계량 등을 점검하며 데이터의 특징과 내재하는 구조적 관계를 알아내는 과정입니다. 이 과정에서 시각화(ex. 히스토그램, box plot, 산점도)와 간단한 통계 검정(ex. 정규성 검정, 평균차이 검정, 상관관계 검정)을 진행하기도 합니다.

![image](https://github.com/user-attachments/assets/b004e8de-366b-419f-bf86-86087c9b255d)
출처: seaborn 시각화 예제(https://kite-mo.github.io/python/2020/04/20/python-5-weeks/)

![image](https://github.com/user-attachments/assets/7f8a274e-bde7-4887-a472-ab3c9c87e908)
출처: 평균 차이 검정 중 분산 분석(ANOVA) (https://recipesds.tistory.com/entry/%EB%B6%84%EC%82%B0%EB%B6%84%EC%84%9DANOVA-%EC%95%84%EB%8B%88-%EB%8B%A4%EC%A7%91%EB%8B%A8-%EC%B0%A8%EC%9D%B4%EC%97%90-%EC%99%9C-%EA%B0%91%EC%9E%90%EA%B8%B0-%EB%B6%84%EC%82%B0%EC%9D%84-%EB%B3%B4%EC%A7%80%EC%9A%94)

![image](https://github.com/user-attachments/assets/e831c2a6-d3a8-4f47-a04e-f90260780f18)
출처: 피어슨 상관계수 (https://statisticsplaybook.com/covariance-and-correlation/)
