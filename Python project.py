from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


# Creating a screen for
screen = Tk()
screen.geometry("600x550")
screen.title("Age Calculator")
img = ImageTk.PhotoImage(Image.open("C:\\Users\\rauf.alibakhshov\\Downloads\\AgeCalculator.png"))
title = Label(screen, image=img )
# screen.attributes('-alpha',0.9)
# title = Label(text="Age Calculator", bg="lightblue", fg="black", width="80", height="2",font="Arial 18 bold italic")
title.pack()

# Creating selectbox for Date
date_value = StringVar()
date = ttk.Combobox(screen, width=3, textvariable=date_value)
date['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                  '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
date.place(x=255, y=80)


# Creating selectbox for Month
month_value = StringVar()
month = ttk.Combobox(screen, width=3, textvariable=month_value)
month['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
month.place(x=370, y=80)


# Creating selectbox for Year
year_value = StringVar()
year = ttk.Combobox(screen, width=7, textvariable=year_value)
year['values'] = ('1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1970',
                  '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980','1981' , '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990',
                   '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001',
                  '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010')
year.place(x=475, y=80)


# defining a function to close the screen
def close():
    screen.destroy()

# Creating labels for the inputs
liv_text = Label(text="You have been living for:", font="Ariel 16 bold" , bg="dodgerblue4", fg="white")
date_text = Label(text="Date", font="Ariel 16 bold" , bg="dodgerblue4", fg="white")
month_text = Label(text="Month", bg="dodgerblue4", fg="white", font="Ariel 16 bold")
year_text = Label(text="Year", bg="dodgerblue4", fg="white", font="Ariel 16 bold")
month1_text = Label(text="In months:", bg="dodgerblue4", fg="white", font="Ariel 16 bold")
day_text = Label(text="In days:", bg="dodgerblue4", fg="white", font="Ariel 16 bold")
hour_text = Label(text="In hours:", bg="dodgerblue4", fg="white", font="Ariel 16 bold")
minute_text = Label(text="In minutes:", bg="dodgerblue4", fg="white", font="Ariel 16 bold")
next_birthday_text = Label(text="Your next birthday will be in:", bg="dodgerblue4", fg="white", font="Ariel 16 bold")

# Packing the labels
liv_text.place(x=100, y=120)
date_text.place(x=200, y=75)
month_text.place(x=300, y=75)
year_text.place(x=420, y=75)
month1_text.place(x=100, y=160)
day_text.place(x=100, y=200)
hour_text.place(x=100, y=240)
minute_text.place(x=100, y=285)
next_birthday_text.place(x=100, y=330)

# Creating an entries
month_entry = Entry(width="30", bd="3")
day_entry = Entry(width="34", bd="3")
hour_entry = Entry(width="33", bd="3")
minute_entry = Entry(width="30", bd="3")
next_birthday_entry = Entry(width="45", bd="3")

# Packing the entries
month_entry.place(x="225", y="165")
day_entry.place(x="200", y="203")
hour_entry.place(x="205", y="245")
minute_entry.place(x="225", y="287")
next_birthday_entry.place(x="100", y="370")

# Calculation button
Calculate = Button(screen, text="Calculate", width="3", height="9", bd="5", fg="black", font="Arial 16 bold", wraplength=5)
Calculate.place(x="425", y="120")

screen.mainloop()


