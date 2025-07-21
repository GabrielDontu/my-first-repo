print(f"Tema pentru acasă - Input, Print") 

print(f"==================================================")
print(f"Exercițiul 1 - Afișează un mesaj care folosește variabile pentru temperatura într-un oraș, creând doua variabile oras si temperatura")
print(f"==================================================")

oraș = "Chisinau"
temperatura = 25
print(f"In orasul {oraș} sunt {temperatura} grade Celsius")

print(f"==================================================")
print(f"Exercițiul 2 - Folosește .format() pentru a afișa distanța dintre două orașe.")
print(f"==================================================")

oras1 = "Bucuresti "
oras2 = "Chisinau"
distanta = 450 
print("Distanta de la {} la {} este de {} kilometri".format(oras1, oras2, distanta))

print(f"==================================================")
print(f"Exercițiul 3 - Folosește f-string pentru a afișa raportul între două numere,creând doar doua variabile.")
print(f"==================================================")

numar1 = 50
numar2 = 10
print(f"Raportul dintre {numar1} și {numar2} este {numar1 / numar2}")

print(f"==================================================")
print(f"Exercițiul 4 - Afișează prețul unui produs după aplicarea unui discount folosind .format().")
print(f"==================================================")

produs = "Laptop"
pret_initial = 3000
discount = 20  
pret_final = pret_initial * (1 - discount / 100)
print("Prețul final al produsului {} după un discount de {}% este {:.2f} lei.".format(produs, discount, pret_final))

print(f"==================================================")
print(f"Exercițiul 5 - Folosește f-string pentru a afișa volumul unui cub cu latura, citita de la tastatura")
print(f"==================================================")

latura = float(input("Introdu latura cubului: "))
volum = latura ** 3
print(f"Volumul cubului cu latura {latura} este {volum}")

print(f"==================================================")
print(f"Exercițiul 6 - Afișează timpul total de lucru după n zile folosind .format().")
print(f"==================================================")

ore_pe_zi = 8
zile = 5
ore_totale = ore_pe_zi * zile
print("Timpul total de lucru după {} zile este {} ore.".format(zile, ore_totale)) 

print(f"==================================================")
print(f"Exercițiul 7 - Folosește f-string pentru a calcula și afișa procentul de rezolvare a unor exerciții.")
print(f"==================================================")

exercitii_rezolvate = 45
exercitii_total = 50
procent = (exercitii_rezolvate / exercitii_total) * 100
print(f"Ai rezolvat {procent:.2f}% din exerciții.")

print(f"==================================================")
print(f"Exercițiul 8 - Folosește .format() pentru a afișa prețul final al unui produs cu TVA.")
print(f"==================================================")

pret = 100
tva = 0.2  
pret_final = pret * (1 + tva)
print("Prețul final al produsului cu TVA este {:.2f} lei.".format(pret_final))

print(f"==================================================")
print(f"Exercițiul 9 - Folosește f-string pentru a afișa vârsta pe care o vei avea în 10 ani.")
print(f"==================================================")

varsta_curenta = 18
varsta_viitoare = varsta_curenta + 10
print(f"Peste 10 ani vei avea {varsta_viitoare} ani.")

print(f"==================================================")
print(f"Exercițiul 10 - Calculează și afișează suma și media a trei numere folosind f-string,citite de la tastatura.")
print(f"==================================================")

numar1 = float(input("Introdu primul număr: "))
numar2 = float(input("Introdu al doilea număr: "))
numar3 = float(input("Introdu al treilea număr: "))
suma = numar1 + numar2 + numar3
media = suma / 3
print(f"Suma celor trei numere este {suma}, iar media este {media:.2f}")
