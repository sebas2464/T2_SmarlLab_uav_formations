import math

def gerar_posicoes_circulo(n):
    # gera posicoes em um circulo com raio =3
    raio = 1
    angulo = 360 / n
    posicoes = []
    for i in range(n):
        x = raio * math.cos(math.radians(i * angulo))
        y = raio * math.sin(math.radians(i * angulo))
        posicoes.append([x, y, 0])
    return posicoes

def gerar_posicoes_poligono(n, lados):
    # gera posicoes para um poligono regular, os primeiros seguidores vao para os vertices, os restantes sao distribuidos entre os lados
    if lados < 3:
        raise ValueError("numero de lados deve ser pelo menos 3")
    
    raio = 1
    vertices = []
    for i in range(lados):
        x = raio * math.cos(2 * math.pi * i / lados)
        y = raio * math.sin(2 * math.pi * i / lados)
        vertices.append([x, y, 0])

    # coloca os seguidores nos vertices
    posicoes = []
    for i in range(min(n, lados)):
        posicoes.append(vertices[i])
    
    # distribui os restantes entre os lados
    restantes = n - lados
    for i in range(lados):
        if restantes <= 0:
            break
        inicio = vertices[i]
        fim = vertices[(i + 1) % lados]
        drones_no_lado = restantes // (lados - i)
        dx = (fim[0] - inicio[0]) / (drones_no_lado + 1)
        dy = (fim[1] - inicio[1]) / (drones_no_lado + 1)
        for j in range(1, drones_no_lado + 1):
            posicoes.append([inicio[0] + j * dx, inicio[1] + j * dy, 0])
        restantes -= drones_no_lado

    return posicoes

def gerar_posicoes_cruz(n):
    # gera posicoes em formato de cruz com 4 bracos
    if n < 4:
        raise ValueError("precisa de pelo menos 4 drones para formar uma cruz")

    bracos = 4
    distancia_maxima = 10
    drones_por_braco = n // bracos
    restantes = n % bracos

    posicoes = []
    for i in range(bracos):
        angulo = i * 90 + 45
        dx = math.cos(math.radians(angulo))
        dy = math.sin(math.radians(angulo))
        for j in range(drones_por_braco):
            distancia = distancia_maxima * (j + 1) / drones_por_braco
            posicoes.append([dx * distancia, dy * distancia, 0])
        if restantes > 0:
            posicoes.append([dx * distancia_maxima, dy * distancia_maxima, 0])
            restantes -= 1

    return posicoes

FORMATIONS = {
    "circle": gerar_posicoes_circulo,
    "triangle": lambda n: gerar_posicoes_poligono(n, 3),
    "square": lambda n: gerar_posicoes_poligono(n, 4),
    "pentagon": lambda n: gerar_posicoes_poligono(n, 5),
    "hexagon": lambda n: gerar_posicoes_poligono(n, 6),
    "heptagon": lambda n: gerar_posicoes_poligono(n, 7),
    "octagon": lambda n: gerar_posicoes_poligono(n, 8),
    "nonagon": lambda n: gerar_posicoes_poligono(n, 9),
    "decagon": lambda n: gerar_posicoes_poligono(n, 10),
    "cross": gerar_posicoes_cruz,
}
