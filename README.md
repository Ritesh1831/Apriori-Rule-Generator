# 🛒 Market-Basket-Analysis(Apriori-Rule-Generator)
Used the Apriori algorithm to predict what else a person will buy based on their purchase.

## 📌 Overview  
This project demonstrates **Market Basket Analysis** using the **Apriori algorithm** to discover association rules from transaction data.  
The application allows users to:

- Upload a dataset of transactions.  
- Apply the **Apriori algorithm** with user-defined thresholds for **Support**, **Confidence**, and **Lift**.  
- Generate association rules in a **tabular format**.  
- Download the results as a `.csv` file.  

The project includes both:
- A **Flask web application** for interactive rule generation.  
- A **Jupyter Notebook** for exploratory data analysis and testing.  

---

## 📂 Folder Structure  
```
Market-Basket-Analysis/
│
├── static/               # Static assets (CSS, JS, images)
├── templates/            # HTML templates for Flask
│   └── index.html
├── uploads/              # Stores uploaded datasets
├── results/              # Stores generated association rules (CSV)
│
├── app.py                # Flask web application
├── apriori_code.ipynb    # Jupyter Notebook for experiments
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .render.yaml          # Deployment configuration (for Render/Cloud hosting)


---

## 🚀 Features
✔ Upload your transaction dataset (`.csv` or `.txt`)  
✔ Customize **support**, **confidence**, and **lift** thresholds  
✔ Generate rules dynamically using **Apriori**  
✔ View results in an interactive **HTML table**  
✔ Download results as **association_rules.csv**  
✔ Web app built with **Flask** + **Bootstrap**  

---

## ⚙️ Tech Stack
- **Python** (Data Processing, Apriori Algorithm)  
- **Flask** (Backend Web Framework)  
- **Pandas** (DataFrame operations)  
- **Apyori** (Apriori implementation)  
- **HTML, CSS (Bootstrap)** (Frontend)  

---

## 📊 Apriori Algorithm
The **Apriori Algorithm** is used to extract rules of the form:  

\[
\text{IF Item A is bought, THEN Item B is likely to be bought.}
\]

### Key Metrics:
- **Support**: Frequency of the itemset in transactions.  
- **Confidence**: Probability of purchase of RHS given LHS.  
- **Lift**: Strength of the rule compared to random chance.  

Example rule:  
```
{Bread} → {Butter}  
Support = 0.3 | Confidence = 0.7 | Lift = 1.5
```


---

## 🖥️ How It Works (Flask App Flow)
1. User uploads a dataset of transactions.  
2. Flask saves the dataset in `/uploads`.  
3. Dataset is read line-by-line into transaction lists.  
4. Apriori algorithm generates rules using user-defined thresholds.  
5. Results are converted into a **pandas DataFrame**.  
6. Sorted by **Lift** and displayed on the webpage.  
7. User can **download results as CSV**.  

---

# Thank You


