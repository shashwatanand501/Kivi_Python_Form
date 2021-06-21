import kivy
import os
from kivy.uix.image import Image,AsyncImage
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.uix.boxlayout import BoxLayout
import time
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp
from kivy.clock import Clock
import cv2
from kivy.uix.camera import Camera
from kivy.uix.dropdown import DropDown
import mysql.connector as mysql

class ImageKv(BoxLayout):
    pass
class MainWindow(Screen):
    pass
class SecondWindow(Screen):
    pass
class LoginWindow(Screen):
    pass
class CameraWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv=Builder.load_string('''
WindowManager:
    MainWindow:
    SecondWindow:
    LoginWindow:
    CameraWindow:
<MainWindow>:
    name:"login_page"
    FloatLayout:   
        ImageKv: 
            Image:
                source:'luke-chesser-eICUFSeirc0-unsplash.jpg'
                allow_stretch:True
                keep_ratio:False   
        Image:
            source:'IIMT University Logo.jpg'
            color:0.3,0.6,0.7,7
            size_hint: 0.8, 0.2
            pos_hint: {"x":0.1, 'top':0.84}
            allow_stretch:False
            keep_ratio:False
        Label:
            text: "IIMT UNIVERSITY"
            color:1,1,1,1
            size_hint: 0.8, 0.2
            pos_hint: {"x":0.094, "top":1}
            font_size: (root.width**2 + root.height**2) / 12**4
        Label:
            text: "ADMISSION NUMBER"
            size_hint: 0.5,0.12
            color:1,1,1,1
            pos_hint: {"x":0.25, "top":0.8-0.17*1}
            font_size: (root.width**2 + root.height**2) / 13**4
        TextInput:
            id:passw
            pos_hint: {"x":0.35, "top":0.8-0.16*2}
            size_hint: 0.3, 0.059
            multiline: False
        SmoothButton:
            text:"login"
            size_hint: 0.3,0.11
            color:1,1,1,1
            pos_hint: {"x":0.35, "top":0.3}
            on_release:
                app.root.current="login_page1" if passw.text=="iimt" else "login_page"
                root.manager.transition.direction = "left"
        SmoothButton:
            text:"Create new"
            size_hint: 0.3,0.11
            pos_hint: {"x":0.35, "top":0.17}
            on_release:
                app.root.current="information_page"
                root.manager.transition.direction = "left"        
<SecondWindow>:
    name:"information_page"
    FloatLayout:
        size:root.width,root.height          
        ImageKv:
            Image:
                source:'Register_background.jpg'
                color:0.3,0.6,0.7,7
                pos_hint: {"x":0.4, 'top':1}
                allow_stretch:True
                keep_ratio: False             
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True
        Label:
            text: "STUDENT NAME->"
            size_hint: 0.2,0.1
            pos_hint: {"x":0.15, "top":1}
            color:1,1,1,1
            font_size: (root.width**1.86 + root.height**2) / 14**4
        TextInput:
            id:student_name
            size_hint: 0.3, 0.059
            pos_hint: {"x":0.47, "top":0.97}
            multiline: False    
        Label:
            text: "FATHER NAME->"
            size_hint: 0.2, 0.01
            pos_hint: {"x":0.15, "top":0.87}
            color:1,1,1,1
            font_size: (root.width**1.86 + root.height**2) / 14**4   
        TextInput:
            id:father_name
            size_hint: 0.3, 0.059
            pos_hint: {"x":0.47, "top":0.89}
            multiline: False    
        Label:
            text: "FATHER PHONE NUMBER->"
            size_hint: 0.26,0.12
            color:1,1,1,1
            pos_hint: {"x":0.15, "top":0.84}
            font_size: (root.width**1.86 + root.height**2) / 14**4   
        TextInput:
            id:father_contact
            size_hint: 0.3, 0.059
            pos_hint: {"x":0.47, "top":0.80}
            multiline: False    
        Label:
            text: "STUDENT PHONE NUMBER->"
            size_hint: 0.26,0.12
            pos_hint: {"x":0.15, "top":0.75}
            color:1,1,1,1
            font_size: (root.width**1.86 + root.height**2) / 14**4
        TextInput:
            id:student_contact
            size_hint: 0.3,0.059
            pos_hint: {"x":0.47, "top":0.71}
            multiline: False    
        Label:
            text: "MOTHER NAMES->"
            size_hint: 0.23,0.12
            color:1,1,1,1
            pos_hint: {"x":0.15, "top":0.66}
            font_size: (root.width**1.86 + root.height**2) / 14**4
        TextInput:
            id:mother_name
            size_hint: 0.3,0.059
            multiline: False
            pos_hint: {"x":0.47, "top":0.62}
            font_size: (root.width**1.86 + root.height**2) / 14**4
        Label:
            text: "10th MARKS->"
            size_hint: 0.23,0.12
            color:1,1,1,1
            pos_hint: {"x":0.15, "top":0.58}
            font_size: (root.width**1.86 + root.height**2) / 14**4
        TextInput:
            id:ten
            size_hint: 0.3,0.059
            pos_hint: {"x":0.47, "top":0.54}
            multiline: False      
        Label:
            text: "12th MARKS->"
            size_hint: 0.23,0.12
            color:1,1,1,1
            pos_hint: {"x":0.15, "top":0.49}
            font_size: (root.width**1.86 + root.height**2) / 14**4  
        TextInput:
            id:twe
            size_hint: 0.3,0.059
            pos_hint: {"x":0.47, "top":0.45}
            multiline: False    
        Label:
            text: "DATE OF BIRTH->"
            size_hint: 0.23,0.12
            color:1,1,1,1
            pos_hint: {"x":0.15, "top":0.41}
            font_size: (root.width**1.86 + root.height**2) / 14**4   
        TextInput:
            id:dob
            size_hint: 0.3,0.059
            pos_hint: {"x":0.47, "top":0.37}
            font_size: (root.width**1.86 + root.height**2) / 14**4
            multiline: False 
        Label:
            text: "ADDRESS"
            size_hint: 0.5,0.12
            color:1,1,1,1
            pos_hint: {"x":0.2, "top":0.0}
            font_size: (root.width**1.86 + root.height**2) / 14**4   
        

        MyTextInput:
            id:ADD
            size_hint: 0.3,0.059
            pos_hint: {"x":0.25, "top":0.0}
            font_size: (root.width**1.86 + root.height**2) / 14**4
            multiline: False       
        SmoothButton:
            text:"click"
            size_hint: 0.3,0.1
            color:1,1,1,1
            pos_hint: {"x":0.48, "top":0.21}
            on_release:
                app.root.current="camera_module" 
                root.manager.transition.direction = "left"  
        SmoothButton:
            text:"Browse"
            size_hint: 0.3,0.1
            color:1,1,1,1
            pos_hint: {"x":0.15, "top":0.21}
            on_release:
                app.root.current="camera_module" 
                root.manager.transition.direction = "left"          
        SmoothButton:
            text:"Submit"
            size_hint: 0.3,0.1
            color:1,1,1,1
            pos_hint: {"x":0.35, "top":0.10}
            on_release:
                app.root.current=app.done(root) 
                root.manager.transition.direction = "left"

<LoginWindow>:
    name:"login_page1"
    SmoothButton:
        text:"Back"
        size_hint: 0.3,0.11
        pos_hint: {"x":0.35, "top":0.19}
        on_release:
            app.root.current="login_page"
            root.manager.transition.direction = "left" 
    
<CameraWindow>:
    name:"camera_module"
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640,320)
        play: False
    SmoothButton:
        text: 'Play'
        pos_hint: {"x":0.2, "top":0.1}
        on_press: camera.play = not camera.play
        size_hint: 0.2,0.1
        height: '48dp'
    SmoothButton:
        text: 'Capture'
        pos_hint: {"x":0.45, "top":0.1}
        size_hint: 0.2,0.1
        height: '48dp'
        on_press:camera.play
        on_press: app.capture(root)

    SmoothButton:
        text: '--->'
        pos_hint: {"x":0.7, "top":0.1}
        size_hint: 0.2,0.1
        height: '38dp'
        on_press:camera.play
        on_press: app.done(root)


<SmoothButton@Button>:
    background_color:(0,0,0,0)
    background_normal:''
    back_color:(204,51,255,0.2)
    border_radius:[18]
    canvas.before:
        Color:
            rgba:204,51,255,0.2
        RoundedRectangle:
            size:self.size
            pos:self.pos
                      
<MyTextInput@TextInput>:
    font_size: '14dp'
    background_color: 0,0,0,0
    canvas.before:
        Color:
            rgba:204,51,255,0.2
        Ellipse:
            angle_start:180
            angle_end:360
            pos:self.pos
            size:self.size
''') 

class MyMainApp(App):
    def capture(self,root):
        camera = root.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")
    def done(self,root):
        db = mysql.connect(
        host="localhost",
        user="root",
        passwd="root"
        )
        print(db)
    
    def build(self):
        return kv 
        
if __name__=="__main__": 
    MyMainApp().run()   