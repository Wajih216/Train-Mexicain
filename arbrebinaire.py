class ArbreBinaire:
        def __init__(self, etiquette = None, sag = None, sad = None):
            self.etiquette = etiquette
            self.sag = sag
            self.sad = sad
        
        def est_vide(self):
            if self.etiquette is None:
                   return True
            else:
                   return False


def taille(arbre):
    if arbre.est_vide() :
        return 0
    else :
        return 1+taille(arbre.sag)+taille(arbre.sad)
    



def hauteur(arbre):
    if arbre.est_vide():
        return 0
    else:
        return 1 + max(hauteur(arbre.sag), hauteur(arbre.sad))


    
    # Définition de l'arbre :
    #       1
    #     /   \
    #    2     3
    #   / \     \
    #  4   5     6
    #       \
    #        7
    
a = ArbreBinaire()
a.etiquette = 1
a.sag = ArbreBinaire(2)
a.sad = ArbreBinaire(3)
a.sag.sag = ArbreBinaire(4, ArbreBinaire(), ArbreBinaire())
a.sag.sad = ArbreBinaire(5)
a.sad.sag = ArbreBinaire()
a.sad.sad = ArbreBinaire(6, ArbreBinaire(), ArbreBinaire())
a.sag.sad.sag = ArbreBinaire()
a.sag.sad.sad = ArbreBinaire(7, ArbreBinaire(), ArbreBinaire())
    
print(hauteur(a))
print(taille(a))
print(a.sag.sad.sag.est_vide())