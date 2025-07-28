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



![Tela Inicial](/FOTO1.jpg)

---



![Gráfico](/fot2.jpg)

---



![Tabela e Performance](/fot3.jpg)

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

Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Execute o aplicativo Streamlit:

bash
Copiar
Editar
streamlit run main.py
O navegador abrirá automaticamente a aplicação. Caso contrário, acesse http://localhost:8501

📁 Estrutura do projeto
bash
Copiar
Editar

├── main.py                
├── requirements.txt       
├── README.md              
└── imagens/ 

🤝 Contribuição
Contribuições são bem-vindas! Para colaborar:

Faça um fork deste repositório

Crie uma branch com a sua feature (git checkout -b feature/nome-da-feature)

Faça commit das suas alterações (git commit -m 'Adiciona nova feature')

Envie para o branch original (git push origin feature/nome-da-feature)

Abra um Pull Request para análise

📄 Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

👩‍💻 Desenvolvido por Tatiana Kami


GitHub: github.com/Tatianakami

LinkedIn: linkedin.com/in/tatianakami

🚀 Projeto desenvolvido para fins de estudo e portfólio pessoal.
