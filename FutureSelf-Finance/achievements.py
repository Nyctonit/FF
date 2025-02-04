ACHIEVEMENTS = {
    'first_sim': {
        'name': '🚀 First Step',
        'condition': lambda sims: len(sims) >= 1
    },
    'debt_free': {
        'name': '🎉 Debt Free',
        'condition': lambda sims: any(s['months_remaining'] == 0 for s in sims)
    },
    'big_payer': {
        'name': '💸 Big Spender',
        'condition': lambda sims: any(s['extra_payment'] > 10000 for s in sims)
    }
}

def check_achievements(simulations):
    unlocked = []
    for key, ach in ACHIEVEMENTS.items():
        if ach['condition'](simulations):
            unlocked.append(ach['name'])
    return unlocked