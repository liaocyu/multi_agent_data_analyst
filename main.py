from agents.coordinator import run_pipeline

if __name__ == "__main__":
    question = input("请输入你的分析问题：")
    result = run_pipeline(question)

    print("\n===== 分析结果 =====")
    print(result["insight"])
