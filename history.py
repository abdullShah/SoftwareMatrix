def move_clockwise_out_contour(matrix, d):
    n = len(matrix)

    temp_up = matrix[d][n - d - 1]
    for j in range(n - d - 1, d, -1):
        matrix[d][j] = matrix[d][j - 1]

    temp_right = matrix[n - d - 1][n - d - 1]
    for i in range(n - d - 1, d, -1):
        matrix[i][n - d - 1] = matrix[i - 1][n - d - 1]
    matrix[1 + d][n - d - 1] = temp_up

    temp_down = matrix[n - d - 1][d]
    for j in range(d, n - d - 1):
        matrix[n - d - 1][j] = matrix[n - d - 1][j + 1]
    matrix[n - d - 1][n - d - 1 - 1] = temp_right

    for i in range(d, n - d - 1):
        matrix[i][d] = matrix[i + 1][d]
    matrix[n - d - 1 - 1][d] = temp_down

    return matrix


def move_counterclockwise_out_contour(matrix, d):
    n = len(matrix)

    temp_up = matrix[d][d]
    for j in range(d, n - d - 1):
        matrix[d][j] = matrix[d][j + 1]

    temp_left = matrix[n - d - 1][d]
    for i in range(n - d - 1, d, -1):
        matrix[i][d] = matrix[i - 1][d]
    matrix[1 + d][d] = temp_up

    temp_down = matrix[n - d - 1][n - d - 1]
    for j in range(n - d - 1, d, -1):
        matrix[n - d - 1][j] = matrix[n - d - 1][j - 1]
    matrix[n - d - 1][1 + d] = temp_left

    for i in range(d, n - d - 1):
        matrix[i][n - d - 1] = matrix[i + 1][n - d - 1]
    matrix[n - d - 1 - 1][n - d - 1] = temp_down

    return matrix


# По часовой с глубиной (без глубины - d заменится на 0)
def move_clockwise_out_contour(matrix, d):
    n = len(matrix)

    top_way = [(d, j) for j in range(n - d)]
    right_way = [(i, n - 1 - d) for i in range(d + 1, n - d)]
    down_way = [(n - 1 - d, j) for j in range(n - d - 1 - 1, d, -1)]
    left_way = [(i, d) for i in range(n - d - 1, d, -1)]

    main_way = top_way + right_way + down_way + left_way

    last_item = matrix[main_way[0][0]][main_way[0][1]]

    for q in range(1, len(main_way)):
        i, j = main_way[q]
        matrix[i][j], last_item = last_item, matrix[i][j]

    matrix[d][d] = last_item

    return matrix


def move_conterclockwise_out_contour(matrix, d):
    _, main_way = move_clockwise_out_contour([row.copy() for row in matrix], d)
    main_way = main_way[::-1]

    last_item = matrix[main_way[0][0]][main_way[0][1]]
    for q in range(1, len(main_way)):
        i, j = main_way[q]
        matrix[i][j], last_item = last_item, matrix[i][j]

    matrix[main_way[0][0]][main_way[0][1]] = last_item

    return matrix, main_way


# Реализация Пашка
# Разворот контура по/против часовой стрелки с чередованием
def rotations(matrix):
    n = len(matrix)
    for a in range(n // 2):
        c = matrix[a][a]
        if a % 2 == 0:
            for k in range(a, n - a):
                c, matrix[a][k] = matrix[a][k], c
            for l in range(1 + a, n - a):
                c, matrix[l][n - a - 1] = matrix[l][n - a - 1], c
            for m in range(1 + a, n - a):
                c, matrix[n - a - 1][n - m - 1] = matrix[n - a - 1][n - m - 1], c
            for r in range(1 + a, n - a):
                c, matrix[n - r - 1][a] = matrix[n - r - 1][a], c
        else:
            for k in range(a, n - a):
                c, matrix[k][a] = matrix[k][a], c
            for l in range(1 + a, n - a):
                c, matrix[n - a - 1][l] = matrix[n - a - 1][l], c
            for m in range(1 + a, n - a):
                c, matrix[n - m - 1][n - a - 1] = matrix[n - m - 1][n - a - 1], c
            for s in range(1 + a, n - a):
                c, matrix[a][n - s - 1] = matrix[a][n - s - 1], c
        return matrix


# Сортировка по последней строке матрицы
trans_matrix = list(zip(*matrix))
trans_matrix.sort(key=lambda x: x[-1])
matrix = list(zip(*trans_matrix))


# Алгоритм поворота на 90 градусов по часовой стрелке
for i in range(n // 2):
    for j in range(i, n - i - 1):
        temp = matrix[i][j]
        matrix[i][j] = matrix[n - j - 1][i]
        matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
        matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
        matrix[j][n - i - 1] = temp

# Алгоритм поворота на 90 градусов против часовой стрелке
for i in range(n // 2):
    for j in range(i, n - i - 1):
        temp = matrix[i][j]
        matrix[i][j] = matrix[j][n - i - 1]
        matrix[j][n - i - 1] = matrix[n - i - 1][n - j - 1]
        matrix[n - i - 1][n - j - 1] = matrix[n - j - 1][i]
        matrix[n - j - 1][i] = temp


def rotate_matrix(matrix):
    n = len(matrix)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - 1 - i] = matrix[i][j]
    return result


def rotate_matrix(matrix):
    n = len(matrix)
    # Транспонирование матрицы
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[i][i] = matrix[j][i], matrix[i][j]
    # Поменять порядок следования элементов в каждой строке
    for row in matrix:
        row.reverse()
    return matrix


# Это по часовой
matrix = [list(row) for row in zip(*matrix)[::-1]]
# А это против
matrix = [list(row) for row in zip(*matrix)][::-1]
