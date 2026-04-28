import copy


class NRegine():

    def __init__(self):
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self.soluzioni = []


#===============APPROCCIO 2=================+
    #rappresentiamo soluzione come un vettore di N regine
    #ognuno rappresentante una regina come riga e colonna
    def solve2(self,N):
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self.soluzioni = []
        self._ricorsione2([],N)


    #pariziale è un vettore di N elementi, ognuno rappresentante una regina come riga e colonna
    def _ricorsione2(self,parziale,N):
        self.n_chiamate +=1

        #caso terminale: ho messo N regine
        if len(parziale) == N:
            #if self._is_soluzione(parziale):
                #self.n_soluzioni += 1
                #print(parziale)
            if self._is_nuova_soluzione(parziale):
                self.n_soluzioni += 1
                self.soluzioni.append(copy.deepcopy(parziale))
            #print(parziale)
        #caso ricorsivo: ho messo <N regine
        else:
            for riga in range(N):
                for col in range(N):
                    nuova_reg = [riga,col]
                    if self._step_is_valid (nuova_reg,parziale) :
                        #aggiungi pezzetto di soluzione in parziale
                        parziale.append(nuova_reg)
                        self._ricorsione2(parziale,N)
                        #backtracking
                        parziale.pop()


    #confrontiamo la soluzione potenziale con tutte quelle già trovate
    #se è diversa, restituiamo True se no False
    def _is_nuova_soluzione(self,soluzione_pot):
        n = len(soluzione_pot)
        for sol in self.soluzioni:
            counter = 0
            for reg in soluzione_pot:
                if reg in sol:
                    counter += 1
            if counter == n:
                return False
        return True

    #Funzione ch controlla se la nuova regina da inserire è ammissibile
    #rispetto alla soluzione parziale costruita finora
    def _step_is_valid(self,nuova_reg,parziale):
        for reg in parziale:
            if not self._is_pair_ammissibile(nuova_reg,reg):
                return False
        return True

    #Funzione che rende due regine e restituisce True se non si possono attaccare, altrimenti False

    def _is_pair_ammissibile(self,r1,r2):
        #1)verifico la riga, return False
        #r è una lista [0] riga
        if r1[0] == r2[0]:
            return False
        #2)verifico la colonna, re False
        # r è una lista [1] colonna
        if r1[1] == r2[1]:
            return False
        #3)verifico diag 1
        #per fare questa verifica devo controllare
        #riga r1 - colonna r1 == riga r2 - colonna r2
        if r1[0] - r1[1] == r2[0] - r2[1] :
            return False
        #4)verifico diag 2
        # colonna r1 + riga r1 == colonna r2 + riga r2
        if r1[0] + r1[1] == r2[0] + r2[1] :
            return False
        #5)controlli passati
        return True

    #Metodo che data una possibile soluzione verifica se è ammissibile, restituisce True se è ammissibile, False non ammissibile
    def _is_soluzione(self,soluzione_possibile):
        for i in range (len(soluzione_possibile)-1):
            for j in range (i+1,len(soluzione_possibile)):
                if not self._is_pair_ammissibile(soluzione_possibile[i],soluzione_possibile[j]):
                    return False
        return True


if __name__ == "__main__":
    nreg = NRegine()
    nreg.solve2(4)

    print(nreg.n_soluzioni)
    print(nreg.n_chiamate)
    print(nreg.soluzioni)