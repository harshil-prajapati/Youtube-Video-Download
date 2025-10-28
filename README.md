# YouTube Downloader with Playlist Support

**Made by:** Harshil Prajapati

A simple yet powerful Python-based YouTube downloader using **yt-dlp**, allowing you to download:

* Single videos (video + audio)
* Audio-only tracks
* Entire playlists (video + audio or audio-only)
* Choose your preferred resolution (720p, 1080p, 2K, 4K, or best available)

---

## Features

* Supports **YouTube playlists and single videos**
* Works on **Windows** and **Linux (Ubuntu)**
* Lets you choose **download location and video quality**
* Converts **audio to MP3 automatically**
* Handles **permissions and directory creation**
* Clean and interactive **CLI menu**

---

## Requirements

Before running this script, make sure you have:

### ✅ Common (for both Windows & Ubuntu)

* **Python 3.8+**
* **yt-dlp**
* **ffmpeg**

---

## Windows Installation Guide

### 1️ Install Python

* Download and install the latest version of **Python** from
  👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)
* During installation, check ✅ **“Add Python to PATH”**.

To confirm installation:

```bash
python --version
```

---

### 2️ Install yt-dlp and ffmpeg

Open **Command Prompt (cmd)** and run:

```bash
pip install yt-dlp
```

Now install **ffmpeg**:

Option 1 – Using `scoop` (recommended):

```bash
scoop install ffmpeg
```

Option 2 Manual install:

1. Go to [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Download the Windows build (e.g., from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/))
3. Extract the ZIP file.
4. Add the `bin` folder (inside extracted ffmpeg) to your **System PATH**.

To verify:

```bash
ffmpeg -version
```

---

### 3️ Run the Script

Save your script as `main.py` and open **Command Prompt** in that directory:

```bash
python main.py
```

Follow on-screen instructions to download videos, audio, or playlists.

---

## Ubuntu Installation Guide

### 1️ Install Python

Most Ubuntu versions come with Python pre-installed. Check:

```bash
python3 --version
```

If not installed:

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

---

### 2️ Install yt-dlp and ffmpeg

```bash
sudo apt install ffmpeg -y
pip install yt-dlp
```

Verify installations:

```bash
yt-dlp --version
ffmpeg -version
```

---

### 3️ Run the Script

Navigate to your script folder and run:

```bash
python3 main.py
```

Then follow the interactive menu to start downloading.

---

## Usage Overview

When you run the script, you’ll see this menu:

```
YouTube Downloader with Playlist Support
Choose what to download (type 'exit' to quit):
1. Video with Audio (single video)
2. Audio Only (single video)
3. Playlist Video with Audio
4. Playlist Audio Only
```

* Enter `1–4` based on what you want to download.
* Then follow the prompts:

  * Paste URLs one by one (`done` to finish)
  * Choose a download folder
  * Select quality (for video)
  * For playlists, type `start` to begin all downloads.

## Notes

* Some videos may not be available in all resolutions.
* Long playlists can take time — downloads resume automatically if interrupted.
* If you face permission issues, try running the terminal as **Administrator** (Windows) or using `sudo` (Ubuntu).
* Works with YouTube, but yt-dlp also supports other sites.

---

## Author

**Harshil Prajapati**
- Feel free to modify or improve this script!
- License: MIT

---
