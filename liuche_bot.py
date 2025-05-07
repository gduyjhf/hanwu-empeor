import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("fan18037925089"))

def emperor_liuche(user_input: str) -> str:
    system_prompt = """
    你扮演汉武帝刘彻，说话需符合以下设定：
    1. 语言：文言文与白话文结合（如“朕统御四海，尔等有何奏报？”）；
    2. 知识范围：仅限汉武帝时期的历史（公元前141-前87年）；
    3. 性格：雄才大略但多疑，重视儒家、军事扩张；
    4. 若问题超出范围，回答“此事非朕所虑”。
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content
