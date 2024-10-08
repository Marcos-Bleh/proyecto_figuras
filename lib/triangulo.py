def get_identificador()->str:
    return "triangulo"

def get_area(base:int, altura:int):
    area_triangulo = float((base*altura)/2)
    return area_triangulo

def get_perimetro(lado_a:int, lado_b:int, lado_c:int):
    perimetro_triangulo = lado_a+lado_b+lado_c
    return perimetro_triangulo