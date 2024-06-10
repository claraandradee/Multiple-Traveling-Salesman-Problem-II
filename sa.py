# Clara Andrade Sant´anna Santos - 22124
# Júlia Enriquetto de Brito      - 22139

import math 

# Lê o n caixeiros e a n cidades
# Lê a solucao inicial
n_travells = 7
n_cities = 113
m_initial = [
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

# Metodo SPLIT 
# Esse metodo tem como objetivo dividir igualmente a quantidade de cidades para cada caixeiro 
def middle_split(lst, n):
    length = len(lst)
    div, rest = divmod(length, n)  # length é o dividendo e n é o divisor - div é o resultado da divisão e rest o resto
    parts = []
    
    start = 0
    for i in range(n):
        part_size = div + (1 if i == (n // 2) else 0)
        end = start + part_size
        parts.append(lst[start:end])
        start = end
    
    return parts

# Exemplo de uso
'''
vetor = [10, 20, 25, 155, 4, 2, 0, 74, 15]
partes = 4
result = middle_split(vetor, partes)
print(result)
'''

# Metodo get_distance 
def get_total_distance(mVet):
    total_distance = 0
    for sublist in mVet:
        for v in sublist:
            distance_vector = 0
            for i in range(1, len(v)):
                p_previous = v[i - 1]
                p_current = v[i]
                distance = math.sqrt((p_current[0] - p_previous[0])**2 + (p_current[1] - p_previous[1])**2)
                distance_vector += distance
            total_distance += distance_vector
    return total_distance

# Exemplo de uso 
'''
add_distance = get_total_distance(result)
print("A soma das distâncias dos vetores é:", add_distance)
'''

# gerando a solução inicial dos dados iniciais
solucao_initial = middle_split(m_initial, n_travells)
# result = get_total_distance(solucao_initial)
# print(result)

# 1. Pega a solução inicial e quebra ela - SPLIT 
#    Após isso conta a distance total dela - CONCERTAR ISSO AQUI
def summing_distances(solucao_initial, n):
    total_sum = 0
    for _ in range(20):
        distance = get_total_distance(solucao_initial)
        total_sum += distance
        solucao_initial = middle_split(solucao_initial, n)
    return total_sum

print(summing_distances(solucao_initial, n_travells))

# 2. Com os dados acima implementaremos na heurista SA


# 3. Grafico representativo