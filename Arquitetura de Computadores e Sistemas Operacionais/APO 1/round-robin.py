# round-robin.py
# Implementação do escalonamento Round Robin

import time

# Queue é tipo um array, mas com operações específicas para filas
from queue import Queue

# Definição dos tempos de execução (em milissegundos)
tempos_de_execucao = [5, 10, 3]
quantum = 1  # Quantum de tempo em ms


class Processo:
    def __init__(self, id, tempo_total):
        self.id = id
        self.tempo_restante = tempo_total
        self.tempo_total = tempo_total

    def executar(self, tempo):
        # Checa se o tempo a ser executado é menor que o tempo restante
        # Se for, executa pelo tempo restante, senão, executa pelo tempo do quantum
        tempo_executado = min(tempo, self.tempo_restante)
        time.sleep(tempo_executado / 1000)  # Converte ms para segundos
        return tempo_executado

    def finalizado(self):
        return self.tempo_restante <= 0


def escalonador_round_robin(processos, quantum):
    fila = Queue()

    # Adiciona todos os processos à fila
    for processo in processos:
        fila.put(processo)

    # Executa até que todos os processos sejam finalizados
    while not fila.empty():
        processo_atual = fila.get()

        # Executa o processo pelo tempo do quantum ou pelo tempo restante
        tempo_executado = processo_atual.executar(quantum)
        print(
            f"Processo {processo_atual.id} executando por {tempo_executado}ms... (Restante: {processo_atual.tempo_restante}ms)"
        )
        processo_atual.tempo_restante -= tempo_executado

        # Verifica se o processo foi finalizado
        if not processo_atual.finalizado():
            # Se não foi finalizado, coloca de volta na fila
            fila.put(processo_atual)
        else:
            print(
                f"Processo {processo_atual.id} finalizado após {processo_atual.tempo_total}ms de execução total!"
            )


# Criar processos
# Esse syntax parece estranho, mas é equivalente a dar append em uma lista dentro do for loop
processos = [Processo(i + 1, tempo) for i, tempo in enumerate(tempos_de_execucao)]

# Iniciar o escalonador Round Robin
print("Iniciando simulação Round Robin com quantum =", quantum, "ms")
escalonador_round_robin(processos, quantum)
print("Simulação de escalonamento Round Robin concluída.")
