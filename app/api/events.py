import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.event import Event
from app.validators.events_validator import EventCreate
EventController = Blueprint("events", __name__)


@EventController.route('/')
def index():
    events = Event.query.all()
    return render_template('events/index.html', events=events)


@EventController.route('/events/create', methods=['POST','GET'])
def create():

    form_event = EventCreate(request.form)
    if request.method == 'POST' and form_event.validate():
        # Se crea un nuevo objeto del evento
        event = Event()
        event.name = form_event.name.data
        event.start_date = form_event.start_date.data
        event.end_date = form_event.end_date.data
        event.available_tickets = form_event.available_tickets.data

        # save the object into the database
        event.save()

        flash('¡Evento agregado correctamente!')

        return redirect(url_for('events.index'))
    else :
        return render_template('events/create.html', form=form_event)


@EventController.route("/events/update/<int:id>", methods=["GET", "POST"])
def update_event(id):

    event = Event.query.get(id)

    if request.method == "POST":
        event.name = request.form['nombre']
        event.start_date = request.form['fecha_inicio']
        event.end_date = request.form['fecha_fin']

        event.save()

        flash('¡Su evento ha sido actualizado correctamente!')

        return redirect(url_for('boletos.index'))

    return render_template("update.html", eventos=event)


@EventController.route("/events/delete/<id>", methods=["GET"])
def delete(id):

    now = datetime.datetime.now()
    event = Event.query.get(id)

    if event.end_date > now:
        flash('¡Su evento esta en curso, no puede ser eliminado!')
        return redirect(url_for('events.index'))

    if event.has_sold_tickets():
        flash('¡Su evento tiene boletos vendidos, no puede ser eliminado!')
        return redirect(url_for('events.index'))

    event.delete()

    flash('¡Su evento ha sido eliminado correctamente!')

    return redirect(url_for('events.index'))

@EventController.route("/events/<id>/detail", methods=["GET"])
def detail(id):
    event = Event.query.get(id)

    if event is None:
        flash('¡No existe el evento!')
        return redirect(url_for('events.index'))


    return render_template('events/event_details.html', event=event)