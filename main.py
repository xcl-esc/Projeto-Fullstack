
class Trabalhador:
    def __init__(self, salario_bruto=0, meses_trabalhados=0, meses_trabalhados_decimo=0):
        self.salario_bruto = salario_bruto
        self.meses_trabalhados = meses_trabalhados
        self.meses_trabalhados_decimo = meses_trabalhados_decimo

    def tempo_trab(self, meses_trabalhados):
        """Calcula o tempo de trabalho em meses."""
        if not isinstance(meses_trabalhados, int) or meses_trabalhados < 0:
            return "Número de meses inválido. Deve ser maior que 0 (zero)."
        
        return meses_trabalhados

    def decimo_terceiro(self):
        """Retorna o valor do décimo terceiro salário."""
        if 1 <= self.meses_trabalhados_decimo <=12:
            decimo_total = (self.salario_bruto / 12) * self.meses_trabalhados_decimo
            return  decimo_total
        
        else:
            return "Número de meses inválido."
        
    def desconto_inss(self):
        """Calcula o desconto do INSS."""
        if self.salario_bruto <= 1518.00:
            return self.salario_bruto * 7.5 / 100
        elif 1518.01 <= self.salario_bruto <= 2793.88:
            return self.salario_bruto * 9 / 100 - 22.77
        elif 2793.89 <= self.salario_bruto <= 4190.83:
            return self.salario_bruto * 12 / 100 - 106.59
        elif 4190.84 <= self.salario_bruto <= 8157.41:
            return self.salario_bruto * 14 / 100 - 190.40
        return "Salario inválido."
    
    def contribuinte_avulso(self, tipo_contribuicao, salario):
        "Calcula o valor que deve ser pago na GPS"
        
        if tipo_contribuicao == 1: #Empregado, doméstico, trabalhador avulso

            if salario <= 1518:
                return salario * 7.5 / 100           
            elif 1518.01 <= salario <= 2793.88:
                return salario * 9 / 100
            elif 2793.89 <= salario <= 4190.83:
                return salario * 12 / 100
            elif 4190.84 <= salario <= 8157.41:
                return salario * 14 / 100
            else:
                return "Salário fora da faixa válida."
            
        elif tipo_contribuicao == 2: #Individual e facultativa
            if salario <= 1518:
                return {
                    "alíquota_5%": salario * 5 / 100,
                    "alíquota_11%": salario * 11 / 100,
                    "alíquota_12%": salario * 12 / 100
                }
                
            elif salario >= 1518.01:
                return round(salario * 20 / 100, 2)   
            else:
                return "Salário inválido"
            
        return "Tipo de contribuição inválido."
    
    def calcular_abono_salarial(self, meses_trabalhados):
        """Calcula o valor do abono salarial."""
        if not isinstance(meses_trabalhados, int) or meses_trabalhados < 0 or meses_trabalhados > 12:
            return "Número de meses inválido. Deve estar entre 0 e 12."
        
        return round(126.5 * meses_trabalhados, 2)
    
    def calcular_rescisao(self, meses_trabalhados):
        '''Essa função é responsável por calcular o valor total de uma rescisao incluindo férias atrasadas, FGTS, multa do FGTS e aviso prévio'''
        if not isinstance(meses_trabalhados, int) or meses_trabalhados <=0 or meses_trabalhados > 12:
            raise ValueError("Número de meses inválido. Deve ser maior do que 0 (zero).")
        
        return round((meses_trabalhados * (self.salario_bruto / 30)), 2)
    
    def aviso_previo(self, dias_trabalhados):
    
        if not isinstance(dias_trabalhados, int) or dias_trabalhados < 0 or dias_trabalhados > 30:
                    return "Número de meses inválido. Deve ser maior do que 0 (zero)."
                
        return round((dias_trabalhados * (self.salario_bruto / 30)), 2)
    
    def ferias(self, ferias):
        if not isinstance(ferias, int) or ferias < 0:
            return "Valor inválido. Deve ser maior ou igual a 0 (zero)."
        
        elif ferias == 0:
            return 0
            
        return round((ferias * (self.salario_bruto + (self.salario_bruto / 3))), 2)
        
    def fgts(self, meses_trabalhados):
        if not isinstance(meses_trabalhados, int) or meses_trabalhados < 0:
            return "Valor inválido. Deve ser maior que 0 (zero)."
        
        fgts_total = self.salario_bruto * 0.08 * meses_trabalhados
        multa_fgts = fgts_total * 0.4
        return round(fgts_total + multa_fgts, 2)

    def aviso_previo_maior(self, meses_trabalhados):
        if not isinstance(meses_trabalhados, int) or meses_trabalhados < 0:
            return "Valor inválido. Deve ser maior que 0 (zero)."
        if meses_trabalhados < 13:
            return round(self.salario_bruto, 2)
        
        return round((self.salario_bruto / 30) * ((self.meses_trabalhados / 12 * 3) + 30), 2)