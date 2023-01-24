import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(layout="wide")

#file_path = '/Users/yusukehashimoto/Library/CloudStorage/GoogleDrive-yusuke.hashimoto.b8@tohoku.ac.jp/.shortcut-targets-by-id/1U3Mz7R4Ox5IAA_LP704hqwlJxUBoDEoy/99_研究者マッチング/GteX_蓄電池.csv'
#df_s = pd.read_csv(file_path)

uploaded_file = st.file_uploader("Choose a file")

list_data = ['部門', '部局名', '職位', '総配分額の総額', '件数', '合計', '平均',
       '標準偏差', '職位サイズ', '性別', '年度末\n年齢',
       '総文献数', '国際共著文献数', '国際共著\n文献率（％）', '産学連携共著文献',
       '産学連携共著文献率（％）', '特許からの被引用', '閲覧回数', '総被引用数', '一報当たりの被引用数', 'FWCI\n平均',
       'FWCI\n中央値', 'FWCI\n最大値', 'Top1%文献数(FWCI)', 'Top1%文献率(FWCI)％',
       'Top10%文献数(FWCI)', 'Top10%文献率(FWCI)％', 'オープンアクセス文献数',
       'オープン\nアクセス\n文献率（％）', '著者数\n平均', '機関数\n平均']

with st.sidebar:
    data_x = st.selectbox(
        'x data',
        list_data,
        index=5
    )

    data_y = st.selectbox(
        'y data',
        list_data,
        index=23
    )

    data_color = st.selectbox(
        'color',
        list_data,
        index=0
    )

if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    df_s = pd.read_csv(uploaded_file)

    fig = px.scatter(
        df_s,
        x=data_x,
        y=data_y,
        color=data_color,
        hover_name='まとめ'
    )
    st.plotly_chart(fig, use_container_width=True)
