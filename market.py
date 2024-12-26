from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///market.db"  # SQLite database URI
db = SQLAlchemy(app)

# Define the Item model
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'

# Define routes
@app.route('/')
def home_page():
    return render_template('home_1.html')

@app.route('/about/<username>')
def about_page(username):
    return f'<h1> This is the about page of {username}</h1>'

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

# Main entry point
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
