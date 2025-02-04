from decimal import Decimal

def calculate_net_worth(assets, debts):
    """Assets format: {'savings': 5000, 'investments': 10000}"""
    total_assets = sum(Decimal(str(v)) for v in assets.values())
    total_debt = sum(Decimal(str(d['balance'])) for d in debts)
    return total_assets - total_debt