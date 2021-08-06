# 고객

class Customer:
    def __init__(self) -> None:
        pass

## 고객 - 예금거래 상대방

class Individual(Customer):
    def __init__(self) -> None:
        super().__init__()

class Corporate(Customer):
    def __init__(self) -> None:
        super().__init__()

class VoluntaryAssociation(Customer):
    def __init__(self) -> None:
        super().__init__()

# 행원

class Banker:
    def __init__(self) -> None:
        pass
