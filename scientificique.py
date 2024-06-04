import customtkinter as Ctk

def button_clik(numero):
    current= entry.get()
    entry.delete(0, Ctk.END)
    entry.insert(Ctk.END, current + str(numero))


def button_clear():
    entry.set("")

def button_equal():
    try:
        result=eval(entry.get())
        entry.set(str(result))
        
    except:
        entry.set("error")

# la creation  de la fenetre 
window= Ctk.CTk()
window.title("scientifque" )

# la creation de champs de saisir

entry=Ctk.CTkEntry(window,font=("helvetica",16))
entry.grid(row=0, column=0 ,columnspan=4 ,padx= 100,pady=10)

# la creation des buttons numerique 
button1=Ctk.CTkButton(window, text="7" , command=lambda:button_clik(7),width=50)
button2=Ctk.CTkButton(window, text="8" , command=lambda:button_clik(8),width=50)
button3=Ctk.CTkButton(window, text="9" , command=lambda:button_clik(9),width=50)
button4=Ctk.CTkButton(window, text="4" , command=lambda:button_clik(4),width=50)
button5=Ctk.CTkButton(window, text="5" , command=lambda:button_clik(5),width=50)
button6=Ctk.CTkButton(window, text="6" , command=lambda:button_clik(6),width=50)
button7=Ctk.CTkButton(window, text="1" , command=lambda:button_clik(1),width=50)
button8=Ctk.CTkButton(window, text="2" , command=lambda:button_clik(2),width=50)
button9=Ctk.CTkButton(window, text="3" , command=lambda:button_clik(3),width=50)
button0=Ctk.CTkButton(window, text="0" , command=lambda:button_clik(0),width=50)
#button1=Ctk.CButton(window, text="1" , command=lambda:button_clik(1))

# la creation des operations
button_add=Ctk.CTkButton(window, text="+" , command=lambda:button_clik("+"),width=50)
button_subtract=Ctk.CTkButton(window, text="-",command=lambda:button_clik("-"),width=50)
button_multiplication=Ctk.CTkButton(window, text="x" , command=lambda:button_clik("x"),width=50)
button_divide=Ctk.CTkButton(window, text="/" , command=lambda:button_clik("/"),width=50)
button_equal=Ctk.CTkButton(window, text="=" , command=lambda:button_clik("="),width=50)
button_clear=Ctk.CTkButton(window, text="sup" , command = lambda:button_clear("sup"),width=50)


button_Log=Ctk.CTkButton(window, text="Log" , command=lambda:button_clik("log"),width=50)
button_Poly=Ctk.CTkButton(window, text="Poly",command=lambda:button_clik("Poly"),width=50)
button_Cos=Ctk.CTkButton(window, text="Cos" , command=lambda:button_clik("cos"),width=50)
button_Tang=Ctk.CTkButton(window, text="Tang" , command=lambda:button_clik("tang"),width=50)


button_X=Ctk.CTkButton(window, text="x" , command=lambda:button_clik("X"),width=50)
button_Sin=Ctk.CTkButton(window, text="Sin",command=lambda:button_clik("Sin"),width=50)
button_Eng=Ctk.CTkButton(window, text="Eng" , command=lambda:button_clik("Eng"),width=50)
button_M=Ctk.CTkButton(window, text="M" , command=lambda:button_clik("M"),width=50)


# placement des buttons dans la grille 


button1.grid(row=1,column =0 , padx=5 , pady=5)
button2.grid(row=1,column =1 , padx=5 , pady=5)
button3.grid(row=1,column =2 , padx=5 , pady=5)

button4.grid(row=2,column =0 , padx=5 , pady=5)
button5.grid(row=2,column =1 , padx=5 , pady=5)
button6.grid(row=2,column =2 , padx=5 , pady=5)

button7.grid(row=3,column =0 , padx=5 , pady=5)
button8.grid(row=3,column =1 , padx=5 , pady=5)
button9.grid(row=3,column =2 , padx=5 , pady=5)

button0.grid(row=4,column =0 , padx=5 , pady=5)

button_add.grid(row=1,column =3 , padx=5 , pady=5)
button_subtract.grid(row=2,column =3 , padx=5 , pady=5)
button_multiplication.grid(row=3,column =3 , padx=5 , pady=5)

button_divide.grid(row=4,column =3 , padx=5 , pady=5)
button_equal.grid(row=4,column =2 , padx=5 , pady=5)
button_clear.grid(row=4,column =1, padx=5 , pady=5)

button_Log.grid(row=5,column =0 , padx=5 , pady=5)
button_Poly.grid(row=5,column =3 , padx=5 , pady=5)
button_Cos.grid(row=5,column =2, padx=5 , pady=5)
button_Tang.grid(row=5,column =1, padx=5 , pady=5)

button_X.grid(row=6,column =0 , padx=5 , pady=5)
button_Sin.grid(row=6,column =3 , padx=5 , pady=5)
button_Eng.grid(row=6,column =2, padx=5 , pady=5)
button_M.grid(row=6,column =1, padx=5 , pady=5)




# lancement de la boucle 
window.mainloop()



