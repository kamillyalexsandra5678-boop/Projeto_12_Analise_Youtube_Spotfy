import streamlit as st
import pandas as pd

st.title("Tudo pra cima, nada pra baixo!")
st.sidebar.title("Escolha o seu Artista Favorito")
st.sidebar.image('Logo.png')  
#criando um df
df = pd.read_parquet('Dados_Artistas.parquet')

# Select Box ao lado
artistas = st.sidebar.selectbox('Selecione o Artista', df['Artist'].sort_values().unique())
df_artista = df[df['Artist'] == artistas]

#Informação da pagina principal
st.subheader(f'Os Artista que você curte estão todos aqui!😮‍💨')
st.subheader(f'O seguinte artista foi selecionado 👉 {artistas}')

# Looping
for index, row in df_artista.iterrows():
        with st.container():
            st.markdown(f"### 🎵 **{row['Track']}**")
            
            col1, col2 = st.columns(2)
            col1.metric("🎵 Spotify Streams", f"{row['Stream']:,.0f}")
            col2.metric("📺 YouTube Views", f"{row['Views']:,.0f}")
            
            st.video(row['Url_youtube'])
            st.markdown("---")
st.link_button('Ouça agora no Spotify', url=row['Url_spotify'], type='primary')