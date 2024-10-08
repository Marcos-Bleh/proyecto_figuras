def get_identificador()->str:
    return "rectangulo"

def get_area(base:int, altura:int):
    area_rectangulo = base*altura
    return area_rectangulo

def get_perimetro(base:int, altura:int):
    perimetro_rectangulo= 2*base + 2*altura
    return perimetro_rectangulo