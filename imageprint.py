#imageprint.py
import tkinter as tk
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO
import xml.etree.ElementTree as ET
import urllib.request

def main(url) :
    f = urllib.request.urlopen(url)
    tree = ET.parse(f)
    root1 = tree.getroot()
    f.close()

    for child in root1.iter("item") :
        img_url = child.findtext("imageUrl")

    root = tk.Toplevel()
    response = requests.get(img_url)
    img_data = response.content
    img =Image.open(BytesIO(img_data))
    photo = ImageTk.PhotoImage(img)
    panel = tk.Label(root, image=photo)
    panel.image = photo
    panel.pack(side="bottom", fill="both", expand="yes")
    root.mainloop()

