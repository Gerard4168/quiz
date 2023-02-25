# Programa entregar un número de 3 digitos inverso

print("-----------------------------------")
print("------------Reflejar numero--------")
print("-----------------------------------")

#input
x= int(input("Digite el valor de x: "))

#procesing
mod= x%10
de= x//10%10
m= x//100
xy= mod*100 + de*10 + m

#ouput
print("-------------------------------------")
print("--------El resultado es: ------------")
print("-------------------------------------")
print("Resultado " + str(xy))