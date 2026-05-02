from tools.llm import call_llm

def generate_insight(question, columns, rows):
    prompt = f'''
你是数据分析师，请解释数据结果：

用户问题：
{question}

数据：
columns: {columns}
rows: {rows}

输出：
- 关键发现
- 原因分析
- 建议
'''
    return call_llm(prompt)
