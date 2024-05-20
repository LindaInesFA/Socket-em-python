import socket
HOST = ''              # Endereco IP do Servidor e o endereco atual do computador
PORT = 5000            # Porta que o Servidor na maquina
# Cria o socket do servidor
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT) # Forma a tupla de host, porta

tcp.bind(orig)		# Solicita ao S.O. acesso exclusivo a porta 5000
tcp.listen(10)		# Entra no modo de escuta

estaLogado = False
usuarioEncerrouOChat = False
codigo=""

# gerenciado a leitura do arquivo
with open("dados.txt", "r") as bancoDeDados:
    codigo= bancoDeDados.readline()


print(f'\033[1;34m>>> Aguardando Conexão\033[0;0m')
while True:
    conexao, cliente = tcp.accept() # Aceita conexao do cliente
    print(f'\033[1;36m Concetado por\033[0;0m \033[1;35m {cliente} \033[0;0m')

    while True:
#------- inicio do protocolo --------------

        mensagemRecebida = conexao.recv(1024)
        mensagemRecebidaDecodificada = mensagemRecebida.decode('UTF-8')
        codigoSair = mensagemRecebidaDecodificada.lower()
        print(f'\033[1;33m {cliente} \033[0;0m \033[1;32m {mensagemRecebidaDecodificada} \033[0;0m')

        if (codigoSair == 'sair' and estaLogado):
            estaLogado = False
            usuarioEncerrouOChat = True
            conexao.send("USUARIO DESLOGADO".encode('UTF-8'))
            print(f'\033[1;34m O USUÁRIO ENCERROU O CHAT \033[0;0m')

        if estaLogado :
            mensagemDigitada=input(">> Digite a Mensagem: ")
            mensagemCodificada = mensagemDigitada.encode('UTF-8')
            conexao.send(mensagemCodificada)

        else:
            if (mensagemRecebidaDecodificada == codigo):
                conexao.send("ACESSO LIBERADO".encode('UTF-8'))
                print(f'\033[1;33m {cliente} \033[0;0m \033[1;34m ACESSO LIBERADO \033[0;0m')
                estaLogado = True
            else:
                if not usuarioEncerrouOChat:
                    conexao.send("ACESSO NEGADO".encode('UTF-8'))
                    print(f'\033[1;33m {cliente} \033[0;0m \033[1;31m ACESSO NEGADO \033[0;0m')

        usuarioEncerrouOChat = False

#---------------- fim do protocolo --------------

conexao.close()		# fecha a conexao com o cliente
