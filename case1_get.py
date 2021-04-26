from plans import (PlanSingle, PlanDuo, PlanFamily, PlanUniversity, PlanNotDefined)


class Spotify:
    plans = {
        'single': PlanSingle,
        'duo': PlanDuo,
        'family': PlanFamily,
        'university': PlanUniversity,
    }
    def __init__(self, plan):
        self.plan = plan.casefold()
    
    def return_cost(self):
        return getattr(self.plans.get(self.plan, PlanNotDefined(self.plan)), 'return_cost')()
