agenda = [
    ['Fulano', 'fulano@gmail.com', 27999999999] #INICIALIZANDO A LISTA (NÃO É OBRIGATÓRIO)
]

while True:
        menu = int(input('O que deseja executar?\n\n[1] Criar contato\n[2] Pesquisar contato\n[3] Atualizar contato\n[4] Excluir contato\n[5] Sair\n'))
        if(menu != 1 and menu != 2 and menu != 3 and menu != 4 and menu != 5):
            print("Opção incorreta! Tente novamente...\n")
        elif(menu == 1):
            nome = input('Insira o nome: ')
            email = input('Insira o email: ')
            whatsapp = int(input('Insira o WhatsApp: \n'))
            
            #AGRUPA OS DADOS EM UMA VARIÁVEL COM LISTA
            contato = [nome, email, whatsapp]
            
            #INSERE O CONTATO CRIADO NA LISTA AGENDA
            agenda.append(contato)

            #INFORMA O INDÍCE DO CONTATO NA LISTA AGENDA
            print(f'CONTATO REGISTRADO N° {agenda.index(agenda[index])} COM SUCESSO')

            #MOSTRA AS INFORMAÇÕES DO CONTATO
            print(f'NOME: {nome}')
            print(f'EMAIL: {email}')
            print(f'WHATSAPP: {whatsapp}\n')
        elif(menu == 2):
            buscaNome = input('\nInsira o nome do contato: ')
            nomes = [agenda[0] for agenda in agenda] #BUSCAR O ITEM QUE DESEJA DENTRO DA LISTA AGENDA

            try:
                #TRANFORMAR O INDEX QUE A GENTE PRECISA DENTRO DA LISTA
                index = nomes.index(buscaNome)
                
                print('CONTATO ENCONTRADO COM SUCESSO!')
                print(f'DADOS DO CONTATO N°: {agenda.index(agenda[index])}')
                print(f'NOME: {agenda[index][0]}')
                print(f'EMAIL: {agenda[index][1]}')
                print(f'WHATSAPP: {agenda[index][2]}\n')

            except Exception as Erro:
                print(f'ERRO: {Erro}')
        elif(menu == 3):
            buscaEmail = input('\nInsira o e-mail do contato: ')
            emails = [agenda[1] for agenda in agenda]

            try:
                index = emails.index(buscaEmail)
                
                print('CONTATO ENCONTRADO COM SUCESSO!')
                print(f'DADOS DO CONTATO N°: {agenda.index(agenda[index])}')
                print(f'NOME: {agenda[index][0]}')
                print(f'EMAIL: {agenda[index][1]}')
                print(f'WHATSAPP: {agenda[index][2]}\n')

                alterar = int(input('Deseja alterar o nº de WhatsApp?\n\n[1] SIM\n[2] NÃO\n'))
                if(alterar != 1  and alterar != 2):
                    print("Opção incorreta! Tente novamente...\n")
                elif(alterar == 1):
                    novoWhatsapp = int(input('\nDigite o novo n° de contato: '))

                    #LISTA[INDEX][LOCALIZAÇÃO]: ALTERAR UM ELEMENTO ESPECIFICO, NAVEGANDO ENTRE AS LISTAS
                    agenda[index][2] = novoWhatsapp

                    print('\nCONTATO ALTERADO COM SUCESSO!')
                    print(f'NOME: {agenda[index][0]}')
                    print(f'EMAIL: {agenda[index][1]}')
                    print(f'WHATSAPP: {agenda[index][2]}\n')
                else:
                    print('ALTERAÇÃO CANCELADA!\n')
            
            except Exception as Erro:
                print(f'Erro: {Erro}')

        elif(menu == 4):
            buscaNome = input('Insira o nome do contato: ')
            nomes = [agenda[0] for agenda in agenda]

            try:
                index = nomes.index(buscaNome)
                agenda.pop(index) #RETIRAR UM ITEM DA LISTA

                print(f'\nCONTATO N° {agenda.index(agenda[index])} EXCLUÍDO COM SUCESSO\n')

            except Exception as Erro:
                print(f'Erro: {Erro}')
        else:
            print('\nSESSÃO ENCERRADA! ATÉ A PRÓXIMA...\n')
            break 
            #QUEBRA DO CÓDIGO