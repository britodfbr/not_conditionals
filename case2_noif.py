from plans import (PlanSingle, PlanDuo, PlanFamily, PlanUniversity)


class Spotify:
    def __init__(self, plan):
        self.plan = plan
    
    def return_cost(self):
        return getattr(eval(f"Plan{self.plan.capitalize()}"), 'return_cost')()
