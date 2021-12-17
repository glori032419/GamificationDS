
print("\t\t\tSegundo Ataque")

numero=[]#Creacion de lista vacia

numero.append(int(input("Ingrese numeros de dos cifras: ")))
numero.append(int(input("Ingrese numeros de dos cifras: ")))
numero.append(int(input("Ingrese numeros de dos cifras: ")))
numero.append(int(input("Ingrese numeros de dos cifras: ")))
numero.append(int(input("Ingrese numeros de dos cifras: ")))
print("\n",numero)
#append para agregar elelemtnos a dicha lista.


#suma de todos los elementos de esta lista con sum.
listsum=sum(numero)
print(f"\n\tLa suma es: {listsum}")

#multiplicar dicha suma por 9

for i in numero:
   i=listsum*9
print("\n\tLa suma total multiplicado x9 es: ",i)

#mostrar el numero mayor de la lista.

print("\n\tOrdenar la lista de numeros de mayor a menor.")
numero.sort(reverse=True)
print("\t\t",numero)

#mostrar el numero menor de la lista.
print("\n\tOrdenar la lista de numeros de menor a mayor.")
numero.sort()
print("\t\t",numero)


#Indicar el numero de elementos de la lista.
print(f"\n\tHay {len(numero)} elementos en la lista.")
