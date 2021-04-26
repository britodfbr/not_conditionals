class PlanSingle:
    def return_cost():
        return 16.9


class PlanDuo:
    def return_cost():
        return 21.9


class PlanFamily:
    def return_cost():
        return 26.9


class PlanUniversity:
    def return_cost():
        return 8.5


class PlanNotDefined:
    def __init__(self, plan):
        self.plan = plan

    def return_cost(self):
        return f"name 'Plan{self.plan.capitalize()}' Not defined"