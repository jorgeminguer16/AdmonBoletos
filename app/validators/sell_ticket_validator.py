import datetime

from wtforms import Form, StringField, validators, FloatField, SelectField, ValidationError
from app.models.event import Ticket

class SellTicket(Form):
    client_name = StringField('Nombre del Cliente', [validators.Length(max=255), validators.DataRequired('El campo es requerido')])

    client_last_name = StringField('Apellidos',[validators.Length(max=255), validators.DataRequired('El campo es requerido')])

    price = FloatField('Precio', [validators.DataRequired('El campo es requerido')])

    event_id = SelectField('Evento',[validators.DataRequired('El campo es requerido')], choices=[])



class RedeemedTicket(Form):
    code = StringField('Código del Boleto', [validators.Length(max=255), validators.DataRequired('El campo es requerido')])

    def validate_code(self, field):
        code = field.data

        ticket = Ticket.query.filter(Ticket.code == code).first()

        if ticket is None:
            raise ValidationError("El boleto no existe")

        if ticket.is_interchange:
            raise ValidationError("El boleto ya ha sido canjeado")

        now = datetime.datetime.now()

        if now > ticket.event.end_date:
            raise ValidationError("El evento ha terminado")

        return True