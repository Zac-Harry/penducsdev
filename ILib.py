import unicodedata
import random
import os
from collections import OrderedDict
import platform

allow_letters = "azertyuiopqsdfghjklmwxcvbn"
allow_symb = "-"

def analyseDico():
    dico = getDicoFr(stripAccents = True)
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

def cheackEasy():
    count = 0
    analyse = analyseDico()
    errors = 0
    dico = getDicoFr(path="liste_francais.txt",stripAccents=True)
    global maxErrors
    for word in dico:
        err = 0
        wordTemp = word.replace("-","")
        # print(wordTemp)
        for k,v in analyse.items():
            # print(k+":"+wordTemp+ str(err))
            if err >= maxErrors or wordTemp=="":
                break
            if k in wordTemp:
                wordTemp = wordTemp.replace(k,"")
            else:
                err+=1
        # print(word+" " + str(err)+"/"+str(maxErrors))
        if err < maxErrors:
            count += 1
        # print("\n")
    return count

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

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

def getRandomWord():
    dic = getDicoFr()
    wordNoModify = dic[random.randint(0,len(dic)-1)]
    word = strip_accents(wordNoModify)
    return [wordNoModify,word]

def getClearWord(word,first_letter=False):
    nWord = ""
    for c in word:
        if c in allow_letters:
            nWord +="_"
        else:
            nWord+="-"
    return nWord

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

def firstLetterCapital(word):
    return word[0].upper() + word[1:]


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
print(tri())
exit(0)


errorsPrint = [
"\n\n\n\n\n",
"\n\n\n\n\n____",
"\n|\n|\n|\n|\n|____",
"____\n|\n|\n|\n|\n|____",
"____\n|  |\n|\n|\n|\n|____",
"____\n|  |\n|  o\n|\n|\n|____",
"____\n|  |\n|  o\n|  |\n|\n|____",
"____\n|  |\n|  o\n| /|\n|\n|____",
"____\n|  |\n|  o\n| /|\\\n|\n|____",
"____\n|  |\n|  o\n| /|\\\n| /'\n|____",
"____\n|  |\n|  o\n| /|\\\n| /'\\\n|____"]

bestScore = -1
maxErrors = len(errorsPrint)-1
# print(len(getDicoFr()))
# print(cheackEasy())
# exit(0)

random = getRandomWord()
wordNoModify = random[0]
word = random[1]
clear = getClearWord(word)
end = False
log = []
errors = 0
clear = unClear(word,wordNoModify,clear,word[0])
log.append(word[0])
cmd = 'clear'
if(platform.system()=="Windows"):
    cmd = 'cls'

while(not end):
    os.system(cmd)
    if errors >= maxErrors:
        end = True
        print(errorsPrint[errors])
        print("Vous avez perdu ;( !")
        print("Le mot était " + firstLetterCapital(word))
        break
    if not "_" in clear:
        end = True
        print("*- "+firstLetterCapital(word)+" -*")
        print("Vous avez gagné :) !")
        break
    # print("Erreurs: " + str(errors)+"/"+str(maxErrors))
    print(errorsPrint[errors])
    print("Déjà utilisé: " + ", ".join(log))
    print("Devinez: " + firstLetterCapital(clear))
    inp = requestInput(log)
    log.append(inp)
    clear = unClear(word,wordNoModify,clear,inp)




