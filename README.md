# 🎥 ASCII Video Converter

Convert any video or GIF into **ASCII art animation** — directly in your terminal!

✅ Works with `.gif` and `.mp4` files  
🖥️ Shows ASCII art frame-by-frame  
⚙️ No OpenCV required  
🐍 Pure Python implementation  
💡 Great for fun terminal art projects!

---

## 📂 Project Structure

ascil/ ├── convert_video_to_ascii_py.py  # Main converter script ├── gost.py                       # (Optional) ASCII player script ├── Aura.gif                      # Example input file ├── Aura.py                       # Output ASCII animation

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.x installed
- Terminal (Linux, macOS, Windows CMD/PowerShell, or Termux)
- [Pillow](https://pypi.org/project/Pillow/) library installed

### 📦 Install Required Library

```bash
pip install pillow


---

🔧 Usage

▶️ Step 1: Convert Video/GIF to ASCII

python convert_video_to_ascii_py.py -v Aura.gif

✅ What this does:

Extracts each frame

Converts frame pixels to ASCII

Saves output into a Python script (Aura.py)



---

▶️ Step 2: Play ASCII Animation

python Aura.py

🔁 The animation plays frame-by-frame in your terminal!


---

💻 Termux: Copy to Downloads Folder

To move the project output to the Downloads folder in Termux:

cp -r ~/ascil ~/storage/downloads/


---

🎨 Customization

Edit these variables in convert_video_to_ascii_py.py for customization:

# ASCII gradient (bright to dark)
ascii_chars = '@%#*+=-:. '

# Frame output width
width = 100

# Frame delay (in seconds)
delay = 0.06


---

🧠 How It Works

1. Extracts frames from a video or GIF using Pillow


2. Converts each frame’s brightness to ASCII characters


3. Saves all frames as print statements into a new .py file


4. You can run that file to display animation in your terminal




---

🖼️ Example ASCII Output

From: Aura.gif

@@@@@@@@@@@@%%##**++==--::::....
@@@@@@@@@@@%%##**++==--:::......
@@@@@@@%%%###**++==---:::.......
@@@@%%%##***++===---::::........


---

⚠️ Tips & Notes

Best results with small-size, high-contrast GIFs

Terminal must support monospaced fonts

Resize your terminal window for cleaner display



---

📄 License

MIT License
Free for personal and commercial use.


---
