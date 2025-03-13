# prioridade.py
# Implementação do escalonamento por prioridade de threads em Python

import threading
import time

# Cria uma Classe para representar uma Thread
class Thread:
    def __init__(self, thread_id, tempo, prioridade):
        # Criamos aqui a Thread da biblioteca threading, mas não a iniciamos
        self.thread = threading.Thread(target=self.tarefa, args=(thread_id, tempo))

        # Definimos aqui os atributos da Thread, para que possamos acessá-los posteriormente
        self.tempo = tempo
        self.prioridade = prioridade

    def tarefa(self, thread_id, tempo_execucao):
        print(f"Thread {thread_id} iniciada, executando por {tempo_execucao} segundos...")
        time.sleep(tempo_execucao) # Simula o tempo de execução da thread
        print(f"Thread {thread_id} finalizada!")

# Tempo de execução para cada thread (em segundos)
tempos_de_execucao = [2, 4, 1, 3, 5]
# Prioridade de cada thread (quanto menor, maior a prioridade)
prioridades = [3, 1, 5, 2, 0]

# Cria as threads com base nos tempos de execução e prioridades
threads = [Thread(i+1, tempo, prioridades[i]) for i, tempo in enumerate(tempos_de_execucao)]

# Ordena as threads por prioridade
threads.sort(key=lambda x: x.prioridade, reverse=True)

start_time = time.time()

# Inicia as threads
for thread in threads:
    thread.thread.start()

# Espera todas as threads finalizarem
for thread in threads:
    thread.thread.join()

end_time = time.time()

print(f"Todas as threads finalizadas em {end_time - start_time} segundos!")
