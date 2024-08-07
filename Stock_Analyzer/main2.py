import logging
from dotenv import load_dotenv
from crewai import Crew
from task import Stock_bot
from agents import Stock_bot_agents
import requests
import gradio as gr

def analyze_stock(stock):
    load_dotenv()
    stock = stock.strip()
    print(f"Stock name entered: {stock}")

    # Get Stock Symbol
    try:
        stock = stock.replace(" ", "")
        print(f"Searching for Stock Symbol of {stock}....")
        url = "https://query2.finance.yahoo.com/v1/finance/search"
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        params = {"q": stock, "quotes_count": 1}
        res = requests.get(url=url, params=params, headers={'User-Agent': user_agent})
        data = res.json()
        stock_symbol = data['quotes'][0]['symbol']
        print(f"Stock Symbol: {stock_symbol}")
    except:
        return "Stock Symbol not found"
        
    tasks = Stock_bot()
    agent = Stock_bot_agents()

    # Create agents
    stock_analysis = agent.stock_anaylsis()
    investment_analysis = agent.investment_analysis()

    # Create tasks
    stock_analysis_task = tasks.stock_analysis(stock_analysis, stock_symbol)
    investment_analysis_task = tasks.investment_analysis(investment_analysis, stock_symbol)

    # Execute tasks
    print("Creating Crew instance >>>>")

    stock_analysis_crew = Crew(
        agents=[stock_analysis],
        tasks=[stock_analysis_task],
        verbose=True,
        max_rpm=29
    )

    investment_analysis_crew = Crew(
        agents=[investment_analysis],
        tasks=[investment_analysis_task],
        verbose=True,
        max_rpm=29
    )

    result_stock_analysis = stock_analysis_crew.kickoff()
    result_stock_analysis_str = str(result_stock_analysis)
    stock_analysis_report = f"stock_analysis_{stock}.md"
    with open(stock_analysis_report, "w") as file:
        file.write(result_stock_analysis_str)

    result_investment_analysis = investment_analysis_crew.kickoff()
    result_investment_analysis_str = str(result_investment_analysis)
    investment_analysis_report = f"investment_analysis_{stock}.md"
    with open(investment_analysis_report, "w") as file:
        file.write(result_investment_analysis_str)

    return f"Reports generated:\n\nStock Analysis: {stock_analysis_report}\nInvestment Analysis: {investment_analysis_report}"

# Gradio interface
iface = gr.Interface(
    fn=analyze_stock,
    inputs="text",
    outputs="text",
    title="Stock Investment and Analysis BOT",
    description="Enter the stock name you want to analyze (e.g., Apple, TCS, Tata Motors, etc.)"
)

if __name__ == '__main__':
    iface.launch()