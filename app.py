# Importa módulos Schedule e Time
import schedule
import time

# Função(tarefa) a ser executada
def minha_tarefa():
    print("Executando minha tarefa...")

# Agenda a tarefa para executar em horários específicos
schedule.every().day.at("17:35").do(minha_tarefa)
schedule.every().day.at("17:36").do(minha_tarefa)
schedule.every().day.at("17:37").do(minha_tarefa)
schedule.every().day.at("17:38").do(minha_tarefa)
schedule.every().day.at("17:39").do(minha_tarefa)

while True:
    # Executa as tarefas agendadas
    schedule.run_pending()  

    # Evita sobrecarga da CPU
    time.sleep(1)  


