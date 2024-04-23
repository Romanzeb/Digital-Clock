from tkinter import Label,Tk
import time

def digital_clock(): 
    # Time info Time_
    time_live = time.strftime("%H:%M:%S")
    Time_label.config(text=time_live)
    # Date info
    date_info = time.strftime("%d %B %Y")
    date_label.config(text=date_info)
    Time_label.after(200,digital_clock)

Digital_clock_app_window = Tk()
Digital_clock_app_window.title("Clock")

Digital_clock_app_window.geometry("225x145")
Digital_clock_app_window.resizable(0,0)
Digital_clock_app_window.configure(bg="Black")

text_font = ("boulder",25,'bold')
background = "Black"
foreground = "White"
border_width = 10

# Time Style
Time_label = Label(Digital_clock_app_window,font=text_font,bg=background,fg=foreground,width=border_width)
Time_label.grid(row=0,column=1,padx=border_width,pady=10)

# Date Style
date_label = Label(Digital_clock_app_window,font=text_font,bg=background,fg=foreground,width=border_width)
date_label.grid(row=1,column=1,padx=border_width,pady=10)


digital_clock()
Digital_clock_app_window.mainloop()


