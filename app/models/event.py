from app.models import db, Model
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
class Event(Model):
    name = db.Column(db.String(100))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    available_tickets = db.Column(db.Integer)

    @property
    def tickets_sold(self):
        ticket_sold = Ticket.query.filter(
            Ticket.event_id == self.id
        )
        return ticket_sold.count()

    def has_sold_out_tickets(self) -> bool:
        return self.tickets_sold < self.available_tickets

    def has_sold_tickets(self) -> bool:
        return self.tickets_sold > 0

    @property
    def redeemed_tickets(self):
        redeemed_tickets = Ticket.query.filter(
            Ticket.event_id == self.id,
            Ticket.is_interchange
        )
        return redeemed_tickets.count()




class Ticket(Model):
    code = db.Column(db.String(36), unique=True)
    client_name = db.Column(db.String(255))
    client_last_name = db.Column(db.String(255))
    is_interchange = db.Column(db.Boolean, default=False)
    price = db.Column(db.Float)
    event_id = db.Column(db.Integer, ForeignKey('event.id'))
    event = relationship(Event, backref='tickets')