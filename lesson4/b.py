"""
半径 r の円の面積と円周の長さを求めるプログラムを作成して下さい。
"""
# %%
import math
r = float(input())
area = math.pi * r ** 2
circumference = 2 * math.pi * r
print(f"{area:.6f} {circumference:.6f}")
