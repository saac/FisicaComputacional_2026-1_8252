def fibonacci(n):
    """
        Esta es una funcion para calcular los Fibonachos para el SB
    """
    
    output = []
    
    f1,f2 = 1,1

    while f2 < n:
        output.append(f2)        
        f1,f2 = f2,f1+f2
    
    return output


def Catalan(N):
    C0=1
    for n in range(N):
        Cn = (4*n+2)/(n+2)*C0
        C0 = Cn
        
    return Cn
    
