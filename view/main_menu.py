from estoque.estoque_util import (
    cadastrar_produto, 
    atualizar_quantidade_produto, 
    atualizar_preco_venda, 
    buscar_produto,
    lista_produtos_ordenado_quantidade_asc,  
    lista_produtos_ordenado_quantidade_desc,
    remover_produto,
    consultar_produtos_esgotados,  
    filtrar_produtos_com_baixa_quantidade,
    calcular_lucro_presumido  
)
from .main_menu_util import (
    validar_int_positivo, 
    validar_float_positivo,
    exibir_relatorio_estoque,
    exibir_produtos,
    pressione_enter_para_continuar
)
from estoque.estoque import estoque_lista


def calcular_lucro():
    """
    Calcula o lucro presumido do estoque e exibe no console.
    """
    lucro = calcular_lucro_presumido(estoque_lista)
    print(f"O lucro presumido é: R$ {lucro:.2f}")
    pressione_enter_para_continuar()

def adicionar():
    """
    Adiciona um novo produto ao estoque.
    """
    nome = input("Nome do produto: ")
    quantidade = validar_int_positivo("Quantidade: ")
    preco_custo = validar_float_positivo("Preço de custo: ")
    preco_venda = validar_float_positivo("Preço de venda: ")
    
    novo_produto = cadastrar_produto(estoque_lista, nome, quantidade, preco_custo, preco_venda)
    print(f"Produto adicionado com sucesso! {novo_produto}")
    pressione_enter_para_continuar()

def atualizar():
    """
    Atualiza a quantidade ou o preço de venda de um produto no estoque.
    """
    print("1. Atualizar quantidade")
    print("2. Atualizar preço de venda")
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        codigo = validar_int_positivo("Código do produto a ser atualizado: ")
        print("1. Aumentar quantidade")
        print("2. Reduzir quantidade")
        operacao = input("Escolha uma operação: ")
        
        if operacao == '1':
            quantidade = validar_int_positivo("Quantidade a ser aumentada: ")
            produto_atualizado = atualizar_quantidade_produto(estoque_lista, codigo, quantidade, '+')
        elif operacao == '2':
            quantidade = validar_int_positivo("Quantidade a ser reduzida: ")
            produto_atualizado = atualizar_quantidade_produto(estoque_lista, codigo, quantidade, '-')
        else:
            print("Opção inválida.")
            return
        
        if produto_atualizado:
            print("Quantidade atualizada com sucesso!")
            exibir_produtos([produto_atualizado])
        else:
            print("Erro ao atualizar quantidade.")
    elif escolha == '2':
        codigo = validar_int_positivo("Código do produto a ser atualizado: ")
        novo_preco_venda = validar_float_positivo("Novo preço de venda: ")
        produto_atualizado = atualizar_preco_venda(estoque_lista, codigo, novo_preco_venda)
        if produto_atualizado:
            print("Preço de venda atualizado com sucesso!")
            exibir_produtos([produto_atualizado])
        else:
            print("Erro ao atualizar preço de venda.")
    else:
        print("Opção inválida.")
    
    pressione_enter_para_continuar()
    
def buscar():
    """
    Busca um produto no estoque pelo nome ou código.
    """
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
        return
    
    if produtos_encontrados:
        exibir_produtos(produtos_encontrados)
    else:
        print("Produto não encontrado.")
        pressione_enter_para_continuar()

def ordenar_produtos_por_quantidade():
    """
    Ordena os produtos no estoque pela quantidade em ordem crescente ou decrescente.
    """
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
    """
    Remove um produto do estoque pelo código.
    """
    codigo = validar_int_positivo("Código do produto a ser removido: ")
    produto_removido = remover_produto(estoque_lista, codigo)
    if produto_removido:
        print(f"Produto removido com sucesso! {produto_removido}")
    else:
        print("Erro ao remover produto. Código não encontrado.")
    pressione_enter_para_continuar()

def consultar_esgotados():
    """
    Consulta produtos esgotados no estoque.
    """
    produtos_esgotados = consultar_produtos_esgotados(estoque_lista)
    if produtos_esgotados:
        exibir_produtos(produtos_esgotados)
    else:
        print("Não há produtos esgotados.")
        pressione_enter_para_continuar()

def filtrar_baixa_quantidade():
    """
    Filtra produtos com quantidade abaixo de um limite mínimo.
    """
    limite_minimo = validar_int_positivo("Digite o limite mínimo de quantidade: ")
    produtos_com_baixa_quantidade = filtrar_produtos_com_baixa_quantidade(estoque_lista, limite_minimo)
    if produtos_com_baixa_quantidade:
        exibir_produtos(produtos_com_baixa_quantidade)
    else:
        print("Não há produtos com quantidade abaixo do limite especificado.")
        pressione_enter_para_continuar()

def menu():
    """
    Exibe o menu principal e gerencia a navegação entre as opções.
    """
    while True:
        print("\nmenu:")
        print("1. Adicionar produto")
        print("2. Atualizar produto")
        print("3. Exibir relatório de estoque")
        print("4. Buscar produto")
        print("5. Ordenar produtos por quantidade em estoque")
        print("6. Remover produto")
        print("7. Consultar produtos esgotados")
        print("8. Filtrar produtos com baixa quantidade")
        print("9. Calcular lucro presumido")  
        print("10. Sair")
        
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
            consultar_esgotados()
        elif escolha == '8':
            filtrar_baixa_quantidade()
        elif escolha == '9':
            calcular_lucro()  
        elif escolha == '10':
            print("Saindo do menu...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            pressione_enter_para_continuar()

if __name__ == "__main__":
    menu()