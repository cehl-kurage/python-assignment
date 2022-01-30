"""オンラインジャッジでは、提出されたプログラムが複数の入力データそれぞれに対して正しい出力を行っているかを判定するために、
１つの入力データファイルに複数のデータセットが含まれているものがあります。
この問題は、そのようなデータセットを処理するための練習問題です。

１つの整数 x を読み込み、それをそのまま出力するプログラムを作成して下さい。

ただし、この問題は以下に示すようにいくつかのデータセットが与えられることに注意して下さい。
"""
# %%
case = 0
while True:
    case += 1
    num = input()
    if num == "0":
        break
    print(f"Case {case}: {num}")
# %%