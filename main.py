import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="📈 Gráfico de Ações", layout="wide")

# Título central
st.markdown("""
    <h1 style='text-align: center;'>📈 Evolução do Preço das Ações</h1>
    <p style='text-align: center;'>Selecione uma ou mais ações e o período desejado para visualizar a evolução dos preços de fechamento.</p>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("🔎 Filtros")

# Lista de ações disponíveis
acoes_disponiveis = [
    "ITUB4.SA", "PETR4.SA", "VALE3.SA",
    "AAPL", "GOOGL", "AMZN", "META", "NFLX", "TSLA",
    "BBAS3.SA", "BBDC3.SA", "BBDC4.SA",
    "ABEV3.SA", "WEGE3.SA", "LREN3.SA", "MGLU3.SA", "AZUL4.SA"
]

# Seletor de ações
lista_acoes = st.sidebar.multiselect(
    label="📌 Escolha os códigos das ações:",
    options=acoes_disponiveis,
    default=["ITUB4.SA", "PETR4.SA", "VALE3.SA"]
)

# Definindo as datas para o slider como datetime.date
data_inicio = datetime(2015, 1, 1).date()
data_fim_max = datetime(2024, 1, 1).date()

# Slider para intervalo de datas
data_inicial, data_final = st.sidebar.slider(
    "📅 Período de Análise:",
    min_value=data_inicio,
    max_value=data_fim_max,
    value=(datetime(2020, 1, 1).date(), datetime(2024, 1, 1).date()),
    format="DD/MM/YYYY"
)

# Função para carregar dados da ação
@st.cache_data
def carregar_dados(ticker):
    try:
        df = yf.Ticker(ticker).history(start="2015-01-01", end="2024-01-01")
        df = df[["Close"]].dropna()
        df.index = pd.to_datetime(df.index)
        return df
    except:
        return pd.DataFrame()

# Carregando dados e processando
if lista_acoes:
    dados = {}
    for acao in lista_acoes:
        df = carregar_dados(acao)
        if not df.empty:
            dados[acao] = df

    if dados:
        # Concatenar preços de fechamento
        df_final = pd.concat([df["Close"].rename(acao) for acao, df in dados.items()], axis=1)

        # Filtrar pelo período selecionado
        df_final = df_final[(df_final.index.date >= data_inicial) & (df_final.index.date <= data_final)]

        if not df_final.empty:
            st.subheader("📊 Gráfico de Preço de Fechamento")

            df_plot = df_final.reset_index().melt(id_vars="Date", var_name="Ação", value_name="Preço")

            fig = px.line(
                df_plot,
                x="Date",
                y="Preço",
                color="Ação",
                title="Preço de Fechamento das Ações",
                labels={"Date": "Data", "Preço": "Preço de Fechamento"},
                template="plotly_white"
            )
            st.plotly_chart(fig, use_container_width=True, config={"scrollZoom": True})

            # Tabela últimos 5 dias
            st.subheader("📋 Tabela de Fechamento (últimos 5 dias disponíveis)")
            st.dataframe(df_final.tail())

            # Cálculo de performance no período (primeiro e último valor válido)
            st.subheader("📈 Performance no Período Selecionado")

            perf = {}
            for acao in df_final.columns:
                serie = df_final[acao].dropna()
                if not serie.empty:
                    variacao = ((serie.iloc[-1] / serie.iloc[0]) - 1) * 100
                    perf[acao] = variacao
                else:
                    perf[acao] = float('nan')

            perf_df = pd.DataFrame.from_dict(perf, orient='index', columns=["Performance (%)"])
            perf_df["Performance (%)"] = perf_df["Performance (%)"].map(lambda x: f"{x:.2f}%" if pd.notnull(x) else "Sem dados")
            st.dataframe(perf_df)

        else:
            st.error("⚠️ Nenhum dado disponível para o período selecionado.")
    else:
        st.error("⚠️ Nenhum dado válido foi carregado.")
else:
    st.markdown("""
        <div style='text-align: center;'>
            <h3>⚠️ Nenhuma ação selecionada.</h3>
            <p>Escolha uma ou mais ações no menu lateral para visualizar os dados.</p>
            <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="Cachorro esperando" width="300"/>
        </div>
    """, unsafe_allow_html=True)

# Rodapé
st.markdown("""
<br><hr><br>
<p style='text-align: center; font-size: 16px; color: gray;'>
    🔧 Desenvolvido por <strong>Tatiana Kami</strong>
</p>
""", unsafe_allow_html=True)


