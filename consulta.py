#Consular valores de produtos na loja
#Lista de pdodutos
produtos = ['geladeira', 'televisão', 'celular', 'tablet', 'fogão', 'computador']
#Lista de valores
valores = ['5000', '2000', '1500', '2500', '3000', '6000']
#Buscar por um produto no estoque
consulta = input('Informe qual produto deseja pesquisar: ')
#Verificar se o produto consta no estoque
if consulta in produtos:
    i = produtos.index(consulta)
    valor_produto = valores[i]
    print('O valor do produto "{}" é R$ {}'.format(consulta, valor_produto))
else:
    print('Este produto não consta no estoque')