



def generate_unique_code() -> str:
    import uuid
    from app.models.event import Ticket

    code = uuid.uuid4()

    exists = True

    while(exists):
        record = Ticket.query.filter(
            Ticket.code == code
        ).first()

        exists = record is not None

    return str(code)






