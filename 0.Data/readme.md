# Data

### 개요
이 README 파일은 제공된 Tox21 데이터셋, 데이터 전처리 과정, 그리고 생성된 파일들에 대한 정보를 자세히 설명합니다. 데이터셋은 독성 예측과 관련된 범주형 및 연속형 데이터를 포함하고 있습니다.  

1. 입력 파일

- tox21.xlsm: 범주형 독성 데이터를 포함한 원본 데이터셋 (y).
  
- tox21_ac50.xlsx: 연속형 독성 데이터를 포함한 원본 데이터셋 (y).

2. 전처리 및 분할 후 데이터셋

2-1. 범주형 데이터  

- tox21_dataset.csv: tox21.xlsm 파일을 전처리하여 생성된 데이터셋.

- tox21_train.csv: tox21_dataset.csv 파일에서 학습용으로 분할된 데이터셋.

- tox21_test.csv: tox21_dataset.csv 파일에서 테스트용으로 분할된 데이터셋.

2-2. 연속형 데이터  

- tox21_ac50.csv: tox21_ac50.xlsx 파일을 전처리하여 생성된 데이터셋.

  
### 파일 설명

**1. tox21.xlsm : 범주형 데이터 (y)**


전처리 후


 1.1 tox21_dataset.csv


split 후


 1.2 tox21_train.csv
 1.3 tox21_test.csv

------


**2 tox21_ac50.xlsx : 연속형 데이터 (y)**


전처리 후

2.1 tox21_ac50.csv


