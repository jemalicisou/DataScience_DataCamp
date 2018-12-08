# Execícios sobre o pacote Numpy
#Primeiro passo : devemos instalar o pacote Numpy

import numpy as np;

# Vamos criar um pequeno array capaz de calcular o IMC através da análise do peso * altura
height = [1.73, 1.68, 1.71, 1.89, 1.79]
height =np.array(height)
print(height)


weight = [65.4, 54.2, 63.6, 88.4, 68.7]

weight=np.array(weight)
print(weight)



bmi = weight/height ** 2
print(bmi)


#Selecionando elementos da nossa lista BMI (Que nos mostra o IMC)

print(bmi[1])
print(bmi>20)

#1-Crie uma lista com as idades das pessoas da sua casa
idades = [25, 30, 57, 70]
print(idades)

# Import the numpy package as np
import numpy as np

# Create a numpy array from idades: np_idades
np_idades=np.array(idades)

# Imprima o tipo da variável idades
print(type(idades))

# 2 -  Crie uma lista com o peso das pessoas da lista idades
peso_familia = [67.5, 75.0, 63.5, 86.7]
print (peso_familia)

#Crie um numpy de peso_familia : np_peso_familia
np_peso_familia = np.array(peso_familia)

#Imprima o tipo da variável np_peso_familia
print(type(np_peso_familia))





