from termcolor import colored
from time import sleep


def imc():
    flag = True
    while True:
        # Função para sair
        def close():
            print('\n')
            print('-=' * 20, '\b<*>')
            if input('Precione qualquer tecla para continuar ou (Q),'
                     ' para sair: ').lower() == 'q':
                print('\nAté a proxima...\n')
                exit(0)
        # Try para garantir que o usuario sempre digite um float
        try:
            # Entrada de dados
            na_me_pac = input('\nDigite o nome do paciente: ').title()
            tel_pac = input('Digite o telefone do paciente com o (DDD): ')
            peso_pac = float(input('Digite o peso do paciente: '))
            alt_pac = float(input('Digite a altura do paciente: '))

            # Imprimindo o resultado na tela, usando termcolor,
            # seguido de um close( para sair da função
            res_imc = peso_pac / (alt_pac * alt_pac)
            print('-=' * 20, '\b<*>')
            print('\nNORMALIDADE (IMC ENTRE 18,5 e 25)')
            print(f'\nIMC do paciente {na_me_pac} é:',
                  colored(f'{res_imc:.1f}', 'yellow', attrs=['bold']))

            # O codigo a seguir faz a analize de dados
            if res_imc <= 18.4:
                print(f'O paciente {na_me_pac} está com',
                      colored('MAGREZA', 'red', attrs=['bold']))
                print(f'Entre em contato com o paciente para agendar '
                      f'uma consulta, '
                      f'telefone:',
                      colored(f'{tel_pac}', 'green', attrs=['bold']))
                close()
            if 18.5 <= res_imc <= 25:
                print(f'O paciente {na_me_pac} está com o peso',
                      colored('NORMAL', 'blue', attrs=['bold']))
                close()
            if 25.1 <= res_imc <= 29.1:
                print(f'O paciente {na_me_pac} está com',
                      colored('SOBREPESO', 'red', attrs=['bold']))
                print(f'Entre em contato com o paciente para agendar '
                      f'uma consulta, '
                      f'telefone:',
                      colored(f'{tel_pac}', 'green', attrs=['bold']))
                close()
            if res_imc >= 30:
                print(f'O paciente {na_me_pac} está com',
                      colored('OBESIDADE', 'red', attrs=['bold']))
                print(f'Entre em contato com o paciente para agendar '
                      f'uma consulta, '
                      f'telefone:',
                      colored(f'{tel_pac}', 'green', attrs=['bold']))
                close()
        except TypeError and ValueError:
            print('\nValores incorretos para peso e/ou altura, '
                  'tente novamente em',
                  colored('=> ', 'red', attrs=['bold']), end='')
            for i in reversed(range(3)):
                sleep(1)
                print(colored(f'{i + 1}', 'cyan', attrs=['bold']), end='...')
            close()


imc()
