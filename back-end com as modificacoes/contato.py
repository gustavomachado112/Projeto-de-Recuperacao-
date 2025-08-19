print("Bem-vindo ao sistema de contato(mensagem)!")
while True:
 nome = input("Digite seu nome porfavor: ").strip()
 if nome:
  if len(nome) <= 100:  
   break
  else:
   print(" Nome muito longo , quem teve ideia de te dar esse nome! Maximo 200 caracteres.")
 else:
  print(" Nome nao pode estar vazio, lembra-se!")

while True:
 email = input("Digite seu email: ").strip()
 if "@" in email and "." in email.split("@")[1]:
  if len(email) <= 150:  
   break
  else:
   print(" Email muito longo! Maximo 200 caracteres.")
 else:
  print(" Email invalido! Ex de como usar: alura@gmail.com")

while True:
 mensagem = input("Digite sua mensagem : ").strip()
 if mensagem:
  if len(mensagem) >= 1:
   if len(mensagem) <= 200:  
    break
   else:
    print(" Mensagem muito longa! Maximo 400 caracteres.")
  else:
   print(" Mensagem deve ter no minimo 1 caracter!")
 else:
  print(" Mensagem não pode estar vazia,amigo!")

print(f"\n--- Confirmação ---")
print(f"Nome: {nome}")
print(f"Email: {email}")
print(f"Mensagem: {mensagem[:100]}{'...' if len(mensagem) > 100 else ''}")

confirmar = input("\n Confirmar envio? (s/n): ").lower()
if confirmar == 's':
 print("\n Enviando mensagem...")
 print(" Mensagem enviada com sucesso,ebaaaa!")
 print(" Entraremos em contato em ate 24h , as vezes podemos atrasar!")
else:
 print(" Envio cancelado.")
