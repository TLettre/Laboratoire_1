import tkinter as tk

class CookieClicker:
    def __init__(self, root):
        self.root = root
        self.root.title("Cookie Clicker")
        
        self.cookies = 0
        self.cookies_per_click = 1
        
        self.label = tk.Label(root, text="Cookies: 0", font=("Helvetica", 16))
        self.label.pack(pady=20)
        
        self.button = tk.Button(root, text="Click me!", command=self.click_cookie, font=("Helvetica", 16))
        self.button.pack(pady=20)
        
        self.upgrade_button = tk.Button(root, text="Upgrade (10 cookies)", command=self.upgrade, font=("Helvetica", 16))
        self.upgrade_button.pack(pady=20)
        
    def click_cookie(self):
        self.cookies += self.cookies_per_click
        self.update_label()
        
    def upgrade(self):
        if self.cookies >= 10:
            self.cookies -= 10
            self.cookies_per_click += 1
            self.update_label()
        
    def update_label(self):
        self.label.config(text=f"Cookies: {self.cookies}")

if __name__ == "__main__":
    root = tk.Tk()
    game = CookieClicker(root)
    root.mainloop()