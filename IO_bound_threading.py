"""
with ThreadPoolExecutor() でスレッドプールを作る
executor.map() で簡単にタスクを並列実行できる  (約 2 秒)
結果が順番通りに取得できる
"""

import concurrent.futures
import time


def io_task(name):
    print(f"{name} 開始")
    time.sleep(2)
    print(f"{name} 終了")
    return f"{name} 完了"


start = time.time()

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(io_task, [f"タスク{i+1}" for i in range(5)]))

end = time.time()
print(f"トータル時間: {end - start:.2f} 秒")
print("結果:", results)
