"""
GILの制限を受けないから、本当に並列で動く！
トータル時間はスレッドの時よりかなり短くなるはず！ (約 0.31 秒)
"""

import multiprocessing
import time


def cpu_task(name):
    print(f"{name} 開始")
    count = 0
    for _ in range(10**7):
        count += 1
    print(f"{name} 終了")


def main():
    start = time.time()

    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=cpu_task, args=(f"プロセス{i+1}",))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    end = time.time()
    print(f"トータル時間: {end - start:.2f} 秒")


if __name__ == "__main__":
    main()  # windows 環境では関数化して実行する必要あり
