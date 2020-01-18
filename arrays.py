vetor = []
siglas = ['ES', 'MG', 'RJ', 'SP', 'MT']
nomes = ['Mato Grosso', 'São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Espírito Santo']
for siglas_nomes in zip(reversed(siglas), nomes):
   vetor.append(siglas_nomes)

print(vetor)
