#Faça um programa para uma loja de tintas,O program devera pedir o tamanho em m
#quadrados da area a ser pintada .Considere a cobertura da tinta como 1 l para cada
#3metros e que a lata de tinta de 18 litros é 80 reais, informe a quantidade de latas de tintas
# a serem compradas
area=input("Qual o tamanho da area a ser pintada, em metros quadrados: ")
rendimento_litro=area/3
rendimento_lata=rendimento_litro/18
print(rendimento_lata)
