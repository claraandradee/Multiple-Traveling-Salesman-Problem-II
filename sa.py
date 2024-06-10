# Clara Andrade Sant´anna Santos - 22124
# Júlia Enriquetto de Brito      - 22139

import math 

# Lê o n caixeiros e a n cidades
# Lê a solucao inicial

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
    add_distance = 0
    for v in mVet:
        distance_vector = 0
        for i in range(1, len(v)):
            p_previous = v[i - 1]
            p_current = v[i]
            distance = abs(p_current - p_previous)
            distance_vector += distance
        add_distance += int(distance_vector)
    return add_distance

# Exemplo de uso 
'''
add_distance = get_total_distance(result)
print("A soma das distâncias dos vetores é:", add_distance)
'''

# 1. Pega a solução inicial e quebra ela - SPLIT 
#    Após isso conta a distance total dela



# 2. Com os dados acima implementaremos na heurista SA


# 3. Grafico representativo