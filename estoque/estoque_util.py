def cadastrar_produto(estoque_lista, nome, quantidade, preco_custo, preco_venda):
    """
    Cadastra um novo produto no estoque.

    Args:
        estoque_lista (list): Lista de produtos no estoque.
        nome (str): Nome do produto.
        quantidade (int): Quantidade do produto.
        preco_custo (float): Preço de custo do produto.
        preco_venda (float): Preço de venda do produto.

    Returns:
        dict: O novo produto cadastrado.
    """
    codigo = gerar_novo_codigo(estoque_lista)
    novo_produto = {
        'nome': nome,
        'codigo': int(codigo),
        'quantidade': int(quantidade),
        'preco_custo': float(preco_custo),
        'preco_venda': float(preco_venda)
    }
    estoque_lista.append(novo_produto)
    return novo_produto
    
def gerar_novo_codigo(estoque_lista):
    """
    Gera um novo código para um produto.

    Args:
        estoque_lista (list): Lista de produtos no estoque.

    Returns:
        int: O novo código gerado.
    """
    if not estoque_lista:
        return 1  
    ultimo_codigo = max(produto['codigo'] for produto in estoque_lista)
    return ultimo_codigo + 1

def lista_produtos_ordenado_quantidade_asc(estoque_lista):
    """
    Lista os produtos ordenados pela quantidade em ordem crescente.

    Args:
        estoque_lista (list): Lista de produtos no estoque.

    Returns:
        list: Lista de produtos ordenados pela quantidade em ordem crescente.
    """
    return sorted(estoque_lista, key=lambda produto: produto['quantidade'])

def lista_produtos_ordenado_quantidade_desc(estoque_lista):
    """
    Lista os produtos ordenados pela quantidade em ordem decrescente.

    Args:
        estoque_lista (list): Lista de produtos no estoque.

    Returns:
        list: Lista de produtos ordenados pela quantidade em ordem decrescente.
    """
    return sorted(estoque_lista, key=lambda produto: produto['quantidade'], reverse=True)

def buscar_produto(*, estoque_lista, nome_usuario=None, codigo=None):
    """
    Busca produtos no estoque pelo nome ou código.

    Args:
        estoque_lista (list): Lista de produtos no estoque.
        nome_usuario (str, optional): Nome do produto a ser buscado.
        codigo (int, optional): Código do produto a ser buscado.

    Returns:
        list: Lista de produtos encontrados.
    """
    produtos_encontrados = []
    
    for produto in estoque_lista:
        if nome_usuario and nome_usuario.lower() in produto['nome'].lower():
            produtos_encontrados.append(produto)
        elif codigo and produto['codigo'] == codigo:
            produtos_encontrados.append(produto)
    
    return produtos_encontrados

def remover_produto(estoque_lista, codigo):
    """
    Remove um produto do estoque pelo código.

    Args:
        estoque_lista (list): Lista de produtos no estoque.
        codigo (int): Código do produto a ser removido.

    Returns:
        dict: O produto removido, ou None se não encontrado.
    """
    produto_removido = None
    
    for produto in estoque_lista:
        if produto['codigo'] == codigo:
            produto_removido = produto
            estoque_lista.remove(produto)
            return produto_removido
    return None
    
def consultar_produtos_esgotados(estoque_lista):
    """
    Consulta produtos esgotados no estoque.

    Args:
        estoque_lista (list): Lista de produtos no estoque.

    Returns:
        list: Lista de produtos esgotados, ou None se não houver produtos esgotados.
    """
    produtos_esgotados = []
    
    for produto in estoque_lista:
        if produto['quantidade'] == 0:
            produtos_esgotados.append(produto)
    
    if not produtos_esgotados:
        return None
    else:
        return produtos_esgotados
          
def filtrar_produtos_com_baixa_quantidade(estoque_lista, limite_minimo=5):
    """
    Filtra produtos com quantidade abaixo de um limite mínimo.

    Args:
        estoque_lista (list): Lista de produtos no estoque.
        limite_minimo (int, optional): Limite mínimo de quantidade. Default é 5.

    Returns:
        list: Lista de produtos com quantidade abaixo do limite mínimo.
    """
    produtos_com_baixa_quantidade = []
    
    for produto in estoque_lista:
        if produto['quantidade'] < limite_minimo:
            produtos_com_baixa_quantidade.append(produto)
    
    return produtos_com_baixa_quantidade

def atualizar_quantidade_produto(estoque_lista, codigo, quantidade):
    """
    Atualiza a quantidade de um produto no estoque.

    Args:
        estoque_lista (list): Lista de produtos no estoque.
        codigo (int): Código do produto a ser atualizado.
        quantidade (int): Nova quantidade do produto.

    Returns:
        dict: O produto atualizado, ou None se não encontrado ou quantidade inválida.
    """
    for produto in estoque_lista:
        if produto['codigo'] == codigo:
            if validar_quantidade_produto(produto, quantidade):
                produto['quantidade'] -= quantidade
                return produto
    return None

def atualizar_preco_venda(estoque_lista, codigo, novo_preco_venda):
    """
    Atualiza o preço de venda de um produto no estoque.

    Args:
        estoque_lista (list): Lista de produtos no estoque.
        codigo (int): Código do produto a ser atualizado.
        novo_preco_venda (float): Novo preço de venda do produto.

    Returns:
        dict: O produto atualizado, ou None se não encontrado ou preço inválido.
    """
    for produto in estoque_lista:
        if produto['codigo'] == codigo:
            if validar_preco_venda(produto, novo_preco_venda):
                produto['preco_venda'] = novo_preco_venda
                return produto
    return None  

def validar_preco_venda(produto, novo_preco_venda):
    """
    Valida se o novo preço de venda é maior ou igual ao preço de custo.

    Args:
        produto (dict): Produto a ser validado.
        novo_preco_venda (float): Novo preço de venda do produto.

    Returns:
        bool: True se o novo preço de venda é válido, False caso contrário.
    """
    return novo_preco_venda >= produto['preco_custo']

def validar_quantidade_produto(produto, quantidade):
    """
    Valida se a quantidade a ser atualizada é válida.

    Args:
        produto (dict): Produto a ser validado.
        quantidade (int): Quantidade a ser validada.

    Returns:
        bool: True se a quantidade é válida, False caso contrário.
    """
    return produto['quantidade'] >= quantidade

def calcular_lucro_presumido(estoque_lista):
    """
    Calcula o lucro presumido do estoque.

    Args:
        estoque_lista (list): Lista de produtos no estoque.

    Returns:
        float: O lucro presumido total.
    """
    lucro_total = 0.0
    
    for produto in estoque_lista:
        lucro_individual = (produto['preco_venda'] - produto['preco_custo']) * produto['quantidade']
        lucro_total += lucro_individual
    
    return lucro_total

def calcular_valor_total_estoque(estoque_lista):
    """
    Calcula o valor total do estoque.

    Args:
        estoque_lista (list): Lista de produtos no estoque.

    Returns:
        float: O valor total do estoque.
    """
    valor_total = 0.0
    for produto in estoque_lista:
        valor_total += produto['quantidade'] * produto['preco_venda']
    return valor_total