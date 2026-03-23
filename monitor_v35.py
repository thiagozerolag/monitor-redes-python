import subprocess
import re
import platform
import time

COR_POSITIVA = "\033[92m"
COR_DE_ERRO = "\033[91m"
COR_ESTAVEL = "\033[93m"
RESET = "\033[0m"

def analisar_rede(site):
    global HISTORICO
    sistema = platform.system().lower()
    parametro = '-n' if sistema == 'windows' else '-c'
    comando = ['ping', parametro, '10', site]

    try:
        saida = subprocess.check_output(comando, stderr=subprocess.STDOUT, universal_newlines=True)

        if sistema == 'windows':
            padrao_perda = r"\((\d+)% perda\)"
        else:
            padrao_perda = r"(\d+)% packet loss"

        busca = re.search(padrao_perda, saida)
        perda = busca.group(1) if busca else "0"
        HISTORICO.append(100 - int(perda))

        print(f"\nMonitoramento de: {site}")

        if int(perda) > 0:
            print(f"Status: {COR_DE_ERRO}QUEDA DETECTADA!{RESET}")
            print(f"Perda de Pacotes: {COR_DE_ERRO}{perda}%{RESET}")
        else:
            print(f"Status: {COR_POSITIVA}CONECTADO{RESET}.")
            print(f"Perda de Pacotes: {COR_POSITIVA}{perda}%{RESET}")

    except Exception as Erro_ao_investigar_servidor:
        print(f"{COR_DE_ERRO}Erro ao investigar servidor: {Erro_ao_investigar_servidor}{RESET}")
alvo = input("Qual servidor vamos investigar hoje ou IP:")

try:
    HISTORICO = []
    while True:
        analisar_rede(alvo)
        data_hoje = time.strftime("%d/%m/%Y")
        agora = time.strftime("%H:%M:%S")
        print(f"\n{COR_ESTAVEL}[{data_hoje}] - [{agora}] Aguardando 3 segundos para o próximo teste...('Ctrl + C para parar'){RESET}")
        time.sleep(3)

except KeyboardInterrupt:
    print(f"\n{COR_ESTAVEL}--- GERANDO RELATÓRIO PERICIAL FINAL ---.{RESET}")
    if HISTORICO:
        media = sum(HISTORICO) / len(HISTORICO)
        total_testes = len(HISTORICO)
        print(f"Total de testes realizados: {total_testes}")
        print(f"Índice de Estabilidade Geral: {COR_POSITIVA}{media:.1f}%{RESET}")
    
    print(f"\n{COR_ESTAVEL}Monitoramento encerrado Perito.{RESET}")

