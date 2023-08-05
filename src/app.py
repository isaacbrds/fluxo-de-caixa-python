from flask import Flask, render_template, request

# Cria a instância do aplicativo Flask
app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Execução do aplicativo
if __name__ == '__main__':
    app.run(debug=True)
