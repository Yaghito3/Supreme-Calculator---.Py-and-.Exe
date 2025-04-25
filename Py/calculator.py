import tkinter as tk
from tkinter import Toplevel
import math

# Dizionario delle traduzioni
traduzioni = {
    "it": {
        "title": "Supreme Calculator 1.0",
        "info": "Info",
        "settings": "Impostazioni",
        "readme": "Leggi il ReadMe",
        "close": "Chiudi",
        "welcome": "Benvenuto nella Supreme Calculator 1.0!",
        "error": "Errore",
        "select_language": "Seleziona la lingua:"
    },
    "en": {
        "title": "Supreme Calculator 1.0",
        "info": "Info",
        "settings": "Settings",
        "readme": "Read the ReadMe",
        "close": "Close",
        "welcome": "Welcome to Supreme Calculator 1.0!",
        "error": "Error",
        "select_language": "Select the language:"
    },
    "de": {
        "title": "Supreme Calculator 1.0",
        "info": "Info",
        "settings": "Einstellungen",
        "readme": "Lies das ReadMe",
        "close": "Schließen",
        "welcome": "Willkommen beim Supreme Calculator 1.0!",
        "error": "Fehler",
        "select_language": "Sprache auswählen:"
    }
}

# Lingua corrente
lingua_corrente = "en"

# Funzione per aggiungere testo allo schermino
def scrivi_schermino(testo):
    if testo == ',':
        testo = '.'
    schermino.insert(tk.END, testo)

# Funzione per calcolare il risultato dell'espressione
def calcola_risultato():
    try:
        espressione = schermino.get().replace('X', '*').replace(':', '/')
        risultato = eval(espressione)
        schermino.delete(0, tk.END)
        schermino.insert(0, str(risultato))
    except Exception:
        schermino.delete(0, tk.END)
        schermino.insert(0, traduzioni[lingua_corrente]["error"])

# Funzione per calcolare la radice quadrata
def calcola_radice():
    try:
        valore = float(schermino.get())
        risultato = math.sqrt(valore)
        schermino.delete(0, tk.END)
        schermino.insert(0, str(risultato))
    except ValueError:
        schermino.delete(0, tk.END)
        schermino.insert(0, traduzioni[lingua_corrente]["error"])

# Funzione per cambiare lingua
def cambia_lingua(lingua):
    global lingua_corrente
    lingua_corrente = lingua
    aggiorna_testi()

# Funzione per aggiornare i testi
def aggiorna_testi():
    root.title(traduzioni[lingua_corrente]["title"])
    btn_info.config(text=traduzioni[lingua_corrente]["info"])
    btn_settings.config(text=traduzioni[lingua_corrente]["settings"])

# Funzione per aprire la finestra "Impostazioni"
def apri_impostazioni():
    settings_window = Toplevel(root)
    settings_window.title(traduzioni[lingua_corrente]["settings"])
    settings_window.geometry("400x300")
    settings_window.configure(bg="#2c3e50")
    
    label_settings = tk.Label(
        settings_window, 
        text=traduzioni[lingua_corrente]["select_language"],
        font=("Arial", 14),
        bg="#2c3e50",
        fg="#ecf0f1"
    )
    label_settings.pack(pady=20)
    
    btn_italiano = tk.Button(
        settings_window, 
        text="Italiano", 
        command=lambda: cambia_lingua("it"), 
        font=("Arial", 12),
        bg="#3498db",
        fg="white",
        activebackground="#2980b9",
        activeforeground="white"
    )
    btn_italiano.pack(pady=5)
    
    btn_inglese = tk.Button(
        settings_window, 
        text="English", 
        command=lambda: cambia_lingua("en"), 
        font=("Arial", 12),
        bg="#3498db",
        fg="white",
        activebackground="#2980b9",
        activeforeground="white"
    )
    btn_inglese.pack(pady=5)
    
    btn_tedesco = tk.Button(
        settings_window, 
        text="Deutsch", 
        command=lambda: cambia_lingua("de"), 
        font=("Arial", 12),
        bg="#3498db",
        fg="white",
        activebackground="#2980b9",
        activeforeground="white"
    )
    btn_tedesco.pack(pady=5)

# Funzione per aprire la finestra "Info"
def mostra_info():
    info_window = Toplevel(root)
    info_window.title(traduzioni[lingua_corrente]["info"])
    info_window.geometry("400x200")
    info_window.configure(bg="#2c3e50")
    
    label_info = tk.Label(
        info_window, 
        text=traduzioni[lingua_corrente]["welcome"],
        font=("Arial", 14),
        bg="#2c3e50",
        fg="#ecf0f1",
        wraplength=380,
        justify="center"
    )
    label_info.pack(pady=20)
    
    btn_close = tk.Button(
        info_window, 
        text=traduzioni[lingua_corrente]["close"], 
        command=info_window.destroy, 
        font=("Arial", 12),
        bg="#e74c3c",
        fg="white",
        activebackground="#c0392b",
        activeforeground="white"
    )
    btn_close.pack(pady=10)

# Creazione della finestra principale
root = tk.Tk()
root.title(traduzioni[lingua_corrente]["title"])
root.geometry("400x600")
root.minsize(400, 600)
root.configure(bg="#34495e")

# Contenitore per i bottoni Info e Impostazioni
top_frame = tk.Frame(root, bg="#34495e")
top_frame.pack(fill="x")

# Bottone Info
btn_info = tk.Button(
    top_frame, 
    text=traduzioni[lingua_corrente]["info"], 
    command=mostra_info, 
    font=("Arial", 12, "bold"),
    bg="#3498db",
    fg="white",
    activebackground="#2980b9",
    activeforeground="white"
)
btn_info.pack(side="left", fill="x", expand=True, padx=5, pady=5)

# Bottone Impostazioni
btn_settings = tk.Button(
    top_frame, 
    text=traduzioni[lingua_corrente]["settings"], 
    command=apri_impostazioni, 
    font=("Arial", 12, "bold"),
    bg="#3498db",
    fg="white",
    activebackground="#2980b9",
    activeforeground="white"
)
btn_settings.pack(side="left", fill="x", expand=True, padx=5, pady=5)

# Schermino (campo di input)
schermino = tk.Entry(root, font=("Arial", 18), justify="right", bg="#ecf0f1", fg="#2c3e50")
schermino.pack(fill="x", padx=10, pady=10)

# Creazione dei tasti numerici e operazioni
tasti = [
    ('7', '8', '9', 'X'),
    ('4', '5', '6', '-'),
    ('1', '2', '3', '+'),
    ('%', '0', '=', 'C'),
    ('√', ':', ',', '')
]

for riga in tasti:
    frame = tk.Frame(root, bg="#34495e")
    frame.pack(pady=5)
    for tasto in riga:
        if tasto == 'C':
            btn = tk.Button(frame, text=tasto, font=("Arial", 14), command=lambda: schermino.delete(0, tk.END), bg="#e74c3c", fg="white")
        elif tasto == '=':
            btn = tk.Button(frame, text=tasto, font=("Arial", 14), command=calcola_risultato, bg="#4e9a06", fg="white")
        elif tasto == '√':
            btn = tk.Button(frame, text=tasto, font=("Arial", 14), command=calcola_radice, bg="#3498db", fg="white")
        elif tasto:
            btn = tk.Button(frame, text=tasto, font=("Arial", 14), command=lambda t=tasto: scrivi_schermino(t), bg="#3498db", fg="white")
        else:
            btn = tk.Label(frame, text="", bg="#34495e", width=5)  # Placeholder for empty buttons
        btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)

root.mainloop()