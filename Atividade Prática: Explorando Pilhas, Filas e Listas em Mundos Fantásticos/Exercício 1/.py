# Exercício Nº 1
# Inicializa um catálogo vazio para armazenar livros
catalogo_magico = []

# Função que adiciona um livro ao catálogo
def adicionar_livro(catalogo, livro):
    # Adiciona o livro no final da lista 'catalogo'
    catalogo.append(livro)

# Adiciona três livros mágicos ao catálogo usando a função 'adicionar_livro'
adicionar_livro(catalogo_magico, "O feitiço da Lua Crescente ")
adicionar_livro(catalogo_magico, "A Jornada do Unicórnio Perdido")
adicionar_livro(catalogo_magico, "Segredos da Floresta Encantada ")

# Imprime o catálogo mágico para verificar os livros adicionados
print(catalogo_magico)

# Inicializa um catálogo vazio para armazenar livros
catalogo_magico = []

# Função que adiciona um livro ao catálogo
def adicionar_livro(catalogo, livro):
    # Adiciona o livro no final da lista 'catalogo' usando o método append
    catalogo.append(livro)

# Adiciona três livros mágicos ao catálogo usando a função 'adicionar_livro'
adicionar_livro(catalogo_magico, "O feitiço da Lua Crescente ")  # Primeiro livro
adicionar_livro(catalogo_magico, "A Jornada do Unicórnio Perdido")  # Segundo livro
adicionar_livro(catalogo_magico, "Segredos da Floresta Encantada ")  # Terceiro livro

# Imprime o catálogo mágico para verificar os livros adicionados
print(catalogo_magico)  # Exibe a lista com todos os livros adicionados

# Remove o livro "A Jornada do Unicórnio Perdido"
catalogo_magico.remove("A Jornada do Unicórnio Perdido")

# Imprime o catálogo mágico para verificar os livros restantes
print(catalogo_magico)

 Função que verifica se um livro está no catálogo
def verificar_livro(catalogo, livro):
    # Verifica se o livro está presente no catálogo
    if livro in catalogo:
        return True  # Retorna True se o livro estiver no catálogo
    else:
        return False  # Retorna False se o livro não estiver no catálogo

# Definindo o nome do livro que queremos verificar
verificacao_livro = "A Jornada do Unicórnio Perdido"

# Chamando a função verificar_livro e passando o catálogo e o livro a ser verificado
result = verificar_livro(catalogo_magico, verificacao_livro)

# Imprimindo o resultado da verificação
print(f'O livro "{verificacao_livro}" está no catálogo {result}')
