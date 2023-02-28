#GUI приложение(какое я пока не решил)

import tkinter as tk

window = tk.Tk()
window.title('Здесь что-то будет')
text1 = tk.Label(window, text = " Привет ! ")

button1 = tk.Button(window, text = 'кнопка 1', fg = 'red')
button2 = tk.Button(window, text = 'кнопка 2', fg = 'green')
button3 = tk.Button(window, text = 'кнопка 3', fg = 'blue')
text1.pack()
button1.pack() 
button2.pack()
button3.pack()               
window.mainloop()