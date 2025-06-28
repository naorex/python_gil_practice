"""
各スレッドは「2秒待つだけ」のI/O処理。
マルチスレッドだと並列に動くから、全体で約2秒で終わる。
"""

import threading
import time


def io_task(name):
    print(f"{name} 開始")
    time.sleep(2)  # 2秒のI/O待ち（イメージとして）
    print(f"{name} 終了")


start = time.time()

threads = []
for i in range(5):
    t = threading.Thread(target=io_task, args=(f"スレッド{i+1}",))
    t.start()
    threads.append(t)

# すべてのスレッドが処理を完了するまでメインスレッドの実行を待機
for t in threads:
    t.join()

end = time.time()
print(f"トータル時間: {end - start:.2f} 秒")
