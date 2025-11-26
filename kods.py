import random

#klase ar produktu informāciju
class Produkti:
    def __init__(self, numurs,  nosaukums, cena):
        self.numurs = numurs
        self.nosaukums = nosaukums
        self.cena = cena
    
    #izprintēprodukta nosaukumu un cēnu
    def get_info(self):
        print(self.numurs, self.nosaukums, self.cena)

p1 = Produkti(1, "ceptu ābolu kārums", 0.43)
p2 = Produkti(2, "šokolādes müllermilch", 1.65)
p3 = Produkti(3, "NESCAFE Brown sugar 3 in 1", 0.33)
p4 = Produkti(4, "AriZona Sweet Tea Real Brewed", 2.15)
p5 = Produkti(5, "čili citruss Ādažu čipsi", 2.49)

visi_p = [p1, p2, p3, p4, p5]
current_p = visi_p[0]

atlaide = [5, 10, 15, 20]

#produktu skaits grozā
g = 0
print("Ievādi produkta numuru, lai pievienotu grozam")

while visi_p.index(current_p) < 4:
    print(current_p.get_info())
    current_p = visi_p[visi_p.index(current_p) + 1]

print(f"Grozs: {g}")
num = input(":  ")
if input == [0, 4]: ########
    g += 1
    print(f"Grozs: {g}")
else:
    print("Jaievāda ciparu")
