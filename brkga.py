import numpy as np

# 1. 
# indicar nossas coordenadas matriz
coordinates = [
    [(500, 500), (354, 887), (594, 824), (973, 340), (66, 245), (251, 403), (426, 346), (114, 203), (587, 752), (341, 515)],
    [(941, 723), (101, 10), (774, 432), (35, 344), (54, 311), (720, 88), (2, 28), (106, 624), (444, 698), (126, 631)],
    [(451, 351), (72, 972), (413, 995), (450, 930), (302, 118), (111, 448), (981, 57), (757, 721), (141, 424), (636, 889)],
    [(228, 186), (979, 146), (336, 868), (323, 213), (688, 216), (949, 617), (404, 678), (799, 34), (119, 381), (620, 29)],
    [(391, 812), (207, 723), (863, 665), (282, 824), (614, 66), (382, 216), (496, 645), (241, 934), (206, 287), (262, 793)],
    [(568, 833), (356, 468), (528, 818), (409, 265), (549, 471), (895, 116), (213, 723), (703, 615), (713, 985), (80, 970)],
    [(943, 187), (314, 137), (540, 251), (14, 598), (477, 460), (660, 518), (139, 623), (584, 975), (694, 953), (650, 362)],
    [(886, 637), (84, 752), (910, 718), (43, 680), (998, 683), (261, 406), (441, 439), (627, 393), (50, 754), (28, 841)],
    [(954, 655), (839, 279), (955, 723), (21, 823), (987, 384), (49, 623), (501, 550), (393, 348), (302, 227), (495, 374)],
    [(468, 668), (154, 262), (484, 611), (554, 848), (968, 870), (470, 518), (917, 3), (781, 829), (804, 773), (991, 297)],
    [(820, 629), (259, 24), (956, 921), (773, 973), (859, 681), (549, 1), (585, 435), (954, 797), (33, 173), (961, 136)],
    [(687, 424), (342, 263), (426, 877), (915, 244)]
]

# inidicar o numero da populacao que é o numero de cidades
# indicar o numero de gerações (eu escolho e pode ser bem alto)
num_cities = 10  # Número de cidades
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

    return best_solution, best_fitness


# EXEMPLO DE USO E RESULTADOS
best_solution_keys, best_fitness = brkga(len(flat_coordinates), 3, population_size, num_generations, elite_proportion, crossover_probability, mutation_probability, distance_matrix)
best_solution_routes = decode_solution(best_solution_keys, 3)

print("Melhor solução encontrada:")
for i, route in enumerate(best_solution_routes):
    print(f"Caixeiro {i + 1}: {route}")
print(f"Distância total: {best_fitness}")
