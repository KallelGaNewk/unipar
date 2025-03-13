# prioridade.py
# Implementação do escalonamento por prioridade de threads em Python

import time

# Cria uma Classe para representar uma Thread
class Processo:
    def __init__(self, thread_id, tempo, prioridade):
        # Definimos aqui os atributos da Thread, para que possamos acessá-los posteriormente
        self.thread_id = thread_id
        self.tempo = tempo
        self.prioridade = prioridade

    def tarefa(self):
        print(f"Thread {self.thread_id} iniciada, executando por {self.tempo}ms...")
        time.sleep(self.tempo / 1000) # Simula o tempo de execução da thread
        print(f"Thread {self.thread_id} finalizada!")
        return self.tempo

# Tempo de execução para cada thread (em milissegundos)
tempos_de_execucao = [5, 10, 3]
# Prioridade de cada thread (quanto menor, maior a prioridade)
prioridades = [1, 0, 2]

# Cria as threads com base nos tempos de execução e prioridades
threads = [Processo(i+1, tempo, prioridades[i]) for i, tempo in enumerate(tempos_de_execucao)]

# Ordena as threads por prioridade
threads.sort(key=lambda x: x.prioridade)

total_time = 0

# Inicia as threads
for thread in threads:
    total_time += thread.tarefa()

print(f"Todas as threads finalizadas em {total_time}ms!")
