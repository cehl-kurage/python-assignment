"""
n個の整数a_i(i = 1, 2, ...n)
を入力し、それらの最小値、最大値、合計値を求めるプログラムを作成してください。
"""
# %%
_ = int(input())
a = list(map(int, input().split()))
print(min(a), max(a), sum(a))
"""
ちなみに、list(map)としないとmax(a)のところでエラーになる
mapはイテレータとして各要素を出した後空配列になってしまうのかも
"""
