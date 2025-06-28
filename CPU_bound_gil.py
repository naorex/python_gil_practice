"""
これも完全に順番に実行される
1タスクに数秒かかるなら、全体で×5倍！ (約 0.9 秒)
GILの素の動きは基本これ
"""

import time


def cpu_task(name):
    print(f"{name} 開始")
    count = 0
    for _ in range(10**7):
        count += 1  # 重い計算
    print(f"{name} 終了")


start = time.time()

for i in range(5):
    cpu_task(f"タスク{i+1}")

end = time.time()
print(f"トータル時間: {end - start:.2f} 秒")
