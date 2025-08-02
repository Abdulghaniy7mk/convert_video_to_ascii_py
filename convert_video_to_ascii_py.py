import os
import argparse
from PIL import Image, ImageSequence

# ASCII characters for different grayscale levels
ASCII_CHARS = "@%#*+=-:. "

def image_to_ascii(image_path, width=100):
    """Convert a single image to ASCII"""
    try:
        img = Image.open(image_path).convert('L')
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        return ""
    
    w_percent = width / float(img.size[0])
    height = int(float(img.size[1]) * w_percent * 0.55)
    img = img.resize((width, height))

    pixels = list(img.getdata())
    ascii_str = "".join([ASCII_CHARS[pixel * len(ASCII_CHARS) // 256] for pixel in pixels])

    ascii_img = "\n".join([ascii_str[i:i+width] for i in range(0, len(ascii_str), width)])
    return ascii_img

def extract_frames(video_path, frame_dir, fps=10):
    """Extract frames from gif or video using Pillow"""
    os.makedirs(frame_dir, exist_ok=True)
    frame_interval = int(1000 / fps)

    print(f"[+] Extracting frames from {video_path}...")
    img = Image.open(video_path)

    count = 0
    for i, frame in enumerate(ImageSequence.Iterator(img)):
        if (i * img.info.get('duration', 100)) % frame_interval == 0:
            frame = frame.convert('RGB')
            frame.save(os.path.join(frame_dir, f"frame_{count:04d}.png"))
            count += 1

    return count

def generate_ascii_player_script(ascii_frames, output_py):
    """Generate player Python script to display ASCII animation"""
    with open(output_py, "w") as f:
        f.write("import time, os\n\n")
        f.write("frames = [\n")
        for frame in ascii_frames:
            f.write('r"""' + frame + '""",\n')
        f.write("]\n\n")
        f.write("try:\n")
        f.write("    while True:\n")
        f.write("        for frame in frames:\n")
        f.write("            os.system('clear')\n")
        f.write("            print(frame)\n")
        f.write("            time.sleep(0.1)\n")
        f.write("except KeyboardInterrupt:\n")
        f.write("    pass\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert video or gif to ASCII animation")
    parser.add_argument("-v", "--video", required=True, help="Path to video or gif file")
    args = parser.parse_args()

    video_path = args.video
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    frame_dir = "frames"

    total_frames = extract_frames(video_path, frame_dir, fps=10)

    print(f"[+] Converting {total_frames} frames to ASCII...")
    ascii_frames = []
    for i in range(total_frames):
        frame_path = os.path.join(frame_dir, f"frame_{i:04d}.png")
        ascii_frame = image_to_ascii(frame_path)
        ascii_frames.append(ascii_frame)

    output_script = f"{video_name}.py"
    generate_ascii_player_script(ascii_frames, output_script)
    print(f"[+] ASCII animation saved to {output_script}")

    # Clean up frames
    os.system(f"rm -rf {frame_dir}")
