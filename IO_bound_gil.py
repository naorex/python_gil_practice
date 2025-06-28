"""
完全に順番に実行される
2秒 × 5タスク → 約10秒かかる！
これが「I/Oバウンドの直列処理が遅い」ってやつ！
"""

import time


def io_task(name):
    print(f"{name} 開始")
    time.sleep(2)  # 2秒のI/O待ち（イメージ）
    print(f"{name} 終了")


start = time.time()

for i in range(5):
    io_task(f"タスク{i+1}")

end = time.time()
print(f"トータル時間: {end - start:.2f} 秒")
