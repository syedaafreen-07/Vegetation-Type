# 🌲 Forest Cover Type Classification

A Machine Learning project to predict forest vegetation type using environmental and terrain features.

---

## 📌 Project Overview  
This project uses the **Forest Cover Type dataset** to classify land areas into one of **seven forest cover types** using features such as elevation, slope, aspect, soil types, wilderness area, and hydrology distances.  
The task is a **multi-class classification problem**.

---

## 📂 Steps Followed in the Project

### **1. Importing the Dataset**
- Loaded the dataset using pandas.
- Explored structure, shape, and data types.
- Checked basic statistics and attribute descriptions.

---

### **2. Data Preprocessing**
- Verified that the dataset contains no missing values.
- Scaled numerical features where necessary.
- Prepared one-hot encoded wilderness and soil features.
- Converted the target variable **Cover_Type** into categorical format (if needed).

---

### **3. Exploratory Data Analysis (EDA)**
- Visualized distributions of major features.
- Used histograms, boxplots, and pairplots for pattern understanding.
- Checked balance of the **Cover_Type** classes.

---

### **4. Correlation Analysis**
- Generated a correlation heatmap.
- Analyzed how major features relate to **Cover_Type**.
- Identified low-correlation or redundant attributes.

---

### **5. Feature Selection & Dropping Unnecessary Columns**
- Removed features that showed extremely low correlation.
- Eliminated redundant variables that did not affect learning.
- Validated that accuracy improved or stayed stable after feature removal.

---

### **6. Train-Test Split**
- Split the dataset into **train** and **test** sets (typically 80/20).
- Ensured shuffling for fair and random distribution.

---

### **7. Machine Learning Models Used**
Trained the following models for comparison:

- **Decision Tree Classifier**
- **Random Forest Classifier**
- **Extra Trees Classifier**
- **Gradient Boosting / Gradient Forest**
- **Support Vector Machine (SVM)**

Each model was evaluated using accuracy metrics on the test set.

---

### **8. Model Performance**
- Compared all model accuracies.
- **Extra Trees Classifier achieved the highest accuracy of 87%**, making it the best model for this dataset.

---

## 🎯 Final Result
The **Extra Trees Classifier** was selected as the final model, offering the best combination of accuracy, speed, and robustness in handling many features.

---

## 🛠️ Tools & Libraries Used
- **Python**
- **NumPy**, **Pandas**
- **Matplotlib**, **Seaborn**
- **Scikit-learn (sklearn)**

---

## 🚀 Conclusion
The project successfully predicts forest cover types using environmental features.  
After preprocessing, EDA, feature selection, and model comparison, the **Extra Trees model** delivered the best accuracy of **87%**.  
This model can be effectively used for forest management, vegetation analysis, and ecological planning.


