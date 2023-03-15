import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_de_tentativas = 0

while True:

    letra_digitade = input('Digite uma letra:')
    numero_de_tentativas+= 1

    if len(letra_digitade) > 1:
        print('Digite apenas uma letra')
        continue
    
    if letra_digitade in  palavra_secreta:
        letras_acertadas += letra_digitade

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('Voce Ganhou!!!!')
        print('A palava secreta era: ', palavra_secreta)
        print('Tentativa: ', numero_de_tentativas)
        letras_acertadas = ''
        numero_de_tentativas = 0