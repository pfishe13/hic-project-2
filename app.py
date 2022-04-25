from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
# home page
def index():
    return render_template('index.html')

# buy page
@app.route('/buy')
def render_buy():
    return render_template('buy.html')

# sell page
@app.route('/sell')
def render_sell():
    return render_template('sell.html')

# portfolio page
@app.route('/portfolio')
def render_portfolio():
    return render_template('portfolio.html')

# Upcoming Release page
@app.route('/upcoming')
def render_upcoming():
    return render_template('upcoming.html')

# account page
@app.route('/account')
def render_account():
    return render_template('account.html')

# about page
@app.route('/about')
def render_about():
    return render_template('about.html')

# shoe page
@app.route('/shoe')
def render_shoe():
    return render_template('shoe.html')

# shoe2 page
@app.route('/shoe2')
def render_shoe2():
    return render_template('shoe2.html')

# shoe3 page
@app.route('/shoe3')
def render_shoe3():
    return render_template('shoe3.html')

# shoe4 page
@app.route('/shoe4')
def render_shoe4():
    return render_template('shoe4.html')

if __name__ == "__main__":
    app.run(debug=True)