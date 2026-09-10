import os
import requests

def main():
    print("=" * 50)
    print("       SEQUENTIAL BATCH MEDIA DOWNLOADER")
    print("=" * 50)

    base_url = input("[?] Target Base URL: ").strip()
    while not base_url:
        base_url = input("[!] URL cannot be empty. Enter Base URL: ").strip()

    base_url = base_url.rstrip("/")

    prefix = input("[?] File prefix / Dataset name: ").strip()
    while not prefix:
        prefix = input("[!] Prefix cannot be empty. Enter prefix: ").strip()

    cartella_input = input("[?] Output directory [default: downloads]: ").strip()
    output_dir = cartella_input if cartella_input else "downloads"

    max_files_input = input("[?] Maximum items to download [default: 40]: ").strip()
    max_files = int(max_files_input) if max_files_input.isdigit() else 40

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0"
	# ADD MORE IF YOU LIKE
    }
    
    os.makedirs(output_dir, exist_ok=True)

    print("\n" + "-" * 40)
    print(f"[+] Starting batch: {prefix} (Target: {max_files} files)")
    print(f"[+] Destination: {output_dir}/")
    print("-" * 40 + "\n")

    for index in range(1, max_files + 1):
        index_str = f"{index:04d}"
        filename = f"{prefix}_{index_str}.jpg"
        img_url = f"{base_url}/{filename}"

        print(f"[i] Fetching: {img_url}")

        try:
            response = requests.get(img_url, headers=headers, timeout=10)
            if response.status_code == 200:
                filepath = os.path.join(output_dir, filename)
                with open(filepath, "wb") as f:
                    f.write(response.content)
                print(f"[✓] Saved: {filepath}")
            elif response.status_code == 404:
                print(f"[-] End of sequence or missing file (HTTP 404)")
            else:
                print(f"[!] Warning: HTTP {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"[!] Network error: {e}")
        except Exception as e:
            print(f"[!] Unexpected error: {e}")

    print("\n[+] Batch task finished.")

if __name__ == "__main__":
    main()