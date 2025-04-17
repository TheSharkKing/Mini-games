from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main game page"""
    return render_template('index.html')

@app.route('/game')
def game():
    """Route for game state handling"""
    return {'status': 'running'}

@app.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)