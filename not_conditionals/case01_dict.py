class Spotify:
    plans= {
        'single': 16.9,
        'duo': 21.9,
        'family': 26.9,
        'university': 8.5,
    }
    def __init__(self, plan):
        self.plan = plan
    
    def return_cost(self):
        return self.plans.get(self.plan.casefold(), f'name "{self.plan}" not defined')