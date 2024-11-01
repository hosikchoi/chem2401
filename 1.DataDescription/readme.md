# Data Description

## 1. Data Description

Tox21 데이터와 AC50는 독성 평가 및 약물 개발 연구에서 중요한 역할을 합니다.

> 1. Tox21 데이터   
>    `Tox21` dataset은 특정 화합물에 대한 독성 예측을 위한 대규모 데이터셋으로, 미국 환경보호청(EPA), 미국 보건복지부(DHHS), 미국 식품의약국(FDA), 미국 국립보건원(NIH) 등 여러 정부 기관이 협력하여 개발했습니다. 데이터에는 여러 가지 생체 독성 반응을 나타내는 변수가 포함되어 있습니다. 변수로는 화합물 id, 화학 구조, NR 관련 변수,  SR 관련 변수가 있습니다.
> 
>    화합물 id
>    - mol_id: 각 화합물의 고유 식별자
>      
>    화학 구조   
>    - smiles: 화합물의 화학적 구조를 나타내는 SMILES(Simplified Molecular Input Line Entry System) 문자열
>   
>    NR (핵수용체) 관련 변수   
>    - NR-AR: 안드로겐 수용체(Androgen Receptor)에 대한 반응 여부   
>    - NR-AR-LBD: 안드로겐 수용체의 리간드 결합 도메인에 대한 반응   
>    - NR-AhR: 아릴 하이드로카본 수용체(Aryl hydrocarbon receptor)에 대한 반응   
>    - NR-Aromatase: 아로마타제 효소에 대한 반응   
>    - NR-ER: 에스트로겐 수용체(Estrogen Receptor)에 대한 반응   
>    - NR-ER-LBD: 에스트로겐 수용체의 리간드 결합 도메인에 대한 반응   
>    - NR-PPAR-gamma: PPAR 감마 수용체에 대한 반응 (Peroxisome Proliferator-Activated Receptor Gamma)
>
>    SR (스트레스 반응) 관련 변수   
>    - SR-ARE: 항산화 반응 요소(Antioxidant Response Element)에 대한 반응   
>    - SR-ATAD5: DNA 손상 반응과 관련된 ATAD5에 대한 반응   
>    - SR-HSE: 열 충격 요소(Heat Shock Element)에 대한 반응   
>    - SR-MMP: 매트릭스 메탈로프로테아제(Matrix Metalloproteinase)에 대한 반응   
>    - SR-p53: 종양 억제 단백질 p53에 대한 반응
> 
>    ![image](https://github.com/user-attachments/assets/ce400220-f0ff-4473-bb81-47d57ffa051e)
>    출처: [EPA’s Distributed Structure-Searchable Toxicity (DSSTox) Database, EPA][1]   
>   
>   [1]: "https://www.epa.gov/comptox-tools/distributed-structure-searchable-toxicity-dsstox-database"
>    ~~Tox21은 미국 환경보호청(EPA), 미국 보건복지부(DHHS), 미국 식품의약국(FDA), 미국 국립보건원(NIH) 등 여러 정부 기관이 협력하여 개발한 독성 예측을 위한 대규모 데이터셋입니다.
이 데이터셋은 다양한 화합물에 대한 독성 정보를 포함하고 있으며, 특히 신약 개발, 환경 독성 평가 등에서 화합물이 인간 건강에 미치는 영향을 예측하기 위한 목적으로 사용됩니다.
Tox21 데이터는 독성 평가를 위한 다중 분석(assays) 결과를 포함하며, 각 화합물의 화학 구조, 생물학적 특성, 독성 반응 등 다양한 변수를 제공합니다. 이를 통해 특정 화합물이 인체의 특정 시스템(예: 간, 신경계)에 미치는 영향을 평가하고, 독성 프로파일을 이해하는 데 도움을 줍니다.~~

> 2. AC50 (Half-maximal Activity Concentration) 데이터    
>    `Tox21_ac50` dataset은 화합물의 AC50 수치를 기록한 데이터입니다. AC50는 화합물이 활성 부위에서 반응의 절반을 일으키는 화합물의 농도입니다. 약리학 및 독성학에서 매우 중요한 지표로, 특정 화합물이 생체에서 반응을 일으키기 위해 필요한 최소 농도를 평가하는 데 사용됩니다. 예를 들어, Tox21 데이터 내 화합물의 AC50 값은 화합물이 특정 독성 반응(예: 세포 사멸, 효소 억제)을 절반 정도 일으키는 데 필요한 농도를 나타냅니다. 데이터의 변수는 화합물 이름, CAS 등록 번호, 화학 구조, AC50로 이루어져있습니다.   
>    
>    화합물 이름      
>    - PREFERRED NAME: 각 화합물의 고유 식별자   
>    
>    CAS 등록 번호   
>    - CASRN: CAS 등록 번호. 각 화합물에 대한 고유 번호로, 전 세계적으로 화합물 식별에 사용   
>      
>    화학 구조     
>    - SMILES: 화합물의 화학적 구조를 나타내는 SMILES(Simplified Molecular Input Line Entry System) 문자열   
>        
>    AC50   
>    - AC50: 화합물이 반응의 절반을 유발하는 농도 (단위: µM). AC50 값이 낮을수록 해당 화합물이 강한 독성을 나타낼 가능성이 큼
>    ![image](https://github.com/user-attachments/assets/f68a9734-2da9-4130-82bb-633ae76d491a)   
>    출처: [EC50, Wikipedia][1]   
>   
>   [1]: "https://en.wikipedia.org/wiki/EC50"
>   ~~AC50는 화합물이 반응의 절반을 유발하는 농도를 의미합니다. 여기서 "AC"는 "Activity Concentration"을 나타내며, 50은 반응의 절반에 해당하는 수치를 의미합니다.
약리학 및 독성학에서 매우 중요한 지표로, 특정 화합물이 생체에서 반응을 일으키기 위해 필요한 최소 농도를 평가하는 데 사용됩니다.
예를 들어, Tox21 데이터 내 화합물의 AC50 값은 화합물이 특정 독성 반응(예: 세포 사멸, 효소 억제)을 절반 정도 일으키는 데 필요한 농도를 나타냅니다. 낮은 AC50 값은 특정 독성 반응을 유발하는 데 필요한 농도가 낮음을 의미하며, 이는 해당 화합물이 더 높은 독성을 지닐 수 있음을 시사합니다.
이를 통해 연구자들은 화합물의 효능 및 독성을 평가하고, 최적의 농도를 설정하여 독성 위험을 최소화할 수 있습니다.
Tox21 데이터와 AC50은 함께 사용되어 화합물의 독성 예측, 약물 안전성 평가, 그리고 환경 독성 연구 등에서 매우 중요한 역할을 하며, 특히 독성 평가 모델 및 머신러닝 알고리즘의 훈련에 유용하게 활용됩니다.~~

---

## 2. Data Preprocessing

실제 데이터를 활용해 탐색적 데이터 분석(Exploratory Data Analysis, 이하 EDA)을 합니다. 본격적으로 데이터 분석을 들어가기 전에 데이터 구조를 파악하고 전처리를 수행할 수 있습니다.

> 2-1. tox21_EDA  
> 범주형 데이터를 가지는 전처리 전 데이터셋 `tox21.xlsm`을 EDA한 코드입니다. 코드를 통해 결측값을 확인할 수 있습니다. 

> 2-2. tox21_ac50_EDA  
> `tox21.xlsm`을 보충하기 위해, 연속형 데이터를 가지는 데이터셋 `tox21_ac50.xlsx`을 EDA한 코드입니다. 코드를 통해 결측값을 제거한 후 요약통계량을 확인하고, 시각화를 할 수 있습니다.

> 2-3. tox21_Preprocessing  
> `tox21.xlsm`의 데이터 전처리 코드입니다.
> - 이용 패키지: pandas, numpy, rdkit
> - `rdkit` 패키지는 화학 데이터 처리에서 이용됩니다. 해당 노트에서는 `rdkit.Chem`을 통해 SMILES 문자열을 분자 객체로 변환하고, `rdkit.Chem.MACCSkeys`를 통해 분자의 특징을 이진 형식으로 표현한 MACCS 지문을 생성하는데 사용됩니다.

---

## 3. Model Fitting


아래의 10가지 모델을 통해 독성 유무 예측


* 3-1.Logistic_Regression


* 3-2.Decision_Tree_Classifier


* 3-3.Random_Forest_Classifier 


* 3-4.Gradient_Boosting_Classifier 


* 3-5.XGB_Classifier


* 3-6.LGBM_Classifier


* 3-7.Linear_Discriminant_Analysis


* 3-8.Quadratic_Discriminant_Analysis


* 3-9.PLS_Regression


* 3-10.MLP_Classifier

---

## 4. Model Evaluation

평가지표와 교차 검증을 통해 모델 성능 평가

### 4-1. Evaluation

모델을 구축하는 과정은 Training Data를 통해 모델에 Fitting 한 후, Test Data로 테스트하는 과정을 거칩니다.
실제 값과 예측 값의 차이를 의미하는 Error가 작은 Fit 한 모델을 만드는 것이 목적입니다.

1. 분류모델
- Confusion Matrix (Accuracy, Precision, Sensitivity, Specificity)
- F1 Score
- ROC AUC Curve
    
2. 회귀모델
- MSE
- MAPE
- R2 score

### Cross-Validation이란?
교차 검증(Cross-Validation)은 모델이 데이터를 얼마나 잘 일반화할 수 있는지를 평가하기 위해 데이터셋을 여러 부분으로 나눠 여러 번 학습-평가 과정을 반복하는 기법입니다. 과적합을 방지, 데이터 활용의 극대화, 성능의 안정성 평가, 모델 선택에 도움을 주기 위해 이용합니다.
- K-Fold 
- Stratified K-Fold
