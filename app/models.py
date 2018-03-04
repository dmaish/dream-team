from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


from app import db, login_manager


class Employee(UserMixin, db.Model):
    """ Create an Employee table """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)



    @property
    def password(self):
        """prevent password from being accessed this is achieved
        by not including a return statement to this method """
        raise AttributeError('password is not a readable attribute')

    # the password argument to this method comes from the
    #  employee object in the auth views in the register route
    @password.setter
    def password(self, password):
        """set password to a hashed password"""
        self.password_hash = generate_password_hash(password)

    def verify_password(self, form_password):
        """ check if hashed password matches actual password"""
        return check_password_hash(self.password_hash, form_password)

    def __repr__(self):
        return '<Employee: {} >'.format(self.username)


# setting up the user_loader
# this is a user_loader callback, which Flask-Login uses to reload the user
# object from the user ID stored in the session
@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))


class Department(db.Model):
    """ create a Department table """
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='department', lazy='dynamic')

    def __repr__(self):
        return '<Department: {} >'.format(self.name)


class Role(db.Model):
    """ Creating a Role table"""
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role: {} >'.format(self.name)














