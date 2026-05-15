# BizGenius 🚀
## AI-Based Startup Idea Validation and Success Prediction System
BizGenius is an AI-powered platform built to help founders validate their startup ideas before they go all in. Instead of relying on expensive consultants or gut feeling, founders can enter their startup details and get instant, data-driven insights on whether their idea has what it takes.

## Tech Stack

| Layer                              | Technologies / Tools Used                               |
| ---------------------------------- | ------------------------------------------------------- |
| **Frontend**                       | React.js, Tailwind CSS                                  |
| **Backend API**                    | FastAPI                                                 |
| **Web Scraping & Data Collection** | BeautifulSoup, Requests                                 |
| **Machine Learning Models**        | Scikit-learn, Random Forest, Gradient Boosting, XGBoost |
| **Data Processing & Analysis**     | Pandas, NumPy                                           |
| **Vector Database / RAG**          | ChromaDB                                                |
| **LLM Integration**                | LLaMA 3.3 via Groq API                                  |
| **Data Visualization**             | Matplotlib, Seaborn                                     |
| **Report Generation**              | Python PDF Libraries, PPTX Automation                   |
| **Programming Language**           | Python 3.9+                                             |


## What it does
BizGenius is an AI-powered startup validation platform that tells founders within minutes whether their business idea has real potential. A user simply enters their startup details:
🏢 Business domain & idea description 📅 Company age & funding history 👥 Team size & number of investors 💰 Funding per round

BizGenius then delivers a complete startup intelligence report across 5 key outputs:

1.Success Prediction Using a Random Forest Classifier trained on 3,000 startup records, the system predicts whether the startup falls into one of three categories: Success Uncertain Failure Along with a confidence probability score for each category.

2.Funding Estimation A Gradient Boosting Regressor predicts how much funding the startup is likely to raise in its next round, with a prediction error of just 2.27% MAPE.

3.Ecosystem Analysis Load synthetic dataset Generate: startup distribution graphs city-wise success rates funding trend analysis

4.Competitor Analysis Using a RAG (Retrieval-Augmented Generation) system powered by ChromaDB, BizGenius finds semantically similar startups from its database and benchmarks the user's idea against real market patterns.

5.AI Strategic Insights LLaMA 3.3 (via Groq) processes the ML predictions and competitor data to generate:

6.Risk factors & mitigation strategies Competitive differentiation advice Step-by-step 30-day action plan Investor-ready narrative summary

7.Automated Report & Pitch Deck With one click, BizGenius generates:
A downloadable PDF business report A professional PPTX investor pitch deck

Our Data Foundation Unlike tools that rely purely on generic or synthetic data, BizGenius is grounded in real startup intelligence:
Crunchbase : funding rounds, investor data, company stages Wikipedia : company histories, founding details, market domains Other public startup directories : geographic and sector data
The scraped dataset of ~300 real startup records was then statistically augmented to 3,000 records using log-normal, Poisson, and exponential distributions preserving real-world correlations while solving the problem of startup data scarcity.


## System Design 
<img width="1024" height="768" alt="Blue and White Simple Warranty Claim Process Flowchart (4)" src="https://github.com/user-attachments/assets/bd2b8e0c-a593-4324-8543-75e474cad28c" />

## Usage

Open the app in your browser
1.Browse the ecosystem dashboard to understand current startup trends

2.Navigate to the prediction section and enter your startup details

3.Click Predict & Analyse

4.Review your success score, risk level, competitor insights, and AI strategy

5.Download your PDF report or investor pitch deck




