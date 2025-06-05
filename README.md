Retail Sales Data Analysis & Insights

An exploratory data analysis (EDA) project using Pandas for data manipulation, Seaborn for visualization, and a Large Language Model (LLM) for generating automated insights from a sample sales dataset.

📊 About the Dataset

This project analyzes a sample Superstore sales dataset. It contains detailed, row-level information about customer orders for a retail company. The data includes order details, customer information, product categorization, and sales figures, making it ideal for comprehensive business performance analysis.

Key columns include:

Order ID & Order Date

Customer ID, Customer Name, & Segment

Country, City, State, & Region

Product ID & Product Name

Category & Sub-Category

Sales

🔎 Key Analyses Performed

This analysis explores the dataset from multiple angles to uncover actionable insights. The core components of the analysis are:

Sales Performance Analysis

Total sales by region, state, and city to identify top-performing markets.

Sales trends over time (monthly, quarterly, yearly) to spot seasonal patterns and growth.

Average order value and sales distribution analysis.

Customer Analysis

Customer segmentation analysis (Consumer vs. Corporate vs. Home Office).

Identification of top customers by total sales volume.

Geographic distribution and regional preferences of customers.

Product Analysis

Identification of best-selling categories and sub-categories.

Product performance ranking by sales volume.

Category-wise sales contribution analysis.

Operational & Geographic Insights

Analysis of shipping mode preferences and their relation to customer segments.

Calculation of order processing times (Ship Date - Order Date).

Mapping of state-wise and city-wise sales performance.

🛠️ Tools & Technologies

Language: Python 3.13+

Data Manipulation: Pandas

Data Visualization: Seaborn, Matplotlib

Analysis Environment: Jupyter Notebook / JupyterLab

Insight Generation: Large Language Model (LLM)

📋 Requirements

Python: 3.13+ (recommended)

Package Manager: pip

Virtual Environment: venv or virtualenv

🚀 Quick Start
1. Clone the Repository
git clone https://github.com/yourusername/smart-sales-summary.git
cd smart-sales-summary

1. Set Up a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

🐧 Linux/macOS
python3 -m venv venv
source venv/bin/activate
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END
🪟 Windows Command Prompt
python -m venv venv
venv\Scripts\activate
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Cmd
IGNORE_WHEN_COPYING_END
3. Install Dependencies

Install all the necessary libraries from the requirements.txt file.

pip install -r requirements.txt
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END

1. Launch Jupyter and Run the Analysis

Start the Jupyter Notebook server to open and run the analysis file.

jupyter notebook
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END

This will open a new tab in your web browser. Navigate to the main analysis notebook (e.g., analysis.ipynb) and run the cells to see the data processing, visualizations, and insights.

🚨 Troubleshooting
Common Issues

Virtual Environment Not Activating?

Ensure you're in the project's root directory.

On Windows, you might need to adjust your script execution policy. Run PowerShell as Administrator and execute: Set-ExecutionPolicy RemoteSigned -Scope CurrentUser.

Dependencies Not Installing?

Make sure your virtual environment is active.

Upgrade pip first: pip install --upgrade pip

Clear the pip cache if issues persist: pip cache purge

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

Explore the notebook to see how raw sales data is transformed into actionable insights! 🚀