#CALCULADORA DE MULTIPLICAÇÃO
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

#mult = num1 * num2

def cal_mult(): #Calculo da Multiplicação
    mult = num1 * num2
    print("O resuntaldo da Multiplicação é: ", round(mult, 2))

def letra(): #Verificar se foi digitado uma letra
    if num1 or num2 == str:
        print("Só podem ser usados valores númericos!!!")


if num1 or num2 == str:
    letra()

else:
  cal_mult()

