pessoa = {
    "cpf" : "123456789012",
    "nome" : "Fernando",
    "dataNascimento" : "10/10/1910"
}

# print(pessoa)

# print(pessoa["cpf"])
# print(pessoa["dataNascimento"])

pessoa["nome"] = "Fernando Passos"

# print(pessoa)

pessoa["dataEmissao"] = "02/02/2002"

# print(pessoa)


usuario = {}

# print(type(usuario))

usuario["nomeUsuario"] = "fernando"
usuario["senha"] = "123"
usuario["nomeCompleto"] = "Fernando Passos"
usuario["dataDeRegistro"] = "10/10/2010"

# print(usuario)

# u = input("Digite seu nome de usuário: ")
# s = input("Digite sua senha: ")

# if(usuario["nomeUsuario"] == u and usuario["senha"] == s):
#     print("Bem vindo ao sistema X!")
# else:
#     print("Usuário ou senha invalidos!")

for chave in usuario:
    # print(chave)
    # print(f"Chave: {chave} - Valor: {usuario[chave]}")
    pass


leitor = {
    "nome" : "Fulano",
    "identidade" : "0987654",
    "livros" : ["1808", "1822", "1889"]
}

# print(leitor["livros"])

for livro in leitor["livros"]:
    # print(f"Nome do leitor: {leitor['nome']} - Nome do livro: {livro}")
    pass

leitores = [
    {
        "nome" : "Fulano",
        "identidade" : "0987654",
        "livros" : ["1808", "1822", "1889"],
        "atrasado" : True
    },
    {
        "nome" : "Beltrano",
        "identidade" : "99887766",
        "livros" : ["Livro 1", "Livro 2", "Livro 3"],
        "atrasado" : False
    },
    {
        "nome" : "Sicrano",
        "identidade" : "22334455",
        "livros" : ["Livro 7", "Livro 8", "Livro 9"],
        "atrasado" : True
    },
    {
        "nome" : "Wally",
        "identidade" : "554433399",
        "livros" : ["Livro 4", "Livro 5", "Livro 6"],
        "atrasado" : False
    }
]

# print(leitores)
for leitor in leitores:
    for chave in leitor:
        print(chave, leitor[chave])