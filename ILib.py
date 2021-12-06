# Hugues FARTHOUAT Baptiste RENOUARD 06/12/2021
import unicodedata
import random
import os
from collections import OrderedDict
import platform

allow_letters = "azertyuiopqsdfghjklmwxcvbn"
allow_symb = "-"

# Fonction permettant d'analyser une liste
# de mots retournant les propotions de
# présence des lettres
# Entré: pth = chemin du dictionnaire
# Sortie: Dictionnaire -> charactère : nombre de mots où il est présent
def analyseDico(pth="liste_francais.txt"):
    dico = getDicoFr(pth=path,stripAccents = True)
    analyse = {}
    for char in allow_letters:
        analyse[char] = 0
    for word in dico:
        for char in allow_letters:
            if char in word:
                analyse[char] += 1
        pass
    sortedAnalyse = dict(sorted(analyse.items(), key=lambda item: item[1],reverse=True))
    print("Nombre de mots comportant la lettre:")
    l = len(dico)
    for k,v in sortedAnalyse.items():
        print(str(k)+": " + str(v) + " -> "+str(round(v*100/l,2))+"%")
    return sortedAnalyse

# Fonction de test permettant de compter le
# nombre de mots finissables "bêtement" en
# utiliser les lettres les plus probables
# Entré: path = chemin du dictionnaire
# Sortie: Nombres de mots complétables facilement
def cheackEasy(path="liste_francais.txt"):
    count = 0
    analyse = analyseDico()
    errors = 0
    dico = getDicoFr(pth=path,stripAccents=True)
    global maxErrors
    for word in dico:
        err = 0
        wordTemp = word.replace("-","")
        for k,v in analyse.items():
            if err >= maxErrors or wordTemp=="":
                break
            if k in wordTemp:
                wordTemp = wordTemp.replace(k,"")
            else:
                err+=1
        if err < maxErrors:
            count += 1
    return count

# Fonction permettant de supprimer les accents
# Entré: s = mot avec accents
# Sortie: mot sans accents
def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

# Fonction permettant de lire un fichier texte
# et de retourner un liste de mots formatés
# Entré: path : chemin du dictionnaire
# Sortie: liste des mots
def getDicoFr(path="liste_francais.txt",stripAccents = False):
    l = []
    f = open(path, "r")
    for x in f:
        s2 = (x.split(" ")[0].lower().replace("œ","oe").replace("\n",""))
        if stripAccents:
            s2 = strip_accents(s2)
            s3 = s2
        else:
            s3 = strip_accents(s2)
        for v in s3:
            if not (v in allow_letters) and not (v in allow_symb):
                s2.replace(v,"")
        l.append(s2)
    f.close()
    return l

# Fonction permettant de générer un mot aléatoire
# Entré: NON
# Sortie: Mot aléatoire du dictionnaire de base.
def getRandomWord():
    dic = getDicoFr()
    wordNoModify = dic[random.randint(0,len(dic)-1)]
    word = strip_accents(wordNoModify)
    return [wordNoModify,word]

# Fonction générant le mot à afficher avec les _
# Entré: word : mot
# Sortie: mot modifié
def getClearWord(word):
    nWord = ""
    for c in word:
        if c in allow_letters:
            nWord +="_"
        else:
            nWord+="-"
    return nWord

# Fonction d'entrée clavier demandant si il
# faut rejouer ou non
# Entré: NON
# Sortie: boolean True si arret, False si rejoue
def playAgainInput():
    while True:
        inp = input("Pour rejouer tappez 1, sinon 0:\n")
        if inp != '1' and inp != '0':
            print("Non reconnu")
            continue
        if inp == "1":
            return False
        if inp == "0":
            return True
    return False

# Fonction d'entrée clavier permettant de
# saisir une lettre
# Entré: log : liste des lettres déjà utilisées
# Sortie: charactère à ajouter
def requestInput(log=[]):
    valid = False
    while not valid:
        inp = input("Votre lettre: ")
        if len(inp) != 1:
            print("Vous ne pouvez rentrer que une lettre!")
            continue
        if not inp in allow_letters:
            print("Cette lettre est invalide!")
            continue
        if inp in log:
            print("Cette lettre a déjà été utilisée!")
            continue
        return inp

# Met la première lettre du mot en majuscule
# Entré: word : mot
# Sortie: mot avec sa première lettre en majuscule
def firstLetterCapital(word):
    return word[0].upper() + word[1:]

# Fonction permettant de trier un fichier texte
# par taille puis ordre aplhabétique
# Entré: NON
# Sortie: NON
def tri():

    l=getDicoFr(path="liste_francais.txt")
    dic={}
    maxsize=0

    for w in l:
        size = len(w)
        t =  []
        if size in dic:
            t = dic[size]
        t.append(w)
        dic[size] = t
        if maxsize<size:
            maxsize=size
    l2=[]
    for i in range(5,maxsize):
        t=[]
        if i in dic:
            t = dic[i]
        t.sort()
        l2.extend(t)

    with open("liste_francais_trie.txt", "w") as file:
        for i in range(0,len(l2)):
            file.write(l2[i]+"\n")
