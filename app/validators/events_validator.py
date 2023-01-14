from wtforms import Form, StringField, validators, IntegerField, DateTimeLocalField, ValidationError



class GreatherThan(object):

    def __init__(self, fieldname : str):
        self.fieldname = fieldname

    def __call__(self, form, field):
        try:
            other = form[self.fieldname]
        except KeyError:
            raise ValidationError(field.gettext("Invalid field name '%s'.") % self.fieldname)

        if field.data < other.data:
            raise ValidationError(field.gettext("Campo '%s' debe ser mayor que '%s'  .") % (field.label.text, other.label.text))



class EventCreate(Form):
    name = StringField('Nombre', [validators.Length(max=255), validators.DataRequired('El campo es requerido')])

    start_date = DateTimeLocalField('Fecha Inicio', [validators.DataRequired('El campo es requerido')], format='%Y-%m-%dT%H:%M')

    end_date = DateTimeLocalField('Fecha Finalización', [
        validators.DataRequired('El campo es requerido'),
        GreatherThan('start_date')
    ], format='%Y-%m-%dT%H:%M')

    available_tickets = IntegerField('Tickets Disponibles', [
        validators.DataRequired('El campo es requerido'),
        validators.NumberRange(1, 300, message='Numero debe estar entre 1 y 300')
    ])
