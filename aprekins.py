
class Rekins:

    def __init__(self,vards, teksts, izmeri, materials) -> object:
        self.vards = vards
        self.teksts = teksts
        self.izmeri = izmeri
        self.materials = materials
        laiks = datetime.datetime.now()

    def aprekinat_laukumu(self):
        laukums = self.izmeri[0] * self.izmeri[1] * self.izmeri[2]
        print(laukums)





