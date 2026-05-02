from agents.analysis_agent import analyze_question
from agents.nl2sql_agent import generate_sql
from agents.insight_agent import generate_insight
from tools.db import run_sql

def run_pipeline(question):
    analysis = analyze_question(question)
    sql = generate_sql(question)
    columns, rows = run_sql(sql)
    insight = generate_insight(question, columns, rows)

    return {
        "analysis": analysis,
        "sql": sql,
        "data": rows,
        "insight": insight
    }
