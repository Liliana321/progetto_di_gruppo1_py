#Esercizio di gruppo

#dati esercizio e costanti
utenti_registrati=[]
concerti_registrati= 0
prenotazioni_sala = 0
password_giusta="GHIBLI"

#definizione funzione per la registrazione degli utenti 

def registrazione_nome():
    print("Registrazione nuovo utente.")
    name=input("inserisci nome: ")
    password=input("inserisci password: ")
    utenti_registrati.append(name)
    utenti_registrati.append(password)
    print(f"Utente {name, password}. Registrazione effettuata con successo")

registrazione_nome()
print("Adesso effettua l'accesso.")

# Funzione per il login
def login():
    global prenotazioni_sala, concerti_registrati 
    name=input("inserisci nome: ")
    password=input("inserisci password: ")
# Controlla se nome e password corrispondono
    if name and password in utenti_registrati:
        scelta=int(input("Scegli tra le due opzioni (1/2):"))
        print("1. Prenotare posti")
        print("2. Creare concerti")
            
        match scelta:
            case 1:
                print("Prenotazione effettuata con successo.")
            case 2:
                password=input("Inserisci password: ")
                if password==password_giusta:
                      print("Concerto creato!")
                else:
                        print("Password sbagliata. Riprovare.")
            case _:
                print("Scelta non valida.")
    else:
        print("Utente non registrato.")
        
login()


