import tkinter as tk
from tkinter import ttk
import pyjokes
from tkinter.font import Font


class jokegenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Giggle Galaxy")
        self.root.geometry("600x500")
        self.root.configure(bg="#f8f9fa")
        self.root.resizable(False, False)

        self.title_font = Font(family="Poppins", size=24, weight="bold")
        self.joke_font = Font(family="Roboto", size=14)
        self.label_font = Font(family="Poppins", size=11)
        self.button_font = Font(family="Poppins", size=12, weight="bold")

        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.style.configure("TFrame", background="#f8f9fa")
        self.style.configure("TLabel", background="#f8f9fa", font=self.label_font)

        self.main_frame = ttk.Frame(root, style="TFrame")
        self.main_frame.pack(fill="both", expand=True, padx=30, pady=30)

        self.header_frame = ttk.Frame(self.main_frame, style="TFrame")
        self.header_frame.pack(fill="x", pady=(0, 20))

        self.title_label = tk.Label(self.header_frame,
                                    text="🎭 Giggle Galaxy 🎭",
                                    font=self.title_font,
                                    fg="#5e72e4",
                                    bg="#f8f9fa")
        self.title_label.pack()

        self.subtitle_label = ttk.Label(self.header_frame,
                                        text="Your daily dose of laughter",
                                        style="TLabel",
                                        foreground="#6c757d")
        self.subtitle_label.pack()

        self.joke_card = tk.Frame(self.main_frame,
                                  bg="white",
                                  bd=0,
                                  highlightthickness=0,
                                  relief="solid")
        self.joke_card.pack(pady=10, padx=10, fill="both", expand=True)

        self.joke_shadow = tk.Frame(self.joke_card, bg="#e9ecef")
        self.joke_shadow.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

        self.joke_text = tk.Text(self.joke_card,
                                 height=8,
                                 width=50,
                                 wrap="word",
                                 font=self.joke_font,
                                 bg="white",
                                 relief="flat",
                                 padx=20,
                                 pady=20,
                                 fg="#343a40",
                                 bd=0,
                                 highlightthickness=0)
        self.joke_text.pack(fill="both", expand=True, padx=5, pady=5)

        self.scrollbar = ttk.Scrollbar(self.joke_text)
        self.scrollbar.pack(side="right", fill="y")
        self.joke_text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.joke_text.yview)

        self.controls_frame = ttk.Frame(self.main_frame, style="TFrame")
        self.controls_frame.pack(fill="x", pady=(20, 10))

        self.lang_frame = ttk.Frame(self.controls_frame, style="TFrame")
        self.lang_frame.pack(side="left", padx=10, expand=True)

        self.lang_label = ttk.Label(self.lang_frame,
                                    text="Language 🌍",
                                    style="TLabel",
                                    foreground="#495057")
        self.lang_label.pack(anchor="w")

        self.language_var = tk.StringVar(value="en")
        languages = [("English", "en"), ("German", "de"),
                     ("Spanish", "es"), ("Galician", "gl"),
                     ("Basque", "eu"), ("Italian", "it")]

        self.language_menu = ttk.Combobox(self.lang_frame,
                                          textvariable=self.language_var,
                                          values=[lang[1] for lang in languages],
                                          font=self.label_font,
                                          state="readonly",
                                          style="Custom.TCombobox")
        self.style.configure("Custom.TCombobox",
                             fieldbackground="white",
                             background="white",
                             foreground="#495057",
                             padding=8,
                             relief="flat")
        self.language_menu.pack(fill="x")

        self.cat_frame = ttk.Frame(self.controls_frame, style="TFrame")
        self.cat_frame.pack(side="left", padx=10, expand=True)

        self.cat_label = ttk.Label(self.cat_frame,
                                   text="Category 😂",
                                   style="TLabel",
                                   foreground="#495057")
        self.cat_label.pack(anchor="w")

        self.category_var = tk.StringVar(value="all")
        categories = [("All Jokes", "all"), ("Neutral", "neutral"), ("Chuck Norris", "chuck")]

        self.category_menu = ttk.Combobox(self.cat_frame,
                                          textvariable=self.category_var,
                                          values=[cat[1] for cat in categories],
                                          font=self.label_font,
                                          state="readonly",
                                          style="Custom.TCombobox")
        self.category_menu.pack(fill="x")

        self.btn_frame = ttk.Frame(self.main_frame, style="TFrame")
        self.btn_frame.pack(fill="x", pady=(10, 20))

        self.generate_btn = tk.Button(self.btn_frame,
                                      text="✨ Generate Joke ✨",
                                      command=self.generate_joke,
                                      font=self.button_font,
                                      bg="#5e72e4",
                                      fg="white",
                                      activebackground="#4a5fc1",
                                      activeforeground="white",
                                      bd=0,
                                      padx=20,
                                      pady=12,
                                      relief="flat",
                                      cursor="hand2")
        self.generate_btn.pack(fill="x", ipady=5)

        self.generate_btn.bind("<Enter>", lambda e: self.generate_btn.config(bg="#4a5fc1"))
        self.generate_btn.bind("<Leave>", lambda e: self.generate_btn.config(bg="#5e72e4"))

        self.footer_frame = ttk.Frame(self.main_frame, style="TFrame")
        self.footer_frame.pack(side="bottom", fill="x", pady=(10, 0))

        self.footer = ttk.Label(self.footer_frame,
                                text="Created by Srihesh",
                                style="TLabel",
                                foreground="#adb5bd",
                                font=("Poppins", 9, "italic"))
        self.footer.pack()

        self.generate_joke()

    def generate_joke(self):
        self.joke_text.config(state="normal")
        self.joke_text.delete(1.0, tk.END)
        category = self.category_var.get()
        language = self.language_var.get()

        try:
            joke = pyjokes.get_joke(language=language, category=category)
            self.joke_text.insert(tk.END, joke)
            self.joke_text.config(fg="#343a40")
        except ValueError:
            self.joke_text.insert(tk.END, "Oops! No jokes available for this combination.")
            self.joke_text.config(fg="#e74c3c")

        self.joke_text.config(state="disabled")
        self.root.update_idletasks()


def main():
    root = tk.Tk()
    try:
        root.iconbitmap("smile.ico")
    except:
        pass

    app = jokegenerator(root)
    root.mainloop()


if __name__ == "__main__":
    main()