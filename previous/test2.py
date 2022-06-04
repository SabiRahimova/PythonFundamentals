users=[]

class User:
    def __init__(self,_ad,_soyad):
        self.ad=_ad
        self.soyad=_soyad
        users.append(self)
    
    def showfullname(self):
        return f'{self.ad}/ {self.soyad} ' 
    
    
class Developer(User):
    def __init__(self,_ad,_soyad,_language):
        super().__init__(_ad,_soyad)
        self.dil=_language
        
    def showprofession(self):
        return f'{self.dil}'

class Marketoloq(User):
    def __init__(self,_ad,_soyad,_profession):
        super().__init__(_ad,_soyad)
        self.ohdelik=_profession
        
    def showresult(self):
        return f'{self.ohdelik}'