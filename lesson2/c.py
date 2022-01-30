"""
３つの整数を読み込み、それらを値が小さい順に並べて出力するプログラムを作成して下さい。
"""
#numsはジェネレータ（map）であってlistではないよというのは伝えるべきか？
#%%
nums = map(int, input().split())
# %%
nums = sorted(nums)
#イテレータのunpackingをつかってほしい
print(*nums)
# %%
