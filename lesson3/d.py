"""
３つの整数 abcを読み込み、
aからbまでの整数の中に、cの約数がいくつあるかを求めるプログラムを作成してください。
"""
# %%
cnt = 0
a, b, c = map(int, input().split())
for i in range(a, b + 1):
    if c % i == 0:
        cnt += 1
print(cnt)

# %%
# こっちの方が好き
# True Falseは1, 0として扱える
a, b, c = map(int, input().split())
counter = 0
for i in range(a, b + 1):
    is_divisor = c % i == 0
    counter += is_divisor
print(counter)
# %%
