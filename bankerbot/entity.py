# 고객

class Customer:
    """고객
    """    
    def __init__(self) -> None:
        self.is_myself = True # 본인 여부

## 고객 - 예금거래 상대방

class Individual(Customer):
    """개인

    Args:
        Customer ([type]): [description]
    """
    def __init__(self) -> None:
        super().__init__()
        self.is_limited_person = False # 제한능력자 여부

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

class IndMinor(Individual):
    """미성년자

    Args:
        Individual ([type]): [description]
    """    
    def __init__(self) -> None:
        super().__init__()

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

### 고객 - 예금거래 상대방 - 임의단체

class VolCooperative(VoluntaryAssociation):
    """조합

    Args:
        VoluntaryAssociation ([type]): [description]
    """    

class VolFoundation(VoluntaryAssociation):
    """권리능력 없는 사단, 재단

    Args:
        VoluntaryAssociation ([type]): [description]
    """    

# 행원

class Banker:
    def __init__(self) -> None:
        pass
