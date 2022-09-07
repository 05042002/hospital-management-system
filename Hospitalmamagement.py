import datetime
from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk
from tkcalendar import DateEntry  # pip install tkcalendar
import sqlite3

# Creating the universal font variables
headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
labelfont = ('Garamond', 14)
entryfont = ('Garamond', 12)

# Connecting to the Database where all information will be stored
connector = sqlite3.connect('HospitalManagement.db')
cursor = connector.cursor()

connector.execute(
"CREATE TABLE IF NOT EXISTS HOSPITAL_MANAGEMENT (PATIENT_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NAME TEXT, NHS  TEXT, STORAGE TEXT, PROBLEM TEXT, EFFECT TEXT, TABLET TEXT, DOSE TEXT, INFORMATION  TEXT, LOT  TEXT, ISSUE  TEXT, EXP  TEXT, DAILY TEXT,  PRESSURE TEXT, DOB  TEXT , ADDRESS TEXT,REFERENCE TEXT)"
)

def display_records():
    tree.delete(*tree.get_children())

    curr = connector.execute('SELECT * FROM HOSPITAL_MANAGEMENT')
    data = curr.fetchall()

    for records in data:
        tree.insert('', END, values=records)

def reset_fields():
    global reference_strvar, nhs_strvar, storage_strvar, problem_strvar, effect_strvar, tablet_strvar,dose_strvar,information_strvar,lot_strvar,issue_strvar,exp_strvar,daily_strvar,pressure_strvar,name_strvar,dob_strvar,address_strvar

    for i in ['reference_strvar', 'nhs_strvar', 'storage_strvar', 'problem_strvar', 'effect_strvar', 'tablet_strvar','dose_strvar','information_strvar','lot_strvar'
    ,'issue_strvar','exp_strvar','daily_strvar','pressure_strvar','name_strvar','dob_strvar','address_strvar']:
         exec(f"{i}.set('')")
    dob.set_date(datetime.datetime.now().date())


def add_record():
    global reference_strvar, nhs_strvar, storage_strvar, problem_strvar, effect_strvar, tablet_strvar,dose_strvar,information_strvar\
        ,lot_strvar,issue_strvar,exp_strvar,daily_strvar,pressure_strvar,name_strvar,dob_strvar,address_strvar


    reference_no = reference_strvar.get()
    nhs_no = nhs_strvar.get()
    storage_problem = storage_strvar.get()
    problem_detail = problem_strvar.get()
    effect_side = effect_strvar.get()
    tablet = tablet_strvar.get()
    dose_name = dose_strvar.get()
    information = information_strvar.get()
    lot_detail = lot_strvar.get()
    issue_date = issue_strvar.get()
    exp_date = exp_strvar.get()
    daily = daily_strvar.get()
    pressure_blood = pressure_strvar.get()
    name_patient = name_strvar.get()
    dob_date = dob_strvar.get()
    address = address_strvar.get()

    if not reference_no or not nhs_no or not storage_problem or not problem_detail or not effect_side or not\
            tablet or not dose_name or not information or not lot_detail or not issue_date or not exp_date or not daily or not pressure_blood or not name_patient or not dob_date or not address:
        mb.showerror('Error!', "Please fill all the missing fields!!")
    else:
        try:
            connector.execute(
            'INSERT INTO HOSPITAL_MANAGEMENT (NAME,NHS, STORAGE, PROBLEM, EFFECT, TABLET, DOSE,INFORMATION, LOT, ISSUE, EXP ,DAILY,PRESSURE, DOB, ADDRESS ,REFERENCE ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                (reference_no, nhs_no, storage_problem, problem_detail, effect_side, tablet,dose_name,information,lot_detail,
                 issue_date,exp_date,daily,pressure_blood,name_patient,dob_date,address)
            )
            connector.commit()
            mb.showinfo('Record added', f"Record of {name} was successfully added")
            reset_fields()
            display_records()
        except:
            mb.showerror('Wrong type', 'The type of the values entered is not accurate. Pls note that the contact field can only contain numbers')



def remove_record():
    if not tree.selection():
        mb.showerror('Error!', 'Please select an item from the database')
    else:
        current_item = tree.focus()
        values = tree.item(current_item)
        selection = values["values"]

        tree.delete(current_item)

        connector.execute('DELETE FROM HOSPITAL_MANAGEMENT WHERE PATIENT_ID=%d' % selection[0])
        connector.commit()

        mb.showinfo('Done', 'The record you wanted deleted to be is successfully deleted.')

        display_records()


def reset_form():
    global tree
    tree.delete(*tree.get_children())


    reset_fields()


#initializing the GUI WINDOW
main = Tk()
main.title('Student Management System')
main.geometry('1540x800')
main.resizable(0, 0)

# Creating the background and foreground color variables
lf_bg = 'MediumSpringGreen' # bg color for the left_frame
cf_bg = 'PaleGreen' # bg color for the center_frame

# Create ringVar or IntVar variables
reference_strvar = StringVar()
nhs_strvar = StringVar()
storage_strvar = StringVar()
problem_strvar = StringVar()
effect_strvar = StringVar()
tablet_strvar = StringVar()
dose_strvar = StringVar()
information_strvar = StringVar()
lot_strvar = StringVar()
issue_strvar = StringVar()
exp_strvar = StringVar()
daily_strvar = StringVar()
pressure_strvar = StringVar()
name_strvar = StringVar()
dob_strvar = StringVar()
address_strvar = StringVar()


lbltitle=Label(bd=20,relief=RIDGE,text="HOSPITAL MANEGEMENT SYSTEM", fg="orange",bg="white",font=("times new roan",50,"bold"))
lbltitle.pack(side=TOP,fill=X)
# Placing the components in the main window
Label(main, text="STUDENT MANAGEMENT SYSTEM", font=headlabelfont, bg='SpringGreen').pack(side=TOP, fill=X)

left_frame = Frame(main, bd=20, relief=RIDGE)
left_frame.place(x=0, y=130, width=1530, height=400)

DataFrameLeft = LabelFrame(left_frame, bd=10, padx=20, relief=RIDGE, font=("times new roman", 12, "bold"),
                           text="Patient Information")
DataFrameLeft.place(x=0, y=5, width=980, height=350)

# center_frame = Frame(main, bg=cf_bg)
# center_frame.place(relx=0.2, y=30, relheight=1, relwidth=0.2)
DataFrameRight = LabelFrame(left_frame, bd=10, padx=20, relief=RIDGE, font=("times new roman", 12, "bold"),text="Prescription")
DataFrameRight.place(x=990, y=5, width=460, height=350)

right_frame=Frame(main,bd=20,relief=RIDGE) #relief=Ridge is use to give 3 d effect around the out side of the width
right_frame.place(x=0,y=600,width=1530,height=190)

reference=Label(DataFrameLeft,font=("arial",12,"bold"),text="Refence no:",padx=2,pady=6)
reference.grid(row=1,column=0,sticky=W)
txtreference=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=reference_strvar,width=35)
txtreference.grid(row=1,column=1)

dose=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dose",padx=2,pady=6)
dose.grid(row=7,column=0,sticky=W)
txtdose=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=dose_strvar,width=35)
txtdose.grid(row=7,column=1)

lot=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
lot.grid(row=1,column=2,sticky=W)
txtlot=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=lot_strvar,width=35)
txtlot.grid(row=1,column=3)


issue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
issue.grid(row=2,column=2,sticky=W)
txtissue=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=issue_strvar,width=35)
txtissue.grid(row=2,column=3)

exp=Label(DataFrameLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
exp.grid(row=3,column=2,sticky=W)
txtexp=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=exp_strvar,width=35)
txtexp.grid(row=3,column=3)

dose=Label(DataFrameLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=6)
dose.grid(row=4,column=2,sticky=W)
txtdose=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=daily_strvar,width=35)
txtdose.grid(row=4,column=3)

pressure=Label(DataFrameLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
pressure.grid(row=5,column=2,sticky=W)
txtpressure=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=pressure_strvar,width=35)
txtpressure.grid(row=5,column=3)

name=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
name.grid(row=6,column=2,sticky=W)
txtname=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=name_strvar,width=35)
txtname.grid(row=6,column=3)

dob=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date of Birth:",padx=2,pady=6)
dob.grid(row=7,column=2,sticky=W)
txtdob=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=dob_strvar,width=35)
txtdob.grid(row=7,column=3)

Patient_Address=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Address",padx=2,pady=6)
Patient_Address.grid(row=8,column=2,sticky=W)
txtPatient_Address=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=address_strvar,width=35)
txtPatient_Address.grid(row=8,column=3)

nhs=Label(DataFrameLeft,font=("arial",12,"bold"),text=" NHS number",padx=2,pady=6)
nhs.grid(row=2,column=0,sticky=W)
txtnhs=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=nhs_strvar,width=35)
txtnhs.grid(row=2,column=1)

storage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Storage Advice ",padx=2,pady=6)
storage.grid(row=3,column=0,sticky=W)
txtstorage=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=storage_strvar,width=35)
txtstorage.grid(row=3,column=1)

further_information=Label(DataFrameLeft,font=("arial",12,"bold"),text="further_information",padx=2,pady=6)
further_information.grid(row=8,column=0,sticky=W)
txtfurther_information=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=information_strvar,width=35)
txtfurther_information.grid(row=8,column=1)

no_tablet=Label(DataFrameLeft,font=("arial",12,"bold"),text="no_tablet",padx=2,pady=6)
no_tablet.grid(row=6,column=0,sticky=W)
txtno_tablet=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=tablet_strvar,width=35)
txtno_tablet.grid(row=6,column=1)

side_effect=Label(DataFrameLeft,font=("arial",12,"bold"),text="side_effect",padx=2,pady=6)
side_effect.grid(row=5,column=0,sticky=W)
txtside_effect=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=effect_strvar,width=35)
txtside_effect.grid(row=5,column=1)

problem=Label(DataFrameLeft,font=("arial",12,"bold"),text="problem",padx=2,pady=6)
problem.grid(row=4,column=0,sticky=W)
txtproblem=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=problem_strvar,width=35)
txtproblem.grid(row=4,column=1)

# Placing components in the center frame
Buttonframe = Frame( bd=20,relief=RIDGE)
Buttonframe.place(x=0, y=530, width=1530, height=70)
Button(Buttonframe, text='Delete Record', font=labelfont, command=remove_record, width=15).place(relx=0.2, rely=0.10)
Button(Buttonframe, text='View Record', font=labelfont, command=display_records, width=15).place(relx=0.4, rely=0.10)
Button(Buttonframe, text='Reset Fields', font=labelfont, command=reset_fields, width=15).place(relx=0.6, rely=0.10)
Button(Buttonframe, text='Delete database', font=labelfont, command=reset_form, width=15).place(relx=0.8, rely=0.10)
Button(Buttonframe, text='Submit and Add Record', font=labelfont, command=add_record, width=18).place(relx=0.0, rely=0.10)
dob = DateEntry(left_frame, font=("Arial", 12), width=15)
dob.place(x=20, rely=0.62)
# Placing components in the right frame
Label(right_frame, text='Patient Records', font=headlabelfont, bg='DarkGreen', fg='LightCyan').pack(side=TOP, fill=X)

tree = ttk.Treeview(right_frame, height=100, selectmode=BROWSE,
                    columns=('Refence no', "Patient Name", "NHS number", "Storage Advice", "problem", "side effect", "no of tablet"
                             ,"Dose","further_informaton","Lot","Issue Date","Exp Date","Daily Dose","Blood Pressure","Date of Birth","Patient Address"))

X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)

X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)

tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)

tree.heading('Refence no', text='REFERENCE', anchor=CENTER)
tree.heading('Patient Name', text='Name', anchor=CENTER)
tree.heading('NHS number', text='NHS', anchor=CENTER)
tree.heading('Storage Advice', text='STORAGE', anchor=CENTER)
tree.heading('problem', text='PROBLEM', anchor=CENTER)
tree.heading('side effect', text='EFFECT', anchor=CENTER)
tree.heading('no of tablet', text='TABLET', anchor=CENTER)
tree.heading('Dose', text='DOSE', anchor=CENTER)
tree.heading('further_informaton', text='INFORMATION', anchor=CENTER)
tree.heading('Lot', text='LOT', anchor=CENTER)
tree.heading('Issue Date', text='ISSUE', anchor=CENTER)
tree.heading('Exp Date', text='EXP', anchor=CENTER)
tree.heading('Daily Dose', text='DAILY', anchor=CENTER)
tree.heading('Blood Pressure', text='PRESSURE', anchor=CENTER)
tree.heading('Date of Birth', text='DOB', anchor=CENTER)
tree.heading('Patient Address', text='ADDRESS', anchor=CENTER)


tree.column('#0', width=0, stretch=NO)
tree.column('#1', width=40, stretch=NO)
tree.column('#2', width=140, stretch=NO)
tree.column('#3', width=200, stretch=NO)
tree.column('#4', width=80, stretch=NO)
tree.column('#5', width=80, stretch=NO)
tree.column('#6', width=80, stretch=NO)
tree.column('#7', width=150, stretch=NO)
tree.column('#8', width=0, stretch=NO)
tree.column('#9', width=40, stretch=NO)
tree.column('#10', width=140, stretch=NO)
tree.column('#11', width=200, stretch=NO)
tree.column('#12', width=80, stretch=NO)
tree.column('#13', width=80, stretch=NO)
tree.column('#14', width=80, stretch=NO)
tree.column('#15', width=150, stretch=NO)


tree.place(y=30, relwidth=1, relheight=0.9, relx=0)

display_records()

# Finalizing the GUI window
main.update()
main.mainloop()



