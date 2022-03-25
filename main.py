from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

#Opening Page
Builder.load_string("""
<Homepage>:
	id: Homepage
	name: "Homepage"
    
	GridLayout:
    	cols: 1
   	 
    	Button:
        	background_normal: "KSquared_Logo.png"
        	on_release:
            	app.root.current = "Menu"
            	root.manager.transition.direction = "left"
        Button:
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Tap anywhere to continue"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "KSquared-math,LLC © : Quadratic Formula"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left"    	 
""")

# Menu
Builder.load_string("""
<Menu>
	id:Menu
	name:"Menu"
    
	ScrollView:
    	name: "Scroll"
    	do_scroll_x: False
    	do_scroll_y: True
   	 
    	GridLayout:
        	cols: 1
        	padding:10
        	spacing:10
        	size_hint: 1, None
        	width:200
        	height: self.minimum_height
       	 
        	Label:
            	font_size: 75
            	size_hint_y: None
            	height: 200
            	padding: 10, 10
            	text: "Menu"
       	 
        	Button:
            	text: "Quadratic Formula Calculator"   
            	font_size: 75
            	background_color: 0, 0 , 1 , 1
            	size_hint_y: None
            	height: 200
            	padding: 10, 10
            	on_release:
                	app.root.current = "Quadratic_Formula_Solver"
                	root.manager.transition.direction = "left"
               	 
        	Button:
            	font_size: 75
            	size_hint_y: None
            	height: 200
            	text: "Visit KSquared,LLC"
            	on_release:
                	import webbrowser
                	webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc')
                    
            Button:
                font_size: 75
                background_color: 1, 0, 1, 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new?"
                on_release:
                    app.root.current = "updates"
                    root.manager.transition.direction = "left"
                    
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Share KSquared-math,LLC ©"
                    
            Image:
                source: 'KSquared_QR_code.png'
                size_hint_y: None
                height: 1000
                width: 1000
""")

#Updates
Builder.load_string("""
<updates>
    id:updates
    name:"updates"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
    
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: 60
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new at KSquared-math?"
            
            Button:
                id: steps
                text: "Menu"   
                font_size: 75
                size_hint_y: None
                background_color: 0, 0 , 1 , 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Menu"
                    root.manager.transition.direction = "right" 
                    
            Label:
                font_size: 40
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Quadratic Calculator v0.1"
                
            Label:
                font_size: 40
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "No new updates as of 1/26/2022"
            
""")

Builder.load_string("""
<Quadratic_Formula_Solver>
    id:Quadratic_Formula_Solver
    name:"Quadratic_Formula_Solver"
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: 50
                size_hint_y: None
                height: 200
                text: "Quadratic Formula Solver"
                
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    text: "Menu"   
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1, 1
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        a.text = ""
                        b.text = ""
                        c.text = ""
                        list_of_steps.clear_widgets()    
            
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
            
                Label:
                    height: 250
                    font_size: 50
                    size_hint_y: None
                    padding: 5,5
                    text: "ax\u00B2 + bx + c = 0"
                
                Label:
                    height: 250
                    font_size: 50
                    size_hint_y: None
                    padding: 5,5
                    text:
                        '''      -b \u00B1 \u221A(b\u00B2 - 4ac)
                        x = -----------------------
                        '''      '''                2a'''    
            
            TextInput:
                id: a
                text: a.text
                multiline: False
                font_size: 125
                size_hint_y: None
                hint_text: "a ="
                height: 200
                padding: 10
                input_filter: lambda text, from_undo: text[:3 - len(a.text)]  
                    
                                                 
            TextInput:
                id: b
                text: b.text
                multiline: False
                hint_text: "b ="
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10          
                input_filter: lambda text, from_undo: text[:3 - len(b.text)]  
                
    
            TextInput:
                id: c
                text: c.text
                multiline: False
                hint_text: "c ="
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10          
                input_filter: lambda text, from_undo: text[:3 - len(c.text)]
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5  
    
                Button:
                    id: steps
                    text: "Calculate"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 1 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Quadratic_Formula_Solver.steps(a.text + "," + b.text + "," + c.text)    
                       
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height                  
                    
""")

class Quadratic_Formula_Solver(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Quadratic_Formula_Solver, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key == 27:
            print("Its working ESC = 27 LENGTH")
            return True

    def set_previous_screen(self):
        print("Length is almost working")        
        if sm.current != "Homepage":
            print("Its working List")
            sm.transition.direction = 'right'
            sm.current = "Menu"
            
    layouts = []
    def steps(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        try:
            entry_list =  entry.split(",")
            print("entry_list",entry_list)
            a = float(entry_list[0])
            b = float(entry_list[1])
            c = float(entry_list[2])
            
            #Check if ax^2 + bx + c = 0
            square = float(b*b - 4*a*c)
            print("square",square)
            
            if square > 0 :
                
                a = str(entry_list[0])
                b_out = "-" + str(entry_list[1])
                b_out = b_out.replace("--","")
                b = str(entry_list[1])
                c = str(entry_list[2])
                
                
                #POSITIVE
                self.ids.list_of_steps.add_widget(Label(text= "x1" ,font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " + \u221A(" + b + "\u00B2 - 4" + "(" + a + ")(" + c + "))" + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = 50, size_hint_y= None, height=300))
                
                ac = " - " + str(4*float(a)*float(c))
                ac = ac.replace("- -","+ ")
                b = str(float(b)**2)
                
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " + \u221A(" + b + ac + ")" + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = 50, size_hint_y= None, height=300))
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " + \u221A(" + str(square) + ")" + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = 50, size_hint_y= None, height=300))
                
                squared = str(square**.5)
                print("squared",squared)
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " + " + squared + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = 50, size_hint_y= None, height=300))
                
                numer = str(float(b_out) + float(squared))
                self.ids.list_of_steps.add_widget(Label(text= "          " + numer + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = 50, size_hint_y= None, height=300))
                
                denom = str(2 * float(a))
                self.ids.list_of_steps.add_widget(Label(text= "          " + numer + "\nx = -------------------------------" + "\n                     " + denom ,font_size = 50, size_hint_y= None, height=300))
                
                answera = str(float(numer) / float(denom))
                print("answera",answera)
                self.ids.list_of_steps.add_widget(Label(text="x1 = " + answera ,font_size = 50, size_hint_y= None, height=150))
                self.layouts.append(layout)
                self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" ,font_size = 50, size_hint_y= None, height=150))
                
                a = str(entry_list[0])
                b_out = "-" + str(entry_list[1])
                b_out = b_out.replace("--","")
                b = str(entry_list[1])
                c = str(entry_list[2])
                
                #NEGATIVE
                self.ids.list_of_steps.add_widget(Label(text= "x2" ,font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " - \u221A(" + b + "\u00B2 - 4" + "(" + a + ")(" + c + "))" + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = 50, size_hint_y= None, height=300))
                
                ac = " - " + str(4*float(a)*float(c))
                ac = ac.replace("- -","+ ")
                b = str(float(b)**2)
                
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " - \u221A(" + b +  ac + ")" + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = 50, size_hint_y= None, height=300))
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " - \u221A(" + str(square) + ")" + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = 50, size_hint_y= None, height=300))
                
                squared = str(square**.5)
                print("squared",squared)
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " - " + squared + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = 50, size_hint_y= None, height=300))
                
                numer = str(float(b_out) - float(squared))
                self.ids.list_of_steps.add_widget(Label(text= "          " + numer + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = 50, size_hint_y= None, height=300))
                
                denom = str(2 * float(a))
                self.ids.list_of_steps.add_widget(Label(text= "          " + numer + "\nx = -------------------------------" + "\n                     " + denom ,font_size = 50, size_hint_y= None, height=300))
                
                answerb = str(float(numer) / float(denom))
                print("answerb",answerb)
                self.ids.list_of_steps.add_widget(Label(text="x1 = " + answerb ,font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" ,font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="FINAL ANSWER ",font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="x1 = " + answera,font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="x2 = " + answerb,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
            
            else:
                self.ids.list_of_steps.add_widget(Label(text= "Invalid Square Root" ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
            
                            
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)
       	 
   	 
class Homepage(Screen):
	pass       	 
      	 
class Menu(Screen):
	pass

class updates(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))
sm.add_widget(updates(name="updates"))
sm.add_widget(Quadratic_Formula_Solver(name="Quadratic_Formula_Solver"))	 
sm.current = "Homepage"   


class Quadratic_Formula_Solver(App):
    def build(app):
        return sm

if __name__ == '__main__':
	Quadratic_Formula_Solver().run()
