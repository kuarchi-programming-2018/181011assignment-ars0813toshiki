﻿# coding: utf-8
'''
演習課題「スライムの合計体重を出力！」
右側のコードエリアにあるプログラムは、出現するスライムの匹数をランダムに生成します。
スライムの体重は、すべて体重100キロです。そして、
「体重100キロのスライムがXX匹あらわれた」と表示します。

そこで、スライムの合計体重を計算して、「スライムの合計体重はYYキロです」と表示してください。

プログラムを実行して、正しく出力されれば演習課題クリアです！

 期待する出力値
体重100キロのスライムがXX匹あらわれた
スライムの合計体重はYYキロです
'''
import random
number = random.randint(1, 10)  # 匹数 1 ～ 10
print("体重100キロのスライムが" + str(number) + "匹あらわれた")
# 合計体重 = 匹数 x 100


total=number*100
print("スライムの合計体重は"+str(total)+"キロです。")
