# src/services/supabase_service.py

from supabase import create_client, Client
import os

# Initialize Supabase client
def get_supabase_client() -> Client:
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url or not key:
        raise ValueError("Missing Supabase credentials. Check .env file.")

    return create_client(url, key)


def save_report_to_db(file_name: str, extracted_text: str, analysis_result: str):
    """Insert report details into Supabase table."""
    try:
        supabase = get_supabase_client()
        data = {
            "file_name": file_name,
            "extracted_text": extracted_text,
            "analysis_result": analysis_result
        }
        response = supabase.table("reports").insert(data).execute()
        return response.data
    except Exception as e:
        return f"Error saving report to Supabase: {str(e)}"


def get_all_reports():
    """Fetch all reports from Supabase."""
    try:
        supabase = get_supabase_client()
        response = supabase.table("reports").select("*").order("id", desc=True).execute()
        return response.data
    except Exception as e:
        return f"Error fetching reports: {str(e)}"
