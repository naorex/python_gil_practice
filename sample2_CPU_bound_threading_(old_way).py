"""
各スレッドが「重い計算」してるだけ。
PythonだとGILのせいで順番に処理されるから、時間はほぼ「5倍」かかる。 (約 0.93 秒)
"""

import threading
import time


def cpu_task(name):
    print(f"{name} 開始")
    count = 0
    for _ in range(10**7):
        count += 1  # 重い計算（CPUフル稼働）
    print(f"{name} 終了")


start = time.time()

threads = []
for i in range(5):
    t = threading.Thread(target=cpu_task, args=(f"スレッド{i+1}",))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()
print(f"トータル時間: {end - start:.2f} 秒")
