from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
 
# counter image
image=1

class YourApp(App):

    #methods for rpevious
    def previous(self, instance):
        #link to our imgae varibales glabal and siubbtract 1
        global image
        image= image - 1

        #chek see if <= 0
        if image <=0:
            image =7

        #if check number 1-5
        if image==1:
            self.img.source = 'one.jpg'
        elif image==2:
            self.img.source = 'two.jpg'
        elif image==3:
            self.img.source = 'three.jpg'
        elif image==4:
            self.img.source = 'four.jpg'
        elif image==5:
            self.img.source = 'five.jpg'
        elif image==6:
            self.img.source = 'six.jpg'
        elif image==7:
            self.img.source = 'seven.jpg'

     #methods for rpevious
    def next(self, instance):
        #link to our imgae varibales glabal and add 1
        global image
        image= image + 1

        #chek see if <= 0
        if image > 7:
            image =1

        #if check number 1-5
        if image==1:
            self.img.source = 'one.jpg'
        elif image==2:
            self.img.source = 'two.jpg'
        elif image==3:
            self.img.source = 'three.jpg'
        elif image==4:
            self.img.source = 'four.jpg'
        elif image==5:
            self.img.source = 'five.jpg'
        elif image==6:
            self.img.source = 'six.jpg'
        elif image==7:
            self.img.source = 'seven.jpg'

    def build(self):

         #create our layout for the box 
         buttonBox = BoxLayout(orientation='horizontal',pos_hint={'center_x':.75})

         #cotainer for overall box layout
         layout = BoxLayout(orientation='vertical',pos_hint={'center_x':.5})

         #create button
         b1 = Button(text='Previous',size=(200,100),size_hint=(None,None))
         
         #link this to the correct method
         b1.bind(on_press = self.previous)

         #create b2
         b2 = Button(text='Next',size=(200,100),size_hint=(None,None))

         #link this to correct method
         b2.bind(on_press = self.next)

         #add buttons to box
         buttonBox.add_widget(b1)
         buttonBox.add_widget(b2)

         #load our first imagfe
         self.img = Image(source='one.jpg')

         #add image to layout
         layout.add_widget(self.img)

         #add button box to layout
         layout.add_widget(buttonBox)

         return layout

YourApp().run()
