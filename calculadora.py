print("=="*12)
print("CALCULADORA DO LELEO")
print("=="*12)
print('Qual e o seu nome?')
nome = input('')

print(f"Okay {nome}, aperte enter para abrir a calculadora.")
enter = input('')

print('a calculadora abriu')
print("Digite um número ")
n1 = int(input(""))


print("Digite o segundo número ")
n2 = int(input(""))
print("Qual operação você deseja usar? (+, -, x, /, raiz, raiz cubica ou potência) ")
op = input("")

if op == "+":
  print(n1, "+", n2, "=", n1 + n2, "é o resultado desta operação")
elif op == "-":
  print(n1, "-", n2, "=", n1 - n2, "é o resultado desta operação")
elif op == "x":
  print(n1, "x", n2, "=", n1 * n2, "é o resultado desta operação")
elif op == "/":
  print(n1, "/", n2, "=", n1 / n2, "é o resultado desta operação")
elif op == 'raiz':
    print(n1, 'raiz','=', n1 **(1/2), 'é o resultado desta operação')
elif op == 'raiz cubica':
    print(n1, 'raiz cubica', '=', n1 **(1/3), 'é o resultado desta operação')
elif op == 'potência':
    print(n1, 'potência', n2, '=', n1 ** n2, 'é o resultado desta operação')
else:
  print("Error")
print("--"*15)
print(f"Obrigado {nome}, volte sempre!")
print("--"*15)
