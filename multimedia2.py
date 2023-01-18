import webbrowser as wb
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import pyautogui
import subprocess
import requests
import pygame
import vlc
import os

# URL's de las paginas web de servicios de streaming
urlN  = 'https://www.netflix.com/mx/'
urlA  = 'https://www.primevideo.com/'
urlD  = 'https://www.disneyplus.com/es-mx'
urlS  = 'https://open.spotify.com/'
urlH  = 'https://www.hbomax.com/mx/es'
urlDy = 'https://www.youtube.com/'

#Definicion del color de fondo
colorFondo="#061848"

# Creación de ventana principal
window = tk.Tk()
window.config(bg=colorFondo, cursor="circle")
# Pygame para reproducir musica
pygame.mixer.init()

# Largo y ancho de la ventana
width  = window.winfo_screenwidth()
height = window.winfo_screenheight()

# Creación de funciones para cada servicio de streaming
def funcion_Netflix():
    wb.open_new(urlN) #Abre la url que se le manda como parámetro
    window.after(500,pantCompleta) #la abre en pantalla completa

def funcion_Amazon():
    wb.open_new(urlA)
    window.after(500,pantCompleta)

def funcion_Disney():
    wb.open_new(urlD)
    window.after(500,pantCompleta)

def funcion_Spotify():
    wb.open_new(urlS)
    window.after(500,pantCompleta)

def funcion_HBO():
    wb.open_new(urlH)
    window.after(500,pantCompleta)

def funcion_Youtube():
    wb.open_new(urlDy)
    window.after(500,pantCompleta)    
    
def pantCompleta():
    pyautogui.press("F11") #se da clic en la tecla F11 del teclado 

def apagar():
    subprocess.call(['shutdown', "-h", "now"])

def cerrar():
    pygame.mixer.music.stop()
    pyautogui.keyDown("alt")
    pyautogui.press("F4")
    pyautogui.keyUp("alt")

def funcion_Salir():
    labelSalir = Label(window, text="Hasta pronto.",
             fg="#fff",    # Foreground
             bg=colorFondo,   # Background
             font=("Verdana Bold",60))
    labelSalir.place(relx=0, rely=0, relheight=1, relwidth=1)
    window.after(5000, apagar)

def reinicio():
    subprocess.run(["reboot"])

def conectarRed(ssid, key):
    global labelConfig
    arch = '/etc/wpa_supplicant/wpa_supplicant.conf'
    subprocess.call(['sudo', "chmod", "777", arch])
    
    with open(arch, 'w') as fp:
        fp.write('ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev')
    with open(arch, 'a') as fp:
        fp.write('\nupdate_config=1')
    with open(arch, 'a') as fp:
        fp.write('\ncountry=MX')
    with open(arch, 'a') as fp:
        fp.write('\nnetwork={ \n')
    with open(arch, 'a') as fp:
        fp.write('\tssid="{}" \n'.format(str(ssid)))
    with open(arch, 'a') as fp:
        fp.write('\tpsk="{}" \n'.format(str(key)))    
    with open(arch, 'a') as fp:
        fp.write('\tkey_mgmt=WPA-PSK')
    with open(arch, 'a') as fp:
        fp.write('\n}')
    labelConfig = Label(window, text="Aplicando configuración\nRequiere reiniciar",
                    fg="#fff", bg=colorFondo,font=("Verdana Bold",60))
    labelConfig.place(relx=0, rely=0, relwidth=1, relheight=1)
    window.after(4000, reinicio)

def configRed():
    labelTitulo = Label(window, text="Configuracion de Red",
             fg="#fff",    # Foreground
             bg=colorFondo,   # Background
             font=("Verdana Bold",60))
    labelTitulo.place(relx=0.3, rely=0.05)
    botonClose.place(relx=0.9, rely=0.9) # Posición del botón de cerrar

    # Llamado de cada botón
    botonNetflix.place_forget()
    botonAmazon.place_forget()
    botonDisney.place_forget()
    botonSpotify.place_forget()
    botonHBO.place_forget()
    botonYoutube.place_forget()
    botonConfig.place_forget()
    botonSalir.place_forget()
    botonUsb.place_forget()

    labelSSID = Label(window, text="SSID", 
                        fg="#fff",    # Foreground
                        bg=colorFondo,   # Background
                        font=("Verdana Bold",40))
    labelSSID.place(relx=0.25, rely=0.35) 

    
    entrySSID.place(relx=0.45, rely=0.35, relheight=0.05, relwidth=0.25)

    labelPWD = Label(window, text="PASSWORD", 
                        fg="#fff",    # Foreground
                        bg=colorFondo,   # Background
                        font=("Verdana Bold",40))
    labelPWD.place(relx=0.25, rely=0.55) 

    entryPWD.place(relx=0.45, rely=0.55, relheight=0.05, relwidth=0.25)

    botonConnect.pack()
    botonConnect.place(relx=0.4, rely=0.75, relheight=0.1, relwidth=0.2)

def funcion_Usb():
    # Llamado de cada botón
    botonNetflix.place_forget()
    botonAmazon.place_forget()
    botonDisney.place_forget()
    botonSpotify.place_forget()
    botonHBO.place_forget()
    botonYoutube.place_forget()
    botonConfig.place_forget()
    botonSalir.place_forget()
    botonUsb.place_forget()
    labelBienvenida.place_forget()
    botonConnect.place_forget()
    
    
    botonClose.place(relx=0.9, rely=0.9) # Posición del botón de cerrar
    botonMusica.pack   ()
    botonFotos.pack     ()
    botonVideo.pack       ()
    
    botonMusica.place      (relx=0.2,  rely=0.4)
    botonFotos.place  (relx=0.45, rely=0.4)
    botonVideo.place  (relx=0.7,  rely=0.4)

def funcion_Musica():
    musicPlayer = tk.Toplevel()
    musicPlayer.config(bg=colorFondo, cursor="circle") #Se define el color de la mini interfaz
    musicPlayer.geometry("%dx%d" % (width, height))

    labelMusica = Label(window, text="Reproductor Multimedia", #Se define el nombre de la ventana
                        fg="#fff",    # Foreground
                        bg=colorFondo,   # Background
                        font=("Verdana Bold",60))
    labelMusica.place(relx=0.3, rely=0.05) #Posición de la ventana

    botonClose = tk.Button(musicPlayer,  # Botón para cerrar 
                            text = "Volver",
                            command = musicPlayer.destroy,
                            bg="#000",  
                            borderwidth= 0.1,
                            fg="#fff",
                            cursor="X_cursor",
                            font=("Verdana Bold", 18))
    botonClose.place(relx=0.9, rely=0.9) # Posición del botón de cerrar
    musicPlayer.focus()
    musicPlayer.grab_set() # Función para que el usuario no pueda utilizar la ventana principal

    # Función para agregar canciones de la memoria USB
    def añadir():
        #se guardan todos los archivos de tipo .mp3 en la lista canciones
        canciones = filedialog.askopenfilenames(initialdir="/media/pi/USB/",title="Elige una canción",filetypes=(("mp3","*.mp3"),("allfiles","*.*")))
        #camiar la extension del nombre de la cancion for cancion in canciones:
        for cancion in canciones:
            cancion=cancion.replace("/media/pi/USB/","") #se cambia la direccion de la cancion para
            cancion=cancion.replace(".mp3","")  #que solo tenga el nombre y la exntension .mp3         
            pantalla.insert (END, cancion) #añadir cancion a la pantalla
            
        cancion= pantalla.get(ACTIVE)
        cancion=f'{cancion}.mp3'

        pygame.mixer.music.load(cancion) #cargar la cancion
        pygame.mixer.music.play(loops=0) #no se puede reproducir más de una vez

    def siguiente():
        proxima = pantalla.curselection() #obtener el numero de la tupla de la cancion que esta sonando
        proxima = proxima[0]+1 #añadir uno al numero de cancion
        cancion= pantalla.get(proxima)  #obtener titulo de cancion 

        cancion= f'{cancion}.mp3'

        pygame.mixer.music.load(cancion) #cargar la cancion
        pygame.mixer.music.play(loops=0) #no se puede reproducir mas de una vez

        pantalla.selection_clear(0,END)
        pantalla.activate(proxima) #activar nueva barra a la siguiente cancion
        
        last = None
        pantalla.selection_set(proxima, last) #mostrar la barra
      
    global paused
    paused=False

    def pause(is_paused):
        global paused
        paused = is_paused

        if paused:
            pygame.mixer.music.unpause() #sigue con la reproducción
            paused=False 
        else:
            pygame.mixer.music.pause() #se pausa en caso de que se de clic en el boton "Pausa"
            paused=True


    #Pantalla
    pantalla= Listbox(musicPlayer, bg="lightblue", fg ="blue", width= 100, selectbackground= "white", selectforeground="black") 
    pantalla.pack(pady=150)
    #pantalla.place(xrel=0.3, rely=0.1)


    #Botones
    siguiente= tk.Button(musicPlayer, text="Siguiente", command= siguiente, #ventana, texto del boton, accion 
                         bg="#000", borderwidth= 0.1, #color de fondo, grosor del boton
                         fg="#fff",
                         cursor="X_cursor",
                         font=("Verdana Bold", 18)) #tamaño y fuente de letra
    siguiente.pack()
    siguiente.place(relx=0.5, rely=0.35) #posicion del boton
    

    pausa= tk.Button(musicPlayer, text="Pausa", command=lambda: pause(paused), #botón pausa
                     bg="#000",borderwidth= 0.1,
                     fg="#fff",
                     cursor="X_cursor",
                     font=("Verdana Bold", 18))
    pausa.pack()
    pausa.place(relx=0.65, rely=0.35)

    buscar = tk.Button(musicPlayer, text = "Buscar canciones", command=añadir, #boton buscar cancion
                       bg="#000", borderwidth= 0.1,
                       fg="#fff",
                       cursor="X_cursor",
                       font=("Verdana Bold", 18))
    buscar.pack()
    buscar.place(relx=0.30, rely=0.35)
    
    
    musicPlayer.attributes('-fullscreen', True)
    
def funcion_Fotos():
    """input_images_path = "/media/pi/USB/"
    files_names = os.listdir(input_images_path)

    for file_name in files_names:
        image_path = input_images_path + "/" + file_name
        print(image_path)
        image = cv2.imread(image_path)
        if image is None:
            continue
        image = cv2.resize(image, (width, height), interpolation=cv2.INTER_CUBIC)
        cv2.namedWindow("WindowName",cv2.WINDOW_FULLSCREEN)
        cv2.imshow("Image", image)
        
        #keyboard.press_and_release("a")
        #time.sleep(1)
        cv2.waitKey(1500)
        
    #keyboard.press_and_release("a")
    cv2.destroyAllWindows()"""

def funcion_Video():
    input_videos_path = "/home/pi/Desktop" #direccion donde se encuentran los videos
    files_names = os.listdir(input_videos_path) #se guardan todos los nombres de los archivos 
                                                #que se encuentran en la carpeta

    for file_name in files_names:
        video_path = input_videos_path + "/" + file_name #se obtiene ruta de acceso de cada video
        #se manda a llamar a Media Player el cual será el reproductor de videos
        video = vlc.MediaPlayer(video_path)#se manda como parametro la ruta de acceso
        
        if video is None:
            continue
        video.play() #se reproduce el video

def principal():
    global botonConnect
    try:
        request = requests.get("http://www.google.com", timeout=5)
    except (requests.ConnectionError, requests.Timeout):
        labelWifi = Label(window, image=img_nowifi,
                       bg=colorFondo)
    else:
        labelWifi = Label(window, image=img_wifi,
                       bg=colorFondo)
    labelWifi.place(relx=0.95, rely=0.05)

    labelTitulo.place(relx=0.3, rely=0.05)
    # Llamado de cada botón
    botonNetflix.pack   ()
    botonAmazon.pack    ()
    botonDisney.pack    ()
    botonSpotify.pack   ()
    botonHBO.pack       ()
    botonYoutube.pack   ()
    botonSalir.pack     ()
    botonUsb.pack     ()

    botonNetflix.place  (relx=0.2,  rely=0.15)
    botonAmazon.place   (relx=0.45, rely=0.15)
    botonDisney.place   (relx=0.7,  rely=0.15)
    botonHBO.place      (relx=0.2,  rely=0.4)
    botonSpotify.place  (relx=0.45, rely=0.4)
    botonYoutube.place  (relx=0.7,  rely=0.4)
    botonUsb.place   (relx=0.2, rely=0.7)
    botonConfig.place   (relx=0.45, rely=0.7)
    botonSalir.place    (relx=0.7, rely=0.7) 

    #Se oculta la pagina de bienvenida
    labelBienvenida.place_forget()
    botonConnect.place_forget()
    botonClose.place_forget()
    


img_prime   = tk.PhotoImage(file="./iconos/prime.png")
img_disney  = tk.PhotoImage(file="./iconos/disney.png")
img_spotify = tk.PhotoImage(file="./iconos/spotify.png")
img_hbo     = tk.PhotoImage(file="./iconos/hbo.png")
img_youtube = tk.PhotoImage(file="./iconos/youtube.png")
img_config  = tk.PhotoImage(file="./iconos/config.png")
img_salir   = tk.PhotoImage(file="./iconos/salir.png")
img_wifi    = tk.PhotoImage(file="./iconos/wifi.png")
img_nowifi  = tk.PhotoImage(file="./iconos/nowifi.png")
img_usb  = tk.PhotoImage(file="./iconos/usb.png")
img_musica  = tk.PhotoImage(file="./iconos/musica.png")
img_fotos  = tk.PhotoImage(file="./iconos/fotos.png")
img_video  = tk.PhotoImage(file="./iconos/video.png")

img_netflix = tk.PhotoImage(file="./iconos/netflix.png") #se guarda la imagen del boton
# Creación de los botones
botonNetflix = tk.Button(window, image=img_netflix, #ventana, imagen que tendrá el botón 
                         borderwidth=0, bg=colorFondo, #grosor del botón, color de fondo
                         cursor="X_cursor", #cursor 
                         command = funcion_Netflix) #acción que hará cuando se oprima el botón

botonAmazon = tk.Button(window, image=img_prime,
                         borderwidth=0, bg=colorFondo,
                         cursor="X_cursor",
                        command = funcion_Amazon)

botonDisney = tk.Button(window, image=img_disney,
                         borderwidth=0, bg=colorFondo,
                         cursor="X_cursor",
                        command = funcion_Disney)

botonSpotify = tk.Button(window, image=img_spotify,
                         borderwidth=0, bg=colorFondo,
                         cursor="X_cursor",
                         command = funcion_Spotify)

botonHBO = tk.Button(window, image=img_hbo,
                         borderwidth=0, bg=colorFondo,
                         cursor="X_cursor",
                         command = funcion_HBO)    

botonYoutube = tk.Button(window, image=img_youtube,
                         borderwidth=0, bg=colorFondo,
                         cursor="X_cursor",
                         command = funcion_Youtube)   

botonConfig = tk.Button(window, image=img_config,
                         borderwidth=0, bg=colorFondo,
                         cursor="X_cursor",
                         command = configRed)

botonSalir = tk.Button(window, image=img_salir,
                         borderwidth=0, bg=colorFondo,
                         cursor="X_cursor",
                         command = funcion_Salir)

botonUsb = tk.Button(window, image=img_usb,
                         borderwidth=0, bg=colorFondo,
                         cursor="X_cursor",
                         command = funcion_Usb)

botonMusica = tk.Button(window, image=img_musica,
                         borderwidth=0, bg=colorFondo,
                         cursor="X_cursor",
                         command = funcion_Musica)

botonFotos = tk.Button(window, image=img_fotos,
                         borderwidth=0, bg=colorFondo,
                         cursor="X_cursor",
                         command = funcion_Fotos)

botonVideo = tk.Button(window, image=img_video,
                         borderwidth=0, bg=colorFondo,
                         cursor="X_cursor",
                         command = funcion_Video)

botonClose = tk.Button(window,
                            text = "Volver",
                            command = principal,
                            bg="#000",  
                            borderwidth= 0.1,
                            fg="#fff",
                            cursor="X_cursor",
                            font=("Verdana Bold", 18))

botonConnect = tk.Button(window, text="Conectar",
                         command=lambda: conectarRed(entrySSID.get(), entryPWD.get()),
                         bg="#fff",  
                         borderwidth= 0.1,
                         fg="#000",
                         cursor="X_cursor",
                         font=("Verdana Bold", 40))                   

#Creacion de los label
labelBienvenida = Label(window, text="Bienvenido",
                        fg="#fff",    # Foreground
                        bg=colorFondo,   # Background
                        font=("Verdana Bold",60))

labelTitulo = Label(window, text="Centro Multimedia",
                    fg="#fff",    # Foreground
                    bg=colorFondo,   # Background
                    font=("Verdana Bold",60))

entrySSID = Entry(window, font=("Verdana Bold",34))
entryPWD = Entry(window, font=("Verdana Bold",34), show="*")
# Geometria de la ventana
window.geometry("%dx%d" % (width, height))
# Atributos de la ventana, en este caso tiene que ser en pantalla completa
window.attributes('-fullscreen', True)
# Nombre de la ventana
window.title("Multimedia Center")


labelBienvenida.place(relx=0, rely=0, relheight=1, relwidth=1)
window.after(4000, principal)

window.mainloop()
