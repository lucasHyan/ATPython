def validar_int_positivo(mensagem):
    while True:
        valor = input(mensagem)
        try:
            valor_int = int(valor)
            if valor_int < 0:
                raise ValueError("O valor deve ser um número inteiro não negativo.")
            return valor_int
        except ValueError as e:
            print(f"Entrada inválida. {e} Tente novamente.")

def validar_float_positivo(mensagem):
    while True:
        valor = input(mensagem)
        try:
            valor_float = float(valor)
            if valor_float < 0:
                raise ValueError("O valor deve ser um número não negativo.")
            return valor_float
        except ValueError as e:
            print(f"Entrada inválida. {e} Tente novamente.")

def exibir_relatorio_estoque(estoque_lista):
    custo_total = 0.0
    faturamento_total = 0.0
    
    descricao_len = 20
    codigo_len = 6
    quantidade_len = 10
    custo_len = 10
    preco_venda_len = 12
    valor_total_len = 12
    
    print(f"{'Descrição'.ljust(descricao_len)} {'Código'.center(codigo_len)} {'Quantidade'.center(quantidade_len)} {'Custo'.rjust(custo_len)} {'Preço Venda'.rjust(preco_venda_len)} {'Valor Total'.rjust(valor_total_len)}")
    print("="*80)
    
    for produto in estoque_lista:
        descricao = produto['nome'][:descricao_len] 
        codigo = str(produto['codigo']).center(codigo_len)
        quantidade = str(produto['quantidade']).center(quantidade_len)
        custo = f"R$ {produto['preco_custo']:.2f}".rjust(custo_len)
        preco_venda = f"R$ {produto['preco_venda']:.2f}".rjust(preco_venda_len)
        valor_total = f"R$ {produto['quantidade'] * produto['preco_venda']:.2f}".rjust(valor_total_len)
        
        print(f"{descricao.ljust(descricao_len)} {codigo} {quantidade} {custo} {preco_venda} {valor_total}")
        
        custo_total += produto['quantidade'] * produto['preco_custo']
        faturamento_total += produto['quantidade'] * produto['preco_venda']
    
    print("="*80)
    print(f"{'Custo Total:'.ljust(descricao_len + codigo_len + quantidade_len + custo_len + preco_venda_len)} {f'R$ {custo_total:.2f}'.rjust(valor_total_len)}")
    print(f"{'Faturamento Total:'.ljust(descricao_len + codigo_len + quantidade_len + custo_len + preco_venda_len)} {f'R$ {faturamento_total:.2f}'.rjust(valor_total_len)}")
    print(f"{'Lucro liquido presumido:'.ljust(descricao_len + codigo_len + quantidade_len + custo_len + preco_venda_len)} {f'R$ {faturamento_total - custo_total:.2f}'.rjust(valor_total_len)}")