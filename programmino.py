# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Inizializzo la variabile per la somma
somma = 0

# Ciclo infinito finché l'utente non inserisce 0
while True:
    # Chiedo all'utente di inserire un numero
    numero = int(input("Inserisci un numero intero (0 per terminare): "))
    
    # Se l'utente inserisce 0, esco dal ciclo
    if numero == 0:
        break
    
    # Aggiungo il numero alla somma
    somma += numero

# Stampo la somma finale
print("La somma dei numeri inseriti è:", somma)
