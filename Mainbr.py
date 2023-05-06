import tkinter as tk
##from PIL import Image,ImageTk
##from io import BytesIO
##import requests

def welcome():
    
    
    welcome_window = tk.Tk()
    welcome_window.title("Welcome to Bus Reservation System")
    
    
    
    welcome_window.geometry("1200x800")
    
    
    welcome_label = tk.Label(welcome_window, text="Welcome to Bus Reservation System!\n \n By-Aishwarya Kumar Singh\n \n XII-D\n \n Click on Enter to Continue", font=("Arial", 20))
    welcome_label.pack(pady=50)
    def enter():
        welcome_window.destroy()
        home()
        
    
    enter_button = tk.Button(welcome_window, text="Enter", command=enter)
    enter_button.pack(pady=20)
    
    welcome_window.mainloop()


def home():
    
    
    
    home = tk.Tk()
    home.geometry("1200x800")
    home.config(bg="white")
    home.title("AK TRAVEL AGENCY ")
    label=tk.Label(home , text="WELCOME TO AK AGENCY",bg="red",font=("Arial",18))
    label.grid(row=0,column=7)
    global name
    global age
    global gender
    global frm
    global to
    global date
    global company
    global mobile
    global email
    global seat
    
    name=tk.StringVar()
    age=tk.StringVar()
    gender=tk.StringVar()
    frm=tk.StringVar()
    to=tk.StringVar()
    date=tk.StringVar()
    company=tk.StringVar()
    mobile=tk.StringVar()
    email=tk.StringVar()
    seat=tk.StringVar()

    
    
        
    def switch():
        home.destroy()
        ticket()


    name_label = tk.Label(home, text="Name",bg="white")
    name_label.grid(row=1, column=0)
    name_entry = tk.Entry(home,textvariable=name)
    name_entry.grid(row=1, column=1)

    age_label = tk.Label(home, text="Age",bg="white")
    age_label.grid(row=2, column=0)
    age_entry = tk.Entry(home,textvariable=age)
    age_entry.grid(row=2, column=1)

    gender_label = tk.Label(home, text="Gender",bg="white")
    gender_label.grid(row=3, column=0)
    
    male_radio = tk.Radiobutton(home, text="Male",bg="white", variable=gender, value="Male")
    male_radio.grid(row=3, column=1)
    female_radio = tk.Radiobutton(home, text="Female",bg="white", variable=gender, value="Female")
    female_radio.grid(row=3, column=2)

    frm_label = tk.Label(home, text="from",bg="white")
    
    frm_label.grid(row=5, column=0)    # 
##    frm_entry = tk.Entry(home,textvariable=frm)
    From_dropdown = tk.OptionMenu(home, frm ,"DELHI","MUMBAI","JAIPUR","NAGPUR","AGRA","INDORE")
    frm.set("Select A Boarding City")
    From_dropdown.grid(row=5, column=1)    

    to_label = tk.Label(home, text="To",bg="white")
    to_label.grid(row=6, column=0)
##    to_entry = tk.Entry(home,textvariable=to)
    to_dropdown = tk.OptionMenu(home, to ,"DELHI","MUMBAI","JAIPUR","NAGPUR","AGRA","INDORE")
    to.set("Select Your Destination")
    to_dropdown.grid(row=6, column=1)

    date_label = tk.Label(home, text="Date",bg="white")
    date_label.grid(row=7, column=0)
    date_entry = tk.Entry(home,textvariable=date)
    date_entry.grid(row=7, column=1)

    company_label = tk.Label(home, text="Travel Company",bg="white")
    company_label.grid(row=8, column=0)
    
    company_dropdown = tk.OptionMenu(home, company, "Hans Travels", "Sharma Travels", "Verma Travels", "Chartered", "Patel Tours and Travels")
    company_dropdown.grid(row=8, column=1)

    mobile_label = tk.Label(home, text="Mobile Number",bg="white")
    mobile_label.grid(row=9, column=0)
    mobile_entry = tk.Entry(home,textvariable=mobile)
    mobile_entry.grid(row=9, column=1)

    email_label = tk.Label(home, text="Email",bg="white")
    email_label.grid(row=10, column=0)
    email_entry = tk.Entry(home,bg="white",textvariable=email)
    email_entry.grid(row=10, column=1)

    seat_label = tk.Label(home, text="Seat Number",bg="white")
    seat_label.grid(row=11, column=0)
    seat_dropdown=tk.OptionMenu(home, seat, "4", "7", "12", "15", "16","19","24")
    seat_dropdown.grid(row=11, column=1)
    
    
    
    change=tk.Button(home,text="SUBMIT",bg="red",command=switch)
    change.grid(row=12, column=2)

##    submit_button = tk.Button(home, text="Submit", command=submit)
##    submit_button.grid(row=11, column=0,)
    home.mainloop()

def ticket():
    ticket=tk.Tk()
    ticket.geometry("1200x800")
    
    inp=tk.Text(ticket,width=1200,height=800,font="Arial 20")
    inp.pack(pady = 50)
##    ticket.config(bg="black")
##    inp.insert(INSERT,name.get())
##    inp.insert(INSERT,age.get())
##    inp.insert(INSERT,gender.get())
##    inp.insert(INSERT,gender.get())
##    inp.insert(INSERT,frm.get())
##    inp.insert(INSERT,to.get())
##    inp.insert(INSERT,date.get())
##    inp.insert(INSERT,comapany.get())
##    inp.insert(INSERT,mobile.get())
##    inp.insert(INSERT,email.get())
##    inp.insert(INSERT,seat.get())
    
    ticket.mainloop()
welcome()    
##home()
