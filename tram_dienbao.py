from datetime import datetime, timedelta
import imp
from multiprocessing.spawn import import_main_path
from tkinter import *
from tkinter import ttk,Tk
from hmo import *

def tao_btn(ten_btn,ten_txt_bt,cmd,ox,oy):
    ten_btn = Button(root, text=ten_txt_bt,width=10, command=cmd)# bt dong
    ten_btn.place(x=ox,y=oy)
def tao_textbox(ten_txt,ox,oy):
    ten_txt = Text(root,width=5,height=1)
    ten_txt.place(x=ox,y=oy)

root =Tk()
w = 800
h = 600

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("THUY VAN")


# Tạo combobox
combo_box = ttk.Combobox(root, values=['Trương Văn Biên', 'Nguyễn Văn Xuyên', 'Trần Văn Cường'],font=('Times New Roman', 13))
combo_box.current(0)  # Chọn vị trí mặc định là 0 (Trương Văn Biên)
# Đặt vị trí (x, y) cho combobox bằng phương thức place()
combo_box.place(x=410, y=83) 


lbl = Label(root,text="ĐÀI KHÍ TƯỢNG THUỶ VĂN KHU VƯC TRUNG TRUNG BỘ" + '\n' + 'ĐÀI KHÍ TƯỢNG THUỶ VĂN TỈNH QUẢNG NGÃI',font=('Arial Bold',14)).pack(padx=10,pady=15)
# lb1 = Label(root,text='TVHN',font=('Arial Bold',14)).place(x=90,y=120)
# lb2 = Label(root,text='TVHV05',font=('Arial Bold',14)).place(x=90+160,y=120)
# lb3 = Label(root,text='TVHD',font=('Arial Bold',14)).place(x=90+320,y=120)
# lb4 = Label(root,text='LŨ LŨ',font=('Arial Bold',14)).place(x=90+320+160,y=120)
# lb5 = Label(root,text='TVHV10',font=('Arial Bold',14)).place(x=90+320+160+130,y=120)
# lb5 = Label(root,text='LQSL',font=('Arial Bold',14)).place(x=860,y=120)
# lb5 = Label(root,text='HHAN',font=('Arial Bold',14)).place(x=860+160,y=120)

lb6 = Label(root,text='Dự báo viên:',font=('Arial Bold',14)).place(x=280,y=80)



# Create a Text widget
text_widget = Tk.Text(root, height=10, width=40)
text_widget.pack()

# Insert some initial text into the Text widget
initial_text = "This is a tkinter Text widget.\nYou can enter and edit text here."
text_widget.insert(Tk.END, initial_text)

# lb1.place(x=90,y=120)

# tao button tvhn
tao_btn('bt_SQL',"SQL",chuye,80+40,160) # load so lieu tu SQL
# tao_btn('bt_CDH',"CDH",get_CDH_API,80-40,160) # load so lieu tu CDH
# tao_btn('bt_tvhv',"Dự báo",dubbao_tvhn,80,160+50) #lam tin
# tao_btn('bt_tvhv',"MAP",vedothihangngay,80,160+100) #lam tin
# tao_btn('bt_tvhd',"Loadtin",TVHN.tin_tvhn,80,160+150) #lam tin
# tao_btn('bt_danhgia',"ĐÁNH GIÁ",danhgia_tvhn,80,160+200) # danh gia
# tao_btn('bt_hoso',"HỒ SƠ",hs_tvhn,80,160+250) # ho so du bao
# tao_btn('bt_upload',"Gửi tin",gui_tvhn,80,160+300) # ho so du bao




# selected_value = combo_box.get()
# TVHN.set_selected_value(selected_value)
# TVHV10.set_selected_value(selected_value)
# LQSL.set_selected_value(selected_value)
# TVHD.set_selected_value(selected_value)
# LULU.set_selected_value(selected_value)
# TVHV.set_selected_value(selected_value)
# def update_selected_value(event):
#     selected_value = combo_box.get()
#     TVHN.set_selected_value(selected_value)
#     TVHV10.set_selected_value(selected_value)
#     TVHV.set_selected_value(selected_value)
#     LQSL.set_selected_value(selected_value)
#     TVHD.set_selected_value(selected_value)
#     LULU.set_selected_value(selected_value)
# # Gắn sự kiện ComboboxSelected với hàm update_selected_value
# combo_box.bind("<<ComboboxSelected>>", update_selected_value)
root.mainloop()