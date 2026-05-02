from tools.llm import call_llm

SCHEMA = '''
Table: sales
columns: date, product, region, revenue
'''

def generate_sql(question):
    prompt = f'''
你是SQL专家，根据表结构生成SQL：

表结构：
{SCHEMA}

用户问题：
{question}

只输出SQL，不要解释
'''
    return call_llm(prompt)
