"""
秒単位の時間 Sが与えられるので、
h:m:s
の形式へ変換して出力してください。
ここでhは時間、mは 60 未満の分、sは 60 未満の秒とします
Input:Sが一行で与えられる
"""
S = int(input())
hour = S // 3600
minutes = (S - 3600 * hour) // 60
seconds = S % 60
# フォーマット済み文字列リテラルを使ってほしい
print(f"{hour}:{minutes}:{seconds}")
