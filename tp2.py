#Utilizador pensa no número
import random

tentativas = 0
min = 0
max = 100
x = random.randint(min,max)
y = (input(f'O número que pensaste é {x}.'))
while y != 'Acertaste!':
    if y =='Maior':
        min = x + 1
        x = random.randint(min,max)
        y = (input(f'O número que pensaste é {x}.'))
        tentativas=tentativas+1
    elif y == 'Menor': 
        max = x - 1
        x=random.randint(min,max)
        y=(input(f'O número que pensaste é {x}.'))
        tentativas=tentativas+1
if y == 'Acertaste!':
   print (f'Acertei! Precisei de {tentativas} tentativas.')

#Computador pensa no número
import random

tentativas= 1
min=0
max=100
x = random.randint(min,max)
y = int(input('Qual é o número que pensei?'))
while y!= x:
    if y<x:
        print (f'O número que pensei é maior que {y}')
        y=int(input('Qual é o número que pensei?'))
        tentativas=tentativas+1
    elif y>x: 
        print (f'O número que pensei é menor que {y}')
        y=int(input('Qual é o número que pensei?'))
        tentativas=tentativas+1
if y == x:
   print (f'Acertaste! Precisaste de {tentativas} tentativas.')