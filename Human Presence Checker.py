# HUMAN PRESENCE CHECKER
# V 1.0.2
# Created by PR@16 Creations

import cv2,numpy,os
import PySimpleGUI as sg
from pydub import AudioSegment
from pydub.playback import play

try:
    def resource_path(relative_path):
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    logo_mn=resource_path("Logo_Main.png")
    sg.Window("Window Title",[[sg.Image(logo_mn)]],transparent_color=sg.theme_background_color(),no_titlebar=True,
       keep_on_top=True).read(timeout=5000,close=True)
    
    def strt(st):
        try:
            # Enable camera
            cap = cv2.VideoCapture(0)
            cap.set(3, 640)
            cap.set(4, 420)
        except:
            ext_1("No Camera Found")
            exit()

        # import cascade file for facial recognition
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        count=0
        fc=0
        td=0
        tb=0
        while True:
            if count==200:
                print("STOP")
                print(fc)
                if td>100:
                    sg.SystemTray.notify('Human Presence Checker', 'Too Dark Environment')
                elif tb>100:
                    sg.SystemTray.notify('Human Presence Checker', 'Too Bright Environment')
                if fc<5:
                    sg.theme("HotDogStand")
                    beep_sound=resource_path("Censor Beep Sound Effect.mp3")
                    path_to_file=beep_sound
                    song = AudioSegment.from_mp3(path_to_file)
                    play(song)
                    window2=sg.Window("Window",[[sg.Text("NO HUMAN PRESENCE FOUND/ BAD LIGHTING CONDITION/ BAD CAMERA QUALITY",font=("Helvetica",20))]],no_titlebar=True,
                         keep_on_top=True).read(timeout=5000,close=True)
                fc=0
                td=0
                tb=0
                count=0
            count+=1
            stat="not live"
            success, img = cap.read()
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            avg_color_per_row = numpy.average(imgGray, axis=0)
            avg_color = numpy.average(avg_color_per_row, axis=0)
            if avg_color>160:
                print("Too Bright")
                tb+=1
            if avg_color<30:
                print("Too Dark")
                td+=1
            # Getting corners around the face
            faces = faceCascade.detectMultiScale(imgGray, 1.3, 5)  # 1.3 = scale factor, 5 = minimum neighbor
            # drawing bounding box around face
            for (x, y, w, h) in faces:
                fc+=1
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                print("DETECTED FACE "+str(fc)+" times")
                stat="live"
            # print(stat)
            # comment the below code to stop showing video output
            if st=="Start with Display":
                cv2.imshow('Human Presence Checker', img)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyWindow('face_detect')
    def not_():
        sg.theme("Topanga")
        layout3=[[sg.Text("!!! CAUTION !!!",font=("Helvetica",20))],
                 [sg.Text("* This is only a Demo Version of the Program\n* Camera permission is required for Running the program\n* You can use Ctrl+C to stop the Program once it has been started\n* Program Written and compiled by PR@16 Creations\n* \n* \n* \n* \n* \n* \n* \n* All Terms and Conditions should be accepted before Executing\n  the main Program",font=("Helvetica",15))],
                 [sg.Text("Check Every ")]+[sg.Checkbox("30 Seconds")]+[sg.Checkbox("1 Minute")]+[sg.Checkbox("5 Minutes")],
                 [sg.Radio("I've read all the above given conditions and informations and will do accordingly", 1,text_color="white")],
                 [sg.Button("Start with Display")]+[sg.Button("Start without Display")]]
        window3=sg.Window("Caution",layout3,element_justification="c")
        while True:
            event,value=window3.read()
            window3.close()
            if value[0]==True:
                if value[1]==True:
                    not_()
                if value[2]==True:
                    not_()
            elif value[1]==True:
                if value[0]==True:
                    not_()
                if value[2]==True:
                    not_()
            elif value[2]==True:
                if value[0]==True:
                    not_()
                if value[1]==True:
                    not_()
            if value[3]==False:
                not_()
            if event==None:
                mn() 
            return event
    def ext():
        sg.theme("Topanga")
        lyt=[[sg.Text("Do You Want to Exit ?",font=("Helvetica",15))],[sg.Button("Exit",button_color="red")]+
             [sg.Button("Cancel",button_color="green")]]
        wnd=sg.Window("Exit",lyt,element_justification="c")
        event,values=wnd.read()
        wnd.close()
        return event
    def ext_1(string):
        sg.theme("Topanga")
        lyt=[[sg.Text(string,font=("Helvetica",15))],[sg.Button("Exit",button_color="red")]]
        wnd=sg.Window("Exit",lyt,element_justification="c")
        event,values=wnd.read()
        wnd.close()
        exit()
    def mn():
        sg.theme("Topanga")
        st="N"
        layout1=[[sg.Text("\nHUMAN PRESENCE",font=("Helvetica",20))],[sg.Text("CHECKER",font=("Helvetica",20))],[sg.Button("Start",font=("Helvetica",20),button_color=("black","green"),size=(100,1),bind_return_key=True)],
                 [sg.Button("Help",button_color=("black","orange"),font=("Helvetica",20),size=(100,1),bind_return_key=True)],[sg.Button("Exit",font=("Helvetica",20),size=(100,1),button_color=("black","red"),bind_return_key=True)],
                 [sg.Text("Version 1.0.1")]]
        window1=sg.Window("Human Presence Checker",layout1,size=(290, 300),element_justification="c")
        event,values=window1.read()
        window1.close()
        if event=="Start":
            st=not_()
            strt(st)
        elif event=="Help":
            k=sg.popup_scrolled("*** HUMAN PRESENCE CHECKER ***\n### V1.0.2\n$ Basically The aim of the Program is to check for Human presence.\n$ Press Ctrl+C to stop the Program.\n$ Requires Camera Permission.",title="Help")
            if k=="OK":
                mn()
            else:
                mn()
        elif event=="Exit" or event==None:
            vl=ext()
            if vl=="Exit":
                exit()
            else:
                mn()
    mn()
except KeyboardInterrupt:
    ext_1("KeyBoard Interrput Detected\n     Exiting Application....")
except FileNotFoundError:
    ext_1("There's an issue with Loading of\nResource data. Please check your\n System Permissions !")
except:
    ext_1("An Error had Occured !!!")
