# fifo.py
# Implementação do escalonamento FIFO (First In, First Out)

import time

# Definição dos tempos de execução (em milissegundos)
tempos_de_execucao = [5, 10, 3]


class Processo:
    def __init__(self, id, tempo_total):
        self.id = id
        self.tempo_total = tempo_total

    def executar(self):
        print(f"Processo {self.id} iniciando execução por {self.tempo_total}ms...")
        time.sleep(self.tempo_total / 1000)  # Converte ms para segundos
        print(f"Processo {self.id} finalizado após {self.tempo_total}ms de execução!")
        return self.tempo_total


def escalonador_fifo(processos):
    print("Iniciando simulação FIFO/FCFS")
    tempo_total_execucao = 0
    tempo_espera_total = 0

    for processo in processos:
        print(f"Processo {processo.id} esperou {tempo_total_execucao}ms")
        tempo_espera_total += tempo_total_execucao

        # Executa o processo do início ao fim sem interrupção
        tempo_execucao = processo.executar()
        tempo_total_execucao += tempo_execucao

    tempo_espera_medio = tempo_espera_total / len(processos)
    print("\nEstatísticas da simulação:")
    print(f"Tempo total de execução: {tempo_total_execucao}ms")
    print(f"Tempo médio de espera: {tempo_espera_medio}ms")


# Criar processos
processos = [Processo(i + 1, tempo) for i, tempo in enumerate(tempos_de_execucao)]

# Iniciar o escalonador FIFO
escalonador_fifo(processos)
print("Simulação de escalonamento FIFO/FCFS concluída.")
