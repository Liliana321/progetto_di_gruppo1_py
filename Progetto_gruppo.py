#Esercizio di gruppo

#dati esercizio 
utenti_registrati=[]
concerti_registrati=[]  #N.B max 3
prenotazioni=[]

# costanti 
max_concerti=3
sala=10
password_giusta="GHIBLI"

#definizione funzione per la registrazione degli utenti 

def registrazione_nome():
    name=input("inserisci nome:")
    password=input("inserisci password:")
    utenti_registrati.append({'name':name,'password':password})
    print(f"utente {name}  Registrazione effettuata con successo")
    


registrazione_nome()

print(utenti_registrati)

#per effettuare un numero di registrazioni 
# contatore=0
# while contatore<5:
#     registrazione_nome() 
    
# Lista di dizionari con utenti e password
utenti_registrati = [{'name': 'Liliana', 'password': 'ciao'}]

# Funzione per il login
def login(name, password):
    for utente in utenti_registrati:
        # Controlla se nome e password corrispondono
        if utente['name'] == name and utente['password'] == password:
            print("1. Prenotare posti")
            print("2. Creare concerti")
            scelta=int(input("Scegli tra le due opzioni (1/2):"))
            match scelta:
                case 1:
                    print("prenotazione effettuata")
                case 2:
                    password=input("inserisci password")
                    if password==password_giusta:
                        print("concerto creato")
                    else:
                        print("Password sbagliata. Riprovare")
                case _:
                    print("Scelta non valida")
    
            return True  # Login riuscito
    print("error password o nome utente")
    return False  # Login fallito

# Esempio di login
login("Liliana", "ciao")



