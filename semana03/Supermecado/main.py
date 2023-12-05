# main.py

def inserir_produto(produtos):
    codigo = input("Digite o código do produto (13 caracteres numéricos): ")
    
    # Verifica se o código é uma string numérica de 13 caracteres
    while len(codigo) != 13 or not codigo.isdigit():
        print("Código inválido. Deve ter 13 caracteres numéricos.")
        codigo = input("Digite o código do produto (13 caracteres numéricos): ")

    nome = input("Digite o nome do produto: ").capitalize()
    preco = float(input("Digite o preço do produto: "))
    
    novo_produto = {
        'codigo': codigo,
        'nome': nome,
        'preco': preco
    }
    
    produtos.append(novo_produto)
    print("Produto inserido com sucesso!")
def excluir_produto(produtos):
    codigo = input("Digite o código do produto a ser excluído: ")
    
    for produto in produtos:
        if produto['codigo'] == codigo:
            produtos.remove(produto)
            print("Produto excluído com sucesso!")
            return
    
    print("Produto não encontrado.")

# Função para listar todos os produtos
def listar_produtos(produtos):
    produtos.sort(key=lambda x: x['preco'])

    for i, produto in enumerate(produtos, start=1):
        print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")

        if i % 10 == 0:
            continuar = input("Pressione Enter para continuar ou digite 'q' para parar a listagem: ")
            if continuar.lower() == 'q':
                break

# Função para consultar o preço de um produto
def consultar_preco(produtos):
    codigo = input("Digite o código do produto para consultar o preço: ")
    
    for produto in produtos:
        if produto['codigo'] == codigo:
            print(f"O preço de {produto['nome']} é R${produto['preco']:.2f}")
            return
    
    print("Produto não encontrado.")

# Função principal
def main():
    produtos = []

    while True:
        print("\nSupermercado - Menu de Opções:")
        print("1. Inserir um novo produto")
        print("2. Excluir um produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar o preço de um produto")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir_produto(produtos)
        elif opcao == '2':
            excluir_produto(produtos)
        elif opcao == '3':
            listar_produtos(produtos)
        elif opcao == '4':
            consultar_preco(produtos)
        elif opcao == '0':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chama a função principal
if __name__ == "__main__":
    main()
