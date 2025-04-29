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



# Exercício Nº 2 
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

# Função para verificar se a fila está vazia
def fila_vazia(fila):
    return len(fila) == 0

# Adicionando pedidos à fila
adicionar_pedido(fila_de_atendimentos, "Martelo Encantado")
adicionar_pedido(fila_de_atendimentos, "Pinça Teleportadora")
adicionar_pedido(fila_de_atendimentos, "Chave de Fenda Sônica")

# 1. Verificar se a fila está vazia
if fila_vazia(fila_de_atendimentos):
    print("A fila está vazia!")
else:
    print("A fila tem pedidos.")

# 1. Verificar se a fila está vazia
if fila_vazia(fila_de_atendimentos):
    print("A fila está vazia!")
else:
    print("A fila tem pedidos.")  

# 4. Verificar a fila após processar todos os pedidos
print("Fila após processar todos os pedidos:", fila_de_atendimentos) 

# Exercício Nº 3 
# Criando a pilha (lista vazia)
torre_de_cristais = []

# Função para empilhar cristais
def empilhar_cristal(pilha, cristal):
    pilha.append(cristal)

# Empilhando cristais
empilhar_cristal(torre_de_cristais, "Cristal do Passado")
empilhar_cristal(torre_de_cristais, "Cristal do Presente")
empilhar_cristal(torre_de_cristais, "Cristal do Futuro")

# Visualizando a pilha
print(torre_de_cristais)

# Visualizando a pilha (o topo estará no final da lista)
print("Pilha de Cristais:", torre_de_cristais)

# Função para desempilhar cristal (remover o topo da pilha)
def desempilhar_cristal(pilha):
    if pilha:
        cristal = pilha.pop()  # Remove o cristal do topo
        print("Cristal utilizado no ritual:", cristal)
        return cristal
    else:
        print("A pilha está vazia!")  

# Função para verificar se a pilha está vazia
def pilha_vazia(pilha):
    return len(pilha) == 0

# Verificando se a pilha está vazia
if pilha_vazia(torre_de_cristais):
    print("A pilha está vazia!")
else:
    print("A pilha tem cristais.") 

# Visualizando a pilha restante
print("Pilha restante:", torre_de_cristais)  

# Desempilhando todos os cristais restantes
while not pilha_vazia(torre_de_cristais):
    desempilhar_cristal(torre_de_cristais)

# Verificando a pilha após desempilhar todos os cristais
print("Pilha após todos os rituais:", torre_de_cristais)
