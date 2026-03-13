import os
import time 

print("-----------------------------------------")
print("    MONITOR DE CONEXÃO DO THIAGO v1.0"    )
print("-----------------------------------------")

#Pergunta qual site queremos testar
site = input("Qual site ou IP de jogo você quer testar? ")

print(f"Entendido! Vou verificar o estado de: {site}")

# O comando para o terminal Linux(enviar 1 pacotinho de dados)
comando = f"ping -c 1 {site}"

# Agora o Python executa o comando e guarda a resposta
status = os.system(comando)
# O LOOP começa aqui! Tudo o que estiver 'empurado' paraa direita vai repetir
try:
    while True:
        comando = f"ping -c 1 {site}"
        status = os.system(comando)

# Mostrando o verdedito
        if status == 0:
            print(f"{site} Servidor Ativo!")
        else:
            print(f"ALERTA: O site {site} Servidor CAIU!")
        # Isso cria ou abre o arquivoe escreve o resultado ládentro
        with open("log_rede.txt", "a") as arquivo:
            arquivo.write(f"Site:{site} - Status: {status} - Hora: {time.ctime()}\n")

        print("Aguardando 10 segundos...(Ctrl + C para parar)")
        time.sleep(10)    # Aqui o programa tira uma 'soneca' de 10 segundos

except KeyboardInterrupt:
    print("\nMonitoramento encerrado!")
    

