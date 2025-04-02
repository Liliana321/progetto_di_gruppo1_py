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

#print(utenti_registrati)

#per effettuare un numero di registrazioni 
# contatore=0
# while contatore<5:
#     registrazione_nome() 
    
# Lista di dizionari con utenti e password
#utenti_registrati = [{'name': 'Liliana', 'password': 'ciao'}]

# Funzione per il login
def login():
    print("Effettuare il login")
    name=input("inserisci nome:")
    password=input("inserisci password:")
    for utente in utenti_registrati:
        # Controlla se nome e password corrispondono
        if name and password in utenti_registrati:
            print("1. Prenotare posti")
            print("2. Creare concerti")
            scelta=int(input("Scegli tra le due opzioni (1/2):"))
            return True  # Login riuscito
    print("error password o nome utente")
    return False  # Login fallito

login()

#funzione per la prenotazione concerti   

def aggiungi_concerto():
    nome_concerto=input("inserisci nome concerto")
    password=input("inserisci password")
    if password != password_giusta:
        print("Password segreta errata.")
        return
    if len(concerti_registrati) >= max_concerti:
        print("Numero massimo di concerti raggiunto")
        return
    concerti_registrati.append({'nome': nome_concerto})
    print(f"Concerto '{nome_concerto}' aggiunto.")
   
   
#funzione per la prenotazione dei posti e la scelta del concerto  
def prenota_posto():
    if not concerti_registrati:
        print("Nessun concerto disponibile.")
        return
    print(concerti_registrati)
    print("Concerti disponibili:")
    
    scelta = int(input("Seleziona il numero del concerto: "))
    match scelta:
        case 1:
            print(f"Prenotazione effettuata per: {concerti_registrati[0]['nome']}")
        case 2:
            print(f"Prenotazione effettuata per: {concerti_registrati[1]['nome']}")
        case 3:
            print(f"Prenotazione effettuata per: {concerti_registrati[2]['nome']}")

#aggiungi_concerto()

#esempio 

registrazione_nome()
login()
if login()==True:
    print("1. Prenotare posti")
    print("2. Creare concerti")
    scelta=input("inserisci una scelta (1/2):")
    match scelta:
                    case 1:
                        prenota_posto()
                    case 2:
                        aggiungi_concerto()
                    case _:
                        print("Scelta non valida")



