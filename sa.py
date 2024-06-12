# Clara Andrade Sant´anna Santos - 22124
# Júlia Enriquetto de Brito      - 22139

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
    total_distance = 0
    for sublist in mVet:
        for v in sublist:
            if isinstance(v, list) and all(isinstance(i, tuple) and len(i) == 2 for i in v):
                distance_vector = 0
                for i in range(1, len(v)):
                    p_previous = v[i - 1]
                    p_current = v[i]
                    distance = math.sqrt((p_current[0] - p_previous[0])**2 + (p_current[1] - p_previous[1])**2)
                    distance_vector += round(distance)  # Arredondando para o inteiro mais próximo
                total_distance += distance_vector
    return total_distance


# 3. Com os dados acima implementaremos na heurista SA
def swap(current_solution):
    i = random.choice(range(len(current_solution)))
    j = random.choice(range(len(current_solution)))
    current_solution[i], current_solution[j] = current_solution[j], current_solution[i]
    return current_solution

def get_neighbors(current_solution):
    return swap(current_solution)

def annealing(initial_solution, n_maximum_iterations, verbose=False):
    current_temperature = 100
    alpha = (1 / current_temperature) ** (1.00 / n_maximum_iterations)
    current_solution = initial_solution
    best_known_solution = initial_solution

    for k in range(n_maximum_iterations):
        neighbor_solution = get_neighbors(copy.deepcopy(current_solution))
        delta = get_total_distance(current_solution) - get_total_distance(neighbor_solution)

        if delta > 0 or random.uniform(0, 1) < math.exp(float(delta) / float(current_temperature)):
            current_solution = neighbor_solution

        if get_total_distance(current_solution) < get_total_distance(best_known_solution):
            best_known_solution = current_solution
            if verbose:
                print(k, current_temperature, get_total_distance(best_known_solution))

        current_temperature = alpha * current_temperature

    return best_known_solution


# EXEMPLO DE USO E RESULTADOS
solucao_initial = middle_split(m_initial, n_travells)
result = get_total_distance(solucao_initial)
print("A soma das distâncias dos vetores é:", result)

best_known_solution = annealing(initial_solution=solucao_initial, n_maximum_iterations=10000, verbose=True)
print("Melhor solução conhecida:", best_known_solution)
print("Distância total da melhor solução:", get_total_distance(best_known_solution))


