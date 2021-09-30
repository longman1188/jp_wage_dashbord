import streamlit as st
import pandas as pd

st.title('タイトル表示')
st.header('ヘッダーの表示')
st.subheader('サブヘッダーの表示')
st.text('テキストの表示')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [40, 30, 20, 10]
})

st.write(df)

st.dataframe(df)
st.dataframe(df, width=200, height=200)
st.dataframe(df.style.highlight_max(axis=0))

st.table(df)

#マジックコマンド

df

x = 100
x

# """の中に文字を入れると表示できる

"""
# マジックコマンドを使ってみる
文字列

```Python
import streamlit as st
print('Hello Streamlit')
```
"""

