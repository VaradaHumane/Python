import tkinter as tk
import webbrowser


a = tk.Tk()

a.title("Enquiry")

label = tk.Label(a, text="Course:")
entry = tk.Entry(a)

s_label = tk.Label(a, text="Where did you hear about us?")
s_var = tk.StringVar(a)

s_options = ["Youtube", "Instagram", "Reddit", "Other"]
s_dropdown = tk.OptionMenu(a, s_var, *s_options)


def formm():
    course = entry.get()
    source = s_var.get()

    if source == "Youtube":
        url = "https://support.google.com/youtube/thread/202433711/frequently-asked-questions?hl=en"
    elif source == "Instagram":
        url = "https://help.instagram.com/"
    elif source == "Reddit":
        url = "https://www.reddit.com/wiki/faq/"
    else:
        url = "https://example.com/faq"

    webbrowser.open(url)


button = tk.Button(a, text="GO", command=formm)

label.grid(row=0, column=0)
entry.grid(row=0, column=1)

s_label.grid(row=1, column=0)
s_dropdown.grid(row=1, column=1)

button.grid(row=2, column=0)

a.mainloop()
