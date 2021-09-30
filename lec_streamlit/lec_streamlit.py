# インタラクティブ機能

from typing import Tuple
import streamlit as st
from PIL import Image
import pandas as pd
import time

#ボタン
option_button = st.button('ボタン１')

if option_button == True:
    st.write('Hello python')
else:
    st.write('ボタンを押してください')

# ラジオボタン

option_radio = st.radio(
        "あなたの好きな果物を選んでください",
        ('APPLE', 'ORANGE', 'BANANA', 'OTHERS')
)
st.write('あなたが選んだ果物は:', option_radio)

#チェックボックス
option_check = st.checkbox('DataFrameの表示')

df = pd.DataFrame({
    'first column' : [1, 2, 3, 4],
    'second column': [40, 30, 20, 10]
})

if option_check == True :
    st.write(df)


# セレクトボックス
option_select = st.selectbox(
    '選択してください',
    ('A', 'B', 'C', 'D'))
st.write('あなたが選んだ選択肢は：',option_select)



# マルチセレクト
# セレクトボックスから２つ以上選択
option_multiselect = st.multiselect(
    '好きな色を選択してください',
    ['赤', '青', '黄', '緑'],       #セレクトボックスでの選択肢
    ['赤', '青']                    #デフォルトで表示するもの
 )


#スライダー
age = st.slider(
    '年齢を選択してください',
     min_value=0,   #スライダーの最小値
     max_value=130, #スライダーの最大値
     step=1,        #スライダーの刻み
     value=20       #スライダーの開始位置
)
st.write('あなたの年齢は；',age, 'です')

#スライダーで範囲を指定する場合
values = st.slider(
    '数値の範囲を入力してください',
    0.0,            #MAX
    100.0,          #MIN
    (25.0, 75.0))   #Default
st.write('Values:', values)



# サイドバー
height = st.sidebar.slider(
    'あなたの身長を選択してください',
     min_value=0,   #スライダーの最小値
     max_value=250, #スライダーの最大値
     step=1,        #スライダーの刻み
     value=170       #スライダーの開始位置
)
st.write('あなたの身長は；',height, 'cmです')

gender =  st.sidebar.selectbox(
    'あなたの性別を教えてください',
    ['男性', '女性'])
st.write('あなたの性別は',gender, 'です')



# プログレスバー
# 進捗状況の可視化など
# Time関数をインポートしておく

progress_button = st.button('プログレスボタン')
if progress_button == True:
    st.write('処理を開始します')
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete+1)
    st.text('処理が終了しました')
else:
    st.write('プログレスボタンを押してください')