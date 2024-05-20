import socket

HOST = '127.0.0.1'  # Endereco IP do Servidor (loopback)
PORT = 5000  # Porta que o Servidor esta usando (identifica qual a aplicacao)
# Cria o socket do cliente
conexao_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (HOST, PORT)  # Forma a tupla de host, porta

conexao_tcp.connect(destino)  # Estabelece a conexao

estaLogado = False
mensagemRecebidaDecodificada = ''

while True:

	if (mensagemRecebidaDecodificada == "ACESSO LIBERADO" or estaLogado and mensagemRecebidaDecodificada != 'USUARIO DESLOGADO'):
		estaLogado = True
		mensagemDigitada = input(">> Digite a Mensagem ou digite 'sair' para finalizar o chat: ")
		mensagemCodificada = mensagemDigitada.encode('UTF-8')  # Codifica a mensagem para UTF-8
		conexao_tcp.send(mensagemCodificada)  # Envio a mensagem para o servidor
	else:
		estaLogado = False
		mensagemDigitada = input(">> Digite o código de acesso: ")
		mensagemCodificada = mensagemDigitada.encode('UTF-8')  # Codifica a mensagem para UTF-8
		conexao_tcp.send(mensagemCodificada)  # Envio a mensagem para o servidor


	mensagemRecebida = conexao_tcp.recv(1024)
	mensagemRecebidaDecodificada = mensagemRecebida.decode('UTF-8')

	if (mensagemRecebidaDecodificada == "ACESSO LIBERADO" or estaLogado and mensagemRecebidaDecodificada != 'USUARIO DESLOGADO'):
		print(f'\033[1;33m {destino} \033[0;0m \033[1;32m {mensagemRecebidaDecodificada} \033[0;0m')
	else:
		print(f'\033[1;33m {destino} \033[0;0m \033[1;31m {mensagemRecebidaDecodificada} \033[0;0m')


# ---------------- fim do protocolo --------------

conexao_tcp.close()  # fecha a conexao com o servidor
