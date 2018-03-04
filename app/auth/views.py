from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from forms import LoginForm, RegistrationForm
from .. import db
from ..models import Employee


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """handle requests to the /register route
    Add an employee to the database through the registration form"""

    # the registrationForm object
    form = RegistrationForm()
    if form.validate_on_submit():
        # there must be a constructor taking this variables that have been declared
        employee = Employee(email=form.email.data,
                            username=form.username.data,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            password=form.password.data,
                            )

        # add employee to the database
        db.session.add(employee)
        db.session.commit()
        flash('you have successfully registered!, you may now login..')

        # redirecting user to the login page
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form, title='Register')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """handles requests to the /login route-logs an employee through the login form"""

    # the loginForm object
    form = LoginForm()
    if form.validate_on_submit():
        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
        employee = Employee.query.filter_by(email=form.email.data).first()
        if employee is not None and employee.verify_password(form.password.data):

            # log employee in
            login_user(employee)

            # redirect to admin_dashboard if the user is the admin

            if employee.is_admin:
                return redirect(url_for('home.admin_dashboard'))
            else:
                # redirect to the dashboard page after login if not admin
                return redirect(url_for('home.dashboard'))

        else:
            flash(' Invalid email or password. ')

    return render_template('auth/login.html', form=form, title='Login')


@auth.route('/logout')
@login_required
def logout():
    """ handles requests to the /logout route
    Logs out an employee out through the logout link"""

    logout_user()
    flash(' You have successfully been logged out.')

    # redirects to the login page
    return redirect(url_for('auth.login'))

























