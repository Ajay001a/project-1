from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image as KivyImage
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from threading import Thread
from PIL import Image
import os
import cv2
import numpy as np

DEFAULT_OUTPUT_DIR = os.path.join(os.path.expanduser('~'), 'converted_files')

kv_string = """
<FileConverterLayout>:
    FloatLayout:
        canvas.before:
            Color:
                rgba: (0.53, 0.81, 0.92, 1)  # Sky blue color
            Rectangle:
                pos: self.pos
                size: self.size

        FileChooserListView:
            id: file_chooser
            path: '/'
            size_hint_y: 0.4  # Occupies 40% of the window height
            pos_hint: {'top': 1}
        
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: 0.2  # Occupies 20% of the window height
            padding: [10, 10]
            spacing: 10
            pos_hint: {'top': 0.6}
            BoxLayout:
                orientation: 'horizontal'
                size_hint_y: 0.5  # Occupies 50% of this BoxLayout's height
                Label:
                    text: 'Output Filename:'
                    size_hint_x: 0.4
                TextInput:
                    id: output_filename_input
                    size_hint_x: 0.6
            BoxLayout:
                orientation: 'horizontal'
                size_hint_y: 0.5  # Occupies 50% of this BoxLayout's height
                Label:
                    text: 'Output Format:'
                    size_hint_x: 0.4
                Spinner:
                    id: output_format_spinner
                    text: 'Select Output Format'
                    values: ['PDF', 'PNG', 'JPG']
                    size_hint_x: 0.6

        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: 0.1  # Occupies 10% of the window height
            padding: [10, 10]
            spacing: 10
            pos_hint: {'bottom': 0.1}
            Button:
                text: 'Convert'
                on_press: root.handle_convert()
                size_hint_x: 0.3
            Button:
                text: 'Capture Image'
                on_press: root.capture_image()
                size_hint_x: 0.3
            Button:
                text: 'Reset'
                on_press: root.reset()
                size_hint_x: 0.3

        Image:
            source: 'logo.png'  # Path to your watermark image
            size_hint: (None, None)
            size: (300, 150)  # Adjust size as needed
            pos_hint: {'center_x': 0.5, 'top': 1}  # Center the watermark at the top
            opacity: 0.5  # Adjust opacity (0.0 is fully transparent, 1.0 is fully opaque)
"""

Builder.load_string(kv_string)

class FileConverterLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(FileConverterLayout, self).__init__(**kwargs)
        self.file_chooser = self.ids.get('file_chooser', None)
        self.output_filename_input = self.ids.get('output_filename_input', None)
        self.output_format_spinner = self.ids.get('output_format_spinner', None)

        if not os.path.exists(DEFAULT_OUTPUT_DIR):
            os.makedirs(DEFAULT_OUTPUT_DIR)

    def handle_convert(self):
        # Placeholder for file conversion logic
        pass

    def capture_image(self):
        # Use a thread to capture the image to avoid blocking the main thread
        capture_thread = Thread(target=self._capture_image_thread)
        capture_thread.start()

    def _capture_image_thread(self):
        cap = cv2.VideoCapture(0)  # 0 is the default camera

        if not cap.isOpened():
            Clock.schedule_once(lambda dt: self.show_popup("Error", "Unable to access the camera."))
            return

        # Capture a single frame from the camera
        ret, frame = cap.read()
        if ret:
            filename = os.path.join(DEFAULT_OUTPUT_DIR, 'captured_image.png')
            # Save the image with a lower resolution to improve speed
            frame = cv2.resize(frame, (640, 480))  # Resize the frame to a smaller size
            cv2.imwrite(filename, frame)
            Clock.schedule_once(lambda dt: self._show_image_popup(filename))
        else:
            Clock.schedule_once(lambda dt: self.show_popup("Error", "Failed to capture image."))
        cap.release()

    def _show_image_popup(self, filename):
        # Show the captured image and ask user for the image name, format, and flip options
        image = Image.open(filename)
        layout = BoxLayout(orientation='vertical')
        
        # Create an Image widget to display the captured image
        kivy_image = KivyImage(size_hint=(1, 0.8))
        kivy_image.texture = self._image_to_texture(image)
        layout.add_widget(kivy_image)

        # Add input fields for file name and format
        name_input = TextInput(hint_text='Enter image name', size_hint=(1, 0.1))
        format_spinner = Spinner(text='Select Format', values=['PNG', 'JPG', 'PDF'], size_hint=(1, 0.1))
        layout.add_widget(name_input)
        layout.add_widget(format_spinner)

        # Add flip and rotate buttons
        flip_buttons = BoxLayout(size_hint=(1, 0.1))
        horizontal_flip = Button(text='Horizontal Flip')
        vertical_flip = Button(text='Vertical Flip')
        rotate_90 = Button(text='Rotate 90°')
        flip_buttons.add_widget(horizontal_flip)
        flip_buttons.add_widget(vertical_flip)
        flip_buttons.add_widget(rotate_90)
        layout.add_widget(flip_buttons)

        # Add save button
        save_button = Button(text='Save Image', size_hint=(1, 0.1))
        layout.add_widget(save_button)

        popup = Popup(title='Captured Image', content=layout, size_hint=(0.8, 0.8))
        save_button.bind(on_press=lambda btn: self._save_image(name_input.text, format_spinner.text, image))
        horizontal_flip.bind(on_press=lambda btn: self._flip_image(image, 'horizontal', kivy_image))
        vertical_flip.bind(on_press=lambda btn: self._flip_image(image, 'vertical', kivy_image))
        rotate_90.bind(on_press=lambda btn: self._rotate_image(image, 90, kivy_image))
        popup.open()

    def _image_to_texture(self, image):
        # Convert PIL image to Kivy texture
        image = image.convert('RGB')
        data = np.frombuffer(image.tobytes(), dtype=np.uint8).reshape(image.size[1], image.size[0], 3)
        texture = Texture.create(size=image.size, colorfmt='rgb')
        texture.blit_buffer(data.flatten(), colorfmt='rgb', bufferfmt='ubyte')
        return texture

    def _flip_image(self, image, direction, kivy_image):
        if direction == 'horizontal':
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
        elif direction == 'vertical':
            image = image.transpose(Image.FLIP_TOP_BOTTOM)
        kivy_image.texture = self._image_to_texture(image)

    def _rotate_image(self, image, angle, kivy_image):
        image = image.rotate(angle, expand=True)
        kivy_image.texture = self._image_to_texture(image)

    def _save_image(self, name, format, image):
        if not name:
            self.show_popup("Error", "Please enter an image name.")
            return
        if format not in ['PNG', 'JPG', 'PDF']:
            self.show_popup("Error", "Invalid format selected.")
            return

        try:
            output_path = os.path.join(DEFAULT_OUTPUT_DIR, f"{name}.{format.lower()}")
            if format == 'PDF':
                image.save(output_path, "PDF")
            else:
                image.save(output_path, format)
            self.show_popup("Success", f"Image saved as {output_path}")
        except Exception as e:
            self.show_popup("Error", f"Failed to save image: {str(e)}")

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.6, 0.4))
        popup.open()

class FileConverterApp(App):
    def build(self):
        return FileConverterLayout()

if __name__ == '__main__':
    FileConverterApp().run()
