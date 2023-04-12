import tkinter as tk
import tkinter.messagebox as messagebox
import pyshorteners


# Set font
font_title = ('Arial', 16, 'bold')
font_label = ('Arial', 10, 'bold')
font_button = ('Arial', 10, 'bold')


class UrlShortenerWindow:
    def __init__(self, root):
        self.root = root
        # Program title
        self.root.title("URL Shortener")
        # Program icon
        self.root.iconbitmap('icon.ico')
        # Program window size
        self.root.geometry("550x300")
        # Program no resize
        self.root.resizable(False, False)

        # Program GUI widgets
        self.title = tk.Label(self.root, text="URL Shortener", font=font_title, fg="gray")
        self.title.place(x=180, y=15)

        tk.Label(self.root, text="Paste Your URL Here ..", font=font_label, fg="gray").place(x=50, y=75)

        self.input = tk.Entry(self.root, width=34, font="14", bg="lightgrey", borderwidth=2)
        self.input.place(x=50, y=95, height=30)

        btn_shorten = tk.Button(self.root, text="Create", font=font_button,
                              bg="gray", fg="white", command=self.create_short_url)
        btn_shorten.place(x=383, y=95, width=65, height=30)

    def create_short_url(self):
        '''takes input from entry widget, shortens the url and displays output with a copy button'''
        try:
            # Get the input URL
            url = self.input.get()
            if url == "":
                raise ValueError("URL input shouldn't be empty")

            # Shorten the URL
            shortener = pyshorteners.Shortener()
            shortened_url = shortener.tinyurl.short(url)

            # Create a new frame to hold the output text box and the copy button
            output_frame = tk.Frame(self.root)
            output_frame.place(x=50, y=200)

            # Create the output text box and insert the shortened URL
            output_box = tk.Entry(output_frame, font="14", width=30, borderwidth=2, border=2)
            output_box.insert(tk.END, shortened_url)
            output_box.pack(side=tk.LEFT)

            # Create the copy button
            copy_button = tk.Button(output_frame, text="Copy", font=font_button, bg="gray", fg="white",
                                    command=lambda: self.copy_to_clipboard(shortened_url))
            copy_button.pack(side=tk.LEFT, padx=60)

        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        except:
            messagebox.showerror("Error", "Invalid URL is entered.")
            return

    def copy_to_clipboard(self, text):
        '''copies the given text to the clipboard'''
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        messagebox.showinfo("Copied", "Shortened URL copied to clipboard!")


# Driver code
if __name__ == "__main__":
    root = tk.Tk()
    obj = UrlShortenerWindow(root)
    root.mainloop()
