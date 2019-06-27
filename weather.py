import tkinter as app
import requests


HEIGHT = 700
WIDTH = 800

#appid 01a2cf0659850c1a8d4ee5cd290cf3e3
#url api.openweathermap.org/data/2.5/weather


# button functionality
def button_func(city):
    print(entry)
    weather_key = '01a2cf0659850c1a8d4ee5cd290cf3e3'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units' : 'metric'}
    response = requests.get(url, params=params)
    print(response.json())



root = app.Tk()
# canvas as in full window
canvas = app.Canvas(root, bg='green', height=HEIGHT, width=WIDTH)
canvas.pack()

bg_image = app.PhotoImage(file='path.png')
bg_label = app.Label(root, image=bg_image)
bg_label.place(relheight=1, relwidth=1)

# frame as in small place holder in window
frame1 = app.Frame(root, bg="#ffd1b3", bd=5)
frame1.place(relx=0.1, rely=0.1, relheight=0.1, relwidth=0.7)

# text for a user entry
entry = app.Entry(frame1, font=('Cambria', 18), bg="white")
entry.place(relx=0, rely=0, relheight=1, relwidth=0.65)

# button
button = app.Button(frame1, text="test button", bg="red", fg="black", command=lambda: button_func(entry.get()))
button.place(relx=0.7, rely=0, relheight=1, relwidth=0.3)

# test frame box to display information
frame2 = app.Frame(root, bg="#ffd1b3", bd=10)
frame2.place(relx=0.1, rely=0.3, relheight=0.6, relwidth=0.7)

# label to display data
label = app.Label(frame2, bd=10, font=('Cambria', 18), anchor='nw', justify='left')
label.place(relheight=1, relwidth=1)

root.mainloop()
