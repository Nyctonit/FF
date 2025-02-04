import firebase_admin
from firebase_admin import firestore
import json
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

def save_simulation(user_id, simulation):
    db = firestore.client()
    doc_ref = db.collection('users').document(user_id).collection('simulations').document()
    doc_ref.set(json.loads(json.dumps(simulation, cls=DecimalEncoder)))

def load_simulations(user_id):
    db = firestore.client()
    docs = db.collection('users').document(user_id).collection('simulations').stream()
    return [doc.to_dict() for doc in docs]