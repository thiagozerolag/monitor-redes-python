# 🔍 Monitor de Redes Gamer & Pericial (v3.5)

Este projeto foi desenvolvido para monitorar a estabilidade de conexões de rede em tempo real. É uma ferramenta essencial para diagnosticar oscilações em jogos online, otimizar fluxos de streaming e coletar evidências técnicas estruturadas (logs periciais) para auditoria de desempenho de operadoras de internet.

---

## 🎥 Demonstração do Funcionamento

---

## 🛠️ Novas Funcionalidades

* **Persistência de Logs em CSV:** O monitor agora salva o histórico de testes em tempo real dentro do arquivo `relatorio_pericial.csv` usando manipulação segura com `with open` no modo append (`'a'`). A estrutura das colunas é totalmente padronizada para integração e análise visual no **Power BI**.
* **Laudo Técnico Pericial Automatizado:** Ao encerrar o monitoramento (`Ctrl + C`), o sistema trata a exceção com segurança e gera um parecer técnico detalhado no terminal, classificando a rede (Excelente, Estável com Oscilação, Instabilidade Moderada ou Crítica) e explicando os impactos diretos na experiência do usuário.
* **Ajuste de Precisão Temporal:** Correção na formatação do carimbo de data e hora (`%d/%m/%Y`), garantindo conformidade com padrões de auditoria.
* **Feedback Visual Otimizado:** Uso de constantes de cores ANSI no terminal para facilitar a leitura rápida de status críticos e alertas de rede.

---

## 🚀 Como Utilizar

1. Certifique-se de possuir o **Python 3** instalado no seu sistema.
2. Faça o download do arquivo `monitor gamer.py`.
3. Abra o terminal na pasta do arquivo e execute:
   ```bash
   python "monitor gamer.py"

   

