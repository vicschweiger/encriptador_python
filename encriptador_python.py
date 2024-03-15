CODIGO = {
        "a": "fui",
        "e": "roi",
        "i": "rei",
        "o": "hal",
        "u": "jhf"
    }

while True:
    entrada = int(input('''
        
    ####################MENU####################
        
        1. Encriptar
        2. Descriptar
        3. Sair

    #############################################

    '''))

    if entrada == 1:   
        def encriptador(mensagem):

            global CODIGO
            for chave, valor in CODIGO.items():
                mensagem = mensagem.replace(chave, valor)
            
            return mensagem

        mensagem = input("Digite sua mensagem: ")

        mensagem_encriptada = encriptador(mensagem)
        print("Mensagem descriptada:", mensagem_encriptada)

    elif entrada == 2:
        
        def descriptador(mensagem):
            global CODIGO
            for chave, valor in CODIGO.items():
                mensagem = mensagem.replace(valor, chave)
            
            return mensagem

        mensagem = input("Digite sua mensagem: ")

        mensagem_descriptada = descriptador(mensagem)
        print("Mensagem descriptada:", mensagem_descriptada)

    elif entrada == 3:
        print("Obrigado por usar nosso mensageiro, até a próxima!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida")