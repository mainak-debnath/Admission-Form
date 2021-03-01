from tkinter import *
from tkinter import ttk
from tkinter import messagebox

parent = Tk()
wv = parent.winfo_screenwidth()
hv = parent.winfo_screenheight()
parent.geometry("%dx%d+0+0" % (wv, hv))
parent.title("Admission Form")

canvas = Canvas(parent, width=1200, height=1800)
scroll_y = Scrollbar(parent, orient="vertical",
                     command=canvas.yview, bd=4, relief="groove")

frame = Frame(canvas)
f1 = Frame(frame, height=2150, width=1550,
           bg="LightBlue1", bd=7, relief="sunken")
f1.pack(expand=True, fill=BOTH)
# group of widgets

l = ["India", "Pakistan", "Bangladesh", "Sri Lanka",
     "Australia", "United States", "Afghanistan"]
l1 = list(range(1, 32))
l2 = list(range(1, 13))
l3 = list(range(1990, 2004))

fn = StringVar()
mn = StringVar()
ln = StringVar()
dob = StringVar()
gen = StringVar()
cn = StringVar()
add = StringVar()
pc = StringVar()
loc = StringVar()
city = StringVar()
dist = StringVar()
po = StringVar()
ps = StringVar()
country = StringVar()
state = StringVar()
eid = StringVar()
nat = StringVar()
bgrp = StringVar()
fathn = StringVar()
fathoccu = StringVar()
fathcn = StringVar()
mothn = StringVar()
mothoccu = StringVar()
mothcn = StringVar()
school = StringVar()
sccountry = StringVar()
sccity = StringVar()
math = StringVar()
phy = StringVar()
chem = StringVar()
comp = StringVar()
pcm = StringVar()

chk_var = IntVar()


################# CLEAR#######################
def remove():
    ck = chk_var.get()
    if (ck != 0):
        entry_1.delete(0, END)
        entry_2.delete(0, END)
        entry_4.delete(0, END)
        entry_5.delete(0, END)
        entry_6.delete(0, END)
#        entry_9.delete(0, END)
        entry_10.delete(0, END)
        entry_11.delete(0, END)
        entry_12.delete(0, END)
        entry_13.delete(0, END)
        entry_15.delete(0, END)
        entry_16.delete(0, END)
        entry_17.delete(0, END)
        entry_18.delete(0, END)
        entry_19.delete(0, END)
        entry_20.delete(0, END)
        entry_21.delete(0, END)
        entry_22.delete(0, END)
        entry_23.delete(0, END)
#        entry_24.delete(0, END)
        entry_25.delete(0, END)
        entry_26.delete(0, END)
        entry_27.delete(0, END)
#        entry_28.delete(0, END)
        entry_30.delete(0, END)
        entry_31.delete(0, END)
        entry_62.delete(0, END)
        entry_122.delete(0, END)
        entry_132.delete(0, END)
        entry_102.delete(0, END)
        entry_112.delete(0, END)
        entry_152.delete(0, END)
        vx = 0
        var.set("Select your country")
        var2x.set("Select your country")
        var2.set("Day")
        var3.set("Month")
        var4.set("Year")
        xm = 0
        entry_28 = Label(f2, text=xm, width=20, font=("bold", 15), bg='white')
        entry_28.place(x=280, y=215)

##################################################


def save_info():
    chk = chk_var.get()
    if (chk == 0):
        messagebox.showerror('Error', 'Please check the checkbutton')
    else:
        file = open("userf.txt", "a")
        file.write("\n\nName : " + fn.get() + " " + mn.get() + " " + ln.get())
        dob = var2.get() + '/' + var3.get() + "/" + var4.get()
        file.write("\nDOB : " + dob)
        g = vara.get()
        file.write("\nGender : ")
        if g == 1:
            file.write("Male")
        elif g == 2:
            file.write("Female")
        elif g == 3:
            file.write("Others")
        file.write("\nEmail I.d. : " + eid.get())
        file.write("\nReligion : " + nat.get())
        file.write("\nBlood Group : " + bgrp.get())
        file.write("\nContact Number : " + cn.get())
        file.write("\nPermanent Address :")  # added
        file.write("\nAddress : " + add.get())  # modified
        file.write("\nPost Office : " + po.get())
        file.write("\nPin Code : " + ps.get())
        file.write("\nDistrict : " + dist.get())
        file.write("\nCity : " + city.get())
        file.write("\nState : " + state.get())
        file.write("\nCountry : " + var.get())
        file.write("\nCurrent Address : ")  # added
        file.write("\nAddress : " + add2.get())  # modified
        file.write("\nPost Office : " + po2.get())
        file.write("\nPin Code : " + ps2.get())
        file.write("\nDistrict : " + dist2.get())
        file.write("\nCity : " + city2.get())
        file.write("\nState : " + state2.get())
        file.write("\nCountry : " + var2x.get())
        file.write("\nParticulars of Guardian:")
        file.write("\nGuardian's Name : " + fathn.get())
        file.write("\nOccupation : " + fathoccu.get())
        file.write("\nContact Number : " + fathcn.get())
        file.write("\nEmail I.D. : " + mothn.get())
        file.write("\nLocal Guardian : " + mothoccu.get())
        file.write("\nSchool Name : " + school.get())
        file.write("\nBoard : " + sccity.get())
        file.write("\nMathematics Marks : " + math.get())
        file.write("\nPhysics Marks : " + phy.get())
        file.write("\nChemistry Marks : " + chem.get())
        l = float(int(math.get()) + int(phy.get()) + int(chem.get())) / 3
        r = round(l, 2)
        file.write("\nPCM Percentage : " + str(r) + "%")
        file.close()
        print("User " + fn.get() + " has been registered successfully")


############################################################################

def show():
    save_info()
    remove()


name1 = Label(f1, text="ST THOMAS COLLEGE OF ENGINNERING AND TECNOLOGY",
              bg="red", font="TimesNewRoman 25 bold")
name1.place(x=250, y=50)

Label(f1, text="ADMISSION FORM", bg="red",
      font="Georgia 20").place(x=550, y=90)

f2 = Frame(f1, height=400, width=1400, bg="#80c1ff", bd=7, relief="groove")
f2.place(x=4, y=140)

name2 = Label(f2, text="PERSONAL DETAILS", bg="#80c1ff",
              font="TimesNewRoman 18 bold")
name2.place(x=10, y=30)
label_1 = Label(f2, text="First Name", width=20,
                font=("bold", 15), bg='#80c1ff')
label_1.place(x=0, y=100)
entry_1 = Entry(f2, width="40", textvariable=fn)
entry_1.place(x=175, y=100)

label_2 = Label(f2, text="Middle Name", width=20,
                font=("bold", 15), bg='#80c1ff')
label_2.place(x=460, y=100)
entry_2 = Entry(f2, width="40", textvariable=mn)
entry_2.place(x=660, y=100)

label_5 = Label(f2, text="Last Name", width=20,
                font=("bold", 15), bg='#80c1ff')
label_5.place(x=860, y=100)
entry_5 = Entry(f2, width="30", textvariable=ln)
entry_5.place(x=1050, y=100)

label_7 = Label(f2, text="Date of Birth", width=20,
                font=("bold", 15), bg='#80c1ff')
label_7.place(x=7, y=145)

var2 = StringVar()
var2.set("Day")
set2 = OptionMenu(f2, var2, *l1)
set2.config(bg='#80c1ff', activebackground='#80c1ff')
set2.place(x=200, y=145)

var3 = StringVar()
var3.set("Month")
set3 = OptionMenu(f2, var3, *l2)
set3.config(bg='#80c1ff', activebackground='#80c1ff')
set3.place(x=270, y=144)

var4 = StringVar()
var4.set("Year")
set4 = OptionMenu(f2, var4, *l3)
set4.config(bg='#80c1ff', activebackground='#80c1ff')
set4.place(x=360, y=145)

label_3 = Label(f2, text="Gender", width=20, font=("bold", 15), bg='#80c1ff')
label_3.place(x=0, y=190)
vara = IntVar()
Radiobutton(f2, text="Male", padx=30, variable=vara, value=1, bg='#80c1ff', activebackground='#80c1ff',
            font="5").place(x=180, y=190)
Radiobutton(f2, text="Female", padx=30, variable=vara, value=2, bg='#80c1ff', activebackground='#80c1ff',
            font="5").place(x=330, y=190)
Radiobutton(f2, text="Others", padx=30, variable=vara, value=3, bg='#80c1ff', activebackground='#80c1ff',
            font="5").place(x=490, y=190)

label_16 = Label(f2, text="Email I.D.", width=20,
                 font=("bold", 15), bg='#80c1ff')
label_16.place(x=0, y=235)
entry_16 = Entry(f2, width="40", textvariable=eid)
entry_16.place(x=200, y=235)

label_17 = Label(f2, text="Religion", width=20,
                 font=("bold", 15), bg='#80c1ff')
label_17.place(x=0, y=280)
entry_17 = Entry(f2, width="40", textvariable=nat)
entry_17.place(x=200, y=280)

label_18 = Label(f2, text="Blood Group", width=20,
                 font=("bold", 15), bg='#80c1ff')
label_18.place(x=0, y=325)
entry_18 = Entry(f2, width="20", textvariable=bgrp)
entry_18.place(x=200, y=325)

######

f2 = Frame(f1, height=650, width=1400, bg="#80c1ff", bd=7, relief="groove")
f2.place(x=4, y=560)
name = Label(f2, text="CONTACT INFORMATION ",
             bg="#80c1ff", font="TimesNewRoman 18 bold")
name.place(x=10, y=30)

label_4 = Label(f2, text="Contact Number", width=20,
                font=("bold", 15), bg='#80c1ff')
label_4.place(x=0, y=100)
entry_4 = Entry(f2, width="40", textvariable=cn)
entry_4.place(x=260, y=100)

label_41 = Label(f2, text="Current Address", width=20,
                 bg='#80c1ff', font="TimesNewRoman 15 bold")
label_41.place(x=8, y=150)

####

label_6 = Label(f2, text="Address", width=20, font=("bold", 15), bg='#80c1ff')
label_6.place(x=0, y=190)
entry_6 = Entry(f2, width="160", textvariable=add)
entry_6.place(x=170, y=190)

label_12 = Label(f2, text="Post Office", width=20,
                 font=("bold", 15), bg='#80c1ff')
label_12.place(x=0, y=235)
entry_12 = Entry(f2, width="40", textvariable=po)
entry_12.place(x=180, y=235)

label_13 = Label(f2, text="Pin Code", width=20,
                 font=("bold", 15), bg='#80c1ff')
label_13.place(x=440, y=235)
entry_13 = Entry(f2, width="40", textvariable=ps)
entry_13.place(x=665, y=235)

label_10 = Label(f2, text="City", width=20, font=("bold", 15), bg='#80c1ff')
label_10.place(x=0, y=280)
entry_10 = Entry(f2, width="40", textvariable=city)
entry_10.place(x=180, y=280)

label_11 = Label(f2, text="District", width=20,
                 font=("bold", 15), bg='#80c1ff')
label_11.place(x=440, y=280)
entry_11 = Entry(f2, width="40", textvariable=dist)
entry_11.place(x=665, y=280)

state = StringVar()
label_15 = Label(f2, text="State", width=20, font=("bold", 15), bg='#80c1ff')
label_15.place(x=0, y=325)
entry_15 = Entry(f2, width="40", textvariable=state)
entry_15.place(x=180, y=325)

label_14 = Label(f2, text="Country", width=20, font=("bold", 15), bg='#80c1ff')
label_14.place(x=440, y=325)
var = StringVar()
var.set("Select your country")
set1 = OptionMenu(f2, var, *l)
set1.config(bg='#80c1ff', activebackground='#80c1ff', width="25")
set1.place(x=670, y=325)

##


label_40 = Label(f2, text="Parmanent Address", width=20,
                 font="TimesNewRoman 15 bold", bg='#80c1ff')
label_40.place(x=0, y=390)


add2 = StringVar()
label_62 = Label(f2, text="Address", width=20, font=("bold", 15), bg='#80c1ff')
label_62.place(x=0, y=430)
entry_62 = Entry(f2, width="160", textvariable=add2)
entry_62.place(x=170, y=430)

po2 = StringVar()
label_122 = Label(f2, text="Post Office", width=20,
                  font=("bold", 15), bg='#80c1ff')
label_122.place(x=0, y=475)
entry_122 = Entry(f2, width="40", textvariable=po2)
entry_122.place(x=180, y=475)

ps2 = StringVar()
label_132 = Label(f2, text="Pin Code", width=20,
                  font=("bold", 15), bg='#80c1ff')
label_132.place(x=440, y=475)
entry_132 = Entry(f2, width="40", textvariable=ps2)
entry_132.place(x=665, y=475)

city2 = StringVar()
label_102 = Label(f2, text="City", width=20, font=("bold", 15), bg='#80c1ff')
label_102.place(x=0, y=520)
entry_102 = Entry(f2, width="40", textvariable=city2)
entry_102.place(x=180, y=520)

dist2 = StringVar()
label_112 = Label(f2, text="District", width=20,
                  font=("bold", 15), bg='#80c1ff')
label_112.place(x=440, y=565)
entry_112 = Entry(f2, width="40", textvariable=dist2)
entry_112.place(x=665, y=520)

state2 = StringVar()
state2 = StringVar()
label_152 = Label(f2, text="State", width=20, font=("bold", 15), bg='#80c1ff')
label_152.place(x=0, y=565)
entry_152 = Entry(f2, width="40", textvariable=state2)
entry_152.place(x=180, y=565)

label_142 = Label(f2, text="Country", width=20,
                  font=("bold", 15), bg='#80c1ff')
label_142.place(x=440, y=565)
var2x = StringVar()
var2x.set("Select your country")
setx = OptionMenu(f2, var2x, *l)
setx.config(bg='#80c1ff', activebackground='#80c1ff', width="25")
setx.place(x=670, y=565)


def same_address():
    if (vx.get() == 1):
        add2.set(entry_6.get())
        po2.set(entry_12.get())
        ps2.set(entry_13.get())
        city2.set(entry_10.get())
        dist2.set(entry_11.get())
        state2.set(entry_15.get())
        var2x.set(var.get())


vx = IntVar()
#vx = 0
vm = Checkbutton(f2, text="Same as Permanent Address", bg='#80c1ff', activebackground="#80c1ff", font="5", bd=15,
                 variable=vx, command=same_address).place(x=400, y=375)

########

f2 = Frame(f1, height=340, width=1400, bg='#80c1ff', bd=7, relief="groove")
f2.place(x=4, y=1240)
name = Label(f2, text="PARTICULARS OF GUARDIAN ",
             bg='#80c1ff', font="TimesNewRoman 18 bold")
name.place(x=10, y=30)

label_19 = Label(f2, text="Guardian's Name", width=20,
                 font=("bold", 15), bg='#80c1ff')
label_19.place(x=0, y=75)
entry_19 = Entry(f2, width="40", textvariable=fathn)
entry_19.place(x=230, y=75)

label_20 = Label(f2, text="Occupation", width=20,
                 font=("bold", 15), bg='#80c1ff')
label_20.place(x=0, y=120)
entry_20 = Entry(f2, width="40", textvariable=fathoccu)
entry_20.place(x=230, y=120)

label_21 = Label(f2, text="Contact Number", width=20,
                 font=("bold", 15), bg='#80c1ff')
label_21.place(x=0, y=165)
entry_21 = Entry(f2, width="40", textvariable=fathcn)
entry_21.place(x=230, y=165)

label_22 = Label(f2, text="Email I.D.", width=20,
                 font=("bold", 15), bg='#80c1ff')
label_22.place(x=0, y=210)
entry_22 = Entry(f2, width="40", textvariable=mothn)
entry_22.place(x=230, y=210)

label_23 = Label(f2, text="Local Guardian", width=20,
                 font=("bold", 15), bg='#80c1ff')
label_23.place(x=0, y=255)
entry_23 = Entry(f2, width="40", textvariable=mothoccu)
entry_23.place(x=230, y=255)

########

f2 = Frame(f1, height=300, width=1400, bg="#80c1ff", bd=7, relief="groove")
f2.place(x=4, y=1610)
name = Label(f2, text="EDUCATION QUALIFICATION ",
             bg="#80c1ff", font="TimesNewRoman 18 bold")
name.place(x=10, y=30)

label_29 = Label(f2, text="School", width=20, font=(
    "bold", 15), bg='#80c1ff').place(x=0, y=80)
entry_30 = Entry(f2, width="60", textvariable=school)
entry_30.place(x=190, y=80)

label_31 = Label(f2, text="Board", width=20, font=(
    "bold", 15), bg='#80c1ff').place(x=0, y=125)
entry_31 = Entry(f2, width="60", textvariable=sccity)
entry_31.place(x=190, y=125)

math = StringVar()
phy = StringVar()
chem = StringVar()
result = StringVar()

xm = 0


def Calc():
    na = math.get()
    nb = phy.get()
    nc = chem.get()
    x = float(int(na) + int(nb) + int(nc)) / 3
    xm = round(x, 2)
    entry_28 = Label(f2, text=xm, width=20, font=("bold", 15), bg='white')
    entry_28.place(x=280, y=215)


label_25 = Label(f2, text="Mathematics", width=20,
                 font=("bold", 15), bg='#80c1ff')
label_25.place(x=0, y=170)
entry_25 = Entry(f2, width='15', textvariable=math)
entry_25.place(x=190, y=170)

label_26 = Label(f2, text="Physics", width=20, font=("bold", 15), bg='#80c1ff')
label_26.place(x=320, y=170)
entry_26 = Entry(f2, width='15', textvariable=phy)
entry_26.place(x=490, y=170)

label_27 = Label(f2, text="Chemistry", width=20,
                 font=("bold", 15), bg='#80c1ff')
label_27.place(x=620, y=170)
entry_27 = Entry(f2, width='15', textvariable=chem)
entry_27.place(x=800, y=170)

Button(f2, text='Calculate Percentage of PCM', width=25,
       bg='grey', fg='white', command=Calc).place(x=60, y=215)

####

chk_1 = Checkbutton(f1,
                    text="I do hereby declare that all the information given above is true to the best of my knowledge and belief.",
                    bg="LightBlue1", activebackground="#80c1ff", font=("bold", 15), bd=15, variable=chk_var).place(x=5, y=1920)

Button(f1, text='Submit', width=15, bg='red', fg='white', font="TimesNewRoman 25 bold", command=show).place(x=500,
                                                                                                            y=2000)

canvas.create_window(0, 0, anchor='nw', window=frame)

canvas.update_idletasks()

canvas.configure(scrollregion=canvas.bbox('all'),
                 yscrollcommand=scroll_y.set)

canvas.pack(fill='both', expand=True, side='left')
scroll_y.pack(fill='y', side='right')
parent.mainloop()
