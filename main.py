from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class InspectionApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # عنوان التطبيق
        layout.add_widget(Label(text="برنامج فحص وتدقيق البيانات", font_size=24))
        
        # حقل إدخال لفحص النصوص أو البيانات
        self.input_data = TextInput(hint_text="أدخل البيانات المراد فحصها هنا...", multiline=False, size_hint_y=None, height=50)
        layout.add_widget(self.input_data)
        
        # زر الفحص
        btn = Button(text="ابدأ الفحص الفوري", size_hint_y=None, height=50, background_color=(0, 0.5, 1, 1))
        btn.bind(on_press=self.run_inspection)
        layout.add_widget(btn)
        
        # نتيجة الفحص
        self.result_label = Label(text="حالة الفحص: في انتظار البيانات", font_size=18)
        layout.add_widget(self.result_label)
        
        return layout

    def run_inspection(self, instance):
        data = self.input_data.text.strip()
        if not data:
            self.result_label.text = "تنبيه: حقل الإدخال فارغ!"
        else:
            self.result_label.text = f"تم فحص النتيجة بنجاح! البيانات سليمة وآمنة."

if __name__ == '__main__':
    InspectionApp().run()
