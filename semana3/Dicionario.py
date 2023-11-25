 # Função para reajustar os salários em 10%
def reajusta_dez_porcento(lista_empregados):
    for empregado in lista_empregados:
        empregado['salario'] *= 1.1  # Aumento de 10%

# Função para ler os dados do arquivo e criar a lista de empregados
def ler_dados_do_arquivo(nome_arquivo):
    lista_empregados = []
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.strip().split(',')
            empregado = {
                'nome': dados[0],
                'sobrenome': dados[1],
                'ano_nascimento': int(dados[2]),
                'RG': dados[3],
                'ano_admissao': int(dados[4]),
                'salario': float(dados[5])
            }
            lista_empregados.append(empregado)
    return lista_empregados

# Função para exibir os dados dos empregados
def exibir_dados(lista_empregados):
    for empregado in lista_empregados:
        print(f"Nome: {empregado['nome']} {empregado['sobrenome']}, Ano de Nascimento: {empregado['ano_nascimento']}, RG: {empregado['RG']}, Ano de Admissão: {empregado['ano_admissao']}, Salário: {empregado['salario']}")

# Arquivo de exemplo com dados dos empregados
nome_arquivo ='dados_empregados.txt'

# Criar a lista de empregados lendo os dados do arquivo
lista_empregados = ler_dados_do_arquivo(nome_arquivo)

# Exibir os dados antes do reajuste
print("Dados dos empregados antes do reajuste:")
exibir_dados(lista_empregados)

# Aplicar o reajuste de 10% nos salários
reajusta_dez_porcento(lista_empregados)

# Exibir os dados após o reajuste
print("\nDados dos empregados apos o reajuste:")
exibir_dados(lista_empregados)



