def adicionar():
    print("Adicionar produto")

def atualizar():
    print("Atualizar produto")

def listar():
    print("Listar produtos")

def buscar():
    print("Buscar produto")

def menu_interativo():
    while True:
        print("\nMenu Interativo:")
        print("1. Adicionar produto")
        print("2. Atualizar produto")
        print("3. Listar produtos")
        print("4. Buscar produto")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            adicionar()
        elif escolha == '2':
            atualizar()
        elif escolha == '3':
            listar()
        elif escolha == '4':
            buscar()
        elif escolha == '5':
            print("Saindo do menu...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_interativo()