#3
pontosJogador = 0
pontosComputador = 0

while True:
  import random

  finalizar = "F"
  corSecreta = random.choice(['R', 'G', 'B'])
  palpite  = input("Adivinhe a cor (R, G ou B): ").upper()

  if palpite not in ['R', 'G', 'B']:

    if palpite == finalizar:
      print("Jogo finalizado!")

      if pontosJogador > pontosComputador:
        print("Você ganhou!!")

      else:
        print("Você perdeu!!")

      break

    else:
      print("Entrada inválida. Escolha  R, G ou B.")

  elif palpite == corSecreta:
    print("Parabén!! Você acertou!")
    pontosJogador = pontosJogador + 1

  else:
    print("Você ERROU!!!")
    print(f"A cor era {corSecreta}")
    print(35*"*")
    pontosComputador = pontosComputador + 1

  print(f"Você {pontosJogador} x PC {pontosComputador}")
