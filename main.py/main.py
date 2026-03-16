print('='*30)
print(f'{"SISTEMA ESCOLAR":^30}')
print('='*30)

nome = str(input('Nome do aluno: ')).strip()
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
n4 = float(input('Nota 4: '))
# --- COMPLETE AQUI (n3 e n4) ---


# --- FAÇA O CÁLCULO DA MÉDIA AQUI ---
media = (n1+n2+n3+n4)/4

print('-' * 30)
print(f'O aluno {nome} obteve a média {media:.1f}')

# --- LÓGICA DE APROVAÇÃO ---
if media >= 7:
    print('Status: APROVADO! Boas férias.')
elif media >= 5:
    print('Status: RECUPERAÇÃO. Ainda há esperança!')
else:
    print('Status: REPROVADO. Estude mais no próximo semestre.')