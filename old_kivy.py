import kivy   
from kivy.app import App  
kivy.require('1.9.0') 
from kivy.lang import Builder 
from kivy.properties import NumericProperty 
from kivy.uix.boxlayout import BoxLayout  
from kivy.clock import Clock 
  

Builder.load_string(''' 
  
<MainWidget>: 
  
    # Assigning the alignment to buttons 
    BoxLayout: 
        orientation: 'vertical' 
  
        # Create Button 
          
        Button: 
            text: 'start' 
            on_press: root.start() 
              
        Button: 
            text: 'stop' 
            on_press: root.stop() 
              
        Button: 
            text: 'Reset' 
            on_press: root.number = 0 
  
    # Create the Label 
    Label: 
        text: str(round(root.number)) 
        text_size: self.size 
        halign: 'center' 
        valign: 'middle' 
    
    Label:
        id: kaj
        text:str("Work Mode ON")
        text_size: self.size 
        halign: 'center' 
        valign: 'middle'
''') 
   

class MainWidget(BoxLayout): 
      
    number = NumericProperty() 
      
    def __init__(self, **kwargs): 
  
        super(MainWidget, self).__init__(**kwargs) 
        Clock.schedule_interval(self.increment_time, .1) 
  
        self.increment_time(0) 

    def increment_time(self, interval): 
        self.number += .1
  

    def start(self): 
          
        Clock.unschedule(self.increment_time) 
        Clock.schedule_interval(self.increment_time, .1)
        self.ids.kaj.text = "Work Mode ON"

    def stop(self): 
        Clock.unschedule(self.increment_time)
        self.ids.kaj.text = "Work Mode OFF" 
  
class TimeApp(App): 
    def build(self): 
        return MainWidget() 
  

TimeApp().run() 