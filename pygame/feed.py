#!/usr/bin/env python3
#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import pandas as pd

class Feedback:

    def __init__(self, master,):
        master.title('feedback window')
        master.resizable(False, False)
        master.configure(background='#e1d8b9')

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#e1d8b9')
        self.style.configure('TButton', background='#e1d8b9')
        self.style.configure('TLabel', background='#e1d8b9', font=('Arial', 11))
        self.style.configure('header.TLabel', font=('Arial', 18, 'bold'))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        ttk.Label(self.frame_header, text="Thanks for Exploring!", style='header.TLabel').grid(row=0, column=1)
        ttk.Label(self.frame_header, text="We're glad you chose to explore Oregon!\nPlease tell us how it was!",
                  justify='center').grid(row=1, column=1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text='Name:').grid(row=0, column=0, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text='Email:').grid(row=0, column=1, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text='Comments:').grid(row=2, column=0, padx=5, sticky='sw')

        self.entry_name = ttk.Entry(self.frame_content, width=24)
        self.entry_email = ttk.Entry(self.frame_content, width=24)
        self.text_comments = Text(self.frame_content, width=50, height=10, font=('Arial', 10))

        self.entry_name.grid(row=1, column=0, padx=5)
        self.entry_email.grid(row=1, column=1, padx=5)
        self.text_comments.grid(row=3, column=0, columnspan=2, padx=5)

        ttk.Button(self.frame_content, text='Submit', command=self.submit).grid(row=4, column=0, padx=5, sticky='e')
        ttk.Button(self.frame_content, text='Clear', command=self.clear).grid(row=4, column=1, padx=5, sticky='w')

    def submit(self):
        fname = self.entry_name.get()
        fcomm = self.text_comments.get(1.0, 'end').strip()
        print(f'Name: {fname}')
        print(f'Email: {self.entry_email.get()}')
        print(f'Comments: {fcomm}')
        self.clear()
        messagebox.showinfo(title="Explore Oregon Feedback", message="Comments Submitted!")
        self.sql_connect(fname, fcomm)

    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')

    def sql_connect(self, fname, fcomm):
        conn = sqlite3.connect('player_data.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS feedback(
            id INTEGER PRIMARY KEY,
            name TEXT,
            comments TEXT
        )''')

        def insert_feedback():
            cursor.execute("INSERT INTO feedback (name, comments) VALUES (?, ?)", ((fname,fcomm)))
            conn.commit()

        def get_feedback():
            cursor.execute("SELECT * FROM feedback")
            return cursor.fetchall()

        # Insert the feedback data into the database
        insert_feedback()

        # Retrieve and display feedback data
        dff = pd.read_sql_query("SELECT * FROM feedback ORDER BY id DESC", conn)
        print(dff.head())

        conn.close()

def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()

if __name__ == "__main__":
    main()

