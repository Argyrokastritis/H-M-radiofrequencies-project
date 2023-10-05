import tkinter as tk

class coordinates_input_GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Location Input")
        self.window.geometry("400x100")

        tk.Label(self.window, text="Enter the latitude and longitude values below:").grid(row=0, column=0, columnspan=2)

        tk.Label(self.window, text="Latitude:").grid(row=1, column=0)
        self.latitude_entry = tk.Entry(self.window)
        self.latitude_entry.grid(row=1, column=1)

        tk.Label(self.window, text="Longitude:").grid(row=2, column=0)
        self.longitude_entry = tk.Entry(self.window)
        self.longitude_entry.grid(row=2, column=1)

        tk.Button(self.window, text="Submit", command=self.submit).grid(row=3, column=0)
        tk.Button(self.window, text="Cancel", command=self.cancel).grid(row=3, column=1)

    def submit(self):
        latitude_str = self.latitude_entry.get()
        longitude_str = self.longitude_entry.get()

        if not latitude_str or not longitude_str:
            print("Please enter valid values for latitude and longitude.")
            return

        try:
            latitude = float(latitude_str)
            longitude = float(longitude_str)
        except ValueError:
            print("Please enter valid numeric values for latitude and longitude.")
            return

        location = [latitude, longitude]
        print("The location you entered is:", location)
        self.location = location
        self.window.destroy()

    def cancel(self):
        self.window.destroy()

def get_location():
    gui = coordinates_input_GUI()
    gui.window.mainloop()
    return gui.location

if __name__ == "__main__":
    location = get_location()








