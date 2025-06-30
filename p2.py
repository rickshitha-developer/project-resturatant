from flask import Flask, render_template, request

app = Flask(__name__)

# Route for Home Page
@app.route('/')
def home():
    return render_template('p2home.html')

# Route for About Page
@app.route('/p2about.html')
def about():
    return render_template('p2about.html')

# Route for Menu Page
@app.route('/p2menu.html')
def menu():
    return render_template('p2menu.html')
@app.route('/p2animate.html')
def animate():
    return render_template('p2animate.html')

# Route for Booking a Table
@app.route('/p2booking.html', methods=['GET', 'POST'])
def book_table():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        date = request.form['date']
        time = request.form['time']
        guests = request.form['guests']
        
        # Show the submitted data on thank-you page
        return render_template('p2submit.html', name=name, date=date, time=time, guests=guests)
    return render_template('p2booking.html')

# Route for Order Page
@app.route('/p2order.html', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        customer_name = request.form['name']
        food_item = request.form['dish']
        quantity = request.form['quantity']
        
        # Display order confirmation with order details
        return render_template('p2orderthank.html', name=customer_name, food_item=food_item, quantity=quantity)
    return render_template('p2order.html')

# Route for Reviews Page
@app.route('/p2reviews.html')
def reviews():
    return render_template('p2reviews.html')

# Route for Gallery Page
@app.route('/p2gallery.html')
def gallery():
    return render_template('p2gallery.html')

# Route for Contact Us Page
@app.route('/p2contact.html', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        
        # Thank You page after contact form submission
        return render_template('p2thankyou.html', name=name, message=message)
    return render_template('p2contact.html')

# Route for FAQ Page
@app.route('/p2faq.html')
def faq():
    return render_template('p2faq.html')

if __name__ == '__main__':
    app.run(debug=True)