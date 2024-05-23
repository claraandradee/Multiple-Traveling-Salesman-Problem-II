# Clara Andrade Sant´anna Santos - 22124
# Júlia Enriquetto de Brito      - 22139

# Lê o n caixeiros e a n cidades
# Lê a solucao inicial

# Metodo SPLIT 
# Esse metodo tem como objetivo dividir igualmente a quantidade de cidades para cada caixeiro 
def middle_split(lst, n):
    length = len(lst)
    div, rest = divmod(length, n) # len é o dividendo e n é o divisor - k é o resultado da divisão e m o resto
    parts = []
    
    start = 0
    for i in range(n):
        part_size = div + (1 if i == (n // 2) else 0)
        end = start + part_size
        parts.append(lst[start:end])
        start = end
    
    return parts

vetor = [10, 20, 25, 155, 4, 2, 0, 74, 15]
partes = 4
result = middle_split(vetor, partes)
print(result)

# Metodo get_distance 


# 1. Pega a solução inicial e quebra ela - SPLIT 
#    Após isso conta a distance total dela


# 2. Com os dados acima implementaremos na heurista SA


# 3. Grafico representativo