from abc import ABC, abstractmethod

# Classe para representar dados de data
class Data:
    def __init__(self, dia=1, mes=1, ano=2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia invalido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês invalido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano invalido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia invalido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês invalido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return  self.__dia == outraData.__dia and \
                self.__mes == outraData.__mes and \
                self.__ano == outraData.__ano
    
    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False
    
    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False
    
# Classe abstrata base para análise de dados
class AnaliseDados(ABC):
   # (Métodos abstratos para serem implementados pelas subclasses)
    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados
        self.__lista = []

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass

    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass

    @abstractmethod
    def listarEmOrdem(self):
        pass

    def calcularMediana(self):
        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)

        if tamanho % 2 == 0:
            meio1 = lista_ordenada[tamanho // 2 - 1]
            meio2 = lista_ordenada[tamanho // 2]
            return meio1, meio2
        else:
            meio = lista_ordenada[tamanho // 2]
            return meio,

    def calcularMedia(self):
        return sum(self.__lista) / len(self.__lista)

class ListaNomes(AnaliseDados):
    def __init__(self):
        super().__init__(type(str))

    def entradaDeDados(self):
        nome = input("Digite um nome: ")
        self._AnaliseDados__lista.append(nome)

    def mostraMediana(self):
        mediana = self.calcularMediana()
        print(f"Mediana: {mediana[0]}")

    def mostraMenor(self):
        menor = min(self._AnaliseDados__lista)
        print(f"Menor: {menor}")

    def mostraMaior(self):
        maior = max(self._AnaliseDados__lista)
        print(f"Maior: {maior}")

    def listarEmOrdem(self):
        return sorted(self._AnaliseDados__lista)

class ListaDatas(AnaliseDados):
    def __init__(self):
        super().__init__(type(Data))
        
   

class ListaDatas(AnaliseDados):
    def __init__(self):
        super().__init__(type(Data))

    def entradaDeDados(self):
        try:
            while True:
                dia = int(input("Digite o dia: "))
                if 1 <= dia <= 31:
                    break
                else:
                    print("Dia invalido. Digite um valor entre 1 e 31.")

            while True:
                mes = int(input("Digite o mes: "))
                if 1 <= mes <= 12:
                    break
                else:
                    print("Mês invalido. Digite um valor entre 1 e 12.")

            while True:
                ano = int(input("Digite o ano: "))
                if 2000 <= ano <= 2500:
                    break
                else:
                    print("Ano invalido. Digite um valor entre 2000 e 2500.")

            data = Data(dia, mes, ano)
            self._AnaliseDados__lista.append(data)
        except ValueError as e:
            print(f"Erro ao inserir a data: {e}")

    def mostraMediana(self):
        mediana = self.calcularMediana()
        print(f"Mediana: {mediana[0]}")

    def mostraMenor(self):
        menor = min(self._AnaliseDados__lista)
        print(f"Menor: {menor}")

    def mostraMaior(self):
        maior = max(self._AnaliseDados__lista)
        print(f"Maior: {maior}")

    def listarEmOrdem(self):
        return sorted(self._AnaliseDados__lista, key=lambda x: (x.ano, x.mes, x.dia))



class ListaSalarios(AnaliseDados):
    def __init__(self):
        super().__init__(type(float))

    def entradaDeDados(self):
        salario = float(input("Digite um salario: "))
        self._AnaliseDados__lista.append(salario)

    def mostraMediana(self):
        mediana = self.calcularMediana()
        print(f"Mediana: {mediana[0]}")

    def mostraMenor(self):
        menor = min(self._AnaliseDados__lista)
        print(f"Menor: {menor}")

    def mostraMaior(self):
        maior = max(self._AnaliseDados__lista)
        print(f"Maior: {maior}")

    def listarEmOrdem(self):
        return sorted(self._AnaliseDados__lista)

class ListaIdades(AnaliseDados):
    def __init__(self):
        super().__init__(type(int))

    def entradaDeDados(self):
        idade = int(input("Digite uma idade: "))
        self._AnaliseDados__lista.append(idade)

    def mostraMediana(self):
        mediana = self.calcularMediana()
        print(f"Mediana: {mediana[0]}")

    def mostraMenor(self):
        menor = min(self._AnaliseDados__lista)
        print(f"Menor: {menor}")

    def mostraMaior(self):
        maior = max(self._AnaliseDados__lista)
        print(f"Maior: {maior}")

    def listarEmOrdem(self):
        return sorted(self._AnaliseDados__lista)
# Função para iterar sobre duas listas simultaneamente
def iterador_zip(lista1, lista2):
    for nome, salario in zip(lista1, lista2):
        yield nome, salario    
# Função para aplicar um reajuste percentual a salários
def reajuste_salarios(lista_salarios, percentual):
    for salario in map(lambda x: x * (1 + percentual / 100), lista_salarios):
        yield salario

def ajuste_datas(lista_datas):
    for data in map(lambda x: x if x.ano >= 2019 else Data(1, x.mes, x.ano), lista_datas):
        yield data

# Função principal para interação com o usuário
def menu():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    while True:
        print("\nMenu de Opçoes:")
        print("1. Incluir um nome na lista de nomes")
        print("2. Incluir um salario na lista de salarios")
        print("3. Incluir uma data na lista de datas")
        print("4. Incluir uma idade na lista de idades")
        print("5. Percorrer as listas de nomes e salarios")
        print("6. Calcular o valor da folha com um reajuste de 10%")
        print("7. Modificar o dia das datas anteriores a 2019")
        print("8. Sair")

        opcao = input("Escolha uma opcao (1-8): ")

        if opcao == "1":
            nomes.entradaDeDados()
        elif opcao == "2":
            salarios.entradaDeDados()
        elif opcao == "3":
            datas.entradaDeDados()
        elif opcao == "4":
            idades.entradaDeDados()
        elif opcao == "5":
            for nome, salario in iterador_zip(nomes.listarEmOrdem(), salarios.listarEmOrdem()):
                print(f"{nome}: R${salario:.2f}")
        elif opcao == "6":
            # Iterador map: reajuste de salários em 10%
            salarios_reajustados = list(map(lambda x: x * 1.10, salarios.listarEmOrdem()))
            print("Salarios Reajustados:", salarios_reajustados)
            print("Custo Total da Folha de Pagamento:", sum(salarios_reajustados))
        elif opcao == "7":
            # Iterador filter e map: modificar dia das datas anteriores a 2019
            datas_ajustadas = list(
                map(lambda x: x if x.ano >= 2019 else Data(1, x.mes, x.ano), datas.listarEmOrdem())
            )
            print("Datas Ajustadas:")
            for data in datas_ajustadas:
                print(data)
        elif opcao == "8":
            print("Encerrando o programa.")
            break
        else:
            print("Opcao invalida. Tente novamente.")
# Ponto de entrada do programa
if __name__ == "__main__":
    menu()



