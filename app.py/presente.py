import streamlit as st
import pandas as pd
import random
import os

# Configurando o título e o ícone da página
st.set_page_config(page_title="Presente de Aniversário 💝", page_icon="💖")

# Cabeçalho que fica fora do Expander
st.markdown("""
# 💖 Olá, namorada linda! Feliz Aniversário!!
            
## Enfim, seus 18 anos!! Já está sentindo a maioridade? haha!

Este é um presente feito com todo o carinho do mundo.  
Cada clique guarda uma lembrança, uma emoção e um pedacinho do meu amor por você. 🌸
""")

# Expander com 3 abas
with st.expander("✨ Clique aqui para abrir seu presente ✨", expanded=True):

    # Todas as abas
    tab1, tab2, tab3 = st.tabs(["💌 Mensagens", "📸 Memórias", "🎁 Surpresa"])

    # Aba 1 – Frases
    with tab1:
        frases = "data/frases_romanticas.csv"
        if frases:
            df = pd.read_csv(frases)
            frases = df['Mensagem'].dropna().tolist()
            if st.button("Clique para ver uma mensagem de amor 💗"):
                st.success(random.choice(frases))
        else:
            st.error("Arquivo de frases não encontrado.")

    # Aba 2 – Imagem
    with tab2:
        imagens_dir = "imagens"
        imagens = [img for img in os.listdir(imagens_dir) if img.endswith((".jpg", ".png", ".jpeg"))]

        if imagens:
            img_escolhida = random.choice(imagens)
            img_path = os.path.join(imagens_dir, img_escolhida)
            if st.button("Clique para ver nossas memórias 💗"):
                st.image(img_path, use_container_width=True, caption="Você é minha lembrança mais bonita 🌸")
        else:
            st.warning("Nenhuma imagem encontrada na pasta 'imagens'.")

    # Aba 3 – Surpresa (Decidir em breve)
    with tab3:
        if st.button("💍 Não clique aqui..."):
            st.balloons()
            st.markdown("Prometo te amar com leveza, carinho e intensidade. Hoje, amanhã e todos os dias. 💘")


st.markdown("---")

st.markdown("""
# 🌹 Como prova do nosso amor:

## Seguem fotos de outros momentos especiais que tivemos, minha princesa!

Caso você não se lembre de alguns desses momentos, é porque você ainda vai viver eles kkkkkkk  
Te amo. 🌸

""")


with st.expander("Quero construir uma vida com você!!! Nosso futuro:", expanded=True):

    tab4, tab5, tab6 = st.tabs(["💍 Casamento", "🏖️ Sweet Home Beach House", "⚽ Filhinhos"])

with tab4:
    if st.button("Clique para ver nosso belos casamento:"):
        foto_casamento = "C:/presente_namorada/imagens_personalizadas/foto_casamento.jpg"
        st.image(foto_casamento, use_container_width=True, caption="Na saúde e na Doença! 🌸")

with tab5:
    if st.button("Clique para ver nossa tão sonhada casa:"):
        foto_casa_propria = "C:/presente_namorada/imagens_personalizadas/casa_propria.jpg"
        st.image(foto_casa_propria, use_container_width=True, caption="Casa com carinha de casa! 🌸")

with tab6:
    if st.button("Clique aqui para ver nossa futura familia linda:"):
        foto_filhos = "C:/presente_namorada/imagens_personalizadas/foto_praia.jpg"
        st.image(foto_filhos, use_container_width=True, caption="Nossas combinações de genes! 🌸")

st.markdown("---")


# Lê todas as abas
df_amor = pd.read_csv("C:/presente_namorada/data/amor_por_meses_juntos.csv")
df_saudade = pd.read_csv("C:/presente_namorada/data/nivel_saudades_horas.csv")
df_momentos = pd.read_csv("C:/presente_namorada/data/felicidade_em_momentos.csv")
df_pensamentos = pd.read_csv("C:/presente_namorada/data/pensamentos_na_semana.csv")
df_palavras = pd.read_csv("C:/presente_namorada/data/frases_mais_faladas.csv")

import matplotlib.pyplot as plt

def create_pizza_chart(df):
    fig, ax = plt.subplots()
    ax.pie(df['porcentagem'], labels=df['frases mais faladas'], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # deixa o gráfico redondinho  
    return fig


st.markdown("""
# 📊 Estatísticas de Amor Geral:

## Esse é um resumo completamente PROFISSIONAL que aborda os principais indicadores de sentimento do Lele!

Caso haja alguma dúvida, fico à disposição!  
Atenciosamente, Leonardo Meduna.  
Te amo. 🌸
""")

with st.expander("Estatísticas Gerais de Sentimentos do Lele", expanded=True):
    
    tab_tabelas, tab_graficos = st.tabs(["📑 Tabelas", "📈 Gráficos"])
    
    with tab_tabelas:
        st.markdown("### Nível de Amor pela Malu")
        st.dataframe(df_amor, hide_index=True)

        st.markdown("### Nível de Saudade por hora do dia")
        st.dataframe(df_saudade, hide_index=True)

        st.markdown("### Nível de Felicidade por momento vivido")
        st.dataframe(df_momentos, hide_index=True)

        st.markdown("### Frequência de pensamentos nela (por dia da semana)")
        st.dataframe(df_pensamentos, hide_index=True)

        st.markdown("### Palavras mais faladas")
        st.dataframe(df_palavras, hide_index=True)

    with tab_graficos:
        st.markdown("### Gráfico de Amor Crescente 💘")
        st.line_chart(df_amor, x="Meses juntos", y="Nivel de Amor pela Malu")

        st.markdown("### Saudade ao longo do dia 🕒")
        st.line_chart(df_saudade, x="horas", y="saudade")

        st.markdown("### Felicidade por momentos vividos 🥰")
        st.bar_chart(df_momentos.set_index("momento"))

        st.markdown("### Pensamentos por dia da semana 🧠")
        st.bar_chart(df_pensamentos.set_index("dias da semana"))

        st.markdown("### Palavras mais faladas 💬")
        st.pyplot(create_pizza_chart(df_palavras))