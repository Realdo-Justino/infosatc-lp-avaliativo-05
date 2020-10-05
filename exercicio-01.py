listaNome=[]
listaSobrenome=[]
listaCpf=[]
listaEndereco=[]
listaEmail=[]
listaCelular=[]
listaSenha=[]
tamanhoValor=0
tamanhoMinimo=0
usuario=0
contaBancaria=[]
confirmaçãoCadastro="s"
pessoa=""
login=0
quantiaDinheiro=0
nomeAdministrador=["Realdo"]
senhaAdmistrador=["46365@"]


import re
def procura():
    login=0
    while(login==0):
        contador=0
        contador2=0
        variavel=0
        pessoa=(input("Qual é o nome do usuario?\n"))
        for i in listaNome:
            contador=contador+1
            if i==pessoa:
                variavel=1
                contador2=contador
                pass
        if(variavel==0):
            print("Nome invalido")
            pass
        if(variavel==1):
            contador2=contador2-1
            senha=(input("Qual é a senha desse usuario?\n"))
            if senha==listaSenha[contador2]:
                login=1
                return contador2
            else:
                print("Senha incorreta")
                login=0

def atualizarCliente():
    contador2=procura()
    contador=0
    while(contador==0):
        opcao=(input("\nO que deseja mudar?\n1-Nome\n2-Sobrenome\3-Endereço\n4-E-mail\n5-Celular\n6-Senha\n7-CPF\n8-Todos\n9-Nada\n"))
        if(opcao=="1"):
            listaNome.pop(contador2)
            listaNome.insert(contador2,valor(3,"Insira seu novo nome: ",0)) 
        
        if(opcao=="2"):
            listaSobrenome.pop(contador2)
            listaSobrenome.insert(contador2,valor(3,"Insira seu novo Sobrenomenome: ",0))

        if(opcao=="3"):
            listaEndereco.pop(contador2)
            listaEndereco.insert(contador2,valor(0,"Insira seu novo Endereço: ",0))
            
        if(opcao=="4"):
            listaEmail.pop(contador2)
            listaEmail.insert(contador2,valor(0,"Insira seu novo Email: ",2))

        if(opcao=="5"):
            listaCelular.pop(contador2)
            listaCelular.insert(contador2,valor(0,"Insira seu novo Numero de Celular: ",0))

        if(opcao=="6"):
            listaSenha.pop(contador2)
            listaSenha.insert(contador2,valor(5,"Insira sua nova senha: ",1))

        if(opcao=="7"):
            listaCpf.pop(contador2) 
            listaCpf.insert(contador2,valor(0,"Insira seu  novo Cpf: ",0))

        if(opcao=="8"):
            listaNome.pop(contador2)
            listaSenha.pop(contador2)
            listaCelular.pop(contador2)
            listaCpf.pop(contador2)
            listaEmail.pop(contador2)
            listaSobrenome.pop(contador2)
            listaEndereco.pop(contador2)

            listaNome.insert(contador2,valor(3,"Insira seu novo nome: ",0))
            listaSobrenome.insert(contador2,valor(3,"Insira seu novo Sobrenomenome: ",0))
            listaEndereco.insert(contador2,valor(0,"Insira seu novo Endereço: ",0))
            listaEmail.insert(contador2,valor(0,"Insira seu novo Email: ",2))
            listaCelular.insert(contador2,valor(0,"Insira seu novo Numero de Celular: ",0))
            listaSenha.insert(contador2,valor(5,"Insira sua nova senha: ",1))
            listaCpf.insert(contador2,valor(0,"Insira seu  novo Cpf: ",0))
            

        if(opcao=="9"):
            finalizar=(input("Deseja realmente encerrar? s/n\n"))
            if(finalizar=="s"):
                contador=1

def deletarCliente():
    contador2=procura()
    listaNome.pop(contador2)
    listaSenha.pop(contador2)
    listaCelular.pop(contador2)
    listaCpf.pop(contador2)
    listaEmail.pop(contador2)
    listaSobrenome.pop(contador2)
    listaEndereco.pop(contador2)
            
def mostrarCliente():
    contador2=procura()
    print("O usuario é: ",listaNome[contador2])
    print("Seu sobrenome é: ",listaSobrenome[contador2])
    print("A senha é: ",listaSenha[contador2])
    print("Seu Cpf é: ",listaCpf[contador2])
    print("Seu endereco é: ",listaEndereco[contador2])
    print("Seu e-mail é: ",listaEmail[contador2])
    print("Seu celular é: ",listaCelular[contador2])

def numeroValido(texto,numero,conta):
    validacao=1
    contador=1
    quantiaDinheiro=(float(input(texto)))
    while(validacao==1):
        if(quantiaDinheiro<0):
            quantiaDinheiro=(float(input("Quantidade atribuida é menor que 0, por favor insira uma quantia valida\n")))
        else:
            if(numero==0):
                while(contador==1):
                    if(quantiaDinheiro>conta):
                        quantiaDinheiro=(float(input("Quantidade atribuida é maior que sau possui atualmente, por favor insira uma quantia valida\n")))
                    if(quantiaDinheiro<0):
                        quantiaDinheiro=(float(input("Quantidade atribuida é menor que 0, por favor insira uma quantia valida\n")))
                    else:
                        contador=0
                        return quantiaDinheiro
                        pass
            else:
                validação=0
                return quantiaDinheiro
    
def procurarAdministrador():
    login=0
    while(login==0):
        contador=0
        contador2=0
        variavel=0
        pessoa=(input("Qual é o nome do Administrador?\n"))
        for i in nomeAdministrador:
            contador=contador+1
            if i==pessoa:
                variavel=1
                conatdor2=contador
                pass
        if(variavel==0):
            print("Nome invalido")
            pass
        if(variavel==1):
            senha=(input("Qual é a senha desse Administrador?\n"))
            contador2=contador2-1
            if senha==senhaAdmistrador[contador2]:
                login=1
                return contador
            else:
                print("Senha incorreta")
                login==0

def email(email):
    regex = re.compile('@') 
    if(regex.search(email) == None):
        print("O email inserido é invalido, por favor insira outro\n")
        return 1
    else: 
        valorLetras=len(email)
        contador=0
        variavel=0
        for i in range(valorLetras):
            if((contador>=1)and(email[contador]=="@")and(contador+1<valorLetras)):
                variavel=1
            contador=contador+1
        if(variavel==0):
            print("O email inserido é invalido, por favor insira outro")
            return 1
        else:
            return 0

def caracterEspecial(text):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
    if(regex.search(text) == None):
        print("Não tem caracter especial, por favor insira outra senha")
        return 1
    else: 
        return 0

def valor(tamanhoMinimo,texto,caracter):
    contador=1
    tamanhoValor=0
    while(contador>0):
        valor=(input(texto))
        tamanhoValor=(len(valor))
        if(tamanhoValor<tamanhoMinimo):
            print("Numero de caracters minimos não foi atingido")
            pass
        else:
            if(caracter==0):
                contador=0
                return valor
            if(caracter==1):
                contador2=caracterEspecial(valor)
                if(contador2==0):
                    return valor
                    contador=0
            if(caracter==2):
                contador2=email(valor)
                if(contador2==0):
                    return valor
                    contador=0

def cadastroCliente():
    listaNome.append(valor(3,"Insira seu nome: ",0)) 
    listaSenha.append(valor(5,"Insira sua senha: ",1))
    listaSobrenome.append(valor(3,"Insira seu Sobrenomenome: ",0))
    listaCpf.append(valor(0,"Insira seu Cpf: ",0))
    listaEndereco.append(valor(0,"Insira seu Endereço: ",0))
    listaEmail.append(valor(0,"Insira seu Email: ",2))
    listaCelular.append(valor(0,"Insira seu Numero de Celular: ",0))

confirmaçãoCadastro=(input("Deseja cadastrar uma pessoa? s/n\n"))
while(confirmaçãoCadastro=="s"):
    cadastroCliente()
    usuario=usuario+1
    confirmaçãoCadastro=(input("Deseja cadastrar mais uma pessoa? s/n\n"))

for i in range(usuario):
    contaBancaria.append(0)

conta=(input("Deseja acessar uma conta? s/n\n"))
adminstrador=(input("Voce é um admisitrador? s/n\n"))
if(conta=="s" and adminstrador=="n"):
    login=procura()
    contador=0
    while(contador==0):
        opcao=(input("\nDeseja executar qual função\n1-Depositar\n2-Sacar\n3-Conferir Saldo\n4-Transferir\n5-Encerrar Conta\n\n"))
        if(opcao=="1"):
            quantiaDinheiro=numeroValido("Insira a quantia em dinheiro a depositar ",1,contaBancaria[login])
            contaBancaria[login]=contaBancaria[login]+quantiaDinheiro

        if(opcao=="2"):
            quantiaDinheiro=numeroValido("Insira a quantia em dinheiro a sacar ",0,contaBancaria[login])
            contaBancaria[login]=contaBancaria[login]-quantiaDinheiro
        if(opcao=="3"):
            print("Sua conta atual possui ",contaBancaria[login]," reais")

        if(opcao=="4"):
            usurioAnterior=login
            login=procura()
            quantiaDinheiro=numeroValido("Insira a quantia em dinheiro a transferir ",0,contaBancaria[login])
            contaBancaria[login]=contaBancaria[login]+quantiaDinheiro
            contaBancaria[usurioAnterior]=contaBancaria[usurioAnterior]-quantiaDinheiro

        if(opcao=="5"):
            finalizar=(input("Deseja realmente encerrar? s/n\n"))
            if(finalizar=="s"):
                contador=1
                pass

if(conta=="s" and adminstrador=="s"):
    login=procurarAdministrador()
    print("Login bem sucedido\n")
    contador=0
    while(contador==0):
        opcao=(input("\nDeseja executar qual função\n1-Consultar um cliente\n2-Consultar lista de clientes\n3-Deletar um cliente\n4-Atualizar dados de um cliente específico.\n5-Encerrar Conta\n\n"))
        if(opcao=="1"):
            mostrarCliente()

        if(opcao=="2"):
            for i in range(usuario):
                print("\nO nome do usuario ",i+1," é ",listaNome[i])
                print("A senha do usuario ",i+1," é ",listaSenha[i])
                print("O seu sobrenome ",i+1," é: ",listaSobrenome[i])
                print("Seu Cpf ",i+1," é: ",listaCpf[i])
                print("Seu endereco ",i+1," é: ",listaEndereco[i])
                print("Seu e-mail ",i+1," é: ",listaEmail[i])
                print("Seu celular ",i+1," é: ",listaCelular[i])

        if(opcao=="3"):
            deletarCliente()
            usuario=usuario-1

        if(opcao=="4"):
            atualizarCliente()
        
        if(opcao=="5"):
            finalizar=(input("Deseja realmente encerrar? s/n\n"))
            if(finalizar=="s"):
                contador=1

if(conta=="n"):
    print("Tenha um bom dia")
    pass
