from icalendar import Calendar, Event
from datetime import datetime, timedelta

def generate_payment_calendar(simulation_data):
    cal = Calendar()
    cal.add('prodid', '-//Debt Destroyer Calendar//mxm.dk//')
    cal.add('version', '2.0')
    
    current_date = datetime.now()
    
    for idx, payment in enumerate(simulation_data):
        event = Event()
        event.add('summary', f'Debt Payment: €{payment["amount_paid"]}')
        event.add('dtstart', current_date + timedelta(days=30*idx))
        event.add('description', 
                f"Paid: €{payment['amount_paid']}\n"
                f"Remaining Balance: €{payment['remaining_balance']}")
        cal.add_component(event)
    
    return cal.to_ical()