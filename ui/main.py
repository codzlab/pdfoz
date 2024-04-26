# ui/main.py
import sys
import os

# Add project directory to Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(project_dir, '..'))

# ui/main.py
import tkinter as tk
from tkinter import filedialog, ttk
import fitz  # Import PyMuPDF

class PDFReaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDFOZ by CODZLAB")
        self.root.geometry("1000x800")
       # Load your logo image
        icon_path = "./ui/iconh.png"  # Adjust the path to your icon image
        try:
            self.root.iconphoto(True, tk.PhotoImage(file=icon_path))
        except tk.TclError:
            print(f"Error: Failed to load the icon image from {icon_path}")

        # Set window title
        self.root.title("PDFOZ by Codzlab")

        self.zoom_factor = 1.0  # Initial zoom factor
        self.page_number = 0    # Current page number
        self.pdf_documents = {}  # Dictionary to store opened PDF documents
        self.pdf_canvas = {}     # Dictionary to store canvas references
        self.create_widgets()
        # Bind arrow keys to vertical scrolling
        self.root.bind("<Up>", lambda event: self.scroll_vertical(-1))
        self.root.bind("<Down>", lambda event: self.scroll_vertical(1))
        # Bind mouse wheel event to the on_mousewheel method
        self.root.bind("<MouseWheel>", self.on_mousewheel)
        # Create a dictionary to store close buttons for each tab
        self.close_buttons = {}
        # Create a dictionary to store tab IDs for each document
        self.tab_ids = {}

    def create_widgets(self):
        # Create a header frame
        header_frame = tk.Frame(self.root)
        header_frame.pack(side="top", fill="x")

        # Create buttons for opening PDF, zooming, and page navigation
        open_button = tk.Button(header_frame, text="Open PDF", command=self.open_pdf)
        open_button.pack(side="left", padx=5, pady=5)

        zoom_out_button = tk.Button(header_frame, text="Zoom Out (-)", command=self.zoom_out)
        zoom_out_button.pack(side="left", padx=5, pady=5)

        zoom_in_button = tk.Button(header_frame, text="Zoom In (+)", command=self.zoom_in)
        zoom_in_button.pack(side="left", padx=5, pady=5)


        prev_page_button = tk.Button(header_frame, text="Previous Page", command=self.prev_page)
        prev_page_button.pack(side="left", padx=5, pady=5)

        next_page_button = tk.Button(header_frame, text="Next Page", command=self.next_page)
        next_page_button.pack(side="left", padx=5, pady=5)

        # Create a Notebook widget for tabbed interface
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Bind mousewheel to zoom functionality
        self.root.bind("<MouseWheel>", self.on_mousewheel)

        # Bind arrow keys to page navigation
        self.root.bind("<Left>", lambda event: self.prev_page())
        self.root.bind("<Right>", lambda event: self.next_page())

        self.close_buttons = {}  # Dictionary to store close button references

    def open_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.display_pdf(file_path)

    def display_pdf(self, file_path):
     # Open the PDF file using PyMuPDF
     pdf_document = fitz.open(file_path)
     self.pdf_documents[file_path] = pdf_document

     # Get the file name from the file path
     file_name = os.path.basename(file_path)
 
     # Create a new tab for the opened PDF with the file name as tab text
     tab_frame = ttk.Frame(self.notebook)
     self.notebook.add(tab_frame, text=file_name)

     

     # Create a canvas to display the PDF content in the tab
     pdf_canvas = tk.Canvas(tab_frame)
     pdf_canvas.pack(fill="both", expand=True)

     # Store the canvas reference in a dictionary
     self.pdf_canvas[file_path] = pdf_canvas

     # Add the tab ID to the pdf_documents dictionary
     self.tab_ids[file_path] = self.notebook.index("end") - 1

     # Create a close button for the tab
     close_button = tk.Button(tab_frame, text="x", command=lambda fp=file_path: self.close_tab(fp))
     close_button.place(relx=1.0, rely=0, anchor="ne")

     # Store the close button reference in the close_buttons dictionary
     self.close_buttons[file_path] = close_button

     # Display the first page
     self.render_page(file_path)
    def render_page(self, file_path):
        # Clear the canvas
        self.pdf_canvas[file_path].delete("all")

        # Get the current PDF document
        pdf_document = self.pdf_documents[file_path]

        # Load the current page
        current_page = pdf_document.load_page(self.page_number)

        # Get the dimensions of the page
        width = current_page.rect.width
        height = current_page.rect.height

        # Get the scaled dimensions based on the zoom factor
        scaled_width = int(width * self.zoom_factor)
        scaled_height = int(height * self.zoom_factor)

        # Render the page as an image
        image = current_page.get_pixmap(matrix=fitz.Matrix(self.zoom_factor, self.zoom_factor))

        # Convert the image to a Tkinter PhotoImage
        photo_image = tk.PhotoImage(data=image.tobytes())

        # Display the image on the canvas
        self.pdf_canvas[file_path].create_image(0, 0, anchor="nw", image=photo_image)
        self.pdf_canvas[file_path].image = photo_image

        # Configure the canvas scroll region
        self.pdf_canvas[file_path].config(scrollregion=(0, 0, scaled_width, scaled_height))

    def zoom_in(self):
        # Increase the zoom factor by 10%
        self.zoom_factor *= 1.1
        for file_path in self.pdf_canvas:
            self.render_page(file_path)

    def zoom_out(self):
        # Decrease the zoom factor by 10%
        self.zoom_factor *= 0.9
        for file_path in self.pdf_canvas:
            self.render_page(file_path)

    def prev_page(self):
        if self.page_number > 0:
            self.page_number -= 1
            for file_path in self.pdf_canvas:
                self.render_page(file_path)

    def next_page(self):
     for file_path in self.pdf_documents:
         num_pages = len(self.pdf_documents[file_path])
         if self.page_number < num_pages - 1:
             self.page_number += 1
             self.render_page(file_path)

    def close_tab(self, file_path):
     # Get the tab ID associated with the file path
     tab_id = self.tab_ids[file_path]

     # Destroy the tab and remove it from the notebook using the tab ID
     self.notebook.forget(tab_id)
    
     # Delete the tab ID from the tab_ids dictionary
     del self.tab_ids[file_path]
 


    def on_mousewheel(self, event):
        # Detect mouse wheel scrolling for zooming
     if event.num == 4 or event.delta > 0:
         self.zoom_in()
     elif event.num == 5 or event.delta < 0:
          self.zoom_out()

        # Detect two-finger trackpad scrolling for vertical scrolling
     elif event.delta > 0:
          self.scroll_vertical(-1)
     elif event.delta < 0:
          self.scroll_vertical(1)


    def on_trackpad_scroll(self, event):
        # Detect two-finger trackpad scrolling for vertical scrolling
        if event.delta > 0:
            self.scroll_vertical(-1)
        elif event.delta < 0:
            self.scroll_vertical(1)

    def scroll_vertical(self, direction):
        for file_path in self.pdf_canvas:
            self.pdf_canvas[file_path].yview_scroll(direction, "units")
if __name__ == "__main__":
    root = tk.Tk()
    app = PDFReaderApp(root)
    root.mainloop()
