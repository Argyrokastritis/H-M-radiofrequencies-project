import PySimpleGUI as sg

class coordinates_input_GUI:
    def __init__(self):
        sg.theme('DarkAmber')

        layout = [[sg.Text('Enter the latitude and longitude values below:')],
                  [sg.Text('Latitude:'), sg.InputText(size=(20, 1)), sg.Text('Longitude:'), sg.InputText(size=(20, 1))],
                  [sg.Button('Submit'), sg.Button('Cancel')]]

        self.window = sg.Window('Location Input', layout)

    def get_location(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
            elif event == 'Submit':
                latitude = float(values[0])
                longitude = float(values[1])
                location = [latitude, longitude]
                print("The location you entered is:", location)
                return location

        self.window.close()

