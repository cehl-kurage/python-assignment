"""
２つの整数 a, b と１つの演算子 op を読み込んで、a op b を計算するプログラムを作成して下さい。
ただし、演算子 op は、"+"(和)、"-"(差)、"*"(積)、"/"(商)、のみとし、
割り算で割り切れない場合は、小数点以下を切り捨てたものを計算結果とします。
Input:
op が '?' のとき 入力の終わりを示します。このケースの出力は行ってはいけません
"""
# %%
# これがすっきり
while True:
    # str型のreplaceメソッドは第一引数を第二引数に置き換える
    calculation = input().replace("/", "//")
    if "?" in calculation:
        break
    result = eval(calculation)
    print(result)
