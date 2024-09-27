def cadastrar_produto(estoque_lista, nome, quantidade, preco_custo, preco_venda):
    codigo = gerar_novo_codigo(estoque_lista)
    novo_produto = {
        'nome': nome,
        'codigo': int(codigo),
        'quantidade': int(quantidade),
        'preco_custo': float(preco_custo),
        'preco_venda': float(preco_venda)
    }
    estoque_lista.append(novo_produto)
    
def gerar_novo_codigo(estoque_lista):
    if not estoque_lista:
        return 1  
    ultimo_codigo = max(produto['codigo'] for produto in estoque_lista)
    return ultimo_codigo + 1

def lista_produtos_ordenado(estoque_lista, asc=True):
    return sorted(estoque_lista, key=lambda produto: produto['quantidade'], reverse=not asc)

def buscar_produto(*, estoque_lista, nome=None, codigo=None):
    produtos_encontrados = []
    
    for produto in estoque_lista:
        if nome and nome.lower() in produto['nome'].lower():
            produtos_encontrados.append(produto)
        elif codigo and produto['codigo'] == codigo:
            produtos_encontrados.append(produto)
    
    if not produtos_encontrados:
        print("Nenhum produto encontrado.")
    else:
        for produto in produtos_encontrados:
            print(f"Nome: {produto['nome']}, Código: {produto['codigo']}, Quantidade: {produto['quantidade']}, Preço de Custo: {produto['preco_custo']}, Preço de Venda: {produto['preco_venda']}")
    
    return produtos_encontrados

def get_produto_por_codigo(estoque_lista, codigo):
    for produto in estoque_lista:
        if produto['codigo'] == codigo:
            return produto
    return None