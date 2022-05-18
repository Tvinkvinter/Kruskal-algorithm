import matrix as mt


def in_bouquets(v):
    global bouquets
    for b in bouquets:
        if v in b:
            return bouquets.index(b)
    return -1


def merge_bouquets(b1, b2):
    global bouquets
    min_i = min(bouquets.index(b1), bouquets.index(b2))
    if bouquets.index(b1) == min_i:
        bouquets[bouquets.index(b1)] += bouquets[bouquets.index(b2)]
        bouquets.remove(b2)
    elif bouquets.index(b2) == min_i:
        bouquets[bouquets.index(b2)] += bouquets[bouquets.index(b1)]
        bouquets.remove(b1)


graph = mt.matrix_from_file('graph.txt')  # загружаем матрицу весов
E = {}  # множество всех ребер, где ключ - пара вершин, соединенных ребром, а значение - вес ребра
for i in range(graph.n):
    for j in range(graph.m):
        if graph.matrix[i][j] > 0 and (j + 1, i + 1) not in E:
            E.setdefault((i + 1, j + 1), graph.matrix[i][j])

sorted_keys = sorted(E, key=E.get, reverse=True)
sorted_E = {}
for key in sorted_keys:
    sorted_E[key] = E[key]
print(f'E = {sorted_E}')
bouquets = []
T = []
W = 0
for edge in sorted_E.keys():
    if in_bouquets(edge[0]) == in_bouquets(edge[1]) and in_bouquets(edge[0]) != -1:  # Вершины 0 и 1 находятся в одном букете
        continue
    elif in_bouquets(edge[0]) != -1 and in_bouquets(edge[1]) == -1:  # Вершина 0 находится в одном из букетов, вершины 1 нет ни в одном букете
        bouquets[in_bouquets(edge[0])].append(edge[1])
        T.append(edge)
        W += sorted_E[edge]
        continue
    elif in_bouquets(edge[1]) != -1 and in_bouquets(edge[0]) == -1:  # Вершина 1 находится в одном из букетов, вершины 0 нет ни в одном букете
        bouquets[in_bouquets(edge[1])].append(edge[0])
        T.append(edge)
        W += sorted_E[edge]
        continue
    elif in_bouquets(edge[0]) != -1 and in_bouquets(edge[1]) != -1 and in_bouquets(edge[0]) != in_bouquets(edge[1]):  # Вершины находятся в разных букетах
        merge_bouquets(bouquets[in_bouquets(edge[0])], bouquets[in_bouquets(edge[1])])
        T.append(edge)
        W += sorted_E[edge]
        continue
    elif in_bouquets(edge[0]) == -1 and in_bouquets(edge[1]) == -1:  # Обе вершины не находятся ни в одном букете
        bouquets.append([edge[0], edge[1]])
        T.append(edge)
        W += sorted_E[edge]


print(f'T = {T}')
print(f'W = {W}')

