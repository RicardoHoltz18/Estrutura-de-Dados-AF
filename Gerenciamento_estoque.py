from Arvore import BinaryTree

def main():
    estoque = BinaryTree()

    while True:
        print("1. Adicionar categoria")
        print("2. Adicionar produto a uma categoria")
        print("3. Remover produto de uma categoria")
        print("4. Mostrar produtos de uma categoria")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            categoria = input("Digite o nome da nova categoria: ")
            estoque.insert(categoria)
        elif escolha == "2":
            categoria = input("Digite o nome da categoria: ")
            produto = input("Digite o nome do produto: ")
            categoria_node = estoque.find(categoria)
            if categoria_node:
                categoria_node.produtos.insert(produto)
            else:
                print("Categoria não encontrada!")
        elif escolha == "3":
            categoria = input("Digite o nome da categoria: ")
            produto = input("Digite o nome do produto a ser removido: ")
            categoria_node = estoque.find(categoria)
            if categoria_node:
                if categoria_node.produtos.remove(produto):
                    print("Produto removido com sucesso!")
                else:
                    print("Produto não encontrado!")
            else:
                print("Categoria não encontrada!")
        elif escolha == "4":
            categoria = input("Digite o nome da categoria: ")
            categoria_node = estoque.find(categoria)
            if categoria_node:
                print("Produtos na categoria {}: ".format(categoria))
                categoria_node.produtos.display()
            else:
                print("Categoria não encontrada!")
        elif escolha == "5":
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
