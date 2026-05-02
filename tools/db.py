from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///sample.db")

def run_sql(sql):
    with engine.connect() as conn:
        result = conn.execute(text(sql))
        rows = result.fetchall()
        columns = result.keys()
    return columns, rows
