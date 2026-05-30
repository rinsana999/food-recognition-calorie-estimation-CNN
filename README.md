# food-recognition-calorie-estimation-CNN
SMART FOOD RECOGNITION AND NUTRITION ANALYSIS SYSTEM USING DEEP LEARNING AND EFFICIENTNETB0.
----------------------------------------------------------------------------------------------
This project presents an advanced AI-powered dashboard for food image classification and calorie estimation using Convolutional Neural Networks (CNNs). The system automatically recognizes food categories from uploaded images and estimates nutritional values such as calories, carbohydrates, proteins, fats, fiber, sugar, and sodium.

DASHBOARD PREVIEW:
-----------------------
SMART FOOD PREDICTION INTERFACE
---------------------------------
<img width="1536" height="1024" alt="DASHBOARD" src="https://github.com/user-attachments/assets/2b65bdc8-c69f-4fdd-aabd-99a75293e772" />

DASHBOARD FEATURES:
----------------------
Feature	Description
🍔 Food Recognition	Detects food category from uploaded images|
🔥 Calorie Estimation	Predicts calorie values using nutrition dataset|
🥗 Nutrition Analysis	Displays protein, carbs, fat, fiber & sugar|
📊 Interactive Dashboard	User-friendly Streamlit frontend|
🧠 Deep Learning Model	CNN with EfficientNetB0 transfer learning|
📈 Visual Analytics	EDA graphs and performance metrics|
⚡ Real-time Prediction	Instant food classification|

Technologies Used:
-------------------
Category	         |    Technology
-------------------------------------
Deep Learning      :  TensorFlow / Keras|
CNN Architecture	 :  EfficientNetB0|
Frontend	         :  Streamlit|
Visualization	     :  Matplotlib & Seaborn|
Data Handling      : 	Pandas & NumPy|
Evaluation	          Scikit-learn|

Dataset Details:
------------------
Dataset	Food    -     11    |
Total Images	  -    ~16,000 |
Classes         -	   11 Food Categories|
Model Input Size -	 224 × 224  |
Framework        -	 TensorFlow / Keras  |
Dataset Type	Multiclass Image Classification

DATASET SOURCE: KAGGLE

MODEL PERFORMANCE:
------------------

| Metric              | Performance              |
| ------------------- | ------------------------ |
| Training Accuracy   | ~90%                     |
| Validation Accuracy | ~88%                     |
| Optimizer           | Adam                     |
| Loss Function       | Categorical Crossentropy |
| Transfer Learning   | EfficientNetB0           |

SAMPLE PREDICTION OUTPUT
-------------------------
<img width="1290" height="860" alt="csIKp9lmr2AueI3KliVfmX30SErNGQbRPCimiwafl2bX6jgyVZh28OLV8Dpdpl5aZBuolYqb3-jXhxqHcOHkNQzqw2OVKpnQFlWbAILyadLhuQWkx4xRfqI-9MpA1M2sxtpnP9rbonC1px4aOOeg3xncXBf9ziM3S8bRSE-cPtruPE3vGK4jZ5M4gZsXmHTS" src="https://github.com/user-attachments/assets/35e3969b-c001-485c-a664-ac74ebeb843a" />
Predicted Food : Rice
Confidence      : 96.4%

Calories        : 130 kcal
Protein         : 2.7 g
Carbohydrates   : 28 g
Fat             : 0.3 g
Fiber           : 0.4 g
Sugar           : 0.1 g
Sodium          : 1 mg

PROJECT STRUCTURE
------------------
Food-Recognition-CNN/
│

├── app.py

├── food11_model.h5

├── food11_calories_full.csv

├── Food_Recognition.ipynb

├── README.md

├── requirements.txt

└── sample_images/
