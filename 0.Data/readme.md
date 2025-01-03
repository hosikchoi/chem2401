# Data

### 개요
이 README 파일은 제공된 Tox21 데이터셋, 데이터 전처리 과정, 그리고 생성된 파일들에 대한 정보를 자세히 설명합니다. 데이터셋은 독성 예측과 관련된 범주형 및 연속형 데이터를 포함하고 있습니다.  

#### 1. 입력 파일
  
1-1. 범주형 데이터
  
- `tox21.xlsm`: 범주형 독성 데이터를 포함한 원본 데이터셋 (y).

1-2. 연속형 데이터  
  
- `tox21_ac50.xlsx`: 연속형 독성 데이터를 포함한 원본 데이터셋 (y).
  

#### 2. 전처리 및 분할 후 데이터셋

2-1. 범주형 데이터  

- `tox21_dataset.csv`:`tox21.xlsm` 파일을 전처리하여 생성된 데이터셋.

- `tox21_train.csv`: `tox21_dataset.csv` 파일에서 학습용으로 분할된 데이터셋.

- `tox21_test.csv`: `tox21_dataset.csv` 파일에서 테스트용으로 분할된 데이터셋.

2-2. 연속형 데이터  

- `tox21_ac50.csv`: `tox21_ac50.xlsx` 파일을 전처리하여 생성된 데이터셋.

<img src="https://github.com/user-attachments/assets/bc17af84-0874-4b66-9cf2-fba99d8beb54" width="500" height="200"/>

------  
### 파일 설명

**1. tox21.xlsm**


- 설명: 독성 물질에 대한 원본 데이터셋.

- 목표 변수 (y): 범주형

- 목적: 독성 물질의 독성 여부를 예측하는 이진 분류 문제 해결.

- 전처리 과정:
1. 결측치 보완: 데이터 내 결측값을 적절히 처리.   
2. 특징 선택: 분석에 불필요한 열 제거 및 유용한 변수만 선택.  
3. 데이터 변환: 필요한 경우 데이터 정규화 또는 스케일링.   

![image](https://github.com/user-attachments/assets/a5eeecb1-8f82-48af-9254-887dff391fc3)


**2. tox21_ac50.xlsx**

- 설명: 독성 물질에 대한 연속형 데이터셋.

- 목표 변수 (y): 연속형 

- 목적: 정량적인 독성 수준을 예측하는 회귀 문제 해결.  

- 전처리 과정:  
1. 결측치 및 이상치 처리: 데이터의 품질을 높이기 위해 적절한 방식으로 처리.  
2. 데이터 스케일링: 모델 학습에 적합하도록 정규화 또는 표준화.  

![image](https://github.com/user-attachments/assets/c2b9b0a1-2381-4af3-9080-c22173a38292)


**3. tox21_dataset.csv**

- 설명: tox21.xlsm에서 전처리된 데이터셋으로, 선택된 변수를 정리된 목표 변수(y)를 포함.
  
- 목표 변수 (y): 범주형

- 목적: 머신러닝 모델링에 바로 사용할 수 있는 데이터셋.

![image](https://github.com/user-attachments/assets/16eae862-5b8d-4cf5-a8cb-9786c84f3936)


**4. tox21_train.csv 및 tox21_test.csv**

- 설명: tox21_dataset.csv를 학습용(tox21_train.csv)과 테스트용(tox21_test.csv)으로 분할한 데이터셋입니다.

- 내용: 학습(train) 데이터셋은 모델 학습에 사용하고, 테스트(test) 데이터셋은 모델 성능 평가에 사용.

![image](https://github.com/user-attachments/assets/507556fc-eeec-4388-8034-7a20f77f21cf)

![image](https://github.com/user-attachments/assets/f8d1edf2-2f27-4eb3-97d3-996352ad9ab0)


**5. tox21_ac50.csv**

- 설명: tox21_ac50.xlsx에서 전처리된 데이터셋으로, 전처리 후 선택된 변수들과 연속형 목표 변수(y)를 포함.

- 목표 변수 (y): 연속형

- 목적: 회귀 분석 및 독성 수준 예측 모델 개발에 사용.

![image](https://github.com/user-attachments/assets/ffb5ba9c-f285-4f9e-99e8-2508bd6d2ad7)

