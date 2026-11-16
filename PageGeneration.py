import customtkinter as ctk
import tkinter as tk
class PageGeneration(ctk.CTkFrame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.bouton_var = tk.StringVar(value="Aucun")
        self.create_widgets()

    def create_widgets(self):
        #Titre de la page
        self.titre = ctk.CTkLabel(self, text = "Générateur de playlist", fg_color="transparent", font=("Arial", 30))
        self.grid_columnconfigure(0,weight= 0)
        self.grid_columnconfigure(1,weight=1)
        self.titre.grid(row = 0, column=0, padx=20, pady=(20,10), sticky="nsew")
        #Inititalisation et placement de Entry nb chansons
        self.entry_nb_chansons = ctk.CTkEntry(self, placeholder_text="Entrez le nombre de chansons de la playlist")
        self.entry_nb_chansons.grid(row=1,column=0,padx=20,pady=10, sticky = "nsw")

        #Initialisation des 3 Radio Buttons
        self.date_rb= ctk.CTkRadioButton(self,text="Filtrer selon une date", variable = self.bouton_var, value="Date")
        self.artiste_rb = ctk.CTkRadioButton(self,text="Filtrer selon un artiste", variable =self.bouton_var, value="Artiste")
        self.moment_rb = ctk.CTkRadioButton(self,text= "Filtrer selon le moment de la journée", variable=self.bouton_var,value="Moment")
        #Placement
        self.date_rb.grid(row=2,column=0,padx=20,pady=10,sticky="nsw")
        self.artiste_rb.grid(row=3,column=0,padx=20,pady=10,sticky="nsw")
        self.moment_rb.grid(row=4,column=0,padx=20,pady=10,sticky="nsw")

        #Initialisation entry date et artiste
        self.entry_date = ctk.CTkEntry(self, placeholder_text="Entrez la date")
        self.entry_artiste = ctk.CTkEntry(self, placeholder_text="Entrez le nombre de l'artiste")
        #Placement
        self.entry_date.grid(row = 2,column=1,pady=10,sticky="nsw")
        self.entry_artiste.grid(row = 3,column=1,pady=10,sticky="nsw")


