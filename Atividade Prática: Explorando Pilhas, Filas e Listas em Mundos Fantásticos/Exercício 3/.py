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
