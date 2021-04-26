class Spotify:
    def __init__(self, plan):
        self.plan = plan
    
    def return_cost(self):
        if self.plan == 'single':
            return 16.9
        elif self.plan == 'duo':
            return 21.9
        elif self.plan == 'family':
            return 26.9
        elif self.plan == 'university':
            return 8.5
        raise NameError(f'name "{self.plan}" not defined')