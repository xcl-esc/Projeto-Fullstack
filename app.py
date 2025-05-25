from main import Trabalhador
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# ROTA PARA A PÁGINA INICIAL
@app.route('/')
def index():
    return render_template('index.html')

#ROTA PARA CÁLCULO DO DÉCIMO TERCEIRO
@app.route('/calcular_decimo_terceiro', methods=['POST'])
def calcular_decimo_terceiro():
    data = request.json
    salario_bruto = data.get('salario_bruto')
    meses_trabalhados_decimo = data.get('meses_trabalhados_decimo')

    trabalhador = Trabalhador(salario_bruto=salario_bruto, meses_trabalhados_decimo=meses_trabalhados_decimo)
    resultado = trabalhador.decimo_terceiro()

    return jsonify({"decimo_terceiro": resultado})

#ROTA PARA CÁLCULO DE CONTRIBUIÇÃO PARA EMPREGADOS OU CONTRIBUIIÇÃO AVULSA/INDIVIDUAL
@app.route('/contribuinte_avulso', methods=['POST'])
def calcular_contribuinte_avulso():
    data = request.json
    tipo_contribuição = int(data.get('tipo_contribuicao'))
    salario = data.get('salario_bruto')

    trabalhador = Trabalhador(salario_bruto=salario)
    resultado = trabalhador.contribuinte_avulso(tipo_contribuição, salario)

    return jsonify({"resultado": resultado})

#ROTA PARA O CÁLCULO DO ABONO SALARIAL
@app.route('/abono_salarial', methods=['POST'])
def calcular_abono_salarial():
    """Calcula o valor do abono salarial com base nos meses trabalhados."""
    data = request.json
    meses_trabalhados = data.get('meses_trabalhados')

    trabalhador = Trabalhador(0)
    resultado = trabalhador.calcular_abono_salarial(meses_trabalhados)

    if isinstance(resultado, str):
        return jsonify({"erro": resultado}), 400

    return jsonify({"abono_salarial": resultado})

#ROTA PARA CALCULO DE RESCISAO BASEANDO FATORES COMO FÉRIAS ATRASADAS, FGTS E AVISO PRÉVIO
@app.route('/rescisao', methods=['POST'])
def calcular_rescisao():
    data = request.json
    salario_bruto = float(data.get('salario_bruto'))
    meses_trabalhados = int(data.get('meses_trabalhados'))
    ferias_vencidas = data.get('ferias_vencidas', 0)
    try:
        ferias_vencidas = int(ferias_vencidas)
    except ValueError:
        return jsonify({"erro": "Férias vencidas deve ser um número inteiro."}), 400

    if salario_bruto is None or meses_trabalhados is None:
        return jsonify({"erro": "Dados insuficientes."}), 400
                        
    trabalhador = Trabalhador(salario_bruto, meses_trabalhados=meses_trabalhados, meses_trabalhados_decimo=0)

    try:
        saldo_salario = trabalhador.calcular_rescisao(meses_trabalhados)
        ferias = trabalhador.ferias(ferias_vencidas)
        aviso_previo = trabalhador.aviso_previo_maior(meses_trabalhados)
        fgts_total = trabalhador.fgts(meses_trabalhados)

        total = saldo_salario + ferias + aviso_previo + fgts_total

        return jsonify({
            "rescisao": round(total, 2),
            "detalhes": {
                "saldo_salario": round(saldo_salario, 2),
                "ferias_vencidas": round(ferias, 2),
                "aviso_previo": round(aviso_previo, 2),
                "fgts_com_multa": round(fgts_total, 2)
            }
            })
    except Exception as e:
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
