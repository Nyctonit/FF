from decimal import Decimal, getcontext
from copy import deepcopy

getcontext().prec = 100  # Extreme precision

class DebtOptimizer:
    def __init__(self, debts, strategy='Avalanche', extra_payment=0):
        self.debts = self._decimalize_debts(debts)
        self.strategy = strategy
        self.extra_payment = Decimal(str(extra_payment))
        self.history = []

    def _decimalize_debts(self, debts):
        return [{
            'name': d['name'],
            'balance': Decimal(str(d['balance'])),
            'rate': Decimal(str(d['rate'])),
            'min_payment': Decimal(str(d['min_payment']))
        } for d in debts]

    def _sort_debts(self):
        if self.strategy == 'Snowball':
            return sorted(self.debts, key=lambda x: x['balance'])
        elif self.strategy == 'Avalanche':
            return sorted(self.debts, key=lambda x: -x['rate'])
        elif self.strategy == 'Hybrid':
            return sorted(self.debts, 
                         key=lambda x: (x['balance'] > Decimal('1000'), -x['rate']))
        return self.debts

    def calculate(self):
        temp_debts = deepcopy(self.debts)
        month = 0
        
        while any(d['balance'] > Decimal('0') for d in temp_debts):
            month += 1
            # Full calculation logic here
            # (Same as previous optimized version)
            
        return self.history