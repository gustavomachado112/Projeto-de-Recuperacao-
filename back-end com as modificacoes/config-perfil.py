import getpass

def exibir_configuracoes(usuario):
    """Exibe as configuracoes atuais do usuario."""
    print("\n--- Configuracoes Atuais ---")
    print(f"1. Foto de Perfil: {usuario['foto_perfil']}")
    print(f"2. Nome de Usuario: {usuario['nome_usuario']}")
    print(f"3. Nome de Perfil: {usuario['nome_perfil']}")
    print(f"4. E-mail: {usuario['email']}")
    print(f"5. Telefone: {usuario['telefone']}")
    print(f"6. Senha: {'*' * len(usuario['senha'])}") 
    print("--------------------------")

def validar_email(email):
    return "@" in email and "." in email.split("@")[1]

def validar_telefone(telefone):
    return telefone.isdigit() and len(telefone) >= 10

def validar_senha(senha):
    return len(senha) >= 6

def alterar_configuracoes(usuario):
    """Permite ao nosso usuario alterar as configuracoes."""
    while True:
        exibir_configuracoes(usuario)
        opcao = input("Deseja alterar alguma configuracao? (s/n): ").lower()

        if opcao == 'n':
            print("Configuracoes salvas.")
            break
        elif opcao == 's':
            try:
                escolha = int(input("Qual configuracao deseja alterar amigo? (1-6): "))
                
                if escolha == 1:
                    usuario['foto_perfil'] = input("Nova foto de perfil: ")
                    print("✅ Foto alterada com sucesso!")
                
                elif escolha == 2:
                    usuario['nome_usuario'] = input("Novo nome de usuário: ")
                    print("✅ Nome de usuario alterado com sucesso!")
                
                elif escolha == 3:
                    usuario['nome_perfil'] = input("Novo nome de perfil: ")
                    print("✅ Nome de perfil alterado com sucesso!")
                
                elif escolha == 4:
                    while True:
                        novo_email = input("Novo e-mail: ")
                        if validar_email(novo_email):
                            usuario['email'] = novo_email
                            print("✅ E-mail alterado com sucesso!")
                            break
                        print("❌ E-mail invalido! Tente novamente.")
                
                elif escolha == 5:
                    while True:
                        novo_tel = input("Novo telefone: ")
                        if validar_telefone(novo_tel):
                            usuario['telefone'] = novo_tel
                            print("✅ Telefone alterado com sucesso!")
                            break
                        print(" Telefone invalido! Use apenas numeros com DDD.")
                
                elif escolha == 6:
                    while True:
                        nova_senha = getpass.getpass("Nova senha: ")
                        if validar_senha(nova_senha):
                            confirmar = getpass.getpass("Confirmar nova senha: ")
                            if nova_senha == confirmar:
                                usuario['senha'] = nova_senha
                                print("✅ Senha alterada com sucesso!")
                                break
                            else:
                                print("❌ Erro: Senhas não coincidem entre si!")
                        else:
                            print(" Senha muito curta! tem que ter no minimo 6 caracteres.")
                
                else:
                    print("❌ Opção invalida. Digite um numero de 1 a 6.")
                    continue
                
                
                continuar = input("\nDeseja alterar outra configuracao? (s/n): ").lower()
                if continuar != 's':
                    print("✅ Configurações salvas com sucesso!")
                    break
                    
            except ValueError:
                print("❌ Entrada invalida. Digite um numero porfavor.")
        else:
            print(" Opção invalida. Digite 's' para sim ou 'n' para nao.")


minha_conta = {
    'foto_perfil': 'avatar_padrao.png',
    'nome_usuario': 'usuario_ayuda',
    'nome_perfil': 'Doações Ayuda',
    'email': 'contato@ayuda.com',
    'telefone': '11999999999',
    'senha': 'senha123'
}


print("Bem-vindo ao sistema Ayuda!")
alterar_configuracoes(minha_conta)
print("\n--- Configurações Finais ---")
exibir_configuracoes(minha_conta)
print("\nObrigado por usar o Ayuda!")
