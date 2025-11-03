import os
from langchain_openai import ChatOpenAI
from config.prompts import HEALTH_REPORT_PROMPT
from dotenv import load_dotenv


load_dotenv()
llm=ChatOpenAI(
    temperature=0.4,
    api_key=os.getenv("OPENAI_API_KEY"),
)

def analyse_health_report(report_text:str)->str:
    """
    Uses ChatOpenAI to analyze extracted health report text.
    Returns a concise summary and interpretation.
    """
    try:
        prompt=HEALTH_REPORT_PROMPT.format(report_text=report_text)
        response=llm.invoke(prompt)
        return response.content.strip()
     
    except Exception as e:
        return f"Error analyzing report: {str(e)}"