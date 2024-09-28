from estoque.estoque_util import (
    cadastrar_produto, 
    atualizar_quantidade_produto, 
    atualizar_preco_venda, 
    buscar_produto,
    lista_produtos_ordenado_quantidade_asc,  
    lista_produtos_ordenado_quantidade_desc,
    remover_produto
)
from .main_menu_util import (
    validar_int_positivo, 
    validar_float_positivo,
    exibir_relatorio_estoque,
    exibir_produtos,
    pressione_enter_para_continuar
)
from estoque.estoque import estoque_lista

def adicionar():
    nome = input("Nome do produto: ")
    quantidade = validar_int_positivo("Quantidade: ")
    preco_custo = validar_float_positivo("Preço de custo: ")
    preco_venda = validar_float_positivo("Preço de venda: ")
    
    novo_produto = cadastrar_produto(estoque_lista, nome, quantidade, preco_custo, preco_venda)
    print(f"Produto adicionado com sucesso! {novo_produto}")
    pressione_enter_para_continuar()

def atualizar():
    print("1. Atualizar quantidade")
    print("2. Atualizar preço de venda")
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        codigo = validar_int_positivo("Código do produto a ser atualizado: ")
        quantidade = validar_int_positivo("Nova quantidade: ")
        produto_atualizado = atualizar_quantidade_produto(estoque_lista, codigo, quantidade)
        mensagem = "Quantidade atualizada com sucesso!" if produto_atualizado else "Erro ao atualizar quantidade."
    elif escolha == '2':
        codigo = validar_int_positivo("Código do produto a ser atualizado: ")
        novo_preco_venda = validar_float_positivo("Novo preço de venda: ")
        produto_atualizado = atualizar_preco_venda(estoque_lista, codigo, novo_preco_venda)
        mensagem = "Preço de venda atualizado com sucesso!" if produto_atualizado else "Erro ao atualizar preço de venda."
    else:
        mensagem = "Opção inválida."
    
    print(mensagem)
    pressione_enter_para_continuar()

def buscar():
    print("1. Buscar por nome")
    print("2. Buscar por código")
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        nome = input("Nome do produto: ")
        produtos_encontrados = buscar_produto(estoque_lista, nome_usuario=nome)
    elif escolha == '2':
        codigo = validar_int_positivo("Código do produto: ")
        produtos_encontrados = buscar_produto(estoque_lista, codigo=codigo)
    else:
        print("Opção inválida.")
        pressione_enter_para_continuar()
        return
    
    if produtos_encontrados:
        exibir_produtos(produtos_encontrados)
    else:
        print("Produto não encontrado.")
        pressione_enter_para_continuar()

def ordenar_produtos_por_quantidade():
    print("Escolha a ordem de exibição dos produtos:")
    print("1. Ordem crescente")
    print("2. Ordem decrescente")
    escolha = input("Digite 1 ou 2: ")
    
    if escolha == '1':
        produtos_ordenados = lista_produtos_ordenado_quantidade_asc(estoque_lista)
    elif escolha == '2':
        produtos_ordenados = lista_produtos_ordenado_quantidade_desc(estoque_lista)
    else:
        print("Opção inválida. Retornando ao menu principal.")
        pressione_enter_para_continuar()
        return
    
    exibir_produtos(produtos_ordenados)

def remover():
    codigo = validar_int_positivo("Código do produto a ser removido: ")
    produto_removido = remover_produto(estoque_lista, codigo)
    if produto_removido:
        print(f"Produto removido com sucesso! {produto_removido}")
    else:
        print("Erro ao remover produto. Código não encontrado.")
    pressione_enter_para_continuar()

def menu():
    while True:
        print("\nmenu:")
        print("1. Adicionar produto")
        print("2. Atualizar produto")
        print("3. Exibir relatório de estoque")
        print("4. Buscar produto")
        print("5. Ordenar produtos por quantidade em estoque")
        print("6. Remover produto") 
        print("7. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            adicionar()
        elif escolha == '2':
            atualizar()
        elif escolha == '3':
            exibir_relatorio_estoque(estoque_lista)
            pressione_enter_para_continuar()
        elif escolha == '4':
            buscar()
        elif escolha == '5':
            ordenar_produtos_por_quantidade()
        elif escolha == '6':
            remover()  
        elif escolha == '7':
            print("Saindo do menu...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            pressione_enter_para_continuar()

if __name__ == "__main__":
    menu()