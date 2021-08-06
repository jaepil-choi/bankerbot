from bankerbot.entity import Customer, Banker

class RealName:
    def __init__(self, banker: Banker, customer: Customer) -> None:
        self.banker = banker()
        self.customer = customer()
    
    def __str__(self) -> None:
        return

    def run(self):
        raise NotImplementedError
