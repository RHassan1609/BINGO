import numpy as np
import random
import tkinter as tk
import time
import sys
import os
window=tk.Tk()

frame_2=tk.Frame(master=window,relief=tk.RAISED,borderwidth=10)  

label_dim=tk.Label(master=window,text='DIMENSION:',height=1,width=20,font=("Times New Roman",28),relief=tk.RAISED,borderwidth=2,activeforeground='red3',background='red3')
entry_dim=tk.Entry(master=window,width=23,font=("Times New Roman",28),relief=tk.RAISED,borderwidth=2,background='white')
label_player=tk.Label(master=window,text='NUMBER OF PLAYERS:',height=1,width=20,font=("Times New Roman",28),relief=tk.RAISED,borderwidth=2,activeforeground='red3',background='red3')
entry_player=tk.Entry(master=window,width=23,font=("Times New Roman",28),relief=tk.RAISED,borderwidth=2,background='white')
label_dim.grid(row=1,column=0)
entry_dim.grid(row=1,column=1)
label_player.grid(row=2,column=0)
entry_player.grid(row=2,column=1)
NR=[]
CC=[]
CRC=[]
CR=[]
CCl=[] 
Man=[] 
Love_for_Rifa=[]
globals()['Result']=''
computer=[] 
for i in range(0,2):

    globals()['computer_'+str(i)]=[]
    
    for c1 in range(0,5):
        globals()['computer_'+str(i)+'_'+str(c1)]=[]   
        for c2 in range(0,5):
            globals()['computer_'+str(i)+'_'+str(c1)].append(0)   
        globals()['computer_'+str(i)].append((globals()['computer_'+str(i)+'_'+str(c1)])) 

    computer.append(globals()['computer_'+str(i)])
   



LLLL=[]
for num in range(1,26):
    LLLL.append(num)
    
Account=[]
for num in range(1,26):
    Account.append(num) 

R=[]
for i in range(0,2):    
    globals()['R_'+str(i)]=[]
    R.append(globals()['R_'+str(i)])
    
C=[]
for i in range(0,2):    
    globals()['C_'+str(i)]=[]
    C.append(globals()['C_'+str(i)])
    
row=[]
   
for c1 in range(0,5):
    globals()['rows_'+str(c1)]=[]   
    for c2 in range(0,5):
        globals()['rows_'+str(c1)].append(0)   
    row.append(globals()['rows_'+str(c1)])
    
column=[]
for c1 in range(0,5):
    globals()['columns_'+str(c1)]=[]   
    for c2 in range(0,5):
        globals()['columns_'+str(c1)].append(0)   
    column.append(globals()['columns_'+str(c1)])
        
cross=[] 

reverse_cross=[]

LLL=[]
for numm in range(1,26):
    LLL.append(numm)
    
com_row=[]
for i in range(0,2):  
    globals()['com_rows_'+str(i)]=[]  
    for c1 in range(0,5):
        globals()['com_rows_'+str(i)+'_'+str(c1)]=[]   
        for c2 in range(0,5):
            globals()['com_rows_'+str(i)+'_'+str(c1)].append(0) 
        globals()['com_rows_'+str(i)].append(globals()['com_rows_'+str(i)+'_'+str(c1)])            
    com_row.append(globals()['com_rows_'+str(i)])

com_column=[]
for i in range(0,2): 
    globals()['com_columns_'+str(i)]=[]   
    for c1 in range(0,5):
        globals()['com_columns_'+str(i)+'_'+str(c1)]=[]   
        for c2 in range(0,5):
            globals()['com_columns_'+str(i)+'_'+str(c1)].append(0) 
        globals()['com_columns_'+str(i)].append(globals()['com_columns_'+str(i)+'_'+str(c1)])            
    com_column.append(globals()['com_columns_'+str(i)])


        
com_cross=[] 
for i in range(0,2):
    globals()['comp_cross'+str(i)]=[]
    com_cross.append(globals()['comp_cross'+str(i)])

com_reverse_cross=[]
for i in range(0,2):
    globals()['comp_reverse_cross'+str(i)]=[]
    com_reverse_cross.append(globals()['comp_reverse_cross'+str(i)])
    
    
    
def Rules():
    w=tk.Tk()
    T1='1. Enter Dimension and Number of Players First. They Must be Real Integers. Do not Keep the Boxes Empty.\n'
    t1=T1.upper()
    T2='2. Then Click New Game.\n'
    t2=T2.upper()
    T3='3. Then Fill up the Empty Boxes with Integers from One to Square of Dimension. Do not Keep Any Box Empty.\n'
    t3=T3.upper()
    T4='4. If You Want You Can also fill the boxes automatically. Click Fill Automatically.'
    t4=T4.upper()
    T5='5. Then Click Start Game.\n'
    t5=T5.upper()
    T6='6. Then Put Any Integer between One and Square of Dimension in the Appeared Box. Do not Put Anything Which Already Have Been Booked.\n'
    t6=T6.upper()
    T7='7. Do not Keep the Box Empty.\n'
    t7=T7.upper()
    T8='8. Then Click Play.\n'
    t8=T8.upper()
    T9='9. Now Other Players will Tell Their Digits. Once One Digit is Told by Any Player, it Will be Booked for Every Player.\n'
    t9=T9.upper()
    T10='10. Choose Another Digit. Click Play Again. Then Other Players Will Choose Theirs Too. Thus the Game Progresses.\n'
    t10=T10.upper()
    T11='11. If All the Digits of Any Row, Column or Diagonal is Booked, That Row, Column or Diagonal Will be Marked.\n'
    t11=T11.upper()
    T12='12. One Who Will Have Number of Marked Lines Equal to the Dimension First, Will Win. So Try to Choose Digits Accordingly.\n'
    t12=T12.upper()
    T13='13. If Anytime between Play You Want to Change Dimension or Number of Players, Change Accordingly. Then Click New Game.\n'
    t13=T13.upper()


    r=len(t6)
 
    for i in range (1,14):
     
        locals()['l'+str(i)]=tk.Label(master=w,text=locals()['t'+str(i)],height=2,anchor='w',width=r,font=("Times New Roman",16),relief=tk.RAISED,borderwidth=2,activeforeground='HotPink4',background='dark slate gray')
        locals()['l'+str(i)].grid(row=i-1,column=0)     
    
    
 
def new_game():
    
    p0=1
    p1=1
    d1=1
    d0=1
    globals()['Result']=''
    
    try:
        window_e7.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love'    
    
    try:
        window_a.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love'
    try:
        window_ab.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love'     
    try:
        window_e1.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love'    
    
    try:
        window_e2.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love'    
    try:
        window_e3.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love'    
    
    try:
        window_e4.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love'    
    try:
        window_e5.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love'    
    try:
        window_e6.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love'    
    
    try:
        window_eeee.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love'    
    try:
        window_eee.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love'    
    try:
        window_ee.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love'     
    
    try:
        globals()['button'].destroy()
    except NameError:
        Imu2=240        
    except KeyError:
        Roti2=259   
    try:
        globals()['aubutton'].destroy()
    except NameError:
        Imu2=240        
    except KeyError:
        Roti2=259         
    try:
        window_e.destroy()
    except NameError:
        L='I LOVE YOU, IMU.'
    except tk.TclError:
        Prerona='Love'         
    try:
        window_2.destroy()
    except NameError:
        vcd=1  
    except tk.TclError:
        vvv=1 
    try: 
        frame.destroy()
    except NameError:
        abc=1        
    try: 
        frame_2.destroy()
    except NameError:
            abcd=1     
    try:        
        pp=int(entry_player.get().strip())
        globals()['Players']=pp
    except ValueError:
        p1=0    
    try:
        dim2=int(entry_dim.get().strip())
        globals()['Dimension']=dim2        
    except ValueError:
        d1=0        
    try:
        if entry_dim.get().strip()=='0':
            d0=0
        if pp!=0:
            p=pp
        else:
            p0=0
        if dim2!=0:
            dim=dim2
        else:
            d0=0              
        for i in range(0,p-1):
            try:
                globals()['window_c'+str(i)].destroy()
            except NameError:
                vbv=1
            except tk.TclError:
                rff=1 
            except KeyError:
                she=1 
   
        CC.clear()
        CRC.clear()
        CR.clear()
        for ri in range(0,dim):
            CR.append([])
            
        CCl.clear()
        for ri in range(0,dim):
            CCl.append([])        
            
        
        computer.clear()
        for i in range(0,p):

            globals()['comp_'+str(i)]=[]
    
            for c1 in range(0,dim):
                globals()['comp_'+str(i)+'_'+str(c1)]=[]   
                for c2 in range(0,dim):
                    globals()['comp_'+str(i)+'_'+str(c1)].append(0)   
                globals()['comp_'+str(i)].append((globals()['comp_'+str(i)+'_'+str(c1)])) 

            computer.append(globals()['comp_'+str(i)])
        
     
        LLLL.clear()
        for num in range(1,dim*dim+1):
            LLLL.append(num)
            
        Account.clear()
        for num in range(1,dim*dim+1):
            Account.append(num)
            
        LLL.clear()
        for numm in range(1,dim*dim+1):
            LLL.append(numm)
            
        row.clear()
        for c1 in range(0,dim):
            globals()['row_'+str(c1)]=[]   
            for c2 in range(0,dim):
                globals()['row_'+str(c1)].append(0)   
            row.append(globals()['row_'+str(c1)])
            
        column.clear()
        for c1 in range(0,dim):
            globals()['column_'+str(c1)]=[]   
            for c2 in range(0,dim):
                globals()['column_'+str(c1)].append(0)   
            column.append(globals()['column_'+str(c1)])   

        com_row.clear()    
        for i in range(0,p-1):  
            globals()['com_row_'+str(i)]=[]  
            for c1 in range(0,dim):
                globals()['com_row_'+str(i)+'_'+str(c1)]=[]   
                for c2 in range(0,dim):
                    globals()['com_row_'+str(i)+'_'+str(c1)].append(0) 
                globals()['com_row_'+str(i)].append(globals()['com_row_'+str(i)+'_'+str(c1)])            
            com_row.append(globals()['com_row_'+str(i)])

        com_column.clear()

        for i in range(0,p-1): 
            globals()['com_column_'+str(i)]=[]   
            for c1 in range(0,dim):
                globals()['com_column_'+str(i)+'_'+str(c1)]=[]   
                for c2 in range(0,dim):
                    globals()['com_column_'+str(i)+'_'+str(c1)].append(0) 
                globals()['com_column_'+str(i)].append(globals()['com_column_'+str(i)+'_'+str(c1)])            
            com_column.append(globals()['com_column_'+str(i)])
    
    
    
        R.clear()
        for i in range(0,p-1):    
            globals()['Rs_'+str(i)]=[]
            R.append(globals()['Rs_'+str(i)])
    
        C.clear()
        for i in range(0,p-1):    
            globals()['Cs_'+str(i)]=[]
            C.append(globals()['Cs_'+str(i)])    
        

        Account.clear()
        for num in range(1,dim*dim+1):
            Account.append(num)
        LLL.clear()
        for mmm in range (1,dim*dim+1):
            LLL.append(mmm)

        for i in range (0,dim):
            row[i].clear()
        for i in range(0,dim):
            column[i].clear()    
        cross.clear() 

        reverse_cross.clear()

        for i in range (0,p-1):
            for j in range(0,dim):
                com_row[i][j].clear()
        for i in range(0,p-1):
            for j in range (0,dim):
                com_column[i][j].clear()
        com_cross.clear() 
        for i in range(0,p-1):
            globals()['com_cross'+str(i)]=[]
            com_cross.append(globals()['com_cross'+str(i)])

        com_reverse_cross.clear()
        for i in range(0,p-1):
            globals()['com_reverse_cross'+str(i)]=[]
            com_reverse_cross.append(globals()['com_reverse_cross'+str(i)])
        
        

        list=[]
        for i in range(0,p-1):
            list.clear()
            for nn in range(0,len(LLLL)):
                list.append(LLLL[nn])
            ll=len(list)
            for ii in range(0,dim):
                for jj in range(0,dim):
                    xx=random.randint(0,ll-1)
                    computer[i][ii][jj]=list[xx]
                    list.remove(list[xx])
                    ll=ll-1
                
                
  

        
   
        globals()['frame']=tk.Frame(master=window,relief=tk.RAISED,borderwidth=2)    

        for i in range(0,dim):
            for j in range(0,dim):
                globals()['entry_'+str(i)+'_'+str(j)]=tk.Entry(master=frame,width=int(20/dim),font=("Times New Roman",28),relief=tk.RAISED,borderwidth=4,background='white')
                globals()['entry_'+str(i)+'_'+str(j)].grid(row=i,column=j)
        globals()['button']=tk.Button(master=window,text='START GAME',activeforeground='blue4',background='green',font=("Times New Roman",28),command=click_button) 
        globals()['aubutton']=tk.Button(master=window,text='FILL AUTOMATICALLY',activeforeground='blue4',background='sea green',font=("Times New Roman",28),command=auto_fill) 
        frame.grid(row=3,column=0)
        aubutton.grid(row=4,column=0)
        button.grid(row=5,column=0,columnspan=2,sticky=tk.W+tk.E) 
    except UnboundLocalError:
        try:
            globals()['button'].destroy()
        except NameError:
            Imu=240        
        except KeyError:
            Roti=259        
        err=''
        if d1==0:
            err=err+'Enter a Valid Number for Dimension.\n'
        if d0==0:
            err=err+'Enter a Valid Number for Dimension Except Zero.\n'   
        if p1==0:
            err=err+'Enter a Valid Number for Players.\n'            
        if p0==0:
            err=err+'Enter a Valid Number for Players Except Zero.\n' 
        leng=len('Enter a Valid Number for Dimension Except Zero.\n')  
        globals()['window_e']=tk.Tk()         
        globals()['label_e']=tk.Label(master=globals()['window_e'],text=err,height=3,width=leng,font=("Times New Roman",28),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='orange')    
        globals()['label_e'].grid(row=0,column=0)
        
        
        
def auto_fill():

    try:
        window_e7.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love' 

    try:
        window_a.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love'
    try:
        window_ab.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love' 
    Love_for_Rifa.clear()
    Love_for_Rifa.append('Rifa')
    Man.clear()
    try:
        dim=int(entry_dim.get().strip())
        p=int(entry_player.get().strip())   
        if dim!=Dimension:
            globals()['w'].destroy()
        if p!=Players:
            globals()['ww'].destroy()                
        
        for i in range(0,dim*dim):
            Man.append(i+1)
        for i in range(0,dim):
            for j in range(0,dim):
                mmm=random.randint(0,len(Man)-1)
                globals()['Man'+str(i)+str(j)]=Man[mmm]
            
                m_label=tk.Label(master=frame,text=Man[mmm],height=1,width=int(20/dim),font=("Times New Roman",28),relief=tk.RAISED,borderwidth=4,activeforeground='white',background='white')  
                m_label.grid(row=i,column=j)
                Man.remove(Man[mmm])
        
        globals()['aubutton'].destroy()   
    except ValueError:
        globals()['window_a']=tk.Tk() 
        a='Dimension and Number of Players Must be Real Numbers. Also Click New Game If You Want to Change Any of Those.'        
        globals()['label_a']=tk.Label(master=globals()['window_a'],text=a,height=3,width=len(a),font=("Times New Roman",20),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='orange')    
        globals()['label_a'].grid(row=0,column=0) 

    except KeyError:
        globals()['window_ab']=tk.Tk() 
        ab='Click New Game If You Want to Change Dimension or Number of Players.'        
        globals()['label_ab']=tk.Label(master=globals()['window_ab'],text=ab,height=3,width=len(ab),font=("Times New Roman",20),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='orange')    
        globals()['label_ab'].grid(row=0,column=0) 
        
        
def click_button():

    try:
        window_e7.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love' 
    try:
        window_a.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love'
    try:
        window_ab.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love' 

    try:
        window_eee.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love'
    try:
        window_eeee.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love'        
    try:
        window_ee.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love'        
   
    
    
    try:
        try:
            dim=int(entry_dim.get().strip())
            p=int(entry_player.get().strip()) 
            
        
        except ValueError:
            z=zz+1
        if dim!=Dimension:
            globals()['w'].destroy()
        if p!=Players:
            globals()['ww'].destroy()   


                
        if len(Love_for_Rifa)!=1:
        
            for k in range(0,dim):
                for l in range(0,dim):
                    for i in range(0,dim):
                        for j in range(0,dim):
                            if k!=i or l!=j:
                                if int(globals()['entry_'+str(k)+'_'+str(l)].get().strip())==int(globals()['entry_'+str(i)+'_'+str(j)].get().strip()):
                                    check='a'+1
                            if int(globals()['entry_'+str(i)+'_'+str(j)].get().strip())==0 or int(globals()['entry_'+str(i)+'_'+str(j)].get().strip())>(dim*dim):
                                check2='a'+1

            for i in range(0,dim):
                for j in range(0,dim):
                    globals()['Man'+str(i)+str(j)]=int(globals()['entry_'+str(i)+'_'+str(j)].get().strip())
        globals()['button'].destroy()
        globals()['frame_2']=tk.Frame(master=window,relief=tk.RAISED,borderwidth=2)  
        label=tk.Label(master=frame_2,text='Enter the Digit:',height=1,width=15,font=("Times New Roman",28),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='orange')
        globals()['entry']=tk.Entry(master=frame_2,width=5,font=("Times New Roman",28),relief=tk.RAISED,borderwidth=2,background='white') 
        label.grid(row=0,column=0)
        entry.grid(row=0,column=1) 
    
        globals()['playbutton']=tk.Button(master=frame_2,text='PLAY',width=20,activeforeground='blue4',background='green',font=("Times New Roman",28),command=play)
        globals()['playbutton'].grid(row=p,column=0,columnspan=2,sticky=tk.W+tk.E)
        frame_2.grid(row=3,column=1)                    
                    
        globals()['aubutton'].destroy()
    except ValueError:
        globals()['window_ee']=tk.Tk() 
        Rif1='Error! Do not Keep Any Box Empty. All Inputs Must be Integers between 1 and '+str(dim*dim)+'. Repeatation not Allowed.'        
        globals()['label_ee']=tk.Label(master=globals()['window_ee'],text=Rif1,height=3,width=len(Rif1),font=("Times New Roman",20),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='orange')    
        globals()['label_ee'].grid(row=0,column=0) 

    except TypeError:
        globals()['window_ee']=tk.Tk() 
        Rif2='Error! Do not Keep Any Box Empty. All Inputs Must be Integers between 1 and '+str(dim*dim)+'. Repeatation not Allowed.'        
        globals()['label_ee']=tk.Label(master=globals()['window_ee'],text=Rif2,height=3,width=len(Rif2),font=("Times New Roman",20),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='orange')    
        globals()['label_ee'].grid(row=0,column=0)         

    except NameError:
        globals()['window_eee']=tk.Tk()   
        Rif3='Error! Dimension and Number of Players Must be Real Integers. Also Click New Game If You Want to Change Dimension or Number of Players.'        
        globals()['label_eee']=tk.Label(master=globals()['window_eee'],text=Rif3,height=3,width=len(Rif3),font=("Times New Roman",20),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='orange')    
        globals()['label_eee'].grid(row=0,column=0) 
    except KeyError:
        globals()['window_eeee']=tk.Tk()         
        Rif4='Click New Game If You Want to Change Dimension or Number of  Players.'
        globals()['label_eeee']=tk.Label(master=globals()['window_eeee'],text=Rif4,height=3,width=len(Rif4),font=("Times New Roman",20),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='orange')    
        globals()['label_eeee'].grid(row=0,column=0)


def play():

    try:
        window_e7.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love' 
    try:
        window_2.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love'
    try:
        window_e1.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love'    
    
    try:
        window_e2.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love'    
    try:
        window_e3.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love'    
    
    try:
        window_e4.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love'    
    try:
        window_e5.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love'    
    try:
        window_e6.destroy()
    except NameError:
        Love='I LOVE YOU, IMU.'
    except tk.TclError:
        Rifa='Love' 
    for i in range(0,Players-1):
        try:
            globals()['window_c'+str(i)].destroy()
        except KeyError:
            Love='I LOVE YOU, IMU.'
        except tk.TclError:
            Rifa='Love'   

    try:
        if globals()['Result']!='':
            Nawshin=[1,2,3]
            print(Nawshin[5])                 
        try:
            dim=int(entry_dim.get().strip())
            p=int(entry_player.get().strip())
        except ValueError:
            z=zz+1 
            
        if dim!=Dimension:
            globals()['w'].destroy()
        if p!=Players:
            globals()['ww'].destroy()  

        if len(Love_for_Rifa)!=1:
            for i in range(0,dim):
                for j in range(0,dim):
                    if globals()['Man'+str(i)+str(j)]!=int(globals()['entry_'+str(i)+'_'+str(j)].get().strip()):
                        globals()['Rifa'].destroy()
            
        try:    
            Digit=int(entry.get().strip())
            if Digit==0 or Digit>(dim*dim):
                Safa=4/0
        except ValueError:
            z=int('a') 
            
        try:
            Account.remove(Digit)
        except ValueError:
            sss='6'+5  

            
        for iii in range(0,dim):
            for jjj in range(0,dim):
                if globals()['Man'+str(iii)+str(jjj)]==Digit:
                    if jjj not in row[iii]:
                        row[iii].append(jjj)
                    if iii not in column[jjj]:
                        column[jjj].append(iii)

                    if iii==jjj and iii not in cross:
                        cross.append(iii) 

                    if dim-1-iii==jjj and jjj not in reverse_cross:
                        reverse_cross.append(jjj)
                    
                    new_label=tk.Label(master=frame,text=entry.get(),height=1,width=int(20/dim),font=("Times New Roman",28),relief=tk.RAISED,borderwidth=4,activeforeground='blue4',background='brown4')  
                    new_label.grid(row=iii,column=jjj)
                    try:
                        LLL.remove(int(entry.get().strip()))
                    except ValueError:
                        Shanta=143
                                               
     
        for i in range(0,p-1):     
            for ij1 in range(0,dim):
                for ij2 in range(0,dim):
                    if computer[i][ij1][ij2]==Digit:
            
                        R[i].append(ij1)
                        C[i].append(ij2)
                        if ij2 not in com_row[i][ij1]:
                            com_row[i][ij1].append(ij2)
                        if ij1 not in com_column[i][ij2]:
                            com_column[i][ij2].append(ij1)

                        if ij1==ij2 and ij1 not in com_cross[i]:
                            com_cross[i].append(ij1) 

                        if dim-1-ij1==ij2 and ij1 not in com_reverse_cross[i]:
                            com_reverse_cross[i].append(ij1)                
                    


        Bingo=0
    
        if len(cross)==dim:
            for ii in range(0,dim): 
                globals()[str(ii)+str(ii)]=tk.Label(master=frame,text=globals()['entry_'+str(ii)+'_'+str(ii)].get(),height=1,width=int(20/dim),font=("Times New Roman",28),relief=tk.RAISED,borderwidth=4,activeforeground='blue4',background='black')  
                globals()[str(ii)+str(ii)].grid(row=ii,column=ii)
            Bingo=Bingo+1
        if len(reverse_cross)==dim:
            for ii in range(0,dim):
                globals()[str(ii)+str(dim-1-ii)]=tk.Label(master=frame,text=globals()['entry_'+str(ii)+'_'+str(dim-1-ii)].get(),height=1,width=int(20/dim),font=("Times New Roman",28),relief=tk.RAISED,borderwidth=4,activeforeground='blue4',background='black')  
                globals()[str(ii)+str(dim-1-ii)].grid(row=ii,column=dim-1-ii)
            Bingo=Bingo+1    
        for count in range(0,dim):
            if len(row[count])==dim:
                for ii in range(0,dim):
                    globals()[str(count)+str(ii)]=tk.Label(master=frame,text=globals()['entry_'+str(count)+'_'+str(ii)].get(),height=1,width=int(20/dim),font=("Times New Roman",28),relief=tk.RAISED,borderwidth=4,activeforeground='blue4',background='black')  
                    globals()[str(count)+str(ii)].grid(row=count,column=ii)        
                Bingo=Bingo+1
        
            if len(column[count])==dim:
                for ii in range(0,dim):
                    globals()[str(ii)+str(count)]=tk.Label(master=frame,text=globals()['entry_'+str(ii)+'_'+str(count)].get(),height=1,width=int(20/dim),font=("Times New Roman",28),relief=tk.RAISED,borderwidth=4,activeforeground='blue4',background='black')  
                    globals()[str(ii)+str(count)].grid(row=ii,column=count)             
                Bingo=Bingo+1 
        CC.clear()
        CRC.clear()
        CR.clear()
        for ri in range(0,dim):
            CR.append([])
            
        CCl.clear()
        for ri in range(0,dim):
            CCl.append([])                  
    
        for i in range(0,p-1):
            globals()['com_Bingo_'+str(i)]=0
            if len(com_cross[i])==dim:
                globals()['com_Bingo_'+str(i)]=globals()['com_Bingo_'+str(i)]+1
                CC.append(i)
            if len(com_reverse_cross[i])==dim:
                globals()['com_Bingo_'+str(i)]=globals()['com_Bingo_'+str(i)]+1
                CRC.append(i)
            for com_count in range(0,dim):
                if len(com_row[i][com_count])==dim:
                    globals()['com_Bingo_'+str(i)]=globals()['com_Bingo_'+str(i)]+1
                    CR[com_count].append(i)
        
                if len(com_column[i][com_count])==dim:
                    globals()['com_Bingo_'+str(i)]=globals()['com_Bingo_'+str(i)]+1  
                    CCl[com_count].append(i)
        if Bingo>=dim:
            globals()['Result']=globals()['Result']+'YOU'
        for i in range(0,p-1):
            if globals()['com_Bingo_'+str(i)]>=dim:
                globals()['Result']=globals()['Result']+' AND PLAYER '+str(i+1)        
        if globals()['Result']!='':
            globals()['window_2']=tk.Tk()
            BINGO=tk.Label(master=globals()['window_2'],text=globals()['Result']+' HAVE WON.',height=3,width=50,font=("Times New Roman",35),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='orange')
            BINGO.grid(row=0,column=0)
            for i in range(0,p-1):
                globals()['window_c'+str(i)]=tk.Tk()
                
                globals()['label_c'+str(i)]=tk.Label(master=globals()['window_c'+str(i)],text='PLAYER '+str(i+1),height=1,width=25,font=("Times New Roman",28),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='white')  
                globals()['frame_c'+str(i)]=tk.Frame(master=globals()['window_c'+str(i)],relief=tk.RAISED,borderwidth=2)
                for ir in range(0,dim):
                    for jc in range(0,dim):
                    
                        globals()['com_label_'+str(i)+'_'+str(ir)+'_'+str(jc)]=tk.Label(master=globals()['frame_c'+str(i)],text=str(computer[i][ir][jc]),height=1,width=5,font=("Times New Roman",28),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='white')  
                        globals()['com_label_'+str(i)+'_'+str(ir)+'_'+str(jc)].grid(row=ir,column=jc)
                for rc in range(0,len(R[i])):
                    
                    globals()['com_label_'+str(i)+'_'+str(R[i][rc])+'_'+str(C[i][rc])]=tk.Label(master=globals()['frame_c'+str(i)],text=str(computer[i][R[i][rc]][C[i][rc]]),height=1,width=5,font=("Times New Roman",28),relief=tk.RAISED,borderwidth=2,activeforeground='red3',background='brown4')  
                    globals()['com_label_'+str(i)+'_'+str(R[i][rc])+'_'+str(C[i][rc])].grid(row=R[i][rc],column=C[i][rc])
                if i in CC:
                    for r in range(0,dim):
                        globals()['L'+str(i)+str(r)]=tk.Label(master=globals()['frame_c'+str(i)],text=str(computer[i][r][r]),height=1,width=5,font=("Times New Roman",28),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='black')                 
                        globals()['L'+str(i)+str(r)].grid(row=r,column=r)
                        
                if i in CRC:
                    for r in range(0,dim):
                        globals()['L2'+str(i)+str(r)]=tk.Label(master=globals()['frame_c'+str(i)],text=str(computer[i][r][dim-1-r]),height=1,width=5,font=("Times New Roman",28),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='black')                 
                        globals()['L2'+str(i)+str(r)].grid(row=r,column=dim-1-r) 
                for j in range(0,dim):
                    if i in CR[j]:
                        for r in range(0,dim):
                            globals()['L3'+str(j)+str(i)+str(r)]=tk.Label(master=globals()['frame_c'+str(i)],text=str(computer[i][j][r]),height=1,width=5,font=("Times New Roman",28),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='black')                 
                            globals()['L3'+str(j)+str(i)+str(r)].grid(row=j,column=r)  
                for j in range(0,dim):
                    if i in CCl[j]:
                        for r in range(0,dim):
                            globals()['L4'+str(j)+str(i)+str(r)]=tk.Label(master=globals()['frame_c'+str(i)],text=str(computer[i][r][j]),height=1,width=5,font=("Times New Roman",28),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='black')                 
                            globals()['L4'+str(j)+str(i)+str(r)].grid(row=r,column=j)                            
               
                globals()['label_c'+str(i)].grid(row=0,column=0)

                globals()['frame_c'+str(i)].grid(row=1,column=0)

        
        




        else:     
            for i in range(0,p-1):
            
                globals()['length'+str(i)]=[]
                for j in range(0,dim):
                    globals()['length'+str(i)].append(len(com_row[i][j]))
                for j in range(0,dim):
                    globals()['length'+str(i)].append(len(com_column[i][j]))
                globals()['length'+str(i)].append(len(com_cross[i]))
                globals()['length'+str(i)].append(len(com_reverse_cross[i]))
                xxx=0
                for j in range(0,len(globals()['length'+str(i)])):
                    if globals()['length'+str(i)][j]==dim:
                        xxx=xxx+1
                for j in range(0,xxx):
                    globals()['length'+str(i)].remove(dim)            
                M=max(globals()['length'+str(i)])    
    
                globals()['row_sep'+str(i)]=[]
                for j in range(0,dim):
                    if len(com_row[i][j])==M:
                        globals()['row_sep'+str(i)].append(j)
                globals()['column_sep'+str(i)]=[]        
                for j in range(0,dim):
                    if len(com_column[i][j])==M:
                        globals()['column_sep'+str(i)].append(j)
    
                for k in globals()['row_sep'+str(i)]:
                    (globals()['empty_row_'+str(k)])=[]
                    for j in range(0,dim):
                        if j not in (com_row[i][k]):
                            (globals()['empty_row_'+str(k)]).append(j)
                
                
                for k in globals()['column_sep'+str(i)]:
                    (globals()['empty_column_'+str(k)])=[]
                    for j in range(0,dim):
                        if j not in (com_column[i][k]):
                            (globals()['empty_column_'+str(k)]).append(j) 

                            
                F=[]    
                T=[]
                TL=[]
                TF=[]    
                for l in globals()['row_sep'+str(i)]:
                    for m in globals()['empty_row_'+str(l)]:
                        T.append((l,m))
                        F.append(len(com_column[i][m]))
            
                for l in globals()['column_sep'+str(i)]:
                    for m in globals()['empty_column_'+str(l)]:
                        T.append((m,l))
                        F.append(len(com_row[i][m]))

                if len(F)==0:
                    acc=random.randint(0,len(Account)-1)
                    com=Account[acc]
                    Account.remove(com)  
                else:                
                    FM=max(F)
                
                    for j in range(0,len(F)):
                        if F[j]==FM:
                            TF.append(T[j])
            
                    for j in range(0,len(F)):
                        if F[j]==FM-1:
                            TL.append(T[j])
                    for (m,j) in TL:
                        if m==j or dim-1-m==j:
                            TF.append((m,j))
                    r=random.randint(0,len(TF)-1)
                    com=computer[i][TF[r][0]][TF[r][1]]  
               
                    Account.remove(com)
            
            

            
       
                globals()['com_label'+str(i)]=tk.Label(master=frame_2,text='Player '+str(i+1)+' Says:',height=1,width=15,font=("Times New Roman",28),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='orange')
                globals()['com_label'+str(i)].grid(row=1+i,column=0)                        
                globals()['com_label2'+str(i)]=tk.Label(master=frame_2,text=str(com),height=1,width=5,font=("Times New Roman",28),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='orange')
                globals()['com_label2'+str(i)].grid(row=1+i,column=1)   
                for iiii in range(0,dim):
                    for jjjj in range(0,dim):
                        if globals()['Man'+str(iiii)+str(jjjj)]==com:
                

                            if jjjj not in row[iiii]:
                                row[iiii].append(jjjj)
                            if iiii not in column[jjjj]:
                                column[jjjj].append(iiii)

                            if iiii==jjjj and iiii not in cross:
                                cross.append(iiii) 

                            if dim-1-iiii==jjjj and jjjj not in reverse_cross:
                                reverse_cross.append(jjjj)
                        
                            new_label2=tk.Label(master=frame,text=str(com),height=1,width=int(20/dim),font=("Times New Roman",28),relief=tk.RAISED,borderwidth=4,activeforeground='blue4',background='brown4')  
                            new_label2.grid(row=iiii,column=jjjj)
                            LLL.remove(com)   
                for b in range(0,p-1):                        
                    for ijk1 in range(0,dim):
                        for ijk2 in range(0,dim):
                            if computer[b][ijk1][ijk2]==com:
                                R[b].append(ijk1)
                                C[b].append(ijk2)
                                if ijk2 not in com_row[b][ijk1]:
                                    com_row[b][ijk1].append(ijk2)
                                if ijk1 not in com_column[b][ijk2]:
                                    com_column[b][ijk2].append(ijk1)

                                if ijk1==ijk2 and ijk1 not in com_cross[b]:
                                    com_cross[b].append(ijk1) 

                                if dim-1-ijk1==ijk2 and ijk2 not in com_reverse_cross[b]:
                                    com_reverse_cross[b].append(ijk2)                


                Bingo=0
    
                if len(cross)==dim:
                    for ii in range(0,dim):
                        globals()[str(ii)+str(ii)]=tk.Label(master=frame,text=globals()['entry_'+str(ii)+'_'+str(ii)].get(),height=1,width=int(20/dim),font=("Times New Roman",28),relief=tk.RAISED,borderwidth=4,activeforeground='blue4',background='black')  
                        globals()[str(ii)+str(ii)].grid(row=ii,column=ii)
                    Bingo=Bingo+1
                if len(reverse_cross)==dim:
                    for ii in range(0,dim):
                        globals()[str(ii)+str(dim-1-ii)]=tk.Label(master=frame,text=globals()['entry_'+str(ii)+'_'+str(dim-1-ii)].get(),height=1,width=int(20/dim),font=("Times New Roman",28),relief=tk.RAISED,borderwidth=4,activeforeground='blue4',background='black')  
                        globals()[str(ii)+str(dim-1-ii)].grid(row=ii,column=dim-1-ii)
                    Bingo=Bingo+1    
                for count in range(0,dim):
                    if len(row[count])==dim:
                        for ii in range(0,dim):
                            globals()[str(count)+str(ii)]=tk.Label(master=frame,text=globals()['entry_'+str(count)+'_'+str(ii)].get(),height=1,width=int(20/dim),font=("Times New Roman",28),relief=tk.RAISED,borderwidth=4,activeforeground='blue4',background='black')  
                            globals()[str(count)+str(ii)].grid(row=count,column=ii)        
                        Bingo=Bingo+1
        
                    if len(column[count])==dim:
                        for ii in range(0,dim):
                            globals()[str(ii)+str(count)]=tk.Label(master=frame,text=globals()['entry_'+str(ii)+'_'+str(count)].get(),height=1,width=int(20/dim),font=("Times New Roman",28),relief=tk.RAISED,borderwidth=4,activeforeground='blue4',background='black')  
                            globals()[str(ii)+str(count)].grid(row=ii,column=count)             
                        Bingo=Bingo+1  
                        
                CC.clear()
                CRC.clear()
                CR.clear()
                for ri in range(0,dim):
                    CR.append([])
            
                CCl.clear()
                for ri in range(0,dim):
                    CCl.append([])                         
    
                for j in range(0,p-1):
                    globals()['com_Bingo_'+str(j)]=0
                    if len(com_cross[j])==dim:
                        globals()['com_Bingo_'+str(j)]=globals()['com_Bingo_'+str(j)]+1
                        CC.append(j)
                    if len(com_reverse_cross[j])==dim:
                        globals()['com_Bingo_'+str(j)]=globals()['com_Bingo_'+str(j)]+1
                        CRC.append(j)
                    for com_count in range(0,dim):
                        if len(com_row[j][com_count])==dim:
                            globals()['com_Bingo_'+str(j)]=globals()['com_Bingo_'+str(j)]+1
                            CR[com_count].append(j)
        
                        if len(com_column[j][com_count])==dim:
                            globals()['com_Bingo_'+str(j)]=globals()['com_Bingo_'+str(j)]+1  
                            CCl[com_count].append(j)
                if Bingo>=dim:
                    globals()['Result']=globals()['Result']+'YOU'
                for j in range(0,p-1):
                    if globals()['com_Bingo_'+str(j)]>=dim:
                        globals()['Result']=globals()['Result']+' AND PLAYER '+str(j+1)        
                if globals()['Result']!='':
                    globals()['window_2']=tk.Tk()
                    BINGO=tk.Label(master=globals()['window_2'],text=globals()['Result']+' HAVE WON.',height=3,width=50,font=("Times New Roman",35),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='orange')
                    BINGO.grid(row=0,column=0)
                    for j in range(0,p-1):
                        globals()['window_c'+str(j)]=tk.Tk()
                        
                        globals()['label_c'+str(j)]=tk.Label(master=globals()['window_c'+str(j)],text='PLAYER '+str(j+1),height=1,width=25,font=("Times New Roman",28),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='white')  
                        globals()['frame_c'+str(j)]=tk.Frame(master=globals()['window_c'+str(j)],relief=tk.RAISED,borderwidth=10)
                        for ir in range(0,dim):
                            for jc in range(0,dim):
                                globals()['com_label_'+str(j)+'_'+str(ir)+'_'+str(jc)]=tk.Label(master=globals()['frame_c'+str(j)],text=str(computer[j][ir][jc]),height=1,width=5,font=("Times New Roman",28),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='white')  
                                globals()['com_label_'+str(j)+'_'+str(ir)+'_'+str(jc)].grid(row=ir,column=jc)
                        for rc in range(0,len(R[j])):
                            
                            globals()['com_label_'+str(j)+'_'+str(R[j][rc])+'_'+str(C[j][rc])]=tk.Label(master=globals()['frame_c'+str(j)],text=str(computer[j][R[j][rc]][C[j][rc]]),height=1,width=5,font=("Times New Roman",28),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='brown4')  
                            globals()['com_label_'+str(j)+'_'+str(R[j][rc])+'_'+str(C[j][rc])].grid(row=R[j][rc],column=C[j][rc])
                            
                        if j in CC:
                            for r in range(0,dim):
                                globals()['L'+str(j)+str(r)]=tk.Label(master=globals()['frame_c'+str(j)],text=str(computer[j][r][r]),height=1,width=5,font=("Times New Roman",28),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='black')                 
                                globals()['L'+str(j)+str(r)].grid(row=r,column=r)
                        
                        if j in CRC:
                            for r in range(0,dim):
                                globals()['L2'+str(j)+str(r)]=tk.Label(master=globals()['frame_c'+str(j)],text=str(computer[j][r][dim-1-r]),height=1,width=5,font=("Times New Roman",28),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='black')                 
                                globals()['L2'+str(j)+str(r)].grid(row=r,column=dim-1-r) 
                        for k in range(0,dim):
                            if j in CR[k]:
                                for r in range(0,dim):
                                    globals()['L3'+str(k)+str(j)+str(r)]=tk.Label(master=globals()['frame_c'+str(j)],text=str(computer[j][k][r]),height=1,width=5,font=("Times New Roman",28),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='black')                 
                                    globals()['L3'+str(k)+str(j)+str(r)].grid(row=k,column=r)  
                        for k in range(0,dim):
                            if j in CCl[k]:
                                for r in range(0,dim):
                                    globals()['L4'+str(k)+str(j)+str(r)]=tk.Label(master=globals()['frame_c'+str(j)],text=str(computer[j][r][k]),height=1,width=5,font=("Times New Roman",28),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='black')                 
                                    globals()['L4'+str(k)+str(j)+str(r)].grid(row=r,column=k)                             
                
                        globals()['label_c'+str(j)].grid(row=0,column=0)

                        globals()['frame_c'+str(j)].grid(row=1,column=0)

                    break
    
    except ValueError:
        globals()['window_e1']=tk.Tk() 
        Rifa1='Enter an Integer between 1 and '+str(dim*dim)        
        globals()['label_e1']=tk.Label(master=globals()['window_e1'],text=Rifa1,height=3,width=len(Rifa1),font=("Times New Roman",20),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='orange')    
        globals()['label_e1'].grid(row=0,column=0) 


    except TypeError:
        globals()['window_e2']=tk.Tk() 
        Rifa2=str(Digit)+' is Already Booked. Please Enter Another Digit.'        
        globals()['label_e2']=tk.Label(master=globals()['window_e2'],text=Rifa2,height=3,width=len(Rifa2),font=("Times New Roman",20),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='orange')    
        globals()['label_e2'].grid(row=0,column=0)         

    except NameError:
        globals()['window_e3']=tk.Tk() 
        Rifa3='Error! Dimension and Number of Players Must be Real Integers. Also Click New Game If You Want to Change Dimension or Number of Players.'        
        globals()['label_e3']=tk.Label(master=globals()['window_e3'],text=Rifa3,height=3,width=len(Rifa3),font=("Times New Roman",20),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='orange')    
        globals()['label_e3'].grid(row=0,column=0) 
 
    except ZeroDivisionError:
        globals()['window_e5']=tk.Tk() 
        Rifa5='Enter an Integer Between 1 and '+str(dim*dim)        
        globals()['label_e5']=tk.Label(master=globals()['window_e5'],text=Rifa5,height=3,width=len(Rifa5),font=("Times New Roman",20),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='orange')    
        globals()['label_e5'].grid(row=0,column=0)        
        
    except IndexError:
        globals()['window_e6']=tk.Tk() 
        Rifa6='The Game is Finished. Start New Game.'        
        globals()['label_e6']=tk.Label(master=globals()['window_e6'],text=Rifa6,height=3,width=len(Rifa6),font=("Times New Roman",20),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='orange')    
        globals()['label_e6'].grid(row=0,column=0)    

    except KeyError:
        globals()['window_e7']=tk.Tk() 
        Rifa7='Do not Change Any Box Now. Make It Like Before. Click New Game If You Want to Change Dimension or Number of Players.'        
        globals()['label_e7']=tk.Label(master=globals()['window_e7'],text=Rifa7,height=3,width=len(Rifa7),font=("Times New Roman",20),relief=tk.RAISED,borderwidth=2,activeforeground='blue4',background='orange')    
        globals()['label_e7'].grid(row=0,column=0)         
   

newbutton=tk.Button(master=window,text='NEW GAME',activeforeground='blue4',background='green',font=("Times New Roman",28),command=new_game)
newbutton.grid(row=0,column=0,columnspan=2,sticky=tk.W+tk.E)
rbutton=tk.Button(master=window,text='RULES',activeforeground='blue4',background='navy',font=("Times New Roman",28),command=Rules)
rbutton.grid(row=6,column=0,columnspan=2,sticky=tk.W+tk.E)
window.mainloop() 

  
