def clasifTriangulo (l1, l2, l3):

    if type(l1) == str or type(l2) == str or type(l3) == str:
        return "Invalido"

    ## Validamos que los lados no sean mayor a 0
    if (l1 < 0 or l2 < 0 or l3<0):
        return "Invalido"
        
    ## Validamos condicion de triangularidad
    if not ((l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1) :
        return "Invalido"
        
    ## Verif si es un triangulo Escaleno
    if l1 != l3 != l2 and l2 != l1 :
        return "Escaleno"

    ## Verif si es un triangulo Equlatero
    if l1 == l2 == l3 :
        return "Equilatero"
    
    ## Es Isoceles
    return "Isoceles"
