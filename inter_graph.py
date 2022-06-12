from tkinter import *
import webbrowser

def open_projet ():
    webbrowser.open_new("https://github.com/Rostandsuffo/DevOps.git")

#creer une premiere fenetre

window = Tk()

#personnalise cette fenetre
window.title("Projet VLSM")
window.geometry("1080x720")
window.minsize(500 , 400)
window.config(background="#41B77F")

#creer la frame
frame =Frame(window, bg="#41B77F")


#Ajouterun premier texte
label_title = Label(frame , text="Bienvenu sur le projet VLSM" , font= ("courrier" , 40), bg="#41B77F", fg="white")
label_title.pack()

#ajouter un second text
label_subtitle = Label(frame , text="Realisé par Rostand Joel" , font= ("courrier" , 20), bg="#41B77F", fg="white")
label_subtitle.pack()

#Ajouter un premier bouton
yt_button= Button(frame, text= "ouvrir le menu ", font= ("courrier" , 20), bg="white", fg="#41B77F", command= open_projet)
yt_button.pack(pady=25, fill=X)


#ajouter
frame.pack(expand=YES)


#afficher

window.mainloop()
