# Clara Andrade Sant´anna Santos - 22124
# Júlia Enriquetto de Brito      - 22139

import time as t
import math 
import copy
import random
import matplotlib.pyplot as plt


# Lê o n caixeiros e a n cidades
# Lê a solucao inicial
n_travells = 3
n_cities = 31
m_initial = [
    [(500, 500), (826, 465), (359, 783), (563, 182), (547, 438), (569, 676), (989, 416), (648, 750), (694, 978), (493, 969)],
    [(175, 89), (104, 130), (257, 848), (791, 249), (952, 204), (34, 654), (89, 503), (548, 964), (492, 34), (749, 592)],
    [(536, 875), (373, 708), (385, 260), (560, 751), (304, 516), (741, 368), (59, 131), (154, 681), (425, 456), (885, 783)],
    [(30, 415), (61, 25)]
]



# 1. Metodo SPLIT 
# Esse metodo tem como objetivo dividir igualmente a quantidade de cidades para cada caixeiro 
def middle_split(lst, n):
    length = len(lst)
    div, rest = divmod(length, n)  # length é o dividendo e n é o divisor - div é o resultado da divisão e rest o resto
    parts = []
    
    start = 0
    for i in range(n):
        part_size = div + (1 if i == (n // 2) else 0)
        end = start + part_size
        part = lst[start:end]
        if part:  
            part = [0] + part + [0]
        parts.append(part)
        start = end
    
    return parts

# 2. Metodo get_distance 
# esse metodo agora só conta a distancia quando o vetor já está com o split
def get_total_distance(mVet):
    distance_vector = []
    for sublist in mVet:
        for v in sublist:
            if isinstance(v, list) and all(isinstance(i, tuple) and len(i) == 2 for i in v):
                sublist_distance = 0
                for i in range(1, len(v)):
                    p_previous = v[i - 1]
                    p_current = v[i]
                    distance = math.sqrt((p_current[0] - p_previous[0])**2 + (p_current[1] - p_previous[1])**2)
                    sublist_distance += round(distance)  # Arredondando para o inteiro mais próximo
                distance_vector.append(sublist_distance)
    return distance_vector


# 3. Com os dados acima implementaremos na heurista SA
def swap(current_solution):
    i = random.choice(range(len(current_solution)))
    j = random.choice(range(len(current_solution)))
    current_solution[i], current_solution[j] = current_solution[j], current_solution[i]
    return current_solution

def get_neighbors(current_solution):
    return swap(current_solution)

def annealing(initial_solution, n_maximum_iterations, verbose=False):

    start = t.time()

    current_temperature = 100
    alpha = (1 / current_temperature) ** (1.00 / n_maximum_iterations)
    current_solution = initial_solution
    best_known_solution = initial_solution

    for k in range(n_maximum_iterations):
        neighbor_solution = get_neighbors(copy.deepcopy(current_solution))
        delta = sum(get_total_distance(current_solution)) - sum(get_total_distance(neighbor_solution))

        if delta > 0 or random.uniform(0, 1) < math.exp(float(delta) / float(current_temperature)):
            current_solution = neighbor_solution

        if sum(get_total_distance(current_solution)) < sum(get_total_distance(best_known_solution)):
            best_known_solution = current_solution
            if verbose:
                print(k, current_temperature, sum(get_total_distance(best_known_solution)))

        current_temperature = alpha * current_temperature

    end = t.time()

    time = end - start
   
    return best_known_solution, time


# EXEMPLO DE USO E RESULTADOS
solucao_initial = middle_split(m_initial, n_travells)
result = get_total_distance(solucao_initial)
print("A soma das distâncias dos vetores é:", result)

best_known_solution, execution_time = annealing(initial_solution=solucao_initial, n_maximum_iterations=100, verbose=True)
print("Melhor solução conhecida:", best_known_solution)
print("Distância total da melhor solução:", get_total_distance(best_known_solution))
print("Tempo de execução:", execution_time)

# Grafico TTT-Plot
# Função que gera o gráfico
def generate_graph():
    times = []
    for _ in range(100):
        best_known_solution, delta_times = annealing(initial_solution=solucao_initial, n_maximum_iterations=500, verbose=False)
        times.append(delta_times)

    prob = [(i - 0.5) / 100 for i in range(1, 101)]  # cálculo para gerar a probabilidade acumulativa

    times.sort()

    fig, ax = plt.subplots()
    ax.autoscale()
    ax.margins(0.1)
    ax.scatter(times, prob)
    ax.set_title("TTT-Plot Annealing Graphic")
    ax.set_xlabel("Time-To-Target")
    ax.set_ylabel("Accumulated probability")
    plt.show()

generate_graph()


