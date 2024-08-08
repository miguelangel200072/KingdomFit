#########################
# ESTA FUNCIÓN DABA ERROR
#########################


def importe_total_carro(request): # Context processor
    total=0
    if request.user.is_authenticated: # Esta linea permanecerá comentada hasta tener sistema de autentificación
        for key, value in request.session["carro"].items():
            total = total+(float(value["precio"]))
    else:
        total = 'Debes hacer login'
    return {"importe_total_carro":total}

# MODIFICACIÓN DE LA FUNCION PARA QUE NO DE ERROR 

# def importe_total_carro(request):
#     total = 0
#     if request.user.is_authenticated:
#         carro = request.session.get('carro', {})  # Obtén el carrito o un diccionario vacío si no existe
#         for item in carro.values():
#             total = total+(float(item["precio"])*item["cantidad"])
#         # total = sum(item['price'] * item['quantity'] for item in carro.values())
#     return {'importe_total_carro': total}



# Solucion temporal al error
# def importe_total_carro(request):
#     total = 0
#     if request.user.is_authenticated:
#         if 'carro' in request.session:      #  <---
#             for key, value in request.session["carro"].items():
#                 total = total + (float(value["precio"])*value["cantidad"])
#     return {"importe_total_carro":total}