import os
import time

COR_POSITIVA = '\033[92m'
COR_DE_ERRO = '\033[91m'
COR_ESTAVEL = '\033[93m'
RESET = '\033[0m'

print(f"{COR_ESTAVEL}===MONITOR PERICIAL GAMER v3.0 ==={RESET}")

site = input("Qual servidor vamos investigar hoje? ")
HISTORICO =[]

arquivo_nome = "relatorio_pericial.csv"
if not os.path.exists(arquivo_nome):
    with open(arquivo_nome,"w") as arquivo:

        arquivo.write("Data_Hora,Servidor,Status,Estabilidade_Percentual\n")
    

try:
    while True:
        status = os.system(f"ping -c 1 {site} > /dev/null 2>&1")

        horario = time.strftime("%d/%m/%Y %H:%M:%S")

        if status == 0:
            status_texto = "CONECTADO"
            print(f"[{horario}] STATUS: {COR_POSITIVA}{status_texto}{RESET}")
            HISTORICO.append(1)
        else:
            status_texto = "QUEDA DETECTADA"
            print(F"[{horario}] Status: {COR_DE_ERRO}{status_texto}!{RESET}")
            HISTORICO.append(0)
            
        SUCESSOS = sum(HISTORICO)
        TOTAL = len(HISTORICO)
        ESTABILIDADE = (SUCESSOS / TOTAL) * 100
         
        if ESTABILIDADE == 100:
            classificacao = f"{COR_POSITIVA}EXCELENTE (Sem perdas){RESET}"
        elif ESTABILIDADE >= 80 and ESTABILIDADE < 90:
            classificacao = f"{COR_ESTAVEL}BOA (Oscilação aceitável){RESET}"
        elif ESTABILIDADE>= 50 and ESTABILIDADE < 80:
            classificacao = f"{COR_DE_ERRO}ALERTA (Instabilidade na rede){RESET}"
        else:
            classificacao = f"{COR_DE_ERRO}CRÍTICA (Alto Índice de quedas){RESET}"

        print(f"Estabilidade Atual: {COR_ESTAVEL}{ESTABILIDADE:.1f}%{RESET} -> {classificacao}")
        print("-" * 35)

        with open(arquivo_nome, "a") as arquivo:

            arquivo.write(f"{horario},{site},{status_texto},{ESTABILIDADE:.1f}\n")
       
        time.sleep(5)
    
except KeyboardInterrupt:
    print("\n\n" + "=" * 40)
    print("GERANDO RELATÓRIO FINAL DA PERÍCIA")
    print("=" * 40)
    total_testes = len(HISTORICO)
    if total_testes > 0:
        sucessos_finais = sum(HISTORICO)
        taxa_sucesso = (sucessos_finais / total_testes) * 100
        print(f"Total de testes realizados:{total_testes}")
        print(f"Taxa de sucesso final:{taxa_sucesso:.1f}%")
    else:
        print ("Nenhu dado foi coletado.")
        print("=" * 40)
        

