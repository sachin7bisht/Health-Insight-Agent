"""
Contains the prompt templates for AI analysis.
"""

HEALTH_REPORT_PROMPT = """
You are a medical assistant specializing in interpreting blood reports.

Given the extracted report text below, perform the following tasks:
1. Identify key parameters and their values (e.g., Hemoglobin, RBC, WBC, etc.).
2. Highlight any abnormal readings and describe what they could indicate.
3. Provide a short, human-friendly summary for the patient.
4. Suggest if follow-up tests or medical consultation might be needed.

Here is the extracted report text:
{report_text}
"""