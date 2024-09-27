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

def lista_produtos_ordenado_quantidade(estoque_lista, asc=True):
    return sorted(estoque_lista, key=lambda produto: produto['quantidade'], reverse=not asc)

def buscar_produto(*, estoque_lista, nome_usuario=None, codigo=None):
    produtos_encontrados = []
    
    for produto in estoque_lista:
        if nome_usuario and nome_usuario.lower() in produto['nome'].lower():
            produtos_encontrados.append(produto)
        elif codigo and produto['codigo'] == codigo:
            produtos_encontrados.append(produto)
    
    return produtos_encontrados

def remover_produto(estoque_lista, codigo):
    produto_removido = None
    
    for produto in estoque_lista:
        if produto['codigo'] == codigo:
            produto_removido = produto
            estoque_lista.remove(produto)
            return produto_removido
    return None
    
def consultar_produtos_esgotados(estoque_lista):
    produtos_esgotados = []
    
    for produto in estoque_lista:
        if produto['quantidade'] == 0:
            produtos_esgotados.append(produto)
    
    if not produtos_esgotados:
        return None
    else:
        return produtos_esgotados
          
def filtrar_produtos_com_baixa_quantidade(estoque_lista, limite_minimo=5):
    produtos_com_baixa_quantidade = []
    
    for produto in estoque_lista:
        if produto['quantidade'] < limite_minimo:
            produtos_com_baixa_quantidade.append(produto)
    
    return produtos_com_baixa_quantidade

def atualizar_quantidade_produto(estoque_lista, codigo, quantidade):
    for produto in estoque_lista:
        if produto['codigo'] == codigo:
            if validar_quantidade_produto(produto, quantidade):
                produto['quantidade'] -= quantidade
                return produto
    return None


def atualizar_preco_venda(estoque_lista, codigo, novo_preco_venda):
    for produto in estoque_lista:
        if produto['codigo'] == codigo:
            if validar_preco_venda(produto, novo_preco_venda):
                produto['preco_venda'] = novo_preco_venda
                return produto
    return None  

def validar_preco_venda(produto, novo_preco_venda):
    return novo_preco_venda >= produto['preco_custo']

def validar_quantidade_produto(produto, quantidade):
    return produto['quantidade'] >= quantidade