### batch-downloader
A lightweight CLI tool to download sequential image sets.
### Features
* **Automated Indexing:** Zero-padded sequential fetching (`0001` - `N`).
* **Fault Handling:** Graceful network timeout management and automatic missing file skipping.
* **Custom Routing:** Dynamic output directory creation on demand.

---

### Requirements
* Python 3.8+
* requests

# Installing Dependencies
pip install requests

### Usage
Run the script directly via terminal:
python main.py
Provide target parameters at the prompt:
1. Target Base URL: Remote endpoint directory path.
2. File Prefix / Identifier: Dataset or file label pattern.
3. Output Directory: Destination folder path.
4. Max Items: Maximum index range to fetch.
