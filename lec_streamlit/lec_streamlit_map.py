from pydeck.bindings import layer
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import pydeck as pdk

#東京近郊のmap
# 2次元マッピング
tokyo_lat = 35.69   #緯度
tokyo_lon = 139.69  #経度

df_tokyo = pd.DataFrame(
    np.random.randn(1000,2)/[50,50]+[tokyo_lat, tokyo_lon],     #東京近傍に乱数をプロット
    columns=['lat', 'lon']
)

df_tokyo

st.map(df_tokyo)

#3次元マッピング
# ①viewの設定
view = pdk.ViewState(latitude=tokyo_lat, longitude=tokyo_lon, pitch=50, zoom=11)
    # picht 角度
#②レイヤーの設定
# Define a layer to display on a map
hexagon_layer = pdk.Layer(
    "HexagonLayer",
    data=df_tokyo,
    get_position=['lon', 'lat'],
    elevation_scale=5,              #６角形のビンの高さ
    radius=5,                     #binの半径の幅
    extruded=True,                  #６角形の立体感の有無
)
#③deckの設定
layer_map = pdk.Deck(layers=hexagon_layer, initial_view_state=view)

#④グラフを呼び出す
st.pydeck_chart(layer_map)