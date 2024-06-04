import customtkinter

# customtkinter.set_default_color_theme ("dark-blue")
customtkinter.set_appearance_mode("dark")

app= customtkinter.CTk()
app.title("my app")
app.geometry("400x150")

#la creation d'un button 
text =customtkinter.CTkTextbox(app,width=800,height=80)
text.grid(row=0,column=0, pady=20)

button=customtkinter.CTkButton(app, text="1" ,width=50 )
#button=customtkinter.CTkButton(root_tk,fg_color ="red")
button.grid(row=1 ,column=0, padx=10 ,pady=10 )

button=customtkinter.CTkButton(app, text="2",width=50 )
button.grid(row=1 ,column=1, padx=10 ,pady=10 )

button=customtkinter.CTkButton(app, text="3", width=50 )
button.grid(row=1 ,column=2, padx=10 ,pady=10 )

button=customtkinter.CTkButton(app, text="x",width=50 )
button.grid(row=1 ,column=3, padx=10 ,pady=10 )


button=customtkinter.CTkButton(app, text="4", width=50 )
button.grid(row=2 ,column=0, padx=20 ,pady=20 )

button=customtkinter.CTkButton(app, text="5", width=50 )
button.grid(row=2 ,column=1, padx=20 ,pady=20 )

button=customtkinter.CTkButton(app, text="6", width=50 )
button.grid(row=2 ,column=2, padx=10 ,pady=15 )

button=customtkinter.CTkButton(app, text="-", width=50 )
button.grid(row=2 ,column=3, padx=15 ,pady=15) 



button=customtkinter.CTkButton(app, text="7", width=50 )
button.grid(row=3 ,column=0, padx=20 ,pady=20 )

button=customtkinter.CTkButton(app, text="8", width=50 )
button.grid(row=3 ,column=1, padx=20 ,pady=20 )

button=customtkinter.CTkButton(app, text="9" ,width=50 )
button.grid(row=3 ,column=2, padx=20 ,pady=20 )

button=customtkinter.CTkButton(app, text="+",width=50 )
button.grid(row=3 ,column=3, padx=15,pady=15 )

button=customtkinter.CTkButton(app, text="0" ,width=50 )
button.grid(row=4 ,column=0, padx=20 ,pady=20 )



button=customtkinter.CTkButton(app, text="off",width=50 )
button.grid(row=4 ,column=1, padx=10,pady=10 )

button= customtkinter.CTkButton(app, text="on ",width=50 )
button.grid(row=4 ,column=2, padx=15 ,pady=15 )

button=customtkinter.CTkButton(app, text="/",width=50 )
button.grid(row=4 ,column=3, padx=5 ,pady=5 )

app.mainloop()
                 
                 