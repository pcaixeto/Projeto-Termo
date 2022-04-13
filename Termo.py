'''
Pedro Machado Gomes Caixeta
TIA: 42105811

Fernanda Aiko Hamatsu
TIA: 42133025

'''
from random import choice
def read_file(v):                                                            # essa funcao vai pegar as palavras do arquivo e colocar elas num vetor
    with open('palavras.txt') as f:                                          # abre e fecha o arquivo quando o programa acabar
        for i in range(len(v)):
            v[i] = f.readline().rstrip()

    return v

def add_scores(palavra_certa, count):                                        # escreve no arquivo 'scores.txt' as pontuações
    nome = input('Digite o seu nome: ').title()                                 
    with open('scores.txt', 'a') as f: 
        f.write(f'{nome}; {palavra_certa}; {count}\n')

        # apresentação pro usuário
        print(f'\nNome: {nome}\n')
        print(f'Palavra certa: {palavra_certa}\n')
        print(f'Número de tentativas: {count}\n')

def conv_texto(v):                                                           # converte o vetor em string
    resp = ""
    for z in range(len(v)):
        resp += v[z]

    return resp

def ver_letras(certo):                                                       # função para verificar se as entradas do usuário
    word = [0] * 5
    tent = 0
    with open('palavras.txt') as f:                                          # abre e fecha o arquivo quando o programa acabar
        while tent <= 6:                                        
            print(f'\n{tent+1}o tentativa')    
            while True:                                                      # filtra a entrada do usário caso input seja inválido (tamanho inválido)
                entrada = input("Digite uma palavra de 5 letras: ").lower()
                if len(entrada) == 5 and entrada.isalpha():                  # isalpha() é um método que retorna True caso todos os caracteres sejam alfabéticos e False caso contrário
                    break
                
                # Os ifs abaixo devolverão o erro de acordo com a origem dele
                if entrada.isalpha() == False:                               
                    print("Entrada inválida, por favor digite uma palavra de 5 letras com caracteres alfabéticos")
                            
                elif len(entrada) != 5:                                        
                    print("Tamanho errado, por favor digite uma palavra de 5 letras") 
                
            for j in range(len(entrada)):                                    # verifica letra por letra
                aux = 0
                if entrada[j] == certo[j]:                                   # se a letra está na posição correta
                    word[j] = "^"

                else:
                    for k in range(len(certo)):    
                        if entrada[j] == certo[k] and j != k:                # se a letra está contida na palavra mas na posição incorreta
                           word[j] = "!"

                    for l in range(5):
                        if entrada[j] != certo[l]:                           # se a letra não pertence a palavra
                            aux += 1
                            
                    if aux == 5:
                        word[j] = "x"

            if word == ["^", "^", "^", "^", "^"]:                            # se a palavra está correta
                print("\nResposta correta, parabéns!\n")
                print('A palavra era: ')
                print(f'|{conv_texto(certo)}|')
                add_scores(certo, tent+1)
                break

            elif word != ["^", "^", "^", "^", "^"]:                          # se a palavra está incorreta mas ainda há tentativas
                tent += 1
                print(f'|{conv_texto(word)}|')

            if tent == 6:                                                    # se não há mais tentativas
                print(f'\nSuas tentativas acabaram, mais sorte da próxima vez!\n')
                print(f'Palavra correta: {certo}')
                break

def tutorial():                                                              # tutorial do jogo
    print("\nDescubra a palavra certa em até 6 tentativas. Depois de cada tentativa, o jogo retorna o quão próximo você está da palavra seguindo a legenda:")
    print("^: a letra da posição correspondente pertence a palavra e está na posição correta.")
    print("!: a letra da posição correspondente pertence a palavra mas se encontra na posição incorreta.")
    print("x: não pertence a palavra.")
    print("Exemplo: \n")
    print("+-----------+\n")
    print("| T U R M A | \n| ^ x x x ! |")
    print("\n+-----------+\n")
    print("-T faz parte da palavra e está na posição correta.")
    print("-A faz parte da palavra mas não está na posição correta.")
    print("-U, R e M não fazem parte da palavra.\n")

    print('Quer ver o tutorial de novo? (digite o numero)')
    print('1. sim')
    print('2. não')

    while True:
        opcao = input()
        if opcao == '1':
            return tutorial()

        if opcao == '2':
            break

        print('Por favor, digite o numero da opção')

def main():
    vetor_palavras = [0] * 15
    palavra_certa = choice(read_file(vetor_palavras))                        # vai pegar, do vetor retornado das palavras do arquivo, uma palavra aleatoria
    
    print('Bem vindo ao Descubra a Palavra!\nNesse jogo, todas as palavras serão nomes de animais.\n')
    print('Deseja ver o tutorial? (digite o numero)')
    print('1. sim')
    print('2. não')

    while True:
        opcao_tut = input()
        if opcao_tut == '1':
            tutorial()
            break

        if opcao_tut == '2':
            break
        print('Por favor, digite o número da opção')
    
    print('\nEntão vamos começar...')                  
    while True:                                                              # da a opção do usuário jogar mais de uma vez ou fechar o jogo
        ver_letras(palavra_certa)

        print('\nDeseja jogar novamente? (digite o número)')
        print('1. sim')
        print('2. não')

        while True:
            jogar_novamente = input()
            if jogar_novamente == '1':
                break

            if jogar_novamente == '2':
                break

            print('Por favor, digite o número da opção')

        if jogar_novamente == '2':
            print('\nFechando o jogo...')
            break

main()