from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# the following imports are only used in the employee forms only
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from  ..models import Department, Role


# the departments' form class
class DepartmentForm(FlaskForm):
    """ Form for the admin to add or edit a department """

    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


# the roles' form class
class RoleForm(FlaskForm):
    """ form for admin to add or edit a role"""

    name = StringField('name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    submit = SubmitField('submit')


class EmployeeAssignForm(FlaskForm):
    """ form for admin to assign departments and roles to employees """

    department = QuerySelectField(query_factory=lambda: Department.query.all(),
                                  get_label="name")
    role = QuerySelectField(query_factory=lambda: Role.query.all(),
                            get_label="name")
    submit = SubmitField('Submit')


