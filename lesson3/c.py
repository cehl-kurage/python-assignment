"""

２つの整数 x, y を読み込み、それらを値が小さい順に出力するプログラムを作成して下さい。

ただし、この問題は以下に示すようにいくつかのデータセットが与えられることに注意して下さい。
"""
# %%
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    x_y_sorted = sorted([x, y])
    print(*x_y_sorted)
# %%
# こうでもいいかな
while True:
    x_y = input()
    if x_y == "0 0":
        break
    x_y = map(int, x_y.split())
    x_y_sorted = sorted(x_y)
    print(*x_y_sorted)
