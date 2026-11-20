# Define a classe base 'Animal' 
class Animal:
   # Método construtor: é executado automaticamente ao criar um objeto da classe
   def __init__(self, nome, idade):
       self.nome = nome    # Atributo 'nome' é armazenado no objeto
       self.idade = idade   # Atributo 'idade' também é armazenado no objeto

   # Método que imprime um som genérico - pode ser sobrescrito em classes filhas
   def falar(self):
       print("Som genérico")


# Define a subclasse 'Cao' que herda da classe 'Animal'
class Cao(Animal):
    # Construtor da subclasse, recebe nome, idade e raça como parâmetros
    def __init__(self, nome, idade, raça):
        # Chama o construtor da superclasse (Animal) para inicializar nome e idade
        super().__init__(nome, idade)  
        self.raça = raça  # Atributo específico da classe Cao

    # Sobrescre o método 'falar' da classe Animal
    def falar(self):
        print("Woof!")   # Som específico de um cachorro


# Cria uma instância (objeto) da classe Cao com nome "Rex", idade 3 e raça "Amigo"
meu_cao = Cao("Rex", 3, "Amigo")

# Exibe o nome do cão: Rex
print(meu_cao.nome)

# Exibe a idade do cão: 3
print(meu_cao.idade)

# Exibe a raça do cão: Amigo
print(meu_cao.raça)

# Chama o método 'falar' - como foi sobrescrito em Cao, imprimie "Woof!"
meu_cao.falar()
    