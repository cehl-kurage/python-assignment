"""長方形の中に円が含まれるかを判定するプログラムを作成してください。
次のように、長方形は左下の頂点を原点とし、
右上の頂点の座標(W,H)が与えられます。
また、円はその中心の座標(x,y)と半径rで与えられます。"""
W, H, x, y, r = map(int, input().split())
right_lim = W - r
left_lim = r
upper_lim = H - r
lower_lim = r
# 長いけどこれくらいの方が僕は好き
x_isin_area = left_lim <= x <= right_lim
y_isin_area = lower_lim <= y <= upper_lim
# rが大きすぎる場合とかは必ずFalseになる
# 数学ではrが大きいとアウトな表記だが、内部的には and で結んでるのと同じなのでOK
if x_isin_area and y_isin_area:
    print("Yes")
else:
    print("No")
