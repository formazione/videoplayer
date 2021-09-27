import tkinter as tk
import os, glob


root = tk.Tk()
lb = tk.Listbox(root)
lb.pack()
[lb.insert(0, f) for f in os.listdir() if f.endswith(".mp4")]

files = glob.glob("*.mp4")

def launch_mp4(event):
	cur = lb.curselection()
	get_filename = lb.get(cur)
	os.startfile(get_filename)



lb.bind("<Double-Button>", launch_mp4)

def launch_youtube(event):
	url = entry.get()
	os.system(f"start {url}")

lab = tk.Label(root, text="Enter youtube url").pack()
entry = tk.Entry(root)
entry.pack()
entry.bind("<Return>", launch_youtube)


root.mainloop()