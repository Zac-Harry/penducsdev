import os
import platform
import ILib
# Fonction vérifiant si le caractère est présent.
# retourne le nouveau mot "clean"
def unClear(word,wordNoModify,clear,char):
    global errors
    global log
    temp = list(clear)
    found = False
    for i in range(len(word)):
        if word[i] == char:
            temp[i] = wordNoModify[i]
            found = True
    if not found:
        print("Erreur !")
        errors +=1
    return ''.join(temp)

# Fonction initialisant une partie
def initPartie():
    global rdm
    global end
    global log
    global wordNoModify
    global word
    global errors
    global clear
    rdm = ILib.getRandomWord()
    wordNoModify = rdm[0]
    word = rdm[1]
    clear = ILib.getClearWord(word)
    end = False
    log = []
    errors = 0
    clear = unClear(word,wordNoModify,clear,word[0])
    log.append(word[0])

# Liste d'affichage en fonction des erreurs
errorsPrint = [
"\n\n\n\n\n",
"\n\n\n\n\n____",
"\n|\n|\n|\n|\n|____",
"____\n|\n|\n|\n|\n|____",
"____\n|  |\n|\n|\n|\n|____",
"____\n|  |\n|  o\n|\n|\n|____",
"____\n|  |\n|  o\n|  |\n|\n|____",
# "____\n|  |\n|  o\n| /|\n|\n|____",
"____\n|  |\n|  o\n| /|\\\n|\n|____",
# "____\n|  |\n|  o\n| /|\\\n| /'\n|____",
"____\n|  |\n|  o\n| /|\\\n| /'\\\n|____"]

# sauvegarde du meilleur score
bestScore = -1

# nombre maximum d'erreurs
maxErrors = len(errorsPrint)-1

initPartie()

# Permet de clear la console selon l'os
cmd = 'clear'
if(platform.system()=="Windows"):
    cmd = 'cls'

#Boucle principale
while(not end):

    # clear de la console
    os.system(cmd)

    # perdu
    if errors >= maxErrors:
        print(errorsPrint[errors])
        print("Vous avez perdu ;( !")
        print("Le mot était " + ILib.firstLetterCapital(word) + "\n")
        if bestScore != -1:
            print("Meilleur score: "+str(bestScore)+"/"+str(maxErrors))
        else:
            print("Aucun record enregistré.")
        end = ILib.playAgainInput()
        if not end:
            initPartie()
            continue
        else:
            break

    # gagné
    if not "_" in clear:
        end = True
        print("*- "+ILib.firstLetterCapital(word)+" -*")
        print("Vous avez gagné :) !")
        if bestScore == -1:
            bestScore = errors
        elif bestScore > errors:
            bestScore = errors
        if bestScore != -1:
            print("Meilleur score: "+str(bestScore)+"/"+str(maxErrors))
        else:
            print("Aucun record enregistré.")
        end = ILib.playAgainInput()
        if not end:
            initPartie()
            continue
        else:
            if bestScore != -1:
                print("Meilleur score: "+str(bestScore)+"/"+str(maxErrors))
            else:
                print("Aucun record enregistré.")
            break

    # affichage du meilleur score
    if bestScore != -1:
        print("Meilleur score: "+str(bestScore)+"/"+str(maxErrors))
    else:
        print("Aucun record enregistré.")

    # affichage
    print(errorsPrint[errors])
    print("Erreurs: ",errors,"/",maxErrors)
    print("Déjà utilisé: " + ", ".join(log))
    print("Devinez: " + ILib.firstLetterCapital(clear))
    inp = ILib.requestInput(log)
    log.append(inp)
    clear = unClear(word,wordNoModify,clear,inp)
exit(0)
