# Gpay-Statement-Analysis
GPay & ICICI Bank Statement Analyzer App
This app will extract, process, and analyze transaction data from Google Pay (GPay) and ICICI Bank statements, helping users track spending, categorize expenses, and generate insights.

🚀 Features
✅ Extract transactions from GPay transaction history
✅ Auto-categorize expenses (Food, Shopping, Travel, Bills, etc.)
✅ Generate spending insights with charts & trends
✅ Detect anomalies (suspicious transactions, high spending)
✅ Export reports (CSV, PDF)

📌 Tech Stack
🔹 Backend: Python, Spark
🔹 Data Processing: Pandas

1️⃣ Extract Data from GPay Statements
GPay exports are HTML files. We’ll extract transactions from HTML. I first converted HTML into single column csv file 
this div tag had all the necessary info I needed content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1 -- recieved or sent 

🔍 Step 1: Read HTML file to csv

🔍 Step 2: Read GPay Statement (CSV)
  After that I loaded file into Data bricks(I am using community edition). Then started operating on the dataset.
  First priorites were seperating the data.
  
2️⃣ Categorize Expenses Automatically
We'll use keyword matching & AI (NLTK or OpenAI API) to categorize transactions.

3️⃣ Data Analysis & Insights
We’ll analyze wrongly categorized and try to fix the classification.

Then we work on insights month-based, year-based .. etc.

4️⃣ Web App with Streamlit

🚀 Running the App

✨ Future Enhancements
✅ AI-based anomaly detection (Flag unusual transactions) and AI Based learning
✅ Income vs. Expense analysis
✅ Budgeting & Alerts (Notify if exceeding a budget)

Would you like me to help deploy this as a web app or refine it further? 🚀
