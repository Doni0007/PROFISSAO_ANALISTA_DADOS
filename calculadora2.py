print ('Esta é uma  calculadora que executa operações simples')

valor1 = (int(input("Digite um numero de 1 a 10: ")))
valor2 = (int(input("Digite um numero de 1 a 10: ")))

if valor1 < 1 or valor1 > 10 or valor2 < 1 or valor2 > 10:
    print("O(s) número(s) digitado(s) está(ão) fora dos parâmetros solicitados")
    exit()

if valor1 >= 1 and valor1 <= 10 and valor2 >= 1 and valor2 <= 10:
  print(f'Os números informados foram {valor1} e {valor2}')
  print(f'A soma dos números é: {valor1 + valor2}')
  print(f'A multiplicação entre os dois valores é: {valor1 * valor2}')
  if valor1 > valor2:
       print(f'A subtração do maior e menor valor é: {valor1 - valor2}')
  else:
       print(f'A subtração do maior e menor valor é: {valor2 - valor1}')
  if valor1 > valor2:
       print(f'A divisão do maior e menor valor é: {valor1 / valor2}')
  else:
       print(f'A divisão entre maior e menor valor é: {valor2 / valor1}')
