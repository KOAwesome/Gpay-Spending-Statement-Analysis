GPay Statement Analysis

GPay Statement Analyzer App

This app extracts, processes, and analyzes transaction data from Google Pay (GPay) and ICICI Bank statements. It helps users track their spending, categorize expenses, and generate useful insights.

Click here to view a sample analysis.

Features

Extracts transactions from GPay transaction history
Automatically categorizes expenses (e.g., Food, Shopping, Travel, Bills)
Generates spending insights with charts and trends
Detects anomalies like suspicious transactions or unusually high spending
Allows exporting of reports in CSV and PDF formats
Tech Stack

Backend: Python, Apache Spark
Data Processing: Pandas
How It Works

1. Extract Data from GPay Statements
Google Pay exports are provided as HTML files. These files are parsed to extract transaction data.
I first converted the HTML into a single-column CSV file. The div tag with the class:

content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1
contained the necessary transaction details like whether money was received or sent.

Step 1: Convert HTML to CSV
The HTML is parsed and the relevant text is extracted and saved as a CSV.

Step 2: Read the CSV in Databricks
After uploading the CSV to Databricks (Community Edition), I began separating and structuring the data to make it usable for analysis.

2. Automatic Expense Categorization

Expense categories are assigned using a keyword-matching approach. For better accuracy, NLP tools such as NLTK or OpenAI APIs can be integrated to classify transactions more intelligently.

3. Data Analysis & Insights

Misclassified transactions are reviewed and corrected. Further analysis is performed based on various time frames such as monthly or yearly spending trends.

How to Use

Go to Google Takeout
Select Google Pay and download your transaction history
Open the downloaded folder, locate My Activity.html
Upload the file into the application for analysis
Future Enhancements

AI-based anomaly detection to flag unusual transactions
Detailed income vs. expense summaries
Budgeting tools and alert features (e.g., overspending notifications)
Fully deployed web app using Streamlit for user interaction
