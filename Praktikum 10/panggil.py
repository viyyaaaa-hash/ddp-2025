import bangunRuang as br 
import bangunDatar as bd

print("~~~~ BANGUN RUANG ~~~~")
print (f"volum kubus dengan sisi 3 adalah {br.kubus(3)}")
print (f"volum balok adalah {br.balok(4,5,2)}")
print (f"volum prisma segitiga adalah {br.prisma(5,4,5)}")
print (f"volum tabung adalah {br.tabung(3,5)}")
print (f"volum Kerucut adalah {br.Kerucut(5,9)}")

print("~~~~ BANGUN DATAR ~~~~")
print(f"Luas persegi adalah {bd.persegi(8)}")
print(f"Luas persegi panjang adalah {bd.persegi_panjang(8,3)}")
print(f"Luas segitiga adalah {bd.segitiga(3,5)}")
print(f"Luas lingkaran adalah {bd.lingkaran(7)}")
print(f"Luas JajarGenjang adalah {bd.JajarGenjang(4,7)}")