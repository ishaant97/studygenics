#imports
"""main imports"""
from asyncio.windows_events import NULL
from distutils.log import ERROR
import tkinter as tk
from tkinter.constants import BOTH, LEFT, VERTICAL, RIGHT
from PIL import ImageTk as ITK12 
from PIL import Image as IMG

#main window
root= tk.Tk()
root.geometry('{}x{}'.format(1000, 600))
root.minsize(1000, 600)
root.maxsize(1000, 600)

#title and icon
"""title"""
root.title("Studygenics")
"""icon"""
root.iconbitmap(r"icons_img_1/icon1proxy.ico")

#module functions
def mod1():
    global canvas2
    IMAGE_PATH_B_I_2= r"back_img_1/Acknowledgement.png"
    canvas2= tk.Canvas(root, width=1000, height=600)
    backimg2 = ITK12.PhotoImage(IMG.open(IMAGE_PATH_B_I_2).resize((1000, 600), IMG.ANTIALIAS))
    canvas2.background= backimg2
    bg= canvas2.create_image(0, 0, anchor= tk.NW, image= backimg2)
    canvas2.grid(row= 0, column= 0)
    """button for next"""
    but_next_w2 = tk.Button(root, text="NEXT", padx= 50, pady= 15, bg="lightgreen", command= mod2)
    but_next_w2_window = canvas2.create_window(810, 40, anchor=tk.NW, window=but_next_w2)
    
def SUB_JECT():
    canvas3.delete('all')
    global canvasSH
    global canvasSJ
    IMAGE_PATH_B_I_4= r"back_img_1/Untitled_Design_0.png"
    canvasSJ= tk.Canvas(root, width= 1000, height= 600)
    backimg_CNV_FRCH_1 = ITK12.PhotoImage(IMG.open(IMAGE_PATH_B_I_4).resize((1000, 600), IMG.ANTIALIAS))
    canvasSJ.background= backimg_CNV_FRCH_1
    bg= canvasSJ.create_image(0, 0, anchor= tk.NW, image= backimg_CNV_FRCH_1)
    canvasSJ.grid(row= 0, column= 0)
    """button for subject"""
    but_PHY_1 = tk.Button(root, text="Go ➤", padx= 20, pady=10 , bg="lightgreen", command= lambda: CHAP_TER("PHY"))
    but_PHY_1_window = canvasSJ.create_window(155, 240, anchor=tk.NW, window=but_PHY_1)
    but_CS_1 = tk.Button(root, text="Go ➤", padx= 20, pady=10 , bg="lightgreen", command= lambda: CHAP_TER("CS"))
    but_CS_1_window = canvasSJ.create_window(700, 450, anchor=tk.NW, window=but_CS_1)
    but_MTH_1 = tk.Button(root, text="Go ➤", padx= 20, pady=10 , bg="lightgreen", command= lambda: CHAP_TER("MTH"))
    but_MTH_1_window = canvasSJ.create_window(700, 240, anchor=tk.NW, window=but_MTH_1)
    but_CHEM_1 = tk.Button(root, text="Go ➤", padx= 20, pady=10 , bg="lightgreen", command= lambda: CHAP_TER("CHEM"))
    but_CHEM_1_window = canvasSJ.create_window(155, 440, anchor=tk.NW, window=but_CHEM_1)
    """button for content selection"""
    but_MM_1 = tk.Button(root, text="BACK", padx= 20, pady=10 , bg="lightgreen", command= MMR)
    but_MM_1_window = canvasSJ.create_window(454, 520, anchor=tk.NW, window=but_MM_1)
    
def CHAP_TER(code):
    global code_proxy
    code_proxy= code
    canvasSJ.delete('all')
    global canvasCH
    if code == "PHY":
        IMAGE_PATH_B_I_4= r"back_img_1/Untitled_Design_1.png"
    if code == "CHEM":
        IMAGE_PATH_B_I_4= r"back_img_1/Untitled_Design_3.png"
    if code == "MTH":
        IMAGE_PATH_B_I_4= r"back_img_1/Untitled_Design_2.png"
    if code == "CS":
        IMAGE_PATH_B_I_4= r"back_img_1/CS_Chapter_Page.png"            
    canvasCH= tk.Canvas(root, width= 1000, height= 600)
    backimg_CNV_FRCH_1 = ITK12.PhotoImage(IMG.open(IMAGE_PATH_B_I_4).resize((1000, 600), IMG.ANTIALIAS))
    canvasCH.background= backimg_CNV_FRCH_1
    bg= canvasCH.create_image(0, 0, anchor= tk.NW, image= backimg_CNV_FRCH_1)
    canvasCH.grid(row= 0, column= 0)
    """button for subject"""
                                            
    if code == "PHY":
        but_chp1_1 = tk.Button(root, text="Go ➤", padx= 30, pady=10 , bg="lightgreen", command= lambda: SCI_CHAP_TER("ch1_1"))
        but_chp1_1_window = canvasCH.create_window(830, 160, anchor=tk.NW, window=but_chp1_1)    
        but_chp2_1 = tk.Button(root, text="Go ➤", padx= 30, pady=10 , bg="lightgreen", command= lambda: SCI_CHAP_TER("ch2_1"))
        but_chp2_1_window = canvasCH.create_window(830, 275, anchor=tk.NW, window=but_chp2_1)    
        but_chp3_1 = tk.Button(root, text="Go ➤", padx= 30, pady=10 , bg="lightgreen", command= lambda: SCI_CHAP_TER("ch3_1"))
        but_chp3__window = canvasCH.create_window(830, 392, anchor=tk.NW, window=but_chp3_1)    
        but_chp4_1 = tk.Button(root, text="Go ➤", padx= 30, pady=10 , bg="lightgreen", command= lambda: SCI_CHAP_TER("ch4_1"))
        but_chp4_1_window = canvasCH.create_window(830, 490, anchor=tk.NW, window=but_chp4_1)

    if code == "CHEM":
        but_chp1_2 = tk.Button(root, text="Go ➤", padx= 30, pady=10 , bg="lightgreen", command= lambda: SCI_CHAP_TER("ch1_2"))
        but_chp1_2_window = canvasCH.create_window(830, 160, anchor=tk.NW, window=but_chp1_2)    
        but_chp2_2 = tk.Button(root, text="Go ➤", padx= 30, pady=10 , bg="lightgreen", command= lambda: SCI_CHAP_TER("ch2_2"))
        but_chp2_2_window = canvasCH.create_window(830, 275, anchor=tk.NW, window=but_chp2_2)    
        but_chp3_2 = tk.Button(root, text="Go ➤", padx= 30, pady=10 , bg="lightgreen", command= lambda: SCI_CHAP_TER("ch3_2"))
        but_chp3_2_window = canvasCH.create_window(830, 392, anchor=tk.NW, window=but_chp3_2)    
        but_chp4_2 = tk.Button(root, text="Go ➤", padx= 30, pady=10 , bg="lightgreen", command= lambda: SCI_CHAP_TER("ch4_2"))
        but_chp4_2_window = canvasCH.create_window(830, 490, anchor=tk.NW, window=but_chp4_2)  

    if code == "MTH":
        but_chp1_3 = tk.Button(root, text="Go ➤", padx= 30, pady=10 , bg="lightgreen", command= lambda: SCI_CHAP_TER("ch1_3"))
        but_chp1_3_window = canvasCH.create_window(830, 160, anchor=tk.NW, window=but_chp1_3)    
        but_chp2_3 = tk.Button(root, text="Go ➤", padx= 30, pady=10 , bg="lightgreen", command= lambda: SCI_CHAP_TER("ch2_3"))
        but_chp2_3_window = canvasCH.create_window(830, 275, anchor=tk.NW, window=but_chp2_3)    
        but_chp3_3 = tk.Button(root, text="Go ➤", padx= 30, pady=10 , bg="lightgreen", command= lambda: SCI_CHAP_TER("ch3_3"))
        but_chp3_3_window = canvasCH.create_window(830, 392, anchor=tk.NW, window=but_chp3_3)    
        but_chp4_3 = tk.Button(root, text="Go ➤", padx= 30, pady=10 , bg="lightgreen", command= lambda: SCI_CHAP_TER("ch4_3"))
        but_chp4_4_window = canvasCH.create_window(830, 490, anchor=tk.NW, window=but_chp4_3)

    if code == "CS":
        but_chp1_4 = tk.Button(root, text="Go ➤", padx= 30, pady=10 , bg="lightgreen", command= lambda: SCI_CHAP_TER("ch1_4"))
        but_chp1_4_window = canvasCH.create_window(830, 160, anchor=tk.NW, window=but_chp1_4)    
        but_chp2_4 = tk.Button(root, text="Go ➤", padx= 30, pady=10 , bg="lightgreen", command= lambda: SCI_CHAP_TER("ch2_4"))
        but_chp2_4_window = canvasCH.create_window(830, 275, anchor=tk.NW, window=but_chp2_4)    
        but_chp3_4 = tk.Button(root, text="Go ➤", padx= 30, pady=10 , bg="lightgreen", command= lambda: SCI_CHAP_TER("ch3_4"))
        but_chp3_4_window = canvasCH.create_window(830, 392, anchor=tk.NW, window=but_chp3_4)    
        but_chp4_4 = tk.Button(root, text="Go ➤", padx= 30, pady=10 , bg="lightgreen", command= lambda: SCI_CHAP_TER("ch4_4"))
        but_chp4_4_window = canvasCH.create_window(830, 490, anchor=tk.NW, window=but_chp4_4)      
    """button for content selection"""
    but_SH_1 = tk.Button(root, text="BACK", padx= 30, pady=10 , bg="lightgreen", command= SUB_JECT)
    but_SH_1_window = canvasCH.create_window(50, 50, anchor=tk.NW, window=but_SH_1)
   
def mod2():
    global canvas3
    canvas2.delete('all')
    IMAGE_PATH_B_I_3= r"back_img_1/Subject_menu.png"
    canvas3= tk.Canvas(root, width= 1000, height= 600)
    backimg3 = ITK12.PhotoImage(IMG.open(IMAGE_PATH_B_I_3).resize((1000, 600), IMG.ANTIALIAS))
    canvas3.background= backimg3
    bg= canvas3.create_image(0, 0, anchor= tk.NW, image= backimg3)
    canvas3.grid(row= 0, column= 0)
    """button for REVISION NOTES"""
    but_SH_w3 = tk.Button(root, text="Go ➤", padx= 25, pady= 12, bg="lightgreen", command= SUB_JECT)
    but_SH_w3_window = canvas3.create_window(170, 350, anchor=tk.NW, window=but_SH_w3)
    """button for CALCULATOR"""
    but_QB_w3 = tk.Button(root, text="Go ➤", padx= 25, pady= 12, bg="lightgreen", command= calcprototype)
    but_QB_w3_window = canvas3.create_window(721, 350, anchor=tk.NW, window=but_QB_w3)
    """button for help"""
    but_HELP_w3 = tk.Button(root, text="CREDITS ➤", padx= 40, pady= 17, bg="lightgreen", command= wndmod2)
    but_HELP_w3_window = canvas3.create_window(791, 507, anchor=tk.NW, window=but_HELP_w3)

def wndmod2():
    #help window
    root2= tk.Toplevel(root)
    #icon
    root2.iconbitmap(r"icons_img_1/icon1proxy.ico")
    #window configuration
    """window title"""
    root2.title("CREDITS STUDYGENICS")
    """window geometry"""
    root2.geometry('{}x{}'.format(700, 600))
    root2.minsize(700, 600)
    root2.maxsize(700, 600)
    #canvas
    """canvas creation"""
    wcanvas= tk.Canvas(root2, width=700, height=600)
    """first background"""
    IMAGE_PATH_B_I_1_wnd= r"back_img_1/Credits.png"
    wback= ITK12.PhotoImage(IMG.open(IMAGE_PATH_B_I_1_wnd).resize((700, 600), IMG.ANTIALIAS))
    wcanvas.background= wback
    bg= wcanvas.create_image(0, 0, anchor= tk.NW, image= wback)
    wcanvas.grid(row= 0, column= 0)
    
    #infinite loop
    root2.mainloop()

def calcprototype():
    #window
    wnd = tk.Toplevel(root)
    wnd.title("CALCULATOR STUDYGENICS")
    #icon
    wnd.iconbitmap(r"icons_img_1/icon1proxy.ico")
    """window geometry"""
    wnd.geometry('{}x{}'.format(455, 431))
    wnd.minsize(455, 431)
    wnd.maxsize(455, 431)
    #entry box
    ent = tk.Entry(wnd, width= 35, borderwidth= 5)

    #global value constants
    global count
    global s_num
    global gbl
    count = 1
    s_num = ""
    gbl = 0

    #button command function
    #number entry
    def btc(number):
        #ent.delete(0, END)
        crt = ent.get()
        ent.delete(0, tk.END)
        ent.insert(0, str(crt) + str(number))
    #clear button
    def clearbtc():
        ent.delete(0, tk.END)
    #equal to button
    def equalbtc():
        sc_num = ent.get()
        global s_num
        s = float(sc_num)
        s_num = str(s)
        ent.delete(0, tk.END)
        #for addition
        if math == "add":
            ent.insert(0, f_num + s)
        #for substraction
        if math == "mns":
            ent.insert(0, f_num - s)
        #for multiplication
        if math == "mlt":
            ent.insert(0, f_num * s)
        #for division
        if math == "dvd":
            ent.insert(0, f_num / s)
        global n 
        n = "eq"
        mleb()
        global count
        count = count + 1
    #addition button
    def addbtc():
        fst_num = ent.get()
        global f_num
        global n
        n = 1
        global math
        math = "add"
        f_num = float(fst_num)
        ent.delete(0, tk.END)
        mleb()
        global count
        count = count + 1
    #substraction button
    def minusbtc():
        fst_num = ent.get()
        global f_num
        global n
        n = 1
        global math
        math = "mns"
        f_num = float(fst_num)
        ent.delete(0, tk.END)
        mleb()    
        global count
        count = count + 1
    #multiplication button
    def mltbtc():
        fst_num = ent.get()
        global f_num
        global n
        n = 1
        global math
        math = "mlt"
        f_num = float(fst_num)
        ent.delete(0, tk.END)
        mleb()
        global count
        count = count + 1
    #division button 
    def dvdbtc():
        fst_num = ent.get()
        global f_num
        global n
        n = 1
        global math
        math = "dvd"
        f_num = float(fst_num)
        ent.delete(0, tk.END)
        mleb()
        global count
        count = count + 1
        
    #label function 
    def mleb(): 
        global m1
        global m2
        global m3
        global m4
        global m5
        global m6
        global z
        if math == "add":
            v = str(f_num) + "+"
            global z
            z = str(v)
                    
        if math == "mns":
            v = str(f_num) + "-"
            z = str(v)
            
            
        if math == "mlt":
            v = str(f_num) + "*"
            z = str(v)
            
        if math == "dvd":
            v = str(f_num) + "/"
            z = str(v)
            
        if n == "eq":
            global gbl
            global count
            w = z + s_num
            a_a = w + "="
            #condition for placing
            if count == 2:
                #label
                m1 = tk.Label(wnd, text= a_a)
                #placing/orientation
                m1.grid(row= 1, column= 3)
            if count == 4:
                #label
                m2 = tk.Label(wnd, text= a_a)
                #placing/orientation
                m2.grid(row= 2, column= 3)
            if count == 6:
                #label
                m3 = tk.Label(wnd, text= a_a)
                #placing/orientation
                m3.grid(row= 3, column= 3)
            if count == 8:
                #label
                m4 = tk.Label(wnd, text= a_a)
                #placing/orientation
                m4.grid(row= 4, column= 3)
                gbl = gbl + 7*count
            if count == 10:
                #label
                m5 = tk.Label(wnd, text= a_a)
                #placing/orientation
                m5.grid(row= 5, column= 3)
                #loop continuation constant
            if count == 12:
                #label deletion
                m1.destroy()
                m2.destroy()
                m3.destroy()
                m4.destroy()
                m5.destroy()
                #next loop label
                m6 = tk.Label(wnd, text= a_a)
                #placing/orientation
                m6.grid(row= 1, column= 3)
                count = 2
            
                if gbl/7 == 8:
                        m6.destroy()
                        gbl = 0
            
    #label destroyer
    def lebdst():
        try:
            m1.destroy()
            m2.destroy()
            m3.destroy()
            m4.destroy()
            m5.destroy()
            m6.destroy()
        except:
            ERROR       

    #buttons
    bt1 = tk.Button(wnd, text= "1", padx= 40, pady= 20, command= lambda: btc(1))
    bt2 = tk.Button(wnd, text= "2", padx= 40, pady= 20, command= lambda: btc(2))
    bt3 = tk.Button(wnd, text= "3", padx= 40, pady= 20, command= lambda: btc(3))

    bt4 = tk.Button(wnd, text= "4", padx= 40, pady= 20, command= lambda: btc(4))
    bt5 = tk.Button(wnd, text= "5", padx= 40, pady= 20, command= lambda: btc(5))
    bt6 = tk.Button(wnd, text= "6", padx= 40, pady= 20, command= lambda: btc(6))

    bt7 = tk.Button(wnd, text= "7", padx= 40, pady= 20, command= lambda: btc(7))
    bt8 = tk.Button(wnd, text= "8", padx= 40, pady= 20, command= lambda: btc(8))
    bt9 = tk.Button(wnd, text= "9", padx= 40, pady= 20, command= lambda: btc(9))

    bt0 = tk.Button(wnd, text= "0", padx= 40, pady= 20, command= lambda: btc(0))
    btad = tk.Button(wnd, text= "+", padx= 39, pady= 20, command= addbtc)
    bteq = tk.Button(wnd, text= "=", padx= 91, pady= 20, command= equalbtc)
    btclear = tk.Button(wnd, text= "Clear", padx= 77, pady= 20, 
                    command= clearbtc)

    btminus = tk.Button(wnd, text= "-", padx= 41, pady= 20, command= minusbtc)
    btmlt = tk.Button(wnd, text= "*", padx= 41, pady= 20, command= mltbtc)
    btdvd = tk.Button(wnd, text= "/", padx= 41, pady= 20, command= dvdbtc)

    btlogclear = tk.Button(wnd, text= "Clear Log", padx= 50, pady= 10, command= lebdst)

    #placing/orientation
    """entry box"""
    ent.grid(row= 0, column= 0, columnspan= 3, padx= 10, pady= 10)
    """buttons"""
    bt1.grid(row= 3, column= 0)
    bt2.grid(row= 3, column= 1)
    bt3.grid(row= 3, column= 2)

    bt4.grid(row= 2, column= 0)
    bt5.grid(row= 2, column= 1)
    bt6.grid(row= 2, column= 2)

    bt7.grid(row= 1, column= 0)
    bt8.grid(row= 1, column= 1)
    bt9.grid(row= 1, column= 2)

    bt0.grid(row= 4, column= 0)
    btclear.grid(row= 4, column= 1, columnspan= 2)
    btad.grid(row= 5, column= 0)
    bteq.grid(row= 5, column= 1, columnspan= 2)

    btminus.grid(row= 6, column= 0)
    btmlt.grid(row= 6, column= 1)
    btdvd.grid(row= 6, column= 2)

    btlogclear.grid(row= 0, column= 3)

    #mainloop
    wnd.mainloop()
    
def SCI_CHAP_TER(x):
    canvas3.delete('all')
    global canvasSH
    global canvasCH2
    global code_proxy
    IMAGE_PATH_B_I_4= r"back_img_1/Untitled_Design_5.png"
    canvasCH2= tk.Canvas(root, width= 1000, height= 600)
    backimg_CNV_FRCH = ITK12.PhotoImage(IMG.open(IMAGE_PATH_B_I_4).resize((1000, 600), IMG.ANTIALIAS))
    canvasCH2.background= backimg_CNV_FRCH
    bg= canvasCH2.create_image(0, 0, anchor= tk.NW, image= backimg_CNV_FRCH)
    canvasCH2.grid(row= 0, column= 0)
    """chapter list frame"""
    #for PHYSICS code : ("PHY")
    if x == "ch1_1":
        IMAGE_PATH_FRCH_BG=r"back_img_1/Physics_Chapter_1.png"
    if x == "ch2_1":
        IMAGE_PATH_FRCH_BG=r"back_img_1/Physics_Chapter_2.png"
    if x == "ch3_1":
        IMAGE_PATH_FRCH_BG=r"back_img_1/Physics_Chapter_3.png"
    if x == "ch4_1":
        IMAGE_PATH_FRCH_BG=r"back_img_1/Physics_Chapter_4.png"        
    #for CHEMISTRY code : ("CHEM")
    if x == "ch1_2":
        IMAGE_PATH_FRCH_BG=r"back_img_1/Chemistry_Chapter_1.png"
    if x == "ch2_2":
        IMAGE_PATH_FRCH_BG=r"back_img_1/Chemistry_Chapter_2.png"
    if x == "ch3_2":
        IMAGE_PATH_FRCH_BG=r"back_img_1/Chemistry_Chapter_3.png"
    if x == "ch4_2":
        IMAGE_PATH_FRCH_BG=r"back_img_1/Chemistry_Chapter_4.png"
    #for MATHS code : ("MTH")
    if x == "ch1_3":
        IMAGE_PATH_FRCH_BG=r"back_img_1/Maths_Chapter_1.png"
    if x == "ch2_3":
        IMAGE_PATH_FRCH_BG=r"back_img_1/Maths_Chapter_2.png"
    if x == "ch3_3":
        IMAGE_PATH_FRCH_BG=r"back_img_1/Maths_Chapter_3.png"
    if x == "ch4_3":
        IMAGE_PATH_FRCH_BG=r"back_img_1/Maths_Chapter_4.png"
    #for COMPUTER SCIENCE code : ("CS")
    if x == "ch1_4":
        IMAGE_PATH_FRCH_BG=r"back_img_1/Computer_Science_Chapter_1.png"
    if x == "ch2_4":
        IMAGE_PATH_FRCH_BG=r"back_img_1/Computer_Science_Chapter_2.png"
    if x == "ch3_4":
        IMAGE_PATH_FRCH_BG=r"back_img_1/Computer_Science_Chapter_3.png"
    if x == "ch4_4":
        IMAGE_PATH_FRCH_BG=r"back_img_1/Computer_Science_Chapter_4.png"

    frame_CH_LIST= tk.Frame(canvasCH2, width=900,height=450)
    frame_CH_LIST_WND = canvasCH2.create_window(50, 120, anchor= tk.NW, window=frame_CH_LIST)
    """canvas inside the frame"""
    canvasFRCH= tk.Canvas(frame_CH_LIST, width= 700, height= 450, scrollregion=(0,0,2000,2000))
    backimg_CNV_FRCH = ITK12.PhotoImage(IMG.open(IMAGE_PATH_FRCH_BG).resize((700, 2000), IMG.ANTIALIAS))
    canvasFRCH.background= backimg_CNV_FRCH
    bg= canvasFRCH.create_image(0, 0, anchor= tk.NW, image= backimg_CNV_FRCH)
    canvasFRCH.pack(side= LEFT, expand= True, fill= BOTH)
    """scroll bar"""
    ver_FRCH_BAR= tk.Scrollbar(frame_CH_LIST, orient= VERTICAL)
    ver_FRCH_BAR.pack(side= RIGHT, fill= tk.Y)
    ver_FRCH_BAR.config(command= canvasFRCH.yview)
    """final canvas configuration"""
    canvasFRCH.config(yscrollcommand= ver_FRCH_BAR.set)
    """button for main menu"""
    but_SH_1 = tk.Button(root, text="MAIN \nMENU ➤", padx=50, pady=10 , bg="lightgreen", command= MMR)
    but_SH_1_window = canvasCH2.create_window(830, 130, anchor=tk.NW, window=but_SH_1)
    """button for back"""   
    but_back_1 = tk.Button(root, text="BACK ➤", padx= 50, pady=16 , bg="lightgreen", command= lambda: CHAP_TER(code_proxy))
    but_back_1_window = canvasCH2.create_window(830, 280, anchor=tk.NW, window=but_back_1) 
    """button for calculator"""
    but_calc_lst = tk.Button(root, text="CALCULATOR ➤", padx= 30, pady= 12, bg="lightgreen", command= calcprototype)
    but_calc_lst_window = canvas3.create_window(830, 430, anchor=tk.NW, window=but_calc_lst)   
    
#functions
"""delete function bt(start)"""
def can_clear():
    global canvas1
    canvas1.delete('all')
"""window 2 starting"""
def wnd_2():
    mod1()
"""final start command"""
def star_t():
    can_clear()
    wnd_2()      
"""quit button function"""
def qui_t():
    root.destroy()
"""main menu return from chapter list"""
def MMR():
    canvasSJ.delete('all')
    mod2()

#background image (canvas)
"""background image variables"""
IMAGE_PATH_B_I_1= r"back_img_1/ref_1.jpg"
###hello= r"back_img//logo_1.png"
"""canvas creation1"""
canvas1= tk.Canvas(root, width=1000, height=600)

#first screen
"""first background"""
backimg1 = ITK12.PhotoImage(IMG.open(IMAGE_PATH_B_I_1).resize((1000, 600), IMG.ANTIALIAS))
canvas1.background= backimg1
bg= canvas1.create_image(0, 0, anchor= tk.NW, image= backimg1)
"""button for next"""
but_start_w1 = tk.Button(root, text="Start", padx= 50, pady= 15, bg="lightgreen",command= star_t)
but_start_w1_window = canvas1.create_window(770, 528, anchor=tk.NW, window=but_start_w1)
"""button for quit"""
but_quit_w1 = tk.Button(root, text="QUIT", padx= 50, pady= 15, bg="lightgreen", command= qui_t)
but_quit_w1_window = canvas1.create_window(100, 528, anchor=tk.NW, window=but_quit_w1)

#placement of widgets
"""canvases"""
canvas1.grid(row= 0, column= 0)

#infinite loop
root.mainloop()