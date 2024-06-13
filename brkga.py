# Clara Andrade Sant´anna Santos - 22124
# Júlia Enriquetto de Brito      - 22139

import numpy as np
import matplotlib.pyplot as plt
import time as t


# 1. 
# indicar nossas coordenadas matriz
coordinates = [
    [(500, 500), (826, 465), (359, 783), (563, 182), (547, 438), (569, 676), (989, 416), (648, 750), (694, 978), (493, 969)],
    [(175, 89), (104, 130), (257, 848), (791, 249), (952, 204), (34, 654), (89, 503), (548, 964), (492, 34), (749, 592)],
    [(536, 875), (373, 708), (385, 260), (560, 751), (304, 516), (741, 368), (59, 131), (154, 681), (425, 456), (885, 783)],
    [(30, 415), (61, 25)]
]

# inidicar o numero da populacao que é o numero de cidades
# indicar o numero de gerações (eu escolho e pode ser bem alto)
num_cities = 31  # Número de cidades
num_salesmen = 3  # Número de caixeiros viajantes

# a partir dos dados a baixo a gente que decidiu os valores
population_size = 100  # Tamanho da população
elite_proportion = 0.2  # Proporção de elite
crossover_probability = 0.7  # Probabilidade de cruzamento
mutation_probability = 0.1  # Probabilidade de mutação
num_generations = 5000  # Número de gerações

#  transformar uma lista de listas em uma única lista contínua
flat_coordinates = [coord for sublist in coordinates for coord in sublist]

# calcular a distancia da matrix
def calculate_distance_matrix(coords):
    num_coords = len(coords)
    distance_matrix = np.zeros((num_coords, num_coords))
    for i in range(num_coords):
        for j in range(num_coords):
            distance_matrix[i, j] = np.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)
    return distance_matrix

distance_matrix = calculate_distance_matrix(flat_coordinates)

# 2. decoder 
# ordem as visitas (indices)
# aqui eu coloco as distancias de cada cidade
def decode_solution(keys, num_salesmen):
    num_cities = len(keys)
    cities = np.argsort(keys)  # Ordena as cidades baseadas nas chaves
    routes = [[] for _ in range(num_salesmen)]
    
    for i, city in enumerate(cities):
        routes[i % num_salesmen].append(city)
    
    return routes

# 3. Pegar a distancia total de todas de cada caixeiro e ver a qualidade desse caminho 
# ou seja, aqui é o inicio da avaliação
def evaluate_solution(routes, distance_matrix):
    total_distance = 0
    for route in routes:
        if route:
            route_distance = distance_matrix[0, route[0]]  # Do depósito à primeira cidade
            for i in range(len(route) - 1):
                route_distance += distance_matrix[route[i], route[i + 1]]
            route_distance += distance_matrix[route[-1], 0]  # Da última cidade ao depósito
            total_distance += route_distance
    return total_distance

# Inicialização da população
def initialize_population(population_size, num_cities):
    return np.random.rand(population_size, num_cities)

# 4. FITNESS PROBS = pegar os melhores caixeiros de melhor qualidade (30% das 100) 
# mais conhecido como ELITE :)
def select_elite(population, fitness, elite_proportion):
    elite_size = int(len(population) * elite_proportion)
    elite_indices = np.argsort(fitness)[:elite_size]
    return population[elite_indices], elite_indices

# 5. Leavar esses melhores caixeiros e pegar 70% para o crossing over
#  pegar sempre os primeiros valores de cada melhor caixeiro
# vai ser criado um novos caixeiros(filinhos)
def biased_crossover(parent1, parent2, bias=0.7):
    offspring = np.zeros(len(parent1))
    for i in range(len(parent1)):
        offspring[i] = parent1[i] if np.random.rand() < bias else parent2[i]
    return offspring

# 6. Levar 1% dos filinhos para as mutações
# mutação é trocar um valor aleatorio dentro do filinho por outro valor aleatorio
def mutate(solution, mutation_rate=0.1):
    for i in range(len(solution)):
        if np.random.rand() < mutation_rate:
            solution[i] = np.random.rand()
    return solution

# 7. Algoritmo BRKGA implementado
def brkga(num_cities, num_salesmen, population_size, num_generations, elite_proportion, crossover_probability, mutation_probability, distance_matrix):
    population = initialize_population(population_size, num_cities)
    best_solution = None
    best_fitness = float('inf')

    start = t.time()     # para desenhar o grafico

    for generation in range(num_generations):
        # Avaliação da população
        fitness = np.array([evaluate_solution(decode_solution(ind, num_salesmen), distance_matrix) for ind in population])
        
        # Seleção da elite
        elite, elite_indices = select_elite(population, fitness, elite_proportion)
        
        # Geração da nova população
        new_population = []
        while len(new_population) < population_size:
            if np.random.rand() < crossover_probability:
                parent1 = elite[np.random.randint(len(elite))]
                parent2 = population[np.random.randint(population_size)]
                offspring = biased_crossover(parent1, parent2)
            else:
                offspring = np.random.rand(num_cities)
            if np.random.rand() < mutation_probability:
                offspring = mutate(offspring, mutation_probability)
            new_population.append(offspring)
        
        population = np.array(new_population)
        
        # Atualiza a melhor solução
        min_fitness_idx = np.argmin(fitness)
        if fitness[min_fitness_idx] < best_fitness:
            best_fitness = fitness[min_fitness_idx]
            best_solution = population[min_fitness_idx]

    # para desenhor do grafico
    end = t.time()
    time = end - start  

    return best_solution, best_fitness, time


# EXEMPLO DE USO E RESULTADOS
best_solution_keys, best_fitness, elapsed_time = brkga(len(flat_coordinates), num_salesmen, population_size, num_generations, elite_proportion, crossover_probability, mutation_probability, distance_matrix)
best_solution_routes = decode_solution(best_solution_keys, num_salesmen)

print("Melhor solução encontrada:")
for i, route in enumerate(best_solution_routes):
    print(f"Caixeiro {i + 1}: {route}")
print(f"Distância total: {best_fitness}")


# Grafico TTT-Plot
# Função que gera o gráfico
def generate_graph():
    times = []
    for _ in range(100):
        best_known_solution, best_fitness, delta_times = brkga(len(flat_coordinates), num_salesmen, population_size, num_generations, elite_proportion, crossover_probability, mutation_probability, distance_matrix)
        times.append(delta_times)

    prob = [(i - 0.5) / 100 for i in range(1, 101)]  # cálculo para gerar a probabilidade acumulativa

    times.sort()

    fig, ax = plt.subplots()
    ax.autoscale()
    ax.margins(0.1)
    ax.scatter(times, prob)
    ax.set_title("TTT-Plot BRKGA")
    ax.set_xlabel("Time-To-Target")
    ax.set_ylabel("Accumulated probability")
    plt.show()

generate_graph()
