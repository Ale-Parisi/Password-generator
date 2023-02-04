import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bienvenido a PyPassword Generator!")
nr_letters= int(input("Cuantas letras deseas en tu password?\n")) 
nr_symbols = int(input(f"Cuantos simbolos?\n"))
nr_numbers = int(input(f"Cuantos numeros?\n"))

let = []
num = []
sym = []

for password in range(0,nr_letters):
  ele = random.choice(letters)
  let.append(ele) 

for password in range(0,nr_symbols):
  ele = random.choice(symbols)
  sym.append(ele) 
  
for password in range(0,nr_numbers):
  ele = random.choice(numbers)
  num.append(ele) 

password = let+num+sym
random.shuffle(password)
print(''.join(password))