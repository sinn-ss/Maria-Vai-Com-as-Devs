# Exercícios Python [1]
# Você possui uma variável a = 10 e uma variável b = 5, e precisa trocar o valor das duas. Como você faria?
a = 10
b = 5
a,b = b,a
print (a, b)

# Exercícios Python [2]
# Faça um programa que pergunte que dia é, e diga quantos faltam até o final do mês. Considere o mês com trinta e um dias.
dia = int(input("Qual o dia do mês hoje? "))
restante = 31 - dia

print(f"Faltam {restante} dias até o final do mês.")

# Exercícios Python [3]
# Faça um programa que receba o número de brindes do Maria vai com as Devs que a Jéssica vai mandar fazer, e imprima quanto de entrada ela irá que pagar. Considere que cada brinde custa R$25,00, e a entrada para o fabricante é de 50% do valor total.
valor_brinde = 25
qtde_brindes = int(input("Digite a quantidade de brindes a serem confeccionados: "))
entrada = (qtde_brindes*valor_brinde)/2
print(f"O valor da entrada do pagamento a ser pago para o fabricante é R$ {entrada:.2f}")

# Exercícios Python [4]
# A Serasa irá gerar um minicurso de aprendizagem financeira e está planejando um coffee break ás 15 horas.
# Leia o número de participantes do minicurso e imprima:
#    Quantos litros de refrigerante teremos que comprar
#    Quantas coxinhas e quanto iremos gastar.
# Considere que cada participante toma 400ml de refrigerante, come 10 coxinhas, que cada litro de refrigerante custa 4,00 e cada coxinha custa 0,50.
qtde_refri = 0.4
qtde_coxinha = 10
pessoas = int(input("Quantos participantes serão? "))
print("Cada participante consome 400ml de refrigerante e consome 10 coxinhas.")
litros_refri = pessoas * qtde_refri
coxinhas = pessoas * qtde_coxinha
total_gasto = (litros_refri * 4) + (coxinhas * 0.5)
print(f"Iremos precisar de {litros_refri:.0f} litro(s) de refrigerante, e de {coxinhas} coxinhas.")
print(f"Gastaremos um total de R$ {total_gasto:.2f}")

# Dicas [Separando um texto com split()]
# Se você não determinar nenhum caractere de espaçamento para o split(), ele assumirá que é um espaço em branco. Como você dividirá sua entrada em duas, poderá armazená-la em duas variáveis diferentes! Se você não colocar variáveis suficientes, python criará uma lista*.
primeiro_nome, segundo_nome = input("Digite seu nome e sobrenome: ").split()
print(primeiro_nome)
print(segundo_nome)

# Dicas [Separando um texto com split()]
# Na conversão de tipos de dados de entrada, para dividir a entrada em mais de uma variável e já transformar ela para o tipo desejado, utilizamos um comando auxiliar chamado map()
valor1, valor2 = map(float, input("Digite dois valores: ").split(","))
print(valor1)
print(valor2)

# Exercícios Python [5]
# Para que a jéssica consiga enviar os brindes e não errar na preferência de cores de todas as participantes, ela precisa saber a quantidade de pessoas que preferem a cor rosa, roxo ou azul. Faça um programa que leia a quantidade de pessoas que preferem cada cor e retorne a porcentagem de cada uma destas cores.
rosa, roxo, azul = map(int, input("Informe separado por vírgulas quantas participantes por cor: ").split(","))
total_participantes = rosa + roxo + azul

porcentagem_rosa = rosa / total_participantes * 100
porcentagem_roxo = roxo / total_participantes * 100
porcentagem_azul = azul / total_participantes * 100

print(f"{porcentagem_rosa:.2f} % de pessoas preferem rosa.")
print(f"{porcentagem_roxo:.2f} % de pessoas preferem roxo.")
print(f"{porcentagem_azul:.2f} % de pessoas preferem azul.")