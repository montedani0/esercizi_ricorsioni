import copy


class QuadratoMagico():

    def __init__(self,N):
        self.N = N
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self.soluzioni = []


    #soluzione del quadrato magixo rappresentata da un vettore N^2 elementi,
    #ogni elemento rappresenta una cella del quadrato, e il suo valore è il numero che mettiamo nella cella
    def risolvi_quadrato(self):
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self.soluzioni = []
        self._ricorsione([], set(range (1,self.N*self.N+1)))

    def _ricorsione(self,parziale,rimanenti):
        self.n_chiamate += 1
        if len(parziale) == self.N * self.N:
            if self._is_valido(parziale):
                self.n_soluzioni += 1
                self.soluzioni.append(copy.deepcopy(parziale))
            #print(parziale)
        else:
            for numero in rimanenti:
                #1)aggiungere numero a parziale
                parziale.append(numero)
                if self._parziale_is_valido(parziale):
                    #1) tolgo il umero appena inserito dai rimanenti
                    nuovi_rimanenti = copy.deepcopy(rimanenti)
                    nuovi_rimanenti.remove(numero)
                    #2)andare avanti nella ricorsione
                    self._ricorsione(parziale, nuovi_rimanenti)
                #3)backtracking
                parziale.pop()

    def stampa_quadrato(self,soluzione):
        print("---------------")
        for riga in range(self.N):
            print(soluzione[riga*self.N:(riga+1)*self.N])

    def _parziale_is_valido(self,parziale):
        numero_magico = self.N * (self.N * self.N + 1)/2
        n_righe_compleatate = len(parziale)//self.N
        # 1)verifico la riga, return False
        for indice_riga in range (n_righe_compleatate):
            riga = parziale[indice_riga*self.N:(indice_riga+1)*self.N]
            if sum(riga) != numero_magico:
                return False
        # 2)verifico la colonna, re False
        n_col_comp = max(len(parziale)-self.N*(self.N-1),0)
        for indice_col in range (n_col_comp):
            col = parziale[indice_col: (self.N-1)*self.N + indice_col +1 :self.N]
            if sum(col) != numero_magico:
                return False
        # 3)verifico diag 1
        #diag1 = pot_soluzione[0:self.N**2+1:self.N+1]
        #if sum(diag1) != numero_magico:
         #   return False
        # 4)verifico diag 2
        #somma = 0
        #for indice in range(self.N):
          #  somma += pot_soluzione[indice*self.N + (self.N-1)-indice]
        #if somma != numero_magico:
           # return False
        # 5)controlli passati
        return True

    def _is_valido(self,pot_soluzione):
        numero_magico = self.N * (self.N * self.N + 1)/2
        # 1)verifico la riga, return False
        for indice_riga in range (self.N):
            riga = pot_soluzione[indice_riga*self.N:(indice_riga+1)*self.N]
            if sum(riga) != numero_magico:
                return False
        # 2)verifico la colonna, re False
        for indice_col in range (self.N):
            col = pot_soluzione[indice_col: (self.N-1)*self.N + indice_col +1 :self.N]
            if sum(col) != numero_magico:
                return False
        # 3)verifico diag 1
        diag1 = pot_soluzione[0:self.N**2+1:self.N+1]
        if sum(diag1) != numero_magico:
            return False
        # 4)verifico diag 2
        somma = 0
        for indice in range(self.N):
            somma += pot_soluzione[indice*self.N + (self.N-1)-indice]
        if somma != numero_magico:
            return False
        # 5)controlli passati
        return True

if __name__ == '__main__':
    qm = QuadratoMagico(3)
    qm.risolvi_quadrato()
    print(f"Chiamate eff {qm.n_chiamate}")
    print(f"Soluzione {qm.n_soluzioni}")
    for sol in qm.soluzioni:
        qm.stampa_quadrato(sol)