estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#Monitor LG;206;8;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"

estoque_lista = []
itens = estoque_inicial.split('#')
for item in itens:
    nome, codigo, quantidade, preco_custo, preco_venda = item.split(';')
    novo_produto = {
        'nome': nome,
        'codigo': int(codigo),
        'quantidade': int(quantidade),
        'preco_custo': float(preco_custo),
        'preco_venda': float(preco_venda)
    }
    
    estoque_lista.append(novo_produto)

for produto in estoque_lista:
    print(produto)
