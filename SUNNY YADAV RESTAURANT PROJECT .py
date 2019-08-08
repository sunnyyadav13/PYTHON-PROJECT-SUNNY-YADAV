# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 10:27:16 2019

@author: SUNNY YADAV
"""

#==========================================================start=============================================================#
from tkinter import*
import random
import time

# *******************************THIS IS FOR WINDOW***********************************************8
root=Tk()
root.geometry("1600x800+0+0")
root.title("RESTAURANT ORIGIN")
#---------------------------------------------------------------------------------------------------
text_input=StringVar() # FOR DISPLAY OF MY CALCULATOR
operator=""

#*****************************************THEN IT IS DIVIDED IN 3 FRAME************************************
tops=Frame(root,width=1600,height=50,bg='white',relief=SUNKEN)
tops.pack(side=TOP)

f1=Frame(root,width=800,height=800,bg='light yellow',relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=300,height=700,bg='#ffffff',relief=SUNKEN)
f2.pack(side=RIGHT)

# *************************************************function for time*******************************************
local_time=time.asctime(time.localtime(time.time()))

lbl1=Label(tops,font=('arial',49,'bold'),text='RESTAURANT "ORIGIN"',fg="steel blue",bd=10,anchor='w')
lbl1.grid(row=0,column=0)

lbl1=Label(tops,font=('arial',15,'bold'),text=local_time,fg="violet",bd=10,anchor='w')
lbl1.grid(row=0,column=1)
#***************************************************CALCULATOR********************************************************

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)
    
def btnClearDisplay():
    global operator
    operator=""
    text_input.set("")
    
def btnequal():
    global operator
    sumout=str(eval(operator))
    text_input.set(sumout)

    operator=""

txt_Display=Entry(f2,font=('arial',20,'bold'),textvariable=text_input,bd=30,
                  insertwidth=4,bg="powder blue",justify="right")
txt_Display.grid(columnspan=4)

btn7=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),
            text="7",bg="powder blue",command=lambda:btnClick(7))
btn7.grid(row=2,column=0)

btn8=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),
            text="8",bg="powder blue",command=lambda:btnClick(8))
btn8.grid(row=2,column=1)

btn9=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),
            text="9",bg="powder blue",command=lambda:btnClick(9))
btn9.grid(row=2,column=2)

btn4=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),
            text="4",bg="powder blue",command=lambda:btnClick(4))
btn4.grid(row=3,column=0)

btn5=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),
            text="5",bg="powder blue",command=lambda:btnClick(5))
btn5.grid(row=3,column=1)

btn6=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),
            text="6",bg="powder blue",command=lambda:btnClick(6))
btn6.grid(row=3,column=2)

btn1=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),
            text="1",bg="powder blue",command=lambda:btnClick(1))
btn1.grid(row=4,column=0)

btn2=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),
            text="2",bg="powder blue",command=lambda:btnClick(2))
btn2.grid(row=4,column=1)

btn3=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),
            text="3",bg="powder blue",command=lambda:btnClick(3))
btn3.grid(row=4,column=2)

btn0=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),
            text="0",bg="powder blue",command=lambda:btnClick(0))
btn0.grid(row=5,column=1)

ADD=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),
            text="+",bg="powder blue",command=lambda:btnClick('+'))
ADD.grid(row=2,column=3)

SUB=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),
            text="-",bg="powder blue",command=lambda:btnClick('-'))
SUB.grid(row=3,column=3)

MUL=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),
            text="*",bg="powder blue",command=lambda:btnClick('*'))
MUL.grid(row=4,column=3)

DIV=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),
            text="/",bg="powder blue",command=lambda:btnClick('/'))
DIV.grid(row=5,column=3)


clear=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),
            text="C",bg="powder blue",command=btnClearDisplay)# command=btnClearDisplay
clear.grid(row=5,column=0)


equal=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),
            text="=",bg="powder blue",command=btnequal)
equal.grid(row=5,column=2)
#------------------------------------BILL COUNTER------------------------------
rand=StringVar()
BURGER=StringVar()
PIZAA=StringVar()
COLDDRINKS=StringVar()
CHINESE_FOOD=StringVar()
veg_food=StringVar()
nveg_food=StringVar()
cost_of_meal=StringVar()
DISCOUNT=StringVar()
GST=StringVar()
EXTRA=StringVar()
AMT=StringVar()

def ref():
    x=random.randrange(1000,99999)
    randomref=str(x)
    rand.set(randomref)
    #count of foods
    
    
    a=float(BURGER.get())
    b=float(PIZAA.get())
    c=float(COLDDRINKS.get())
    d=float(CHINESE_FOOD.get())
    e=float(veg_food.get())
    f=float(nveg_food.get())
    #cost of foods
    ab=a*500
    bp=b*750
    cc=c*45
    dc=d*350
    ev=e*400
    fnv=f*800
    food_cost=ab+bp+cc+dc+ev+fnv
    costofmeal="Rs",str('%.2f' %food_cost)
    #******************************Lucky********************
    if(randomref==2000):
        disc=100
    else:
        disc=15
    
    disc_price=food_cost*(disc/100)
    DISCOUNT1="Rs",str("%.2f" %disc_price)
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      GST           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    gst=food_cost*0.12
    GST1="Rs"+str("%.2f" %gst)
    
    extra=50 # Parking Charges
    EXTRA1="Rs",str("%.2f" %extra)
    amt=food_cost-disc_price+gst+extra
    AMT1="Rs",str("%.2f" %amt)
    
    cost_of_meal.set(costofmeal)
    DISCOUNT.set(DISCOUNT1)
    GST.set(GST1)
    EXTRA.set(EXTRA1)
    AMT.set(AMT1)
    
def Quit():
    root.destroy()

def reset():
    rand.set("")
    BURGER.set("")
    PIZAA.set("")
    COLDDRINKS.set("")
    CHINESE_FOOD.set("")
    veg_food.set("")
    nveg_food.set("")
    cost_of_meal.set("")
    DISCOUNT.set("")
    GST.set("")
    EXTRA.set("")
    AMT.set("")

def price():
    K = Tk()
    K.geometry("500x300+0+0")
    K.title("Price List")
    lbl1 = Label(K, font=('arial', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lbl1.grid(row=0, column=0)
    lbl1 = Label(K, font=('arial', 15,'bold'), text="_____________", fg="white", anchor='sw')
    lbl1.grid(row=0, column=2)
    lbl1 = Label(K, font=('arial', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lbl1.grid(row=0, column=3)
    lbl1 = Label(K, font=('arial', 15, 'bold'), text="BURGER", fg="steel blue", anchor='sw')
    lbl1.grid(row=1, column=0)
    lbl1 = Label(K, font=('arial', 15, 'bold'), text="500", fg="steel blue", anchor=W)
    lbl1.grid(row=1, column=3)
    lbl1 = Label(K, font=('arial', 15, 'bold'), text="PIZZA", fg="steel blue", anchor='sw')
    lbl1.grid(row=2, column=0)
    lbl1 = Label(K, font=('arial', 15, 'bold'), text="750", fg="steel blue", anchor=W)
    lbl1.grid(row=2, column=3)
    lbl1 = Label(K, font=('arial', 15, 'bold'), text="VEG FOOD", fg="steel blue", anchor='sw')
    lbl1.grid(row=3, column=0)
    lbl1 = Label(K, font=('arial', 15, 'bold'), text="400", fg="steel blue", anchor=W)
    lbl1.grid(row=3, column=3)
    lbl1 = Label(K, font=('arial', 15, 'bold'), text="NON VEG FOOD", fg="steel blue", anchor='sw')
    lbl1.grid(row=4, column=0)
    lbl1 = Label(K, font=('arial', 15, 'bold'), text="800", fg="steel blue", anchor=W)
    lbl1.grid(row=4, column=3)
    lbl1 = Label(K, font=('arial', 15, 'bold'), text="CHINESE FOOD", fg="steel blue", anchor='sw')
    lbl1.grid(row=5, column=0)
    lbl1 = Label(K, font=('arial', 15, 'bold'), text="350", fg="steel blue", anchor='sw')
    lbl1.grid(row=5, column=3)
    lbl1 = Label(K, font=('arial', 15, 'bold'), text="COLD Drinks", fg="steel blue", anchor='sw')
    lbl1.grid(row=6, column=0)
    lbl1 = Label(K, font=('arial', 15, 'bold'), text="45", fg="steel blue", anchor='sw')
    lbl1.grid(row=6, column=3)

    K.mainloop() 
    

lblrefrence=Label(f1,font=('arial',15,'bold'),text='Refrence',bd=16,anchor='w',bg="light yellow")
lblrefrence.grid(row=0,column=0)

textrefrence=Entry(f1,font=('arial',15,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="light yellow",
                   justify='right')
textrefrence.grid(row=0,column=1)
#-------------------------------------------------------------------------------------------------------
lblBURGER=Label(f1,font=('arial',15,'bold'),text='BURGER',bd=16,anchor='w',bg="light yellow").grid(row=1,column=0)

textBURGER=Entry(f1,font=('arial',15,'bold'),textvariable=BURGER,bd=10,insertwidth=4,bg="light yellow",
                   justify='right').grid(row=1,column=1)
#--------------------------------------------------------------------------------------------------------
lblPIZAA=Label(f1,font=('arial',15,'bold'),text='PIZAA',bd=16,anchor='w',bg="light yellow").grid(row=2,column=0)

textPIZAA=Entry(f1,font=('arial',15,'bold'),textvariable=PIZAA,bd=10,insertwidth=4,bg="light yellow",
                   justify='right').grid(row=2,column=1)
#--------------------------------------------------------------------------------------------------------
lblCOLDDRINKS=Label(f1,font=('arial',15,'bold'),text='COLDDRINKS',bd=16,anchor='w',bg="light yellow").grid(row=3,column=0)

textCOLDDRINKS=Entry(f1,font=('arial',15,'bold'),textvariable=COLDDRINKS,bd=10,insertwidth=4,bg="light yellow",
                   justify='right').grid(row=3,column=1)
#--------------------------------------------------------------------------------------------------------
lblCHINESE_FOOD=Label(f1,font=('arial',15,'bold'),text='CHINESE FOOD',bd=16,anchor='w',bg="light yellow").grid(row=4,column=0)
textCHINESE_FOOD=Entry(f1,font=('arial',15,'bold'),textvariable=CHINESE_FOOD,bd=10,insertwidth=4,bg="light yellow",
                   justify='right').grid(row=4,column=1)
#-----------------------------------------------------------------------------------------------------
lblveg_food=Label(f1,font=("arial",15,'bold'),text='VEG FOOD',bd=16,anchor='w',bg="light yellow").grid(row=5,column=0)
textveg_food=Entry(f1,textvariable=veg_food,bd=10,insertwidth=4,font=("arial",15,'bold'),bg="light yellow",
                   justify='right').grid(row=5,column=1)

lblnveg_food=Label(f1,font=("arial",15,'bold'),text='NON-VEG FOOD',bd=16,anchor='w',bg="light yellow").grid(row=6,column=0)
textnveg_food=Entry(f1,textvariable=nveg_food,bd=10,insertwidth=4,font=("arial",15,'bold'),bg="light yellow",
                   justify='right').grid(row=6,column=1)

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&COSTING&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
lblcost_of_meal=Label(f1,font=("arial",15,'bold'),text='COST OF MEAL',bd=16,anchor='w',bg="powder blue")
lblcost_of_meal.grid(row=0,column=3)

textcost_of_meal=Entry(f1,textvariable=cost_of_meal,bd=10,insertwidth=4,font=("arial",15,'bold'),bg="WHITE",
                   justify='right').grid(row=0,column=4)

lblDISCOUNT=Label(f1,font=("arial",15,'bold'),text='DISCOUNT',bd=16,anchor='w',bg="green")
lblDISCOUNT.grid(row=1,column=3)

textDISCOUNT=Entry(f1,textvariable=DISCOUNT,bd=10,insertwidth=4,font=("arial",15,'bold'),bg="green",
                   justify='right').grid(row=1,column=4)

lblGST=Label(f1,font=("arial",15,'bold'),text='GST',bd=16,anchor='w',bg="yellow")
lblGST.grid(row=2,column=3)

textGST=Entry(f1,textvariable=GST,bd=10,insertwidth=4,font=("arial",15,'bold'),bg="yellow",
                   justify='right').grid(row=2,column=4)

lblEXTRA=Label(f1,font=("arial",15,'bold'),text='EXTRA',bd=16,anchor='w',bg="yellow")
lblEXTRA.grid(row=3,column=3)

textEXTRA=Entry(f1,textvariable=EXTRA,bd=10,insertwidth=4,font=("arial",15,'bold'),bg="yellow",
                   justify='right').grid(row=3,column=4)

lblAMT=Label(f1,font=("arial",15,'bold'),text='AMT',bd=16,anchor='w',bg="orange")
lblAMT.grid(row=4,column=3)

textAMT=Entry(f1,textvariable=AMT,bd=10,insertwidth=4,font=("arial",15,'bold'),bg="orange",
                   justify='right').grid(row=4,column=4)

btnprice=Button(f1,padx=5,pady=5, bd=10 ,fg="black",font=('ariel' ,15,'bold'),width=10, 
                text="Price", bg="white",command=price).grid(row=6,column=3)


btnTOTAL=Button(f1,padx=5,pady=5,bd=8,fg="black",font=('arial',15,'bold'),
            text="TOTAL",bg="#ffffff",command=ref).grid(row=5,column=3)

btnreset=Button(f1,padx=10,pady=10,bd=8,fg="black",font=('arial',15,'bold'),
            text="Reset",bg="#ffffff",command=reset).grid(row=5,column=4)
            
btnexit=Button(f1,padx=10,pady=10,bd=8,fg="black",font=('arial',15,'bold'),
            text="QUIT",bg="#ffffff",command=Quit).grid(row=5,column=5)
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

root.mainloop()

