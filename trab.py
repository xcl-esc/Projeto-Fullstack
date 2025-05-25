import time
class Trabalhador:

    '''Ajudar o trabalhador a descobrir informações à respeito do décimo terceiro salário, inss'''    

    def __init__(self):
    
        self.salario_bruto = self.obter_salario()
    
    def obter_salario(self):
        '''Esta função pede o valor do salário do usuário'''
        
        while True:
            try:
                salario = float(input('Digite o valor bruto do seu salário sem descontos:\n'))
                if salario > 0:
                    return salario
                else:
                    print("Por favor, digite um valor válido maior que zero e use ponto ao invés de vírgula.")
            except ValueError:
                print("Entrada inválida")
    
    def menu_opcoes(self):
        '''Esta função mostra o menu em looping'''

        while True:
            try:
                
                escolha_menu =int(input('Olá, seja bem vindo ao menu do trabalhador!\n'
                'Digite a opção que desejar:\n'
                '1 - Décimo Terceiro\n'
                '2 - Desconto INSS\n'
                '3 - Aposentadoria de Contribuinte Avulso\n'
                '4 - Rescisão\n'
                '5 - Abono Salarial\n' 
                '6 - Sair\n'))

                if escolha_menu == 1:
                    self.decimo_terceiro()
                elif escolha_menu == 2:
                    self.desconto_inss()
                elif escolha_menu == 3:
                    self.contribuinte_avulso()
                elif escolha_menu == 4:
                    self.rescisao()
                elif escolha_menu == 5:
                    self.abono_salarial()
            
                elif escolha_menu == 6:
                    print('Saindo do programa...')
                    time.sleep(1)
                    print("Encerrando Programa...")
                    time.sleep(2)
                    print("Programa encerrado!")
                    time.sleep(1) 
                    break
                else:
                    print('Digite uma opção válida!')
                
            except ValueError:
                print("Digite um valor válido!")

    
    def decimo_terceiro(self):
        '''De acordo com a base de meses trabalhados e o salário devolve o valor a receber do décimo terceiro salário'''
        try:
            meses_trab = int(input('Digite a quantidade de meses trabalhados no ano:\n'))
            if 1 <= meses_trab <= 12:
                decimo_total = (self.salario_bruto / 12) * meses_trab
                print(f'Este é o valor que você deve receber do seu Décimo terceiro: {decimo_total:.2f}')
                print("Retornando ao menu principal...")
                time.sleep(3)
            
            else:
                print('Você deve digitar um valor entre 1 e 12 para a quantidade de meses trabalhados.')
        except ValueError:
            print("Erro: Digite um número válido para os meses trabalhados.")

    def desconto_inss(self):
        '''A função calcula o desconto do INSS que deve ser feito de acordo com o salário'''

        if self.salario_bruto <= 1518.00:
            print(f"O valor do desconto é: {self.salario_bruto * 7.5 / 100:.2f}.\nReferente à alíquota de 7,5%.")
        
        elif 1518.01 <= self.salario_bruto <= 2793.88:
            print(f"O valor do desconto é: {self.salario_bruto * 9 / 100 - 22.77:.2f}.\nReferente à alíquota de 9%.")

        elif 2793.89 <= self.salario_bruto <= 4190.83:
            print(f"O valor do desconto é: {self.salario_bruto * 12 / 100 - 106.59:.2f}.\nReferente à alíquota de 12%.")

        elif 4190.84 <= self.salario_bruto <= 8157.41:
            print(f"O valor do desconto é: {self.salario_bruto * 14 / 100 - 190.40:.2f}.\nReferente à alíquota de 14%.")

        print("Retornando ao menu principal...")
        time.sleep(3)
    
    def contribuinte_avulso(self):
        '''Ao informar a tipo de contribuinte, a função calcula o valor que deve ser pago na GPS'''
        
        print('Escolha o tipo de contribuição de INSS para empregado(a), doméstica(a) e trabalhador(a) avulso(a) ou contribuição individual e facultativa?\n')
        escolha_cont = int(input('1 - caso seja empregado(a), empregado(a) doméstica(a) e trabalhador(a) avulso(a)\n' 
                                 '2 - contribuição individual e facultativa\n'
                                 '3 - SAIR.\n'
                                 'Opção: '
                                 ))
        
        if escolha_cont == 1:
            cont_avulso = float(input('Digite o valor do salário que você usa como referência para pagamento da sua GPS:\n'))
            if cont_avulso <= 1518:
                print(f'O valor que deve ser pago é de: {cont_avulso * 7.5 / 100:.2f}')
            
            elif 1518.01 <= cont_avulso <= 2793.88:
                print(f'O valor que deve ser pago é de: {cont_avulso * 9 / 100:.2f}')

            elif 2793.89 <= cont_avulso <= 4190.83:
                print(f'O valor que deve ser pago é de: {cont_avulso * 12 / 100:.2f}')

            elif 4190.84 <= cont_avulso <= 8157.41:
                print(f'O valor que deve ser pago é de: {cont_avulso * 14 / 100:.2f}')
            else:
                print('O valor que digitou não é válido!')
            
        
        if escolha_cont == 2:
            cont_fac = float(input('Digite o valor do salário que você usa como referência para pagamento da sua GPS:\n'))
            if cont_fac <= 1518:
                print(f'Para alíquota de 5%: R${cont_fac * 5 / 100:.2f}\n')
                print(f'Para alíquota de 11%: R${cont_fac * 11 / 100:.2f}\n')
                print(f'Para alíquota de 12%: R${cont_fac * 12 / 100:.2f}\n')
                
            elif cont_fac >= 1518.01:
                print(f'Salário entre 1518,01 - 8157,41 a alíquota é de 20%. Que corresponde à R${cont_fac * 20 / 100:.2f}')   

            else:
                print(f'Salário entre 1518,01 - 8157,41 a alíquota é de 20%. Que corresponde à R${cont_avulso * 20 / 100:.2f}')
        if escolha_cont == 3:
            print('Saindo do programa!')

        print("Retornando ao menu principal...")
        time.sleep(3)

    def rescisao(self):
        '''Essa função é responsável por calcular o valor total de uma rescisao incluindo férias atrasadas, FGTS, multa do FGTS e aviso prévio'''
        
        dias_trabalhados = int(input('Digite quantos foram os dias trabalhados do mês: \n'))
        salario_rescisao = (self.salario_bruto / 30) * dias_trabalhados
        print(f'O saldo do salario é: {salario_rescisao:.2f}\n'
                'Agora vamos calcular o valor das férias.\n')
        
        escolha_ferias = int(input('Você possui menos de 12 meses de trabalho?\n'
                                    '1 - para SIM\n'
                                    '2 - para NÃO\n'))
        total_ferias_prop = 0
        valor_ferias = 0

        if escolha_ferias == 1:
            ferias_prop = int(input('Digite qual o total de meses de trabalho que você possui:\n'))
            total_ferias_prop = (self.salario_bruto / 12) * ferias_prop
            total_ferias_prop += total_ferias_prop / 3
            print(f'O valor á receber de férias proporcionais + 1/3(um terço) é de: R${total_ferias_prop:.2f}')

        if escolha_ferias == 2:
            ferias_vencidas = int(input('Digite quantas férias vencidas possui: '
                                        '\n(caso não possua férias vencidas, digite 0.)\n'))
            valor_ferias = (ferias_vencidas * self.salario_bruto)
            valor_ferias += valor_ferias / 3
            print(f'O valor à receber de férias é de: R${valor_ferias:.2f}')

        tempo_fgts = int(input('Digite o seu total de meses de trabalho na empresa:\n'))
        multa_fgts = 0
        valor_total_fgts = (self.salario_bruto * 0.08) * tempo_fgts
        multa_fgts = valor_total_fgts * 0.4
        print(f'O valor total de FGTS acumulado: R${valor_total_fgts:.2f}')
        print(f'O valor da sua multa rescisória é: R${multa_fgts:.2f}')

        aviso_previo = int(input('Você possui mais de um ano de empresa?'
                                    '1 - para SIM\n'
                                    '2 - para NÃO\n'))

        aviso_total = 0
        
        if aviso_previo == 1:
            tempo_empresa = int(input('Quantos anos completos de empresa você possui :\n'))
            tempo_aviso = (tempo_empresa * 3) + 30
            aviso_total = (self.salario_bruto / 30) * tempo_aviso
            print(f'O valor do seu aviso prévio é de: R${aviso_total:.2f}\n')
        elif aviso_previo == 2:
            aviso_total = self.salario_bruto
            print(f'Seu aviso prévio é de: R${self.salario_bruto:.2f}\n')

        total_rescisao = salario_rescisao + total_ferias_prop + multa_fgts + aviso_total   
        print(f'O valor total da sua rescisão é: R${total_rescisao}\n')

        print("Retornando ao menu principal...")
        time.sleep(3)
    
    def abono_salarial(self):
        '''Essa função serve para informar quanto de abono salarial o trabalhador deve receber, se for apto a recebé-lo.'''

        print('Para saber se é elegível a receber o abono salarial, consulte o aplicativo Carteira de Trabalho\n')
        tempo_trab = int(input('Quantos meses você trabalhou?\n'))
        print(f'Você receberá R${126.5 * tempo_trab:.2f}\n')

        print("Retornando ao menu principal...")
        time.sleep(3)


trab = Trabalhador()

trab.menu_opcoes()