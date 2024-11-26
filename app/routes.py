from flask import Blueprint, render_template, redirect, url_for
from .forms import ContactForm

# Create a Blueprint for the main routes
main = Blueprint('main', __name__)

# Home Page Route
@main.route('/')
def home():
    return render_template('index.html', title="Home - Mihret Film Production")

# Portfolio Page Route
@main.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title="Portfolio - Mihret Film Production")

# About Us Page Route
@main.route('/about')
def about():
    return render_template('about.html', title="About Us - Mihret Film Production")

# Contact Page Route
@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Process the form data here, e.g., send an email, store in the database, etc.
        return redirect(url_for('main.thank_you'))  # Redirect after successful submission
    return render_template('contact.html', title="Contact - Mihret Film Production", form=form)

# Thank You Page Route (Redirect after form submission)
@main.route('/thank_you')
def thank_you():
    return render_template('thank_you.html', title="Thank You - Mihret Film Production")
