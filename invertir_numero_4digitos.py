#programa invertir numerode 4 digitos
print("--------------------------------")
print("-------INVERTIR NUMEROS---------")
print("--------------------------------")

# Input
n = int(input("digite el NUMERO DE 4 DIGITOS PARA INVERTIR: "))

#processing
d1 = ((n%10)*1000)
pe = (n//10) 
d2 = ((pe%10)*100)
pe = (pe//10)
d3 = ((pe%10)*10)
d4 = (pe//10)
ni = (d1+d2+d3+d4)



#output
print("--------------------")
print("-----resultados-----")
print("--------------------")

print("el resultado de ni es: " + str(d1+d2+d3+d4))
