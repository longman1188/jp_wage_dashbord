import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #matplotlibを使えるようにする

# streamlit でグラフを表示
# streamlitのグラフ生成関数を使用する

df = pd.DataFrame(np.random.randn(20, 3), 
                columns=['a', 'b', 'c',])
df

st.line_chart(df)   #折線
st.area_chart(df)   #面グラフ
st.bar_chart(df)    #棒グラフ

# matplotlib
# streamlitと違いインタラクティブな動作はできない
fig = plt.figure(figsize=(10, 5))
ax = plt.axes()
x = [105, 210, 301, 440, 500]
y = [10, 20, 30, 50, 60]
ax.plot(x, y)

st.pyplot(fig)
