import tkinter as tk
from tkinter import READABLE, StringVar, ttk
from tkinter.constants import DISABLED
from ttkthemes.themed_style import ThemedStyle
import os
root = tk.Tk()
style = ThemedStyle()
style.set_theme("arc")
root.title("GUI Nmap Based Port Scanner")
root.geometry("800x600")
notebook = ttk.Notebook(root)
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
notebook.add(frame1, text='Port/IP')
notebook.add(frame2, text='Options')
notebook.add(frame3, text="Start/Output")
nmap_list = ["sudo nmap"]

def create_frame1():
    global ip_address,port
    panel_title = ttk.Label(frame1,text="IP/Ports Config",font="bold")
    ip_label = ttk.Label(frame1,text="Target's IP")
    ip_address = StringVar()
    ip_input = ttk.Entry(frame1,width=24,textvariable=ip_address)
    port = StringVar()
    port_label = ttk.Label(frame1,text="Ports",textvariable=port)
    port_list = ttk.Combobox(frame1,width=22)
    port_list['values'] = ('All Ports', 'Most Popular')
    port_list.configure(state="readonly")
    ip_label.grid(column=0,row=1)
    panel_title.grid(column=0,row=0)
    ip_input.grid(column=1,row=1)
    port_label.grid(column=0,row=2)
    port_list.grid(column=1,row=2)
def create_frame2():
    global os_detection_value,syn_scan_value,speed_value,version_check_value,vuln_scan_value,speed_var,speed_choice
    options_label = ttk.Label(frame2,text="Options",font='bold')
    os_detection_value = StringVar()
    os_detection = ttk.Checkbutton(frame2,text="Os Detection",width=13,variable=os_detection_value)
    syn_scan_value = StringVar()
    syn_scan = ttk.Checkbutton(frame2,text="Syn Scan",width=13,variable=syn_scan_value)
    speed_var = StringVar()
    speed = ttk.Checkbutton(frame2,text="Speed",width=13,variable=speed_var,command=speed_enable)
    speed_value = StringVar()
    speed_choice = ttk.Spinbox(frame2,from_=1,to=5,textvariable=speed_value,width=2,state=DISABLED)
    version_check_value = StringVar()
    version_check = ttk.Checkbutton(frame2,text="Version Check",width=13,variable=version_check_value)
    vuln_scan_value = StringVar()
    vuln_scan = ttk.Checkbutton(frame2,text="Vuln Scan",width=13,variable=vuln_scan_value)
    options_label.grid(column=0,row=0)
    os_detection.grid(column=1,row=1)
    speed.grid(column=1,row=2)
    speed_choice.grid(column=2,row=2)
    version_check.grid(column=1,row=3)
    vuln_scan.grid(column=1,row=4)
    syn_scan.grid(column=1,row=5)
def speed_enable():
    if speed_var.get():
        speed_choice.configure(state=READABLE)
def create_frame3():
    global output_save
    frame3_label = ttk.Label(frame3,text="Start/Output")
    output_label = ttk.Label(frame3,text="Output to:")
    output_save = StringVar()
    output_format = ttk.Combobox(frame3,textvariable=output_save,state="readonly")
    output_format["values"] = "XML","SKID", "TXT","Terminal"
    start_button = ttk.Button(frame3,text="Start",command=command_append)
    frame3_label.grid(column=0,row=0)
    output_label.grid(column=0,row=1)
    output_format.grid(column=1,row=1)    
    start_button.grid(column=0,row=2)
def command_append():
    if port.get() == "All Ports":
        nmap_list.append("-p-")
    if os_detection_value.get():
        nmap_list.append("-O")
    if syn_scan_value.get():
        nmap_list.append("-sS")
    if version_check_value.get():
        nmap_list.append("-sV")
    if vuln_scan_value.get():
        nmap_list.append("-vv --script vuln")
    if speed_value.get():
        speed_flag = "-T" + speed_value.get()
        nmap_list.append(speed_flag)
    if output_save.get():
        if output_save.get() == "XML":
            nmap_list.append("-oX scan")
        elif output_save.get() == "SKID":
            nmap_list.append("-oS scan")
        elif output_save.get() == "TXT":
            nmap_list.append("> scan.txt")
    nmap_list.append(ip_address.get())
    command_string = " ".join(nmap_list)
    print(command_string)
    os.system(command_string)
def create_all_frames():
    create_frame1()
    create_frame2()
    create_frame3()

notebook.grid()
create_all_frames()
root.mainloop()
