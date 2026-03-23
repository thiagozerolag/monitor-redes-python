🔍 Monitor de Redes Gamer & Pericial (v3.5)
Este projeto foi desenvolvido para monitorar a estabilidade de conexões de rede em tempo real. É uma ferramenta essencial para diagnosticar lag em jogos e para a coleta de evidências técnicas (logs) em contextos de perícia digital contra instabilidades de operadoras.

🛠️ Funcionalidades
Teste de Ping Automatizado: Verifica a comunicação contínua com servidores (Google, Cloudflare ou IPs de jogos).

Tratamento de Exceções: O sistema é resiliente e não interrompe o monitoramento mesmo em caso de queda total do sinal de internet.

Carimbo de Tempo (Timestamp): Cada teste gera um log com a data e hora exata da verificação.

Relatório de Estabilidade: Ao encerrar (Ctrl + C), o script calcula automaticamente a média de estabilidade geral da conexão baseada em todo o histórico da sessão.

🚀 Como Utilizar
Certifique-se de que possui o Python 3 instalado no seu sistema.

Faça o download do arquivo monitor_v35.py.

Abra o terminal na pasta do arquivo e execute:
python3 monitor_v35.py

Informe o site ou IP que deseja investigar e acompanhe os resultados em tempo real.

💻 Tecnologias Utilizadas
Python 3: Linguagem principal.

Bibliotecas Nativas:

subprocess: Para execução de comandos de rede do sistema operacional.

re (RegEx): Para mineração e extração precisa de dados dos pacotes.

platform: Para garantir compatibilidade entre Windows e Linux (Ubuntu).

time: Para manipulação de intervalos e formatação de datas.

📊 Exemplo de Relatório Final
Abaixo, um exemplo do monitoramento em ação e o relatório de auditoria gerado pelo sistema:

<img width="1142" height="208" alt="Captura de tela de 2026-03-23 00-07-58" src="https://github.com/user-attachments/assets/d60e8436-4218-4b20-8982-54dd2e4b540a" />



