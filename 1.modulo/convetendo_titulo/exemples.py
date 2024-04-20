# De inteiro para float

preco = 10
print(preco)
# 10

preco = float(preco)
print(preco)
# 10.0

preco = 10 / 2
print(preco)
# 5.0


## Do float pra inteiro

preco = 10.30
print(preco)
10.3

## Conversão por divisão

preco = 10
print(preco)
# 10

print(preco / 2)
# 5.0

print(preco // 2)
# 5 Reparem que aqui ele não retornou no formato float


# _____________________________________________________

# Número para string

preco = 10.50
idade = 28

print(str(preco))
# 10.5

print(str(idade))
# 28

texto = f"idade {idade} preco {preco}"
print(texto)
## idade 28 preco 10.5

## String para número

preco = "10.50"
idade = "19"

print(float(preco))
# 10.50

print(int(idade))
# 28
