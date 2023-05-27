import tkinter
import pickle
from pickle import load
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import sklearn
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate , Paragraph,Frame,PageTemplate
from reportlab.lib.pagesizes import A4, letter , landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table ,TableStyle
from PIL import Image, ImageTk

 
 
ventana = tkinter.Tk()
ventana.title("Detección de fraude con tarjetas de crédito")
ventana.iconbitmap('descarga.ico')
ventana.config(bg="lightblue")
imagen = Image.open("descarga (1).jpeg")
imagen_tk = ImageTk.PhotoImage(imagen)
ventana.title("Fraude Con Tarjetas de Credito")

#Mensaje Edad
def paso_message():
    messagebox.showinfo("Mensaje", "Ingresa el paso(Horas)")
#Mensaje Paso
def tipo_message():
    messagebox.showinfo("Mensaje", "Ingrese el tipo de  Pago  0= Pago, 1=Transferencia, 2=Retiro en Efectivo 3=Débito, 4=Dinero en Efectivo")
#Mensaje tipo 
def Cantidad_message():
    messagebox.showinfo("Mensaje", "Ingrese la Cantidad")
#Mensaje Cantidad
def Antiguo_Saldo_message():
    messagebox.showinfo("Mensaje", "Ingrese el Antiguo Saldo")
#Mensaje Antiguo Saldo
def Nuevo_Saldo_message():
    messagebox.showinfo("Mensaje", "Ingrese el  Nuevo Saldo")
#Mensaje Nuevo Saldo
def Antiguo_Saldo_Destino_message():
    messagebox.showinfo("Mensaje", "Ingrese el Antiguo Saldo Destino")
#Mensaje ID Saldo Destino
def Nuevo_Saldo_Destino_message():
    messagebox.showinfo("Mensaje", "Ingrese el Nuevo Saldo Destino")
#Mensaje Nuevo Saldo destino

frame = tkinter.Frame(ventana)
frame.config(bg="lightblue")
label = ttk.Label( image=imagen_tk)
label.pack()
frame.pack()


info_Detección_fraude_frame = tkinter.LabelFrame(frame, text="Detección de fraude con tarjetas de crédito")
info_Detección_fraude_frame.grid(row=0, column=0 ,padx=10, pady=10)
info_Detección_fraude_frame.config(bg="lightblue")

info_Detección_fraude_frame= tkinter.LabelFrame(frame, text="Detección de fraude con tarjetas de crédito")
info_Detección_fraude_frame.grid(row=0, column=0 ,padx=10, pady=10)
info_Detección_fraude_frame.config(bg="lightblue")


Paso_Detección_fraude_label=tkinter.Label(info_Detección_fraude_frame ,text="Paso")
Paso_Detección_fraude_label.place(x=2, y=1)
Paso_Detección_fraude_label.config(bg="lightblue")
Paso_Detección_fraude_entry = ttk.Entry(info_Detección_fraude_frame)
Paso_Detección_fraude_entry.grid(row=1 , column=1)
Paso_Detección_fraude_entry.bind("<Button-1>", lambda e: paso_message())


Tipo_Detección_fraude_label=tkinter.Label(info_Detección_fraude_frame,text="Tipo")
Tipo_Detección_fraude_label.grid(row=2, column=0 , sticky="w")
Tipo_Detección_fraude_label.config(bg="lightblue")
Tipo_Detección_fraude_combobox= ttk.Combobox(info_Detección_fraude_frame,values=[0,1,2,3] , width="17")
Tipo_Detección_fraude_combobox.grid(row=2, column=1)
Tipo_Detección_fraude_combobox.bind("<Button-1>", lambda e: tipo_message())


Cantidad_Detección_fraude_label=tkinter.Label(info_Detección_fraude_frame,text="Cantidad")
Cantidad_Detección_fraude_label.grid(row=3, column=0, sticky="w")
Cantidad_Detección_fraude_label.config(bg="lightblue")
Cantidad_Detección_fraude_entry = ttk.Entry(info_Detección_fraude_frame)
Cantidad_Detección_fraude_entry.grid(row=3 , column=1)
Cantidad_Detección_fraude_entry.bind("<Button-1>", lambda e: Cantidad_message())

Antiguo_Balance_Origen_fraude_label=tkinter.Label(info_Detección_fraude_frame,text="Antiguo Balance Origen")
Antiguo_Balance_Origen_fraude_label.grid(row=4, column=0, sticky="w")
Antiguo_Balance_Origen_fraude_label.config(bg="lightblue")
Antiguo_Balance_Origen_fraude_entry = ttk.Entry(info_Detección_fraude_frame)
Antiguo_Balance_Origen_fraude_entry.grid(row=4, column=1)
Antiguo_Balance_Origen_fraude_entry.bind("<Button-1>", lambda e: Antiguo_Saldo_message())

Nuevo_Balance_Origen_fraude_label=tkinter.Label(info_Detección_fraude_frame,text="Nuevo Balance Origen")
Nuevo_Balance_Origen_fraude_label.grid(row=5, column=0, sticky="w")
Nuevo_Balance_Origen_fraude_label.config(bg="lightblue")
Nuevo_Balance_Origen_fraude_entry = ttk.Entry(info_Detección_fraude_frame)
Nuevo_Balance_Origen_fraude_entry.grid(row=5 , column=1)
Nuevo_Balance_Origen_fraude_entry.bind("<Button-1>", lambda e: Nuevo_Saldo_message())

Antiguo_Saldo_Destino_Detección_fraude_label=tkinter.Label(info_Detección_fraude_frame,text="Antiguo Saldo Destino")
Antiguo_Saldo_Destino_Detección_fraude_label.grid(row=6, column=0, sticky="w")
Antiguo_Saldo_Destino_Detección_fraude_label.config(bg="lightblue")
Antiguo_Saldo_Destino_Detección_fraude_entry = ttk.Entry(info_Detección_fraude_frame)
Antiguo_Saldo_Destino_Detección_fraude_entry.grid(row=6, column=1)
Antiguo_Saldo_Destino_Detección_fraude_entry.bind("<Button-1>", lambda e: Antiguo_Saldo_Destino_message())
    
Nuevo_Saldo_Destino_Detección_fraude_label=tkinter.Label(info_Detección_fraude_frame,text="Nuevo Saldo Destino")
Nuevo_Saldo_Destino_Detección_fraude_label.grid(row=7, column=0, sticky="w")
Nuevo_Saldo_Destino_Detección_fraude_label.config(bg="lightblue")
Nuevo_Saldo_Destino_Detección_fraude_entry = ttk.Entry(info_Detección_fraude_frame)
Nuevo_Saldo_Destino_Detección_fraude_entry.grid(row=7 , column=1)
Nuevo_Saldo_Destino_Detección_fraude_entry.bind("<Button-1>", lambda e: Nuevo_Saldo_Destino_message())
      
Respuesta_label=tkinter.Label(info_Detección_fraude_frame,text="Respuesta")
Respuesta_label.grid(row=13 , column=0, sticky="w")
Respuesta_label.config(bg="lightblue")


modelo_cargado=pickle.load(open('Modelo Random DT.sav','rb'))



def usar_modelo():
    Target=np.ones((1, 7))
    if not Paso_Detección_fraude_entry.get():
         messagebox.showwarning("Advertencia", "Por favor, ingresa el paso.")
    else:
         Target[0,0]=int(Paso_Detección_fraude_entry.get()) #Paso 
    if not Tipo_Detección_fraude_combobox.get():
         messagebox.showwarning("Advertencia", "Por favor, ingresa el tipo de  Pago  0= Pago, 1=Transferencia, 2=Retiro en Efectivo 3=Débito, 4=Dinero en Efectivo.")
    else:
         Target[0,1]=int(Tipo_Detección_fraude_combobox.get()) #Tipo

    if not Cantidad_Detección_fraude_entry.get():
        messagebox.showwarning("Advertencia", "Por favor, Ingresa la Cantidad.")
    else:
      Target[0,2]=int(Cantidad_Detección_fraude_entry.get()) #Cantidad
 
    if not Antiguo_Balance_Origen_fraude_entry.get():
        messagebox.showwarning("Advertencia", "Por favor, Ingresa el Antiguo Balance")
    else:
       Target[0,3]=int(Antiguo_Balance_Origen_fraude_entry.get()) #Antiguo Balance
    if not Nuevo_Balance_Origen_fraude_entry.get():
       messagebox.showwarning("Advertencia", "Por favor, Ingresa el Nuevo Balance")
    else:       
        Target[0,4]=int(Nuevo_Balance_Origen_fraude_entry.get()) #Nuevo Balance
        
    if not Antiguo_Saldo_Destino_Detección_fraude_entry.get():
       messagebox.showwarning("Advertencia", "Por favor, Ingresa el ID del Saldo Destino")
    else:           
        Target[0,5]=int(Antiguo_Saldo_Destino_Detección_fraude_entry.get()) #fbs

    if not Nuevo_Saldo_Destino_Detección_fraude_entry.get():
         messagebox.showwarning("Advertencia", "Por favor, Ingrese el Nuevo Saldo Destino")
    else:
        Target[0,6]=int(Nuevo_Saldo_Destino_Detección_fraude_entry.get()) #Restecg
    if modelo_cargado.predict (Target)==0:
        Respuesta_label= tkinter.Label(info_Detección_fraude_frame, text="Respuesta: Transacción Segura")
        Respuesta_label.grid(row=13 , column=0, sticky="w")
        Respuesta_label.config(bg="lightblue")
        res=" Transacción Segura "
    else:
       Respuesta_label= tkinter.Label(info_Detección_fraude_frame, text="Respuesta: !ALERTA! Victima de Fraude ")
       Respuesta_label.grid(row=13 , column=0, sticky="w")
       Respuesta_label.config(bg="lightblue")
       res=" !ALERTA! Victima de Fraude "
    return Target,res


def export_pdf():
    resultado=usar_modelo()
    Target=resultado[0]
    res=resultado[1]


    # Crear un nuevo archivo PDF
    pdf = SimpleDocTemplate("informe.pdf", pagesize=A4)
           
    header = PageTemplate(id='header', frames=Frame(pdf.leftMargin, pdf.height + pdf.topMargin - 50, pdf.width, 50))
    pdf.addPageTemplates(header)
    pdf.build([Paragraph("Contenido del documento", getSampleStyleSheet()['Normal'])])

    

    #logo
    #image_file = "logo.jpg"
    #image = Image(image_file)

    #Titulo
    #List=["Edad","sexo","cp","trtbps","chol","fbs","Restecg","thalach","Exng", "oldpeak", "slp","Caa","thall"]

    #nombres_data = [list(row) for row in List]
    #nombre = Table(nombres_data)
    # Crear la tabla con los datos
    table_data = [list(row) for row in Target]
    table = Table(table_data)


 

    # Agregar la tabla al archivo PDF
   
    pdf_table = []
    #pdf_table.append(nombre)
    pdf_table.append(table)
    style = getSampleStyleSheet()["Normal"]
    paragraph = Paragraph(res, style)
    pdf_table.append(paragraph)
    pdf.build(pdf_table)
 
buttonModel=tkinter.Button(ventana,text='Predecir',command=usar_modelo,fg="black")
buttonModel.pack()

buttonExportar=tkinter.Button(ventana,text='Exportar',command=export_pdf,fg="black")
buttonExportar.pack()
ventana.mainloop()
