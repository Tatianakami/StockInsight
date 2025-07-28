# 📈 Evolução do Preço das Ações - Projeto Streamlit

---

## 📋 Descrição

Este projeto é uma aplicação web interativa desenvolvida em **Python** com **Streamlit**, que permite a visualização da evolução dos preços de fechamento de ações selecionadas. Utiliza dados reais fornecidos pela API do **Yahoo Finance (yfinance)** para análise histórica e comparativa, exibindo gráficos dinâmicos e tabelas com dados detalhados.

O usuário pode selecionar múltiplas ações, escolher o período de análise, e obter a performance percentual de cada ativo no intervalo selecionado.

---

## ⚙️ Tecnologias e Bibliotecas

- Python 3.10+
- [Streamlit](https://streamlit.io/) — framework para aplicações web rápidas e interativas
- [pandas](https://pandas.pydata.org/) — manipulação e análise de dados
- [yfinance](https://github.com/ranaroussi/yfinance) — API para dados financeiros do Yahoo Finance
- [plotly](https://plotly.com/python/) — visualização interativa de gráficos

---

## 🚀 Funcionalidades

- Seleção múltipla de ações brasileiras e internacionais (ex.: ITUB4.SA, AAPL, AMZN)
- Filtro dinâmico por período via slider de datas
- Gráfico interativo da evolução dos preços de fechamento
- Tabela dos últimos preços disponíveis
- Cálculo e exibição da performance percentual de cada ação no período selecionado
- Interface amigável com barra lateral para filtros
- Mensagens informativas para casos sem dados ou seleção vazia

---

## 📷 Screenshots

<div align="center">
  <img src="/FOTO1.jpg" alt="Tela Inicial" width="700" />
</div>

---

<div align="center">
  <img src="/fot2.jpg" alt="Gráfico" width="350" />
</div>

---

<div align="center">
  <img src="/fot3.jpg" alt="Tabela e Performance" width="700" />
</div>

---

## 📝 Como executar localmente

### Pré-requisitos

- Python 3.10 ou superior instalado  
- Recomenda-se criar um ambiente virtual (venv)

### Passos

1. Clone este repositório:

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio

