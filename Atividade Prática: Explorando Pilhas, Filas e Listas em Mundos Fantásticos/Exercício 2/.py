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
