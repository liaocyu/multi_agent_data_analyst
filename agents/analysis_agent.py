from tools.llm import call_llm

def analyze_question(question):
    prompt = f'''
你是数据分析专家，请拆解用户问题：

用户问题：
{question}

输出：
1. 分析目标
2. 需要的指标
3. 可能的维度
'''
    return call_llm(prompt)
