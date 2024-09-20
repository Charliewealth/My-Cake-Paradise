from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/trying')
def trying():
    return render_template('trying.html')

@app.route('/submit_order', methods=['POST'])
def submit_order():
    cake_type = request.form['cakeType']
    size = request.form['size']
    crust = request.form['crust']
    toppings = request.form['toppings']
    total = request.form['total']
    # Process the order here (e.g., save to database, send email)
    return f"Order received! Type: {cake_type}, Size: {size}, Crust: {crust}, Toppings: {toppings}, Total: {total}"

if __name__ == '__main__':
    app.run(debug=True)

