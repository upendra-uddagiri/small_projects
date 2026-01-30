from tkinter import *



window=Tk()
window.title("converter")
window.config(padx=20,pady=20)
def converting():
    miles=float(m_input.get())
    km=miles*1.609
    kilometer_result_label["text"]=f"{km}"
m_input=Entry()
m_input.grid(column=1,row=0)
m_label=Label(text="Miles")
m_label.grid(column=2,row=0)
is_equal_label=Label(text="is equal to")
is_equal_label.grid(column=0,row=1)
kilometer_result_label=Label(text='0')
kilometer_result_label.grid(column=1,row=1)
kilometer_label=Label(text="km")
kilometer_label.grid(column=2,row=1)
calculate_button=Button(text="calculate",command=converting)
calculate_button.grid(column=1,row=2)

window.mainloop()