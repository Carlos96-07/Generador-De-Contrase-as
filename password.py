import random
minisculas = "a,b,v,c,f"
mayusculas = "A,F,T,U,H"
numeros =" 2,4,5,6,7"
simbolos = "[], (), ;, /"
todos = minisculas + mayusculas + simbolos + numeros
length = 16 
password = "".join(random.sample(todos ,length))
print(password)
