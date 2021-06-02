usuarios  = []

logado = False

while not logado:
    comando = input('Bem vindo! Digite 1 para login, 2 para criar um novo usuário ou x para sair: ')
    if comando == '1':
        usuario = input('Digite o nome do seu usuário: ')
        senha = input('Digite a senha do seu usuário: ')
        for u in usuarios:
            if u['usuario'] == usuario and u['senha'] == senha:
                logado = True
        if logado == False:
            print('Usuário ou senha inválidos!')

    elif comando == '2':
        usuario = input('Digite o nome para seu novo usuário: ')
        senha = input('Digite uma senha para seu usuário: ')
        # d = {}
        # d["usuario"] = usuario
        # d["senha"] = senha
        # usuarios.append(d)
        usuarios.append({ "usuario" : usuario , "senha" : senha })
        print(f"Usuário {usuario} cadastrado com sucesso!")
    elif comando == 'x':
        print('Até logo!')
        exit(0)
    else:
        print("Você está de brincadeira?")

noProg = True

while noProg:
    print("Bem vindo ao sistema!")
    sair = input('Digite x para sair: ')
    if sair == 'x':
        noProg = False
    