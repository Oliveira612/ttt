# ════════════════════════════════
# PDS · Python · for, while, listas
# 3a Série A · 2026
# exercicios_repeticao.py
# ════════════════════════════════

# ── FOR COM RANGE ──

# Contar de 1 a 5
for i in range(1, 6):
print(f"Número: {i}")

print()

# Tabuada do 7
for i in range(1, 11):
print(f"7 x {i} = {7 * i}")

print()

# Contagem regressiva
for i in range(5, 0, -1):
print(i)

print("Fogo!")

print()

# ── WHILE ──

# Pedir senha até acertar
senha_correta = "python123"
tentativas = 0

while tentativas < 3:
senha = input("Digite a senha: ")

if senha == senha_correta:
print("Acesso liberado!")
break
else:
tentativas += 1
print(f"Senha errada. Tentativas restantes: {3 - tentativas}")

if tentativas == 3:
print("Conta bloqueada!")

print()

# ── LISTAS ──

# Lista de frutas
frutas = ["maçã", "banana", "uva", "manga"]

for fruta in frutas:
print(f"- {fruta}")

print(f"Total: {len(frutas)} frutas")

print()

# Lista com append — 5 notas do usuário
notas = []

for i in range(5):
nota = float(input(f"Nota {i + 1}: "))
notas.append(nota)

media = sum(notas) / len(notas)

print(f"Média: {media:.1f}")
print(f"Maior: {max(notas)}")
print(f"Menor: {min(notas)}")
