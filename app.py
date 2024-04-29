import random

def main():
    print('--- Bem-vindo ao Jogo de Jokenpo ---')
    input('Pressione Enter para iniciar o jogo...')
    nome_jogador = input('Digite seu nome: ')

    jogar_novamente = True

    while jogar_novamente:
        jogar_jogo(nome_jogador)

        resposta = input(f'Deseja jogar novamente? {nome_jogador} (s/n): ').lower()
        jogar_novamente = resposta == 's'

    print('Obrigado por jogar!')

def jogar_jogo(nome_jogador):
    opcoes = ['pedra', 'papel', 'tesoura']
    escolha_computador = random.choice(opcoes)

    escolha_jogador = input('Escolha: pedra, papel ou tesoura: ').lower()

    if escolha_jogador not in opcoes:
        print('Escolha inválida. Tente novamente.')
        return

    print('-'*20)
    print(f'{nome_jogador} escolheu: {escolha_jogador}')
    print(f'O computador escolheu: {escolha_computador}')

    if escolha_jogador == escolha_computador:
        print('Empate!')
    elif (escolha_jogador == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_jogador == 'papel' and escolha_computador == 'pedra') or \
         (escolha_jogador == 'tesoura' and escolha_computador == 'papel'):
        print(f'{nome_jogador} ganhou!')
    else:
        print(f'{nome_jogador} perdeu!')
    print('-'*20)

if __name__ == '__main__':
    main()
