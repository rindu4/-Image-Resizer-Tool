import os
from PIL import Image

def resize_images(input_folder, output_folder, size=(800, 800), output_format="JPEG"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
            file_path = os.path.join(input_folder, filename)
            try:
                with Image.open(file_path) as img:
                    img_resized = img.resize(size, Image.Resampling.LANCZOS)

                    new_filename = os.path.splitext(filename)[0] + "." + output_format.lower()
                    output_path = os.path.join(output_folder, new_filename)

                    img_resized.save(output_path, output_format)
                    print(f"✅ Saved: {output_path}")
            except Exception as e:
                print(f" Error processing {filename}: {e}")


if __name__ == "__main__":
    resize_images(
        input_folder="input_images",      
        output_folder="resized_images",  
        size=(800, 800),                  
        output_format="JPEG"             
    )
