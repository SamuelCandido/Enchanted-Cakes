# Crie uma rota do meu site esta sera minha home
import config.config from *

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
