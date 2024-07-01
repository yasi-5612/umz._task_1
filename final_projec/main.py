from tkinter import *
import back
from tkinter.messagebox import showinfo

def adding(main):
    window = Tk()
    window.geometry("830x400")
    window.title("add food")
    window.configure(bg="#80daeb")
    l1= Label(window,text="please enter your food details",font=(20),bg="#80daeb",fg="black").grid(row=0,column=2)
    l2 = Label(window , text="FOOD NAME :",font=11,bg="#80daeb",fg="#E22B11")
    l2.grid(row=2,column=0)
    food_text= StringVar()
    e2= Entry(window,textvariable=food_text,fg="black",font=8,bg="#C0FFF8").grid(row=2,column=1) 
    meal=["breakfast","lunch","dinner"]
    q=0
    var15=StringVar()
    for i in meal:
        q+=1
        rad = Radiobutton(window,text=i,value=i,variable=var15,fg=("#E22B11"),bg="#80daeb",font=4,activebackground="#80daeb",activeforeground="#E22B11").grid(row=3,column=q)
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 =IntVar()
    var11 =IntVar()
    var12 =IntVar()
    var13= IntVar()
    var14= IntVar()
#---- check material food-----
    mater_food=[]
    def print_selection():
        if (var1.get() == 1):
            if "chicken" not in mater_food:
                mater_food.append("chicken")
        else:
            try:
                mater_food.remove("chicken")
            except:
                pass
        if (var2.get() == 1):
            if "beef" not in mater_food:
                mater_food.append("beef")
        else:
            try:
                mater_food.remove("beef")
            except:
                pass
        if (var3.get() == 1):
            if "tomato" not in mater_food:
                mater_food.append("tomato")
        else:
            try:
                mater_food.remove("tomato")
            except:
                pass
        if (var4.get() == 1):
            if "potato" not in mater_food:
                mater_food.append("potato")
        else:
            try:
                mater_food.remove("potato")
            except:
                pass
        if (var5.get() == 1):
            if "rice" not in mater_food:
                mater_food.append("rice")
        else:
            try:
                mater_food.remove("rice")
            except:
                pass
        if (var6.get() == 1):
            if "bean" not in mater_food:
                mater_food.append("bean")
        else:
            try:
                mater_food.remove("bean")
            except:
                pass
        if (var7.get() == 1):
            if "salt" not in mater_food:
                mater_food.append("salt")
        else:
            try:
                mater_food.remove("salt")
            except:
                pass
        if (var8.get() == 1):
            if "pepper" not in mater_food:
                mater_food.append("pepper")
        else:
            try:
                mater_food.remove("pepper")
            except:
                pass
        if (var9.get() == 1):
            if "egg" not in mater_food:
                mater_food.append("egg")
        else:
            try:
                mater_food.remove("egg")
            except:
                pass
        if (var10.get() == 1):
            if "flour" not in mater_food:
                mater_food.append("flour")
        else:
            try:
                mater_food.remove("flour")
            except:
                pass
        if (var11.get() == 1):
            if "onion" not in mater_food:
                mater_food.append("onion")
        else:
            try:
                mater_food.remove("onion")
            except:
                pass
        if (var12.get() == 1):
            if "vegetable" not in mater_food:
                mater_food.append("vegetable")
        else:
            try:
                mater_food.remove("vegetable")
            except:
                pass
        if (var13.get() == 1):
            if "oil" not in mater_food:
                mater_food.append("oil")
        else:
            try:
                mater_food.remove("oil")
            except:
                pass
        if (var14.get() == 1):
            if "sugar" not in mater_food:
                mater_food.append("sugar")
        else:
            try:
                mater_food.remove("sugar")
            except:
                pass
        print(var15.get())
    c1= Checkbutton(window, text='chicken',variable=var1, onvalue=1, offvalue=0, command=print_selection,font=17,bg="#80daeb",activebackground="#80daeb").grid(row=5,column=1)
    c2 = Checkbutton(window, text='beef',variable=var2, onvalue=1, offvalue=0, command=print_selection,font=17,bg="#80daeb",activebackground="#80daeb").grid(row=5,column=4)
    c3 = Checkbutton(window, text="tomato",variable=var3, onvalue=1, offvalue=0, command=print_selection,font=17,bg="#80daeb",activebackground="#80daeb").grid(row=6,column=1)
    c4 = Checkbutton(window, text='potato',variable=var4, onvalue=1, offvalue=0, command=print_selection,font=17,bg="#80daeb",activebackground="#80daeb").grid(row=6,column=4)
    c5 = Checkbutton(window, text='rice',variable=var5, onvalue=1, offvalue=0, command=print_selection,font=17,bg="#80daeb",activebackground="#80daeb").grid(row=7,column=1)
    c6 = Checkbutton(window, text='bean',variable=var6, onvalue=1, offvalue=0, command=print_selection,font=17,bg="#80daeb",activebackground="#80daeb").grid(row=7,column=4)
    c7 =Checkbutton(window, text='salt',variable=var7, onvalue=1, offvalue=0, command=print_selection,font=17,bg="#80daeb",activebackground="#80daeb").grid(row=8,column=1)
    c8 =Checkbutton(window, text="pepper",variable=var8, onvalue=1, offvalue=0, command=print_selection,font=17,bg="#80daeb",activebackground="#80daeb").grid(row=8,column=4)
    c9 = Checkbutton(window, text='egg ',variable=var9, onvalue=1, offvalue=0, command=print_selection,font=17,bg="#80daeb",activebackground="#80daeb").grid(row=9,column=1)
    c10 =Checkbutton(window, text='flour',variable=var10, onvalue=1, offvalue=0, command=print_selection,font=17,bg="#80daeb",activebackground="#80daeb").grid(row=9,column=4)
    c11 = Checkbutton(window, text='onion',variable=var11, onvalue=1, offvalue=0, command=print_selection,font=17,bg="#80daeb",activebackground="#80daeb").grid(row=10,column=1)
    c12 =Checkbutton(window, text='vegetable',variable=var12, onvalue=1, offvalue=0, command=print_selection,font=17,bg="#80daeb",activebackground="#80daeb").grid(row=10,column=4)
    c13 =Checkbutton(window, text='oil',variable=var13, onvalue=1, offvalue=0, command=print_selection,font=17,bg="#80daeb",activebackground="#80daeb").grid(row=11,column=1)
    c14 =Checkbutton(window, text='sugar',variable=var14, onvalue=1, offvalue=0, command=print_selection,font=17,bg="#80daeb",activebackground="#80daeb").grid(row=11,column=4)
    def meow():
        q=0
        if food_text.get()== "":
            pass
        else:
            q +=1
        if var15.get()=="breakfast" or var15.get()=="lunch" or var15.get()=="dinner":
            q+=1
        else:
            pass
        if mater_food ==[]:
            pass
        else:
            q+=1
        if q==3:
            d= str(food_text.get())
            back.insert(str(d),str(mater_food),var15.get() )
            showinfo(title="notice",message="mission compelete")
        else:
            showinfo(title="notice",message="u miss something")
    b=Button(window,text="save",command=meow,font=10).grid(row=10)
    def mai():
        window.destroy()
        main()
    ex=Button(window,text="back",command=mai,font=10).grid(row=11)
    window.mainloop()
def finding(main):
    window=Tk()
    window.geometry("650x560")
    window.title("find food")
    window.configure(bg='#117EC4')
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 =IntVar()
    var11 =IntVar()
    var12 =IntVar()
    var13= IntVar()
    var14= IntVar()
    mater_food=[]
    def print_selection():
        if (var1.get() == 1):
            if "chicken" not in mater_food:
                mater_food.append("chicken")
        else:
            try:
                mater_food.remove("chicken")
            except:
                pass
        if (var2.get() == 1):
            if "beef" not in mater_food:
                mater_food.append("beef")
        else:
            try:
                mater_food.remove("beef")
            except:
                pass
        if (var3.get() == 1):
            if "tomato" not in mater_food:
                mater_food.append("tomato")
        else:
            try:
                mater_food.remove("tomato")
            except:
                pass
        if (var4.get() == 1):
            if "potato" not in mater_food:
                mater_food.append("potato")
        else:
            try:
                mater_food.remove("potato")
            except:
                pass
        if (var5.get() == 1):
            if "rice" not in mater_food:
                mater_food.append("rice")
        else:
            try:
                mater_food.remove("rice")
            except:
                pass
        if (var6.get() == 1):
            if "bean" not in mater_food:
                mater_food.append("bean")
        else:
            try:
                mater_food.remove("bean")
            except:
                pass
        if (var7.get() == 1):
            if "salt" not in mater_food:
                mater_food.append("salt")
        else:
            try:
                mater_food.remove("salt")
            except:
                pass
        if (var8.get() == 1):
            if "pepper" not in mater_food:
                mater_food.append("pepper")
        else:
            try:
                mater_food.remove("pepper")
            except:
                pass
        if (var9.get() == 1):
            if "egg" not in mater_food:
                mater_food.append("egg")
        else:
            try:
                mater_food.remove("egg")
            except:
                pass
        if (var10.get() == 1):
            if "flour" not in mater_food:
                mater_food.append("flour")
        else:
            try:
                mater_food.remove("flour")
            except:
                pass
        if (var11.get() == 1):
            if "onion" not in mater_food:
                mater_food.append("onion")
        else:
            try:
                mater_food.remove("onion")
            except:
                pass
        if (var12.get() == 1):
            if "vegetable" not in mater_food:
                mater_food.append("vegetable")
        else:
            try:
                mater_food.remove("vegetable")
            except:
                pass
        if (var13.get() == 1):
            if "oil" not in mater_food:
                mater_food.append("oil")
        else:
            try:
                mater_food.remove("oil")
            except:
                pass
        if (var14.get() == 1):
            if "sugar" not in mater_food:
                mater_food.append("sugar")
        else:
            try:
                mater_food.remove("sugar")
            except:
                pass
    label_12=Label(window,text="search by food name",font=6,bg="#117EC4").grid(padx=0)  
    e12_var=StringVar()
    e_12=Entry(window,textvariable=e12_var,font=6).grid(padx=5)
    c1= Checkbutton(window, text='chicken',variable=var1, onvalue=1, offvalue=0, command=print_selection,font=15,bg='#117EC4',activebackground='#117EC4').grid(row=9,column=2)
    c2 = Checkbutton(window, text='beef',variable=var2, onvalue=1, offvalue=0, command=print_selection,font=15,bg='#117EC4',activebackground='#117EC4').grid(row=9,column=5)
    c3 = Checkbutton(window, text="tomato",variable=var3, onvalue=1, offvalue=0, command=print_selection,font=15,bg='#117EC4',activebackground='#117EC4').grid(row=3,column=2)
    c4 = Checkbutton(window, text='potato',variable=var4, onvalue=1, offvalue=0, command=print_selection,font=15,bg='#117EC4',activebackground='#117EC4').grid(row=3,column=5)
    c5 = Checkbutton(window, text='rice',variable=var5, onvalue=1, offvalue=0, command=print_selection,font=15,bg='#117EC4',activebackground='#117EC4').grid(row=4,column=2)
    c6 = Checkbutton(window, text='bean',variable=var6, onvalue=1, offvalue=0, command=print_selection,font=15,bg='#117EC4',activebackground='#117EC4').grid(row=4,column=5)
    c7 =Checkbutton(window, text='salt',variable=var7, onvalue=1, offvalue=0, command=print_selection,font=15,bg='#117EC4',activebackground='#117EC4').grid(row=5,column=2)
    c8 =Checkbutton(window, text="pepper",variable=var8, onvalue=1, offvalue=0, command=print_selection,font=15,bg='#117EC4',activebackground='#117EC4').grid(row=5,column=5)
    c9 = Checkbutton(window, text='egg ',variable=var9, onvalue=1, offvalue=0, command=print_selection,font=15,bg='#117EC4',activebackground='#117EC4').grid(row=6,column=2)
    c10 =Checkbutton(window, text='flour',variable=var10, onvalue=1, offvalue=0, command=print_selection,font=15,bg='#117EC4',activebackground='#117EC4').grid(row=6,column=5)
    c11 = Checkbutton(window, text='onion',variable=var11, onvalue=1, offvalue=0, command=print_selection,font=15,bg='#117EC4',activebackground='#117EC4').grid(row=7,column=2)
    c12 =Checkbutton(window, text='vegetable',variable=var12, onvalue=1, offvalue=0, command=print_selection,font=15,bg='#117EC4',activebackground='#117EC4').grid(row=7,column=5)
    c13 =Checkbutton(window, text='oil',variable=var13, onvalue=1, offvalue=0, command=print_selection,font=15,bg='#117EC4',activebackground='#117EC4').grid(row=8,column=2)
    c14 =Checkbutton(window, text='sugar',variable=var14, onvalue=1, offvalue=0, command=print_selection,font=15,bg='#117EC4',activebackground='#117EC4').grid(row=8,column=5)
    def clear():
        list_1.delete(0,END)
    def view_bot(x):
        book = back.search(x)
        fill_list(book)
    def fill_list(book):
        for i in book:
            list_1.insert(END,i)
    def fin():
        clear()
        if e12_var.get()=='':
            matrial = [i[0] for i in back.update()]
            print(matrial)
            y= set(mater_food)
            for i in matrial:
                k=i
                print(k)
                i = set(eval(i))
                if i & y== y:
                    view_bot(str(k))
        else:
            print(e12_var.get())
            matrial = back.h(e12_var.get())
            for i in matrial:
                list_1.insert(END,i[0])
    list_1 = Listbox(window,width=20,height=13,bg="#B0EAFF",font=35)
    list_1.grid(row=11,column=0)
    def fill_list(book):
        for i in book:
            list_1.insert(END,i)  
    b11= Button(window,text="  find  ",command=fin,font=10).grid(row=11,column=3)
    def mai():
        window.destroy()
        main()
    b12= Button(window,text=" back ",command=mai,font=10).grid(row=11,column=4)
    window.mainloop()
def main():
    window = Tk()
    window.title("food")
    window.geometry("940x400")
    window.configure(bg="#21abcd")
    #------ entry ------
    list_1 = Listbox(window,width=50,height=15,bg="#716C6B",font=50,fg="#ddfcfa")
    list_1.grid(row=3,rowspan=6,columnspan=2)
    sb1= Scrollbar(window)
    sb1.grid(row=3,rowspan=6,column=2)
    list_1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list_1.yview)
    #-----button command------
    def get_selected_row(event):
        global x,index
        index =list_1.curselection()[0]
        x= list_1.get(index)
        print(x)
    list_1.bind("<<ListboxSelect>>",get_selected_row)
    def clear():
        list_1.delete(0,END)
    def fill_list(book):
        for i in book:
            list_1.insert(END,i)
    def view_bot():
        book = back.view()
        clear()
        for i in book:
            list_k=[]
            for j in i:
                list_k.append(j)
            list_k.remove(list_k[2])
            fill_list((list_k,))
    view_bot()
    def delete_bot():
        try:
            back.delete(x[0])
        except:
            showinfo(title="warn",message="u miss something")
        book = back.view()
        clear()
        view_bot()
    def search_bot():
        window.destroy()
        finding(main)
    def add_food():
        window.destroy()
        adding(main)
    def mat_show():
        clear()
        book = back.f(x[0])[0][0]
        print(book)
        list_1.insert(END,book)
    # # ------button-----
    b1= Button(window,text="view all",width=12,command=view_bot,activebackground="#f7fba2",font=("lora",12),bg="#ddfcfa")
    b1.grid(row=3,column=5)
    b2= Button(window,text="add food",width=12,command=add_food,font=("lora",12),activebackground="#f7fba2",bg="#ddfcfa")
    b2.grid(row=4,column=6)
    b3= Button(window,text="delete food",width=12,command=delete_bot,font=("lora",12),activebackground="#f7fba2",bg="#ddfcfa")
    b3.grid(row=5,column=7)
    b4= Button(window,text="material",width=12,comman=mat_show,font=("lora",12),activebackground="#f7fba2",bg="#ddfcfa")
    b4.grid(row=6,column=7)
    b5= Button(window,text="search",width=12,command=search_bot,font=("lora",12),activebackground="#f7fba2",bg="#ddfcfa")
    b5.grid(row=7,column=6)
    b6= Button(window,text="close",width=12,command= window.destroy,font=("lora",12),activebackground="#f7fba2",bg="#ddfcfa")
    b6.grid(row=8,column=5)
    window.mainloop()
main()