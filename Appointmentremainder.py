import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox
from tkinter.ttk import Combobox
import re
import random
import sqlite3
import os
root = tk.Tk()
root.geometry("1200x800")
bg_colour = '#273b7a'
def init_database():
    if os.path.exists('patients_account.db'):
        connection = sqlite3.connect('patients_account.db')
        cursor =connection.cursor()
        cursor.execute("""
        SELECT * FROM data
        """)
        connection.commit()
        print(cursor.fetchall())
        connection.close()
        
    else:
        connection = sqlite3.connect('patients_account.db')
        cursor =connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS data (
        id_number text,
        password text,
        name text,
        age text,
        gender text,
        phone_number text,
        address text,
        email text


        
        )
        """)
        connection.commit()
        connection.close()
def add_data(id_number,password ,name,age,gender,phone_number,address ,email):
     connection = sqlite3.connect('patients_account.db')
     cursor =connection.cursor()
     cursor.execute(f"""
     INSERT INTO data VALUES('{id_number}','{password}','{name}','{age}','{gender}','{phone_number}','{address}','{email}')
     """)
     connection.commit()
     connection.close()
def check_id_already(id_number):
    connection = sqlite3.connect('patients_account.db')
    cursor =connection.cursor()
    cursor.execute("""
    SELECT id_number FROM data WHERE id_number =='{id_number}'
    """)
    connection.commit()
    response =cursor.fetchall()
    connection.close()
    return response

        

def patient_page():
    global user_name
    global pass_word
    def check_function():
        if user_name.get() == "" or pass_word.get() == "":
            messagebox.showerror("ERROR", "PLEASE FILL ABOVE DETAILS", parent=root)
        elif user_name.get() != "sureshkumar" or pass_word.get() != "12345":
            messagebox.showerror("ERROR", "INVALID USERNAME OR PASSWORD", parent=root)
        else:
            frame1.destroy()
            root.update()
            patientnext_page()
    def forward_to_welcome_page():
        frame1.destroy()
        root.update()
        welcome_page()
    root.title("PATIENT PAGE")

    # BACKGROUND IMAGE
    bg = ImageTk.PhotoImage(file=r"D:\zip files\wp3182859-space-background-hd.jpg")
    bg_image = tk.Label(root, image=bg)
    bg_image.place(x=0, y=0, relwidth=1, relheight=1)

    # frame
    frame1 = tk.Frame(root, bg="white")
    frame1.place(x=650, y=150, width=380, height=450)

    # title
    title = tk.Label(frame1, text="PATIENT PAGE", font=("Impact", 35, "bold"), fg='#6162FF', bg='white')
    title.place(x=60, y=30)
    # back button
    back_btn=tk.Button(frame1, text="BACK",cursor="hand2",
                       font=("GOUDY old style", 14, "bold"), fg="#6162FF", bg="white",command=forward_to_welcome_page)
    back_btn.place(x=150, y=370)

    # username
    user_name_label = tk.Label(frame1, text="USERNAME:", font=("GOUDY", 15), fg='grey', bg='white')
    user_name_label.place(x=20, y=120)
    user_name = tk.Entry(frame1, font=("TIMES NEW ROMAN", 12), fg='black', bg='white')
    user_name.place(x=20, y=160, width=320, height=35)

    # password
    pass_word_label = tk.Label(frame1, text="PASSWORD:", font=("GOUDY", 15), fg='grey', bg='white')
    pass_word_label.place(x=20, y=200)
    pass_word = tk.Entry(frame1, font=("TIMES NEW ROMAN", 12), fg='black', bg='white')
    pass_word.place(x=20, y=240, width=320, height=35)

    # button
    log_in = tk.Button(frame1, text="LOG IN", command=check_function, cursor="hand2",
                       font=("GOUDY old style", 14, "bold"), fg="#6162FF", bg="white")
    log_in.place(x=140, y=310)
def patientnext_page():
    def forward_to_welcome_page():
        admin_page.destroy()
        root.update()
        welcome_page()
    def seedetials_page():
        admin_page.destroy()
        root.update()
        
        root.title("PATIENT DETIAL PAGE")
        # frame
        frame1 = tk.Frame(root, bg="white")
        frame1.place(x=650, y=150, width=380, height=450)

    # title
        title = tk.Label(frame1, text="PATIENT DETIALS", font=("Impact", 35, "bold"), fg='#6162FF', bg='white')
        title.place(x=60, y=30)
        info_lb=tk.Label(frame1,text="""  Patient name XXXX he has an  cancer""",font=('Bold',13))
        info_lb.place(x=8,y=250)
        
    def mail_send():
        from email.message import EmailMessage
        import smtplib
        import ssl

        email_sender = 'entrepreneur3004@gmail.com'
        email_password = 'uhnrkmtcnyyltjzj'

        email_receiver = 'dummypro435@gmail.com'
        subject = "APPOINTMENT"
        body = """
        Hey doc i need a appointment on that day[31-5-2023]
        """

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject 
        em.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
    root.title('appointment page')
    # BACKGROUND IMAGE
    bg = ImageTk.PhotoImage(file=r"D:\zip files\wp3182859-space-background-hd.jpg")
    bg_image = tk.Label(root, image=bg)
    bg_image.place(x=0, y=0, relwidth=1, relheight=1)

    # frame
    admin_page = tk.Frame(root, highlightbackground=bg_colour, highlightthickness=5)
    admin_page.pack(pady=30)
    admin_page.configure(width=450, height=500)
    # title
    heading_lb = tk.Label(admin_page, text="PATIENT APPOINTMENT PAGE", font=('Bold', 18), bg=bg_colour, fg='white')
    heading_lb.place(x=0, y=0, width=450, height=50)
    # apointment button
    log_in = tk.Button(admin_page, text="MAKE APPOINTMENT", command=mail_send, cursor="hand2",
                       font=("GOUDY old style", 14, "bold"), fg="black", bg="green")
    log_in.place(x=90, y=200)
    #see detials button
    log_in = tk.Button(admin_page, text="SEE DETIALS", command=seedetials_page, cursor="hand2",
                       font=("GOUDY old style", 14, "bold"), fg="black", bg="white")
    log_in.place(x=90, y=300)
     # back button
    
    back_btn=tk.Button(admin_page, text="BACK",cursor="hand2",
                       font=("GOUDY old style", 14, "bold"), fg="black", bg="white",command=forward_to_welcome_page)
    back_btn.place(x=90, y=400)
    


def doctor_page():
    global user_name
    global pass_word
    def check_function():
        if user_name.get() == "" or pass_word.get() == "":
            messagebox.showerror("ERROR", "PLEASE FILL ABOVE DETAILS", parent=root)
        elif user_name.get() != "sureshkumar" or pass_word.get() != "12345":
            messagebox.showerror("ERROR", "INVALID USERNAME OR PASSWORD", parent=root)
        else:
            admin_page.destroy()
            root.update()
            docnext_page()
    def mail_send():
        from email.message import EmailMessage
        import smtplib
        import ssl

        email_sender = 'dummypro435@gmail.com'
        email_password = 'aqmtnwpsbdpleqhq'

        email_receiver = 'vsksuresh1010@gmail.com'
        subject = "APPOINTMENT"
        body = """
        Hi family i accepted your appointment you can come at your mentioned date.
        """

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject  # Corrected field name
        em.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())






    def forward_to_welcome_page():
        admin_page.destroy()
        root.update()
        welcome_page()
    root.title("DOCTOR PAGE")

    # BACKGROUND IMAGE
    bg = ImageTk.PhotoImage(file=r"D:\zip files\wp3182859-space-background-hd.jpg")
    bg_image = tk.Label(root, image=bg)
    bg_image.place(x=0, y=0, relwidth=1, relheight=1)

    # frame
    admin_page = tk.Frame(root, highlightbackground=bg_colour, highlightthickness=5)
    admin_page.pack(pady=30)
    admin_page.configure(width=450, height=500)
    # back button
    
    back_btn=tk.Button(admin_page, text="BACK",cursor="hand2",
                       font=("GOUDY old style", 14, "bold"), fg="#6162FF", bg="white",command=forward_to_welcome_page)
    back_btn.place(x=280, y=400)


    # title
    heading_lb = tk.Label(admin_page, text="DOCTOR LOG IN PAGE", font=('Bold', 18), bg=bg_colour, fg='white')
    heading_lb.place(x=0, y=0, width=450, height=50)

    # username
    user_name_label = tk.Label(admin_page, text="USERNAME:", font=("GOUDY", 15), fg='grey', bg='white')
    user_name_label.place(x=20, y=120)
    user_name = tk.Entry(admin_page, font=("TIMES NEW ROMAN", 12), fg='black', bg='white')
    user_name.place(x=50, y=180, width=320, height=35)

    # password
    pass_word_label = tk.Label(admin_page, text="PASSWORD:", font=("GOUDY", 15), fg='grey', bg='white')
    pass_word_label.place(x=20, y=240)
    pass_word = tk.Entry(admin_page, font=("TIMES NEW ROMAN", 12), fg='black', bg='white')
    pass_word.place(x=50, y=280, width=320, height=35)

    # button
    log_in = tk.Button(admin_page, text="LOG IN", command=check_function, cursor="hand2",
                       font=("GOUDY old style", 14, "bold"), fg="#6162FF", bg="white")
    log_in.place(x=80, y=400)
def docnext_page():
    def forward_to_welcome_page():
        admin_page.destroy()
        root.update()
        welcome_page()
    def mail_send():
        from email.message import EmailMessage
        import smtplib
        import ssl

        email_sender = 'dummypro435@gmail.com'
        email_password = 'aqmtnwpsbdpleqhq'

        email_receiver = 'vsksuresh1010@gmail.com'
        subject = "APPOINTMENT"
        body = """
        Hi family i accepted your appointment you can come at your mentioned date.
        """

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject 
        em.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
    def rejected_mail():
        from email.message import EmailMessage
        import smtplib
        import ssl

        email_sender = 'dummypro435@gmail.com'
        email_password = 'aqmtnwpsbdpleqhq'

        email_receiver = 'entrepreneur3004@gmail.com'
        subject = "APPOINTMENT"
        body = """
        Hi family Sorry for the incovenience i have other appointments on that day you can choose another day
        """

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject  # Corrected field name
        em.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

        
    root.title('appointment page')
    # BACKGROUND IMAGE
    bg = ImageTk.PhotoImage(file=r"D:\zip files\wp3182859-space-background-hd.jpg")
    bg_image = tk.Label(root, image=bg)
    bg_image.place(x=0, y=0, relwidth=1, relheight=1)

    # frame
    admin_page = tk.Frame(root, highlightbackground=bg_colour, highlightthickness=5)
    admin_page.pack(pady=30)
    admin_page.configure(width=450, height=500)
    # title
    heading_lb = tk.Label(admin_page, text="DOCTOR  NEXT LOG IN PAGE", font=('Bold', 18), bg=bg_colour, fg='white')
    heading_lb.place(x=0, y=0, width=450, height=50)
    # accept button
    log_in = tk.Button(admin_page, text="ACCEPT", command=mail_send, cursor="hand2",
                       font=("GOUDY old style", 14, "bold"), fg="#6162FF", bg="white")
    log_in.place(x=80, y=100)
    #reject button
    
    log_in = tk.Button(admin_page, text="REJECT",command=rejected_mail,cursor="hand2",
                       font=("GOUDY old style", 14, "bold"), fg="#6162FF", bg="white")
    log_in.place(x=80, y=200)
    # send detials button
    log_in = tk.Button(admin_page, text="SEND DETIALS",cursor="hand2",
                       font=("GOUDY old style", 14, "bold"), fg="#6162FF", bg="white")
    log_in.place(x=80, y=300)
    # back button
    back_btn=tk.Button(admin_page, text="BACK",cursor="hand2",
                       font=("GOUDY old style", 14, "bold"), fg="#6162FF", bg="white",command=forward_to_welcome_page)
    back_btn.place(x=80, y=370)

def welcome_page():
    def forward_to_patient_login_page():
        root.title("PATIENT PAGE")
        admin_page.destroy()
        patient_page()
    def forward_to_doctor_login_page():
        
        admin_page.destroy()
        doctor_page()
    def forward_to_newaccount_login_page():
        
        admin_page.destroy()
        createaccount_page()

    root.title("welcome page")
    # BACKGROUND IMAGE
    bg = ImageTk.PhotoImage(file=r"D:\zip files\wp3182859-space-background-hd.jpg")
    bg_image = tk.Label(root, image=bg)
    bg_image.place(x=0, y=0, relwidth=1, relheight=1)
    # frame
    admin_page = tk.Frame(root, highlightbackground=bg_colour, highlightthickness=5)
    admin_page.pack(pady=30)
    admin_page.configure(width=450, height=500)
    # title
    heading_lb = tk.Label(admin_page, text="WELCOME PAGE", font=('Bold', 18), bg='#273b7a', fg='white')
    heading_lb.place(x=0, y=0, width=450, height=50)
    # patient login
    stulogin_lb = tk.Button(admin_page, text="PATIENT LOGIN", font=("GOUDY", 15), fg='grey', bg='#273b7a',
                            command=forward_to_patient_login_page)
    stulogin_lb.place(x=140, y=120)
    # doctor login
    doctor_lb = tk.Button(admin_page, text="DOCTOR LOGIN", font=("GOUDY", 15), fg='grey', bg='#273b7a',command=forward_to_doctor_login_page)
    doctor_lb.place(x=140, y=220)
    # create account
    createacc_lb = tk.Button(admin_page, text="CREATE ACCOUNT", font=("GOUDY", 15), fg='grey', bg='#273b7a',command=forward_to_newaccount_login_page)
    createacc_lb.place(x=140, y=320)

def createaccount_page():
    global patientname_ent
    global age_ent
    global accpassword_ent
    global mobileno_ent
    global email_ent
    global address_ent
    def generate_id_number():
        generated_id=''

        for r in range(6):
            generated_id+=str(random.randint(0,9))


        if not check_id_already(id_number=generated_id):
            print('ID number :',generated_id)
            patient_id.config(state=tk.NORMAL)
            patient_id.delete(0,tk.END)
            patient_id.insert(tk.END,generated_id)
            patient_id.config(state='readonly')
        else:
            generate_id_number()


    def check_invalid_email(email):
        pattern =r'^[\w\.-]+@[\w\.-]+\.\w+$'
        match = re.match(pattern=pattern,string=email)
        return match
    def remove_highlight(entry):
        if entry['highlightbackground']!='gray':
            if entry.get()!='':
                entry.config(highlightcolor=bg_colour,highlightbackground='gray')

    def check_infunction():
        if patientname_ent.get()=='':
            patientname_ent.config(highlightcolor='red',highlightbackground='red')
            patientname_ent.focus()
            messagebox.showerror("ERROR", "PLEASE FILL THE PATIENT DETIALS", parent=root)
        elif age_ent.get()=='':
            age_ent.config(highlightcolor='red',highlightbackground='red')
            age_ent.focus()
            messagebox.showerror("ERROR", "PLEASE FILL THE PATIENT AGE", parent=root)
        elif mobileno_ent.get()=='':
            mobileno_ent.config(highlightcolor='red',highlightbackground='red')
            mobileno_ent.focus()
            messagebox.showerror("ERROR", "PLEASE FILL THE MOBILE NUMBER", parent=root)
        elif address_ent.get()=='':
            address_ent.config(highlightcolor='red',highlightbackground='red')
            address_ent.focus()
            messagebox.showerror("ERROR", "PLEASE FILL THE ADDRESS", parent=root)
        elif email_ent.get()=='':
            email_ent.config(highlightcolor='red',highlightbackground='red')
            email_ent.focus()
            messagebox.showerror("ERROR", "ENTER THE MAIL ID", parent=root)
        elif not check_invalid_email(email=email_ent.get().lower()):
            email_ent.config(highlightcolor='red',highlightbackground='red')
            email_ent.focus()
            messagebox.showerror("ERROR", "ENTER THEMAIL ID", parent=root)
        elif accpassword_ent.get()=='':
            accpassword_ent.config(highlightcolor='red',highlightbackground='red')
            accpassword_ent.focus()
            messagebox.showerror("ERROR", "ENTER THE PASSWORD", parent=root)
        else:
            add_data(id_number=patient_id.get() ,
        password=accpassword_ent.get(),
        name=patientname_ent.get(),
        age=age_ent.get(),
        gender=gender.get(),
        phone_number=mobileno_ent.get(),
        address=address_ent.get(),
        email=email_ent.get())
        messagebox.showinfo('Account Successfully created')
    def forward_to_welcome_page():
        createacc_page.destroy()
        root.update()
        welcome_page()
    gender=tk.StringVar()
    #frame
    createacc_page = tk.Frame(root, highlightbackground=bg_colour, highlightthickness=5)
    createacc_page.pack(pady=30)
    createacc_page.configure(width=1000, height=700)
    # title
    heading_lb = tk.Label(createacc_page, text="CREATE ACCOUNT", font=('Bold', 18), bg='#273b7a', fg='white')
    heading_lb.place(x=0, y=0, width=1200, height=40)
    #username
    patientname_acc=tk.Label(createacc_page,text='ENTER THE PATIENT NAME :',font=('Bold',15))
    patientname_acc.place(x=5,y=100)
    patientname_ent=tk.Entry(createacc_page,font=('bold',13),highlightcolor=bg_colour,highlightbackground='gray', highlightthickness=2)
    patientname_ent.place(x=5,y=140,width=270,height=40)
    patientname_ent.bind('<KeyRelease>',lambda e:remove_highlight(entry=patientname_ent))
    #gender
    gender_lb=tk.Label(createacc_page,text='GENDER :',font=('Bold',15))
    gender_lb.place(x=5,y=200)
    male_btn=tk.Radiobutton(createacc_page,text='MALE',font=('Bold',12),variable=gender,value='MALE')
    male_btn.place(x=5,y=240)
    female_btn=tk.Radiobutton(createacc_page,text='FEMALE',font=('Bold',12),variable=gender,value='FEMALE')
    female_btn.place(x=100,y=240)
    gender.set('MALE')
    #patient age
    age_lb=tk.Label(createacc_page,text='ENTER THE PATIENT AGE :',font=('Bold',15))
    age_lb.place(x=5,y=300)
    age_ent=tk.Entry(createacc_page,font=('bold',13),highlightcolor=bg_colour,highlightbackground='gray', highlightthickness=2)
    age_ent.place(x=5,y=340,width=270,height=40)
    age_ent.bind('<KeyRelease>',lambda e:remove_highlight(entry=age_ent))
    #patient contact number
    mobileno_lb=tk.Label(createacc_page,text='ENTER THE MOBILE NUMBER :',font=('Bold',15))
    mobileno_lb.place(x=5,y=400)
    mobileno_ent=tk.Entry(createacc_page,font=('bold',13),highlightcolor=bg_colour,highlightbackground='gray', highlightthickness=2)
    mobileno_ent.place(x=5,y=440,width=270,height=40)
    mobileno_ent.bind('<KeyRelease>',lambda e:remove_highlight(entry=mobileno_ent))
    #address
    address_lb=tk.Label(createacc_page,text='ENTER PATIENT ADDRESS:',font=('Bold',15))
    address_lb.place(x=5,y=500)
    address_ent=tk.Entry(createacc_page,font=('bold',13),highlightcolor=bg_colour,highlightbackground='gray', highlightthickness=2)
    address_ent.place(x=5,y=540,width=270,height=40)
    address_ent.bind('<KeyRelease>',lambda e:remove_highlight(entry=address_ent))
    #patient id
    id_lb=tk.Label(createacc_page,text='PATIENT ID :',font=('bold',15))
    id_lb.place(x=550,y=100)
    patient_id=tk.Entry(createacc_page,font=('Bold',18),bd=0)
    patient_id.place(x=700,y=97,width=200,height=40)
    patient_id.insert(tk.END,'123456')
    patient_id.configure(state='readonly')
    #generate_id_number()
    #id info
    info_lb=tk.Label(createacc_page,text="""    Automatically Generated ID NUMBER 
    ! Remember Using This ID NUMBER
    Patient Will LOG IN ACCOUNT""",font=('Bold',13),justify=tk.LEFT)
    info_lb.place(x=530,y=130)
    #email id
    email_lb=tk.Label(createacc_page,text='ENTER EMAIL ADDRESS:',font=('Bold',15))
    email_lb.place(x=550,y=220)
    email_ent=tk.Entry(createacc_page,font=('bold',13),highlightcolor=bg_colour,highlightbackground='gray', highlightthickness=2)
    email_ent.place(x=550,y=260,width=270,height=40)
    email_ent.bind('<KeyRelease>',lambda e:remove_highlight(entry=email_ent))
    #email id info
    emailinfo_lb=tk.Label(createacc_page,text="""    Via Email Address Student
    can Recover Account
    ! In Case Forgetting password And Also
    student will get Future Notification""",font=('Bold',12),justify=tk.LEFT)
    emailinfo_lb.place(x=530,y=300)
    #password
    accpassword_lb=tk.Label(createacc_page,text='ENTER PATIENT PASSWORD:',font=('Bold',15))
    accpassword_lb.place(x=550,y=400)
    accpassword_ent=tk.Entry(createacc_page,font=('bold',12),highlightcolor=bg_colour,highlightbackground='gray', highlightthickness=2)
    accpassword_ent.place(x=550,y=440,width=270,height=40)
    accpassword_ent.bind('<KeyRelease>',lambda e:remove_highlight(entry=accpassword_ent))
    #home and submit button
    home_btn=tk.Button(createacc_page,text='HOME',font=('Bold',15,),bg='red',fg='white',bd=0,command=forward_to_welcome_page)
    home_btn.place(x=570,y=520)
    submit_btn=tk.Button(createacc_page,text='SUBMIT',font=('Bold',14,),bg='blue',fg='white',bd=0,command=check_infunction)
    submit_btn.place(x=700,y=520)
welcome_page()
root.mainloop()
