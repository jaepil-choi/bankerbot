# 고객

class Customer:
    """고객
    """    
    def __init__(self) -> None:
        self.is_myself = True # 본인 여부
        self.valid_ids = []
    
    def narrow_down(self) -> None:
        raise NotImplementedError

## 고객 - 예금거래 상대방

class Individual(Customer):
    """개인

    Args:
        Customer ([type]): [description]
    """
    def __init__(self) -> None:
        super().__init__()
        self.age = None
        self.age_class = None
        self.is_family = None
        self.is_limited_person = False # 제한능력자 여부

        self.narrow_down()
    
    def narrow_down(self) -> None:
        
        # 연령별 분류
        if self.age < 14:
            self.age_class = 'minor'
            self.valid_ids = ['']
        elif self.age < 19:
            self.age_class = 'juvenile'
        elif self.age < 65:
            self.age_class = 'adult'
        elif self.age >= 65:
            self.age_class = 'old'
        else:
            raise Exception("Age error")
        

class Corporate(Customer):
    """법인

    Args:
        Customer ([type]): [description]
    """    
    def __init__(self) -> None:
        super().__init__()

class VoluntaryAssociation(Customer):
    """임의 단체

    Args:
        Customer ([type]): [description]
    """    
    def __init__(self) -> None:
        super().__init__()

### 고객 - 예금거래 상대방 - 개인

### 고객 - 예금거래 상대방 - 법인

class CorpPublic(Corporate):
    """공법인

    Args:
        Corporate ([type]): [description]
    """    
    def __init__(self) -> None:
        super().__init__()

class CorpPrivate(Corporate):
    """사법인

    Args:
        Corporate ([type]): [description]
    """    
    def __init__(self) -> None:
        super().__init__()

class CorpEtcPublic(Corporate):
    """기타공공단체

    Args:
        Corporate ([type]): [description]
    """    
    def __init__(self) -> None:
        super().__init__()

### 고객 - 예금거래 상대방 - 임의단체

class VolCooperative(VoluntaryAssociation):
    """조합

    Args:
        VoluntaryAssociation ([type]): [description]
    """    
    def __init__(self) -> None:
        super().__init__()

class VolFoundation(VoluntaryAssociation):
    """권리능력 없는 사단, 재단

    Args:
        VoluntaryAssociation ([type]): [description]
    """    
    def __init__(self) -> None:
        super().__init__()
# 행원

class Banker:
    def __init__(self) -> None:
        pass
