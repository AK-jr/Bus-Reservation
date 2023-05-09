import tkinter as tk
from PIL import Image,ImageTk
from io import BytesIO
import requests

def welcome():

    #Creation of Welcome Window
    welcome_window = tk.Tk()
    welcome_window.title("Welcome to Bus Reservation System")
    welcome_window.attributes('-fullscreen', True)
    welcome_window.geometry("1200x800")
    
    #Applying background Image
    response = requests.get("https://edunext-main-storage-cf.edunexttechnologies.com/dalycollege/school___static/1677579944412_final_logo.jpg")
    img = Image.open(BytesIO(response.content))
    img = img.resize((1350,900), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = tk.Label(image=test)
    bk.image = test
    bk.place(x=0, y=0)

    
    #putting text in Welcom window
    welcome_label = tk.Label(welcome_window,bg="white", text="Welcome to Bus Reservation System!\n \n By-Aishwarya Kumar Singh\n \n XII-D\n \n Click on Enter to Continue", font=("Arial", 20))
    welcome_label.pack(pady=0)
    
    def enter():
        welcome_window.destroy()    #defining function to switch windows
        home()
                                            
    
    enter_button = tk.Button(welcome_window, text="Enter",padx=70,pady=15,bg="White" ,command=enter)
    enter_button.pack(pady=20)
    
    exit_button=tk.Button(welcome_window,text="EXIT",bg="red",padx=30,pady=70,command=welcome_window.destroy)
    exit_button.pack(pady=200)
    welcome_window.mainloop()


def home():
    
    
    #Creating New Window For inputting Ticket Details
    home = tk.Tk()
    home.geometry("1200x800")
    home.config(bg="white")
    home.title("AK TRAVEL AGENCY ")
    home.attributes('-fullscreen', True)
    
    response = requests.get("https://img.freepik.com/premium-vector/bus-logo-abstract_7315-17.jpg")
    img = Image.open(BytesIO(response.content))
    img = img.resize((1350,800), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = tk.Label(image=test)
    bk.image = test
    bk.place(x=0, y=0)
    
    label=tk.Label(home , text="WELCOME TO AK AGENCY",bg="red",font=("Arial",18))
    label.grid(row=0,column=7)
    global name
    global age
    global gender
    global frm
    global to
    global date
    global month
    global year
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
    month=tk.StringVar()
    year=tk.StringVar()
    company=tk.StringVar()
    mobile=tk.StringVar()
    email=tk.StringVar()
    seat=tk.StringVar()

    
    
        
    def switch():
        home.destroy()
        payment()


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
    
    frm_label.grid(row=5, column=0)    

    From_dropdown = tk.OptionMenu(home, frm ,"DELHI","MUMBAI","JAIPUR","NAGPUR","AGRA","INDORE")
    frm.set("Select A Boarding City")
    From_dropdown.grid(row=5, column=1)    

    to_label = tk.Label(home, text="To",bg="white")
    to_label.grid(row=6, column=0)

    to_dropdown = tk.OptionMenu(home, to ,"DELHI","MUMBAI","JAIPUR","NAGPUR","AGRA","INDORE")
    to.set("Select Your Destination")
    to_dropdown.grid(row=6, column=1)

    date_label = tk.Label(home, text="Date",bg="white")
    date_label.grid(row=7, column=0)
    date_dropdown = tk.OptionMenu(home,date,"1","4","5","8","15","16","18","22","25","29","30")
    date.set("Select Date")
    date_dropdown.grid(row=7, column=1)


    month_label = tk.Label(home, text="Month",bg="white")
    month_label.grid(row=8, column=0)
    month_dropdown = tk.OptionMenu(home,month,"January","February","March","April","May","June","July","August")
    month.set("Select Month")
    month_dropdown.grid(row=8, column=1)
    

    year_label = tk.Label(home, text="Year",bg="white")
    year_label.grid(row=9, column=0)
    year_dropdown = tk.OptionMenu(home,year,"2023","2024","2025")
    year.set("Select Year")
    year_dropdown.grid(row=9, column=1)
    

    company_label = tk.Label(home, text="Travel Company",bg="white")
    company_label.grid(row=10, column=0)
    
    company_dropdown = tk.OptionMenu(home, company, "Hans Travels", "Sharma Travels", "Verma Travels", "Chartered", "Patel Tours and Travels")
    company_dropdown.grid(row=10, column=1)

    mobile_label = tk.Label(home, text="Mobile Number",bg="white")
    mobile_label.grid(row=11, column=0)
    mobile_entry = tk.Entry(home,textvariable=mobile)
    mobile_entry.grid(row=11, column=1)
    mobile.set("+91")

    email_label = tk.Label(home, text="Email",bg="white")
    email_label.grid(row=12, column=0)
    email_entry = tk.Entry(home,bg="white",textvariable=email)
    email_entry.grid(row=12, column=1)
    email.set("  @gmail.com")

    seat_label = tk.Label(home, text="Seat Number",bg="white")
    seat_label.grid(row=13, column=0)
    seat_dropdown=tk.OptionMenu(home, seat, "4", "7", "12", "15", "16","19","24")
    seat.set("Select your Seat Number")
    seat_dropdown.grid(row=13, column=1)
    

    
    exithome_button=tk.Button(home, text="EXIT",bg="red",padx=70,pady=10,command=home.destroy)
    exithome_button.grid(row=8,column=15)
    
    
    
    change=tk.Button(home,text="SUBMIT",bg="cyan",padx=70,pady=10,command=switch)
    change.grid(row=15, column=2)


    home.mainloop()

def payment():
    
    pay = tk.Tk()
    pay.title("Payment System")
    pay.config(bg="white")
    pay.attributes('-fullscreen', True)

    response = requests.get("https://img.freepik.com/premium-vector/bus-logo-abstract_7315-17.jpg")
    img = Image.open(BytesIO(response.content))
    img = img.resize((1350,800), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = tk.Label(image=test)
    bk.image = test
    bk.place(x=0, y=0)

    
    amount_label = tk.Label(pay, text=f" Total Amount: 700/- ")
    amount_label.pack(pady=10)
    
    # Credit card number entry
    card_label = tk.Label( pay,text="Enter Credit Card Number:")
    card_label.pack()
    pay.card_entry = tk.Entry( pay,show="*")
    pay.card_entry.pack(pady=5)

    # Expiration date entry
    exp_label = tk.Label(pay, text=("Enter Expiration Date (MM/YY):"))
    exp_label.pack()
    pay.exp_entry = tk.Entry(pay)
    pay.exp_entry.pack(pady=5)

     # CVV number entry
    cvv_label = tk.Label(pay, text="Enter CVV Number:")
    cvv_label.pack()
    pay.cvv_entry = tk.Entry( pay,show="*")
    pay.cvv_entry.pack(pady=5)

    def con():
        pay.destroy()
        thankyou()

    continue_button=tk.Button(pay, text="CONTINUE",bg="GREEN",padx=70,pady=10,command=con)
    continue_button.pack(pady=6)
    
    exitpay_button=tk.Button(pay, text="EXIT",bg="red",padx=70,pady=10,command=pay.destroy)
    exitpay_button.pack(pady=8)   

  
    pay.mainloop()

    

#window for thanking customer For choosing us     

def thankyou():
    thx_window = tk.Tk()
    thx_window.title("Thank you")
    thx_window.config(bg="white")
    thx_window.attributes('-fullscreen', True)    
    thx_window.geometry("1200x800")
    response = requests.get("https://img.freepik.com/premium-vector/bus-logo-abstract_7315-17.jpg")
    img = Image.open(BytesIO(response.content))
    img = img.resize((1350,800), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = tk.Label(image=test)
    bk.image = test
    bk.place(x=0, y=0)
    Thx_label= tk.Label(thx_window,bg="white", text="PAYMENT SUCCESFULL \n\n\n THANK YOU FOR TRUSTING AK AGENCY\n\nYOUR TICKET WILL BE SEND ON YOUR\nENTERED MAIL AND PHONE NUMBER\n\n TOLL FREE NUMBER 1800 XXXXXX", font=("Arial", 20))
    Thx_label.pack(pady=10)
    
    exitthx_button=tk.Button(thx_window, text="EXIT",bg="red",padx=70,pady=10,command=thx_window.destroy)
    exitthx_button.pack(pady=15)


#Calling function to Start The App    
welcome()    
