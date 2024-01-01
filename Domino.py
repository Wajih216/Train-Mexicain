from tkinter import *
from random import randint
from classPile import *
from classDomino import *
from classJeumexicain import *
from classJoueur import *


# Première partie de création des joueurs et du jeu : 


jMexicain = Jeumexicain()
Albert = Joueur(jMexicain.pioche)
jMexicain.ajouterjoueur(Albert)
Mauricette = Joueur(jMexicain.pioche)
jMexicain.ajouterjoueur(Mauricette)
Ginette = Joueur(jMexicain.pioche)
jMexicain.ajouterjoueur(Ginette)
Maurice = Joueur(jMexicain.pioche)
jMexicain.ajouterjoueur(Maurice)

jMexicain.choisirjoueur()

partiefinie=False
gagnant=0


# Deuxième parie : Le fonction principal du jeu 


def jouer() :
    if partiefinie() :
        arretelejeu()
    else :
        jMexicain.jouer()
        afficheres()
        affichetr()
        affichedom() 
        



# Des fonctions d'affichage :
'''

Les fonctions ci-dessous sont définies dans l'ordre comme il est affiché
dans la fenêtre tkinter.

 1. Domino de départ ( Frame 1 ) 
 2. Trains mexicain et trains des joueurs ( Frame 1)
 3. Réserve des trains ( Frame 3 )
 4. Boutton 

'''
def affichedom() :
    '''
    La fonction qui permet l'affichage de domino de depart
    '''
    global photoD,jMexicain
    dom=jMexicain.dominoDepart
    photoD=PhotoImage(file='image\\petit-'+str(dom.A) +'-'+str(dom.B)+'.gif') 
    dominodepart.create_image(20,10, image=photoD,anchor=NW)     


def affichetr():
    '''
    La fonction qui permet d'afficher les trains des joueurs et le train Mexicain
    '''
    global photo,jMexicain
    for i in range(1,6) :
        if i!=1   :
            l=min(5,jMexicain.joueurs[i-2].train.taille())
            for j in range(l):
                dom=jMexicain.joueurs[i-2].train.les_elts[jMexicain.joueurs[i-2].train.taille()-l+j]
                photo[i-1][j]=PhotoImage(file='image\\petit-'+str(dom.A) +'-'+str(dom.B)+'.gif')       
        else :
            l=min(5,jMexicain.trainM.taille()) 
            for j in range(l):
                dom=jMexicain.trainM.les_elts[jMexicain.trainM.nbreDesElts-l+j]
                photo[i-1][j]=PhotoImage(file='image\\petit-'+str(dom.A) +'-'+str(dom.B)+'.gif')              
    for i in range(5) :
        for j in range(5) :
            trains.create_image(20+80*j,10+50*i, image=photo[i][j],anchor=NW)    


  
def afficheres():
    '''
    Affiche la reserve des dominos 
    '''
    global photoR,Maurice
    for i in range(1,4):
        for j in range(5):
            if (i-1)*5+j < len(Maurice.reserve):
                photoR[i-1][j]=PhotoImage(file='image\\petit-'+str(Maurice.reserve[(i-1)*5+j].A) +'-'+str(Maurice.reserve[(i-1)*5+j].B)+'.gif')
            else:
                photoR[i-1][j]=PhotoImage(file="image\\petit--1--1.gif")
    for i in range(3) :
        for j in range(5) :
            reserve.create_image(20+80*j,10+50*i, image=photoR[i][j],anchor=NW)


def arretelejeu():
    '''
    La fonction qui ouvre la fenêtre de fin du jeu
    '''
    filewin = Toplevel(fen)
    chaine='La partie est finie, '+queljoueur(gagnant)+' a gagné.'
    butt = Button(filewin, text=chaine)
    but=Button(filewin,text='quitter',command=fen.quit)
    butt.pack()
    but.pack()
    
   
def partiefinie() :
    '''
    La fonction indicatrice de la fin de la partie
    '''
    global gagnant
    for j in jMexicain.joueurs :
        if j.nombreDominosReserve == 0 :
            gangnant=j
    if jMexicain.piocheVide() :
        gagnant=jMexicain.joueurs[0]
        for j in jMexicain.joueurs :
            if j.valeurReserve() <gagnant.valeurReserve() :
                gangnant=j
    if gagnant!=0 :
        return True
    return False

# la fonction qui retourne le nom de joueur
def queljoueur(j) :
    if j==Albert :
        return 'Albert'
    elif j==Mauricette:
        return 'Mauricette'
    elif j==Ginette :
        return 'Ginette'
    else  :
        return 'Maurice'

'''
La construction des frames et des canvas. 
'''

# Fenetre principale
fen = Tk()
fen.title('Jeu du Train Mexicain')
fen.geometry("800x570")


# l'initialisation des images des domino ou domino vide

i=1

photo=[] # les images sur les trains
for i in range(5) :
    photos=[]
    for j in range(5) :
        photos.append(PhotoImage(file="image\\petit--1--1.gif"))
    photo.append(photos)

photoR=[] # les images de la reserve
for i in range(3) :
    photos=[]
    for j in range(5) :
        photos.append(PhotoImage(file="image\\petit--1--1.gif"))
    photoR.append(photos)

photoD=PhotoImage(file="image\\petit-1-1.gif") # l'image domino de depert

'''
frame 1 : Les trains des joueurs et les noms des joueurs 
'''

frm1=Frame(fen)

#Les joueurs : 
lbl01 = Label(frm1,text='Le jeu du Train Mexicain - Domino de départ : ') 
lbl02= Label(frm1,text='Train Mexicain ') 
lbl03= Label(frm1,text='Albert')
lbl04= Label(frm1,text='Mauricette')
lbl05= Label(frm1,text='Ginette')
lbl06= Label(frm1,text='Maurice')

lbl01.grid(row=1,column=2)
lbl02.grid(row=2,column=1)
lbl03.grid(row=3,column=1)
lbl04.grid(row=4,column=1)
lbl05.grid(row=5,column=1)
lbl06.grid(row=6,column=1)

dominodepart=Canvas(frm1,width=95, height=50,bg='white')
dominodepart.grid(row=1,column=3)

trains=Canvas(frm1,width=420, height=250,bg='white')
trains.grid(row=2,column=2,rowspan=5,padx=10,pady=10)
frm1.pack(side=TOP)

'''
frame 2 : La réserve
'''

frm2=Frame(fen)

reserve=Canvas(frm2,width=440, height=150,bg='white')
reserve.grid(row=4,column=3,rowspan=3,padx=0,pady=0)

frm2.pack(side=TOP)

'''
frame 3 : Bouton de jeu,  GO !
'''

frm3 = Frame(fen)

Go = Button(frm3, width=8, height=1, text='GO !',command=jouer)
Go.grid(row=8,column=3)

frm3.pack(side=TOP)

'''
initialisation
'''

afficheres()
affichetr()
affichedom()

'''
lancer la fenetre
'''

fen.mainloop()
fen.destroy()