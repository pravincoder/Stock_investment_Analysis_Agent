
# Project Name: Multi-Agent Stock Investment and Analysis Platform

### Output(Working Demo)

Once you have successfully done every step mentioned below.
You can also Play around .


https://github.com/user-attachments/assets/26c7ec92-955e-4a6e-98af-ac9a8404d9f3

## Overview

This project is a robust and scalable multi-agent stock investment and analysis platform built using a **Flask** backend and a **Next.js** frontend, leveraging **CrewAI** for sophisticated multi-agent interactions. The platform is designed to provide detailed insights and recommendations for stock investments by utilizing a multi-agent approach, enabling users to make informed decisions even with limited prior knowledge of stocks and market analysis.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
   - [Fast Installation](#fast-installation-via-docker)
   - [Normal Installation](#normal-installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Multi-Agent Analysis**: Utilizes CrewAI to deploy multiple agents for in-depth stock analysis and investment recommendations.
- **User-Friendly Interface**: Intuitive and responsive interface built with Next.js to enhance user experience.
- **Real-Time Data**: Provides real-time stock data and insights to aid in decision-making.
- **Secure and Scalable**: Flask backend ensures the platform is secure and can scale as needed.

## Tech Stack

- **Backend**: Flask
- **Frontend**: Next.js
- **AI/ML Integration**: CrewAI,LangChain
- **Database**: None (For Now)
- **APIs**: YahooFinance Api using yfinance Package
- **Env**:Conda

## Installation
###  Fast Installation (Via Docker)

#### Prerequisites
- **Docker**: Make sure Docker is installed on your system. You can download it from the [official Docker website](https://www.docker.com/get-started).
### Steps to Run Using Docker
1. Clone the repository: See [Backend Setup Step 1 Command](#backend-setup) 
2. Setup Environments : See [Env Setup](#environment-variable-setup)
3. Change Directory to Stock_Analyzer:- 
 ```bash 
   cd Stock_investment_Analysis_Crew/Stock_Analyzer
  ```
4.Docker Build Both Frontend and Backend with Compose (Can even build Frontend and Backend Seperately using *docker build Dockerfile*)
```bash 
   docker-compose build
  ``` 
5.Docker Run build (replace 'up' with 'down' before recreating build)
```bash 
   docker-compose up
  ```

## Normal Installation
### Prerequisites

- Python 3.10+
- Node.js 14+
- npm or yarn
- Conda 20+

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/pravincoder/Stock_investment_Analysis_Agent.git
   ```
2. Navigate to the Main directory:
   ```bash
   cd Stock_investment_Analysis_Agent/Stock_Analyzer
   ```
3. Create  a conda environment:
   ```bash
   conda env create -f environment.yml
   ```
4. Activate the Conda Environment:
   ```bash
   conda activate stock_guru
   ```
5. Run the Flask development server:
   ```bash
   python app.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd nextjs_app
   ```
2. Install the dependencies:
   ```bash
   npx create-next-app@latest --js --tailwind --eslint
   ```
   Keep every option default while setting up the app.
3. Run the Next.js development server:
   ```bash
   npm run dev
   ```
Note:- You need to execute both the backend Flask app and the Frontend as we are using cross connection with flask-cors.

## Environment Variable Setup
### `.env` File Setup 
Create  a .env file and add the below code :- (Make sure to add the api keys from the specified platforms)
#### *Note:- Use .sample.env by renaming as .env and add your Keys.* 
```dotenv
# API Key for GROQ
GROQ_API_KEY=your_groq_api_key_here

# API Key for OpenAI
OPENAI_API_KEY=your_openai_api_key_here

# Base URL for OpenAI API (default for local setup)
OPENAI_API_BASE=http://localhost:11434/v1

# Model name for OpenAI (adjust based on available models)
OPENAI_MODEL_NAME=mistral:latest

# Optional: API Key for LangChain
LANGCHAIN_API_KEY=your_langchain_api_key_here

# Optional: Enable LangChain tracing
LANGCHAIN_TRACING_V2=true
```

### (Optional) Using Local LLM with Ollama
- Use the  files in the setup folder to create a LLama3 , Mistral8b ... or your own LLM model 

- Commands/steps to setup ollama llm comming soon!

## Usage

Once the servers are running, you can access the application in your browser by navigating to `http://localhost:3000`. 

- **Dashboard**: Begin by exploring the dashboard for a quick overview of stock market trends.
- **Stock Analysis**: Use the analysis tools to select specific stocks and view detailed insights provided by the AI agents.
- **Recommendations**: Get tailored investment recommendations based on your portfolio and risk profile.

## API Endpoints

The Flask backend exposes several API endpoints that can be used for data retrieval and interaction:


- `POST /analyze-stock`: Analyze a stock and return Analysis and Investment reports in Markdown format.


  
(Detailed documentation for each endpoint can be provided here. In near future we might make a seperate api endpoints for both reports.)

## Contributing

We welcome contributions! To get started:

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

Please ensure your code adheres to the project's coding standards and passes all tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions, issues, or suggestions, please contact:

- **Project Maintainer**: [Pravin Maurya](mailto:pravincoder@gmail.com)
- **GitHub**: [PravinCoder](https://github.com/pravincoder)

---
