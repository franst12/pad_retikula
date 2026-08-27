import os
import json

def scan_and_generate_json():
    # Folder tempat lu nyimpen ratusan gambar tadi
    image_folder = "reticles_images"
    
    # URL raw GitHub lu (otomatis mengarah ke repo lu)
    base_github_url = "https://raw.githubusercontent.com/franst12/pad_retikula/master/reticles_images/"
    
    json_data = {"data": []}

    # Cek apakah foldernya beneran ada
    if not os.path.exists(image_folder):
        print(f"Waduh, Folder '{image_folder}' nggak ketemu ngab!")
        return

    # Baca file, urutkan sesuai nama (biar rapi dari 001 - 200), lalu masukkan ke JSON
    count = 0
    for filename in sorted(os.listdir(image_folder)):
        if filename.endswith(".png"):
            final_url = f"{base_github_url}{filename}"
            json_data["data"].append(final_url)
            count += 1

    # Bikin file JSON-nya
    with open("reticles_api.json", "w", encoding="utf-8") as json_file:
        json.dump(json_data, json_file, indent=4)
        
    print(f"Mantap! {count} retikula berhasil dimasukkan ke dalam JSON dengan rapi.")

if __name__ == "__main__":
    scan_and_generate_json()