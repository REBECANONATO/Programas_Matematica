def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l
#lista = input("Digite sua lista:")
#lista = [int(x) for x in input("Digite sua lista:").strip()]
lista = eval('[' + input("Digite sua lista: ") + ']')
lista = remove_repetidos(lista)
print (lista)
