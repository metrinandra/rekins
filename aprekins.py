import datetime

class Aprekins:

    def __init__(self,vards, teksts, izmeri, materials) -> object:
        self.vards = vards
        self.teksts = teksts
        self.izmeri = izmeri
        self.materials = materials
        laiks = datetime.datetime.now()

    def aprekinat_laukumu(self):
        laukums = int(self.izmeri[0]) * int(self.izmeri[1]) * int(self.izmeri[2])
        print(laukums)





