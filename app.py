from flask import Flask, render_template, request
import pandas as pd

def create_app():
    app = Flask(__name__)
    
    # puxando a planilha
    planilha = pd.read_excel('dados.xlsx')
    
    @app.route('/')
    def index():
        return render_template('index.html', resultado="")
    
    @app.route('/pesquisar', methods=['POST'])
    def pesquisar():
        uc_pesquisa = request.form.get('uc_pesquisa')
        
        # Verificação se o número foi fornecido na pesquisa
        if not uc_pesquisa:
            return render_template('index.html', resultado="Digite uma UC para pesquisar.")
        
        #pesquisa na planilha
        resultado = ""
        for _, row in planilha.iterrows():
            if str(row['UC']) == uc_pesquisa:
                coordenadas = row['Coordenadas']
                resultado = coordenadas
                break
        
        if not resultado:
            resultado = "Nenhum resultado encontrado, contate seu Monitor CGB"
        
        return render_template('index.html', resultado=resultado)
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
