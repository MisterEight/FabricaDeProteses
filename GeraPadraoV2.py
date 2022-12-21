def gera_padrao(num_elementos):
    pontos = 0
    import random
    padrao=""
    for i in range(1, num_elementos+1):
        n=random.gauss(3,5)
        if n<=1:
            padrao+='#'
            pontos += 3
        if n>1 and n<=4:
            padrao+='-'
            pontos += 1
        if n>4 and n<=5:
            padrao+='$'
            pontos += 2
        if n>5:
            padrao+=' '
    return pontos, padrao