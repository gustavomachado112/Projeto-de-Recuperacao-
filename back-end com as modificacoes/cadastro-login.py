import getpass

print("=== SISTEMA DE CADASTRO DO PYTHON ===")

while True:
    nome_usuario = input("Digite  o seu nome de usuario: ").strip()
    if nome_usuario:
        break
    print("Lembre-se vc nao pode deixar vazio!")

nome_perfil = input("Digite seu nome de perfil porfavor: ").strip() or nome_usuario

while True:
    email = input("Digite seu email: ").strip()
    if "@" in email and "." in email.split("@")[1]:
        break
    print("Email pode estar invalido! use ex:cachorro@dominio.com")

while True:
    telefone = input("Digite seu telefone (apenas números): ").strip()
    if telefone.isdigit() and len(telefone) >= 10:
        break
    print("Telefone inválido! Use números com DDD (obrigatorio usar).")

while True:
    data_nasc = input("Digite sua data de nascimento (DD/MM/AAAA): ").strip()
    partes = data_nasc.split('/')
    if len(partes) == 3 and all(p.isdigit() for p in partes):
        break
    print("Data inválida! Use o formato DD/MM/AAAA.")

while True:
    senha = getpass.getpass("Digite sua senha (não será mostrada): ")
    if len(senha) >= 6:
        break
    print("Senha fragil e curta! Mínimo 6 caracteres.")

print("\n" + "="*50)
print("CADASTRO FEITO COM SUCESSO!")
print("="*50)

print("\nFaça seu login agora:")

tentativas = 3
while tentativas > 0:
    email_login = input("Email: ").strip()
    senha_login = getpass.getpass("Senha: ")
    
    if email_login == email and senha_login == senha:
        print("\n Logado com sucesso!")
        print(f"Bem-vindo, {nome_perfil}!")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f" Credenciais inválidas. {tentativas} tentativa(s) restante(s).")
        else:
            print(" Acesso bloqueado. Entre em contato com o suporte.")
