pareiza_parole = "8"
atlikušie_meginajumi = 3

while atlikušie_meginajumi >0:
    parole = input("Ievadi paroli:")
    if parole == pareiza_parole:
        print("Piekļuva atļauta")
        break

    atlikusie_meginajumi -= 1
    if(atlikusie_meginajumi > 0):
        print(f" Nepareiza parole. Atlikušais mēginājumu skaits: {atlikusie_meginajumi}")
    else:
        print("Piekļuve bloķēta")

