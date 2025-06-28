"""
ThreadPoolExecutor を ProcessPoolExecutor にするだけでマルチプロセスに切り替えられる！
めっちゃお手軽にGILフリー並列が実現できる！  (約 0.36 秒)
"""

import concurrent.futures
import time


def cpu_task(name):
    print(f"{name} 開始")
    count = 0
    for _ in range(10**7):
        count += 1
    print(f"{name} 終了")
    return f"{name} 完了"


def main():
    start = time.time()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(cpu_task, [f"タスク{i+1}" for i in range(5)]))

    end = time.time()
    print(f"トータル時間: {end - start:.2f} 秒")
    print("結果:", results)


if __name__ == "__main__":
    main()  # windows 環境下では関数化する必要あり
