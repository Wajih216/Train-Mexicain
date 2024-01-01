class Pile :
        '''Dans cette classe, je définis la Pile.'''

        def __init__(self):
                ''' -> Pile
                Permet de créer une pile.
                '''
                self.les_elts = []
                self.nbreDesElts = 0

        def empiler(self,elt):
                '''Pile, élément -> Rien
                permet d'empiler un élément au sommet de la pile.
                '''
                
                if len(self.les_elts) == self.nbreDesElts:
                        self.les_elts.append(elt)
                else :
                        self.les_elts[self.nbreDesElts] = elt
                self.nbreDesElts += 1

        def depiler(self):
                '''Pile -> elt
                Permet de retourner l'élément au sommet de la pile et l'enlève.
                '''
                assert not self.estVide()
                elt=self.les_elts[self.nbreDesElts-1]
                del self.les_elts[self.nbreDesElts-1]
                self.nbreDesElts-=1
                return elt

        def estVide(self):
                '''Pile -> Booléen
                Teste si la pile est vide.
                '''
                return self.nbreDesElts==0

        def sommet(self):
                '''Pile -> Objet
                Permet de retourner le sommet de la pile.
                '''
                assert not self.estVide()
                return self.les_elts[self.nbreDesElts-1]

        def taille(self):
                '''Pile -> int
                Permet de retourner la taille de la pile.
                '''
                return self.nbreDesElts