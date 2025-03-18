import numpy as np
import pandas as pd

# サンプルデータ作成
data = {'価格': [100, 102, 105, 103, 101]}
df = pd.DataFrame(data)

# 平均を計算
平均価格 = df['価格'].mean()

print(f"平均価格: {平均価格}")          