senha_correta = "2002"  

while True:
  senha_digitada = input("Digite a senha: ")

  if senha_digitada == senha_correta:
    print("Acesso concedido.")
    break  
  else:
    print("Senha incorreta. Tente novamente.")