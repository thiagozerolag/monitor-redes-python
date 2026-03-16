import os
import time 

COR_POSITIVA = '\033[92m'
COR_DE_ERRO = '\033[91m'
COR_ESTAVEL = '\033[93m'
RESET = '\033[0m'

print(f"{COR_ESTAVEL}===MONITOR PERICIAL GAMER v3.0 ==={RESET}")

site = input("Qual servidor vamos investigar hoje? ")
HISTORICO = []

try:
    while True:
        status = os.system(f"ping -c 1 {site} > /dev/null 2>&1")
        horario = time.strftime("%D/%M/%Y %H:%M:%S")

        if status == 0:
            print(f"[{horario}] Status:{COR_POSITIVA} CONECTADO {RESET}")
            HISTORICO.append(1)
        else:
            print(f"[{horario}] Status :{COR_DE_ERRO} QUEDA DETECTADA!{RESET}\a")
            HISTORICO.append(0)

        
        SUCESSOS = sum(HISTORICO)
        TOTAL = len(HISTORICO)
        ESTABILIDADE = (SUCESSOS / TOTAL) * 100

        print(f"Estabilidade Atual: {COR_ESTAVEL}{ESTABILIDADE:.1f}%{RESET}")
        print("-" * 35)

        time.sleep(5)
except KeyboardInterrupt:
    print(f"\n{COR_ESTAVEL} Gerando relatório final...{RESET}")
    print(f"Total de testes: {len(HISTORICO)}")
    print(f"Taxa de sucesso: {(sum(HISTORICO)/len(HISTORICO))*100:.1f}%")
    

