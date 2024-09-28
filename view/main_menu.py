from estoque.estoque_util import (
    cadastrar_produto, 
    atualizar_quantidade_produto, 
    atualizar_preco_venda, 
    buscar_produto
)
from .main_menu_util import (
    validar_int_positivo, 
    validar_float_positivo,
    exibir_relatorio_estoque
)
from estoque.estoque import estoque_lista

def pressione_enter_para_continuar():
    input("Pressione Enter para continuar...")

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
        if produto_atualizado:
            print(f"Quantidade atualizada com sucesso! Produto atualizado: {produto_atualizado}")
        else:
            print("Erro ao atualizar quantidade.")
        pressione_enter_para_continuar()
    elif escolha == '2':
        codigo = validar_int_positivo("Código do produto a ser atualizado: ")
        novo_preco_venda = validar_float_positivo("Novo preço de venda: ")
        produto_atualizado = atualizar_preco_venda(estoque_lista, codigo, novo_preco_venda)
        if produto_atualizado:
            print(f"Preço de venda atualizado com sucesso! Produto atualizado: {produto_atualizado}")
        else:
            print("Erro ao atualizar preço de venda.")
        pressione_enter_para_continuar()
    else:
        print("Opção inválida.")
        pressione_enter_para_continuar()

def buscar():
    print("1. Buscar por nome")
    print("2. Buscar por código")
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        nome = input("Nome do produto: ")
        produtos_encontrados = buscar_produto(estoque_lista=estoque_lista, nome_usuario=nome)
    elif escolha == '2':
        codigo = validar_int_positivo("Código do produto: ")
        produtos_encontrados = buscar_produto(estoque_lista=estoque_lista, codigo=codigo)
    else:
        print("Opção inválida.")
        pressione_enter_para_continuar()
        return
    
    if produtos_encontrados:
        for produto in produtos_encontrados:
            print(f"Nome: {produto['nome']}, Código: {produto['codigo']}, Quantidade: {produto['quantidade']}, Preço de Custo: {produto['preco_custo']}, Preço de Venda: {produto['preco_venda']}")
    else:
        print("Produto não encontrado.")
    pressione_enter_para_continuar()

def menu():
    while True:
        print("\nmenu:")
        print("1. Adicionar produto")
        print("2. Atualizar produto")
        print("3. Exibir relatório de estoque")
        print("4. Buscar produto")
        print("5. Sair")
        
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
            print("Saindo do menu...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            pressione_enter_para_continuar()

if __name__ == "__main__":
    menu()