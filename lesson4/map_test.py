# %%
input = "まだある"
maped = map(lambda x: x, input.split())
print(type(maped))
# <class 'map'>
for i in maped:
    print(i)
    # まだある
print(type(maped))
for i in maped:
    print(i)
    # なにも出力されない
"""
ジェネレータだから最後まで生成したらイテレーションはストップする
"""
