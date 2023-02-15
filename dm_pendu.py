from fichier_pendu import pendu
""" fichier_pendu contient seulement les pendus en ASCI"""
accents="ÀÁÂÃÄÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÛÜÝ"
def test_mot(mot):
    test=False
    for i in mot:
      if i in accents or i.isnumeric() or not(2<len(mot)<23) or " " in mot:
            test=True
    return test
propositions=''
caractere_cache='_ '
erreurs=0
"""début du prgrm"""
mot=input("Quel mot voulez-vous faire deviner ? \n")
mot=mot.upper()
while  test_mot(mot)==True:
    print("Le mot précedemment entré est incorrect (trop "+
          "court, trop long, contient des chiffres ou accents)")
    mot=input("Quel mot voulez-vous faire deviner ? \n")
    mot=mot.upper()
print("\n"*45)
remplace_lettre=(caractere_cache+"-")*len(mot)
print ("Le mot recherché est: "+"_ "*len(mot))
avancement_mot=caractere_cache*len(mot)
while erreurs<10:
    lettre=input("*"*40+"\nQuelle lettre se trouve dans ce mot ? \n")
    lettre=lettre.upper()
    if len(lettre)>1 or lettre.isdigit() or lettre in accents or " " in lettre or lettre in propositions:
        print("La lettre entrée est invalide, vous l'avez peut-être déjà entrée. Veuillez réessayer")
        continue
    propositions=propositions+lettre
    if lettre in mot:
        numero_lettre=-1
        for testlettre in mot:
            numero_lettre+=1 
            if testlettre==lettre:
                remplace_lettre=remplace_lettre.split("-")
                remplace_lettre[numero_lettre]=lettre
                avancement_mot="".join(remplace_lettre)
                remplace_lettre="-".join(remplace_lettre)
    else:
        print ("Dommage ! La lettre "+lettre+" ne se trouve pas dans le mot !")
        erreurs+=1
        print("Vous avez commis {}/10 erreurs.".format(erreurs)+"\nIl vous reste "+str(10-erreurs)+" essais")
        print(pendu[erreurs-1])
    print(avancement_mot)
    if avancement_mot in mot:
        print("Tu as gagné la partie en "+str((len(mot)+erreurs))+ 
            " essais pour seulement "+str(erreurs)+" erreurs. Bravo !")
        break   
if erreurs==10:
    print("Tu as atteinds les 10 erreurs... Le mot était {}".format(mot))
if erreurs==0:
    print("Tu n'as fait aucune erreur ! N'aurais tu pas triché ?")
