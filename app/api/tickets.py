from flask import Blueprint, request, render_template, url_for, redirect, flash
from app.validators.sell_ticket_validator import SellTicket, RedeemedTicket
from app.models.event import Event, Ticket
from app.helpers import generate_unique_code

TicketController = Blueprint("tickets", __name__)


@TicketController.route('/sell-ticket', methods=['GET', 'POST'])
def sell_ticket():

    form = SellTicket(request.form)
    events = Event.query.all()
    form.event_id.choices = list(map(lambda event: (event.id, event.name), events))

    if request.method == 'POST' and form.validate():

        event_selected = Event.query.get(form.event_id.data)

        if event_selected.has_sold_out_tickets():
            flash('Los boletos estan agotados')
            return redirect(url_for('tickets.sell_ticket'))

        ticket = Ticket()
        ticket.code = generate_unique_code()
        ticket.client_name = form.client_name.data
        ticket.client_last_name = form.client_last_name.data
        ticket.price = form.price.data
        ticket.event_id = form.event_id.data
        ticket.save()

        flash('Codigo del boleto %s' % ticket.code)
        
        return redirect(url_for('tickets.sell_ticket'))


    return render_template('tickets/sell_ticket.html', form=form)

@TicketController.route('/redeem-ticket', methods=['GET', 'POST'])
def redeem_ticket():

    form = RedeemedTicket(request.form)

    if request.method == 'POST' and form.validate():

        ticket = Ticket.query.filter(
            Ticket.code == form.code.data
        ).first()

        ticket.is_interchange = True
        ticket.save()

        flash('El boleto ha sido canjeado')

        return redirect(url_for('tickets.redeem_ticket'))


    return render_template('tickets/redeem_ticket.html', form=form)