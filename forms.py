from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, \
    SelectField
from wtforms.validators import InputRequired


class AddTaskForm(FlaskForm):
    task_id = IntegerField()
    name = StringField('Task Name',validators=[InputRequired()])
    due_date = DateField(
        'Date Due (mm/dd/yyyy)',
        format='%m/%d/%Y',
        validators=[InputRequired()])
        
    priority = SelectField(
        'Priority',
        choices=[
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
        ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')
        ]
    ) 
    status = IntegerField('Status')


