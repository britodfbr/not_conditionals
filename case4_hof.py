from plans import (PlanSingle, PlanDuo, PlanFamily, PlanUniversity)


class Spotify:
    def __init__(self, plan):
        self.plan = plan
    
    def __getattr__(self, name):
        return getattr(eval(f"Plan{self.plan.capitalize()}"), name)
