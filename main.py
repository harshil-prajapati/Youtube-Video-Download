import yt_dlp
import os

def get_download_path():
    path = input("📁 Enter download folder (press Enter for current folder): ").strip()
    path = path if path else os.getcwd()

    if not os.path.exists(path):
        try:
            os.makedirs(path, mode=0o775, exist_ok=True)  # create with default writable permissions
            print(f"📁 Created directory: {path}")
        except PermissionError:
            print(f"❌ Permission denied: Cannot create directory '{path}'. Try a different location or run as sudo.")
            return get_download_path()  # ask again
    else:
        if not os.access(path, os.W_OK):
            print(f"❌ Directory '{path}' is not writable. Please choose another location.")
            return get_download_path()

    return path

def get_video_streams(url):
    opts = {'quiet': True, 'skip_download': True}
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info.get('formats', []), info.get('title', 'video')

def choose_video_format(formats, max_height):
    heights = sorted({f.get('height', 0) for f in formats if f.get('vcodec') != 'none'}, reverse=True)
    for h in heights:
        if h <= max_height:
            return h
    return None

def download_video_audio(url, path, max_height):
    try:
        formats, title = get_video_streams(url)
        chosen_height = choose_video_format(formats, max_height)
        if chosen_height is None:
            print(f"⚠️ '{title}' no video at or below {max_height}p available. Skipping.")
            return
        print(f"📥 Downloading '{title}' at {chosen_height}p (video+audio)...")
        ydl_opts = {
            'format': f'bestvideo[height<={chosen_height}]+bestaudio/best',
            'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'quiet': False,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"✅ Download complete! Saved in: {path}\n")
    except Exception as e:
        print(f"❌ Error: {e}\n")

def download_audio_only(url, path):
    try:
        print("🎧 Downloading audio only (max quality)...")
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
            'quiet': False,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"✅ Audio download complete! Saved in: {path}\n")
    except Exception as e:
        print(f"❌ Error: {e}\n")

def download_playlist(url, path, is_audio_only, max_height=10000):
    try:
        opts = {'quiet': True, 'extract_flat': True}
        with yt_dlp.YoutubeDL(opts) as ydl:
            playlist = ydl.extract_info(url, download=False)
        if 'entries' not in playlist:
            print("❌ Not a playlist URL.")
            return
        entries = playlist['entries']
        print(f"🔽 Found {len(entries)} videos. Starting downloads...")
        for i, entry in enumerate(entries, 1):
            video_url = entry.get('url')
            if not video_url:
                continue
            print(f"\n🎥 Downloading {i}/{len(entries)}")
            if is_audio_only:
                download_audio_only(video_url, path)
            else:
                download_video_audio(video_url, path, max_height)
    except Exception as e:
        print(f"❌ Error: {e}\n")

# ---------- VIDEO MODE ----------
def get_urls_video_mode(choice):
    urls = []
    print("\n📎 Enter URLs one by one :")
    count = 1
    while True:
        print(f"\n🎶 Video {count}")
        url = input(f"URL {count} (type 'done' when finished) : ").strip()
        if url.lower() == "done":
            break
        if url:
            urls.append(url)
            count += 1
    return urls

# ---------- PLAYLIST MODE ----------
def get_urls_playlist_mode(choice):
    playlists = []
    print("\n📎 Enter playlist URLs one by one :")
    count = 1
    while True:
        print(f"\n🎶 Playlist {count}")
        url = input(f"URL : {count} (type 'done' when finished): ").strip()
        if url.lower() == "done":
            break
        if not url:
            continue
        path = get_download_path()
        max_height = 10000
        if choice == '3':  # Playlist video
            print("Select video quality:")
            print("1. 720p")
            print("2. 1080p")
            print("3. 2k (1440p)")
            print("4. 4k (2160p)")
            print("5. Max available")
            quality_choice = input("Enter choice (1-5): ").strip()
            quality_map = {'1':720, '2':1080, '3':1440, '4':2160, '5':10000}
            if quality_choice not in quality_map:
                print("❌ Invalid quality choice. Using Max available.")
            else:
                max_height = quality_map[quality_choice]
        playlists.append((url, path, max_height))
        count += 1
    return playlists

# ---------- MAIN ----------
def main():
    while True:
        print("\n🎬 YouTube Downloader with Playlist Support")
        print("Choose what to download (type 'exit' to quit):")
        print("1. Video with Audio (single video)")
        print("2. Audio Only (single video)")
        print("3. Playlist Video with Audio")
        print("4. Playlist Audio Only")

        choice = input("Enter your choice (1-4 or exit): ").strip().lower()
        if choice == 'exit':
            print("👋 Exiting. Goodbye!")
            break
        if choice not in ['1','2','3','4']:
            print("❌ Invalid choice. Try again.")
            continue

        if choice in ['1','2']:  # Single videos
            urls = get_urls_video_mode(choice)
            if not urls:
                print("❌ No URLs entered.")
                continue
            path = get_download_path()
            if choice == '1':
                print("\nSelect video quality:")
                print("1. 720p")
                print("2. 1080p")
                print("3. 2k (1440p)")
                print("4. 4k (2160p)")
                print("5. Max available")
                quality_choice = input("Enter choice (1-5): ").strip()
                quality_map = {'1':720, '2':1080, '3':1440, '4':2160, '5':10000}
                max_height = quality_map.get(quality_choice, 10000)
                for url in urls:
                    download_video_audio(url, path, max_height)
            else:
                for url in urls:
                    download_audio_only(url, path)

        else:  # Playlists
            playlists = get_urls_playlist_mode(choice)
            if not playlists:
                print("❌ No playlists entered.")
                continue
            print("\n✅ All playlists collected. Type 'start' to begin downloads.")
            cmd = input("Command: ").strip().lower()
            if cmd != "start":
                print("❌ Download canceled.")
                continue
            for i, (url, path, max_height) in enumerate(playlists, 1):
                print(f"\n▶ Starting Playlist {i}/{len(playlists)}...")
                if choice == '3':
                    download_playlist(url, path, is_audio_only=False, max_height=max_height)
                else:
                    download_playlist(url, path, is_audio_only=True)

if __name__ == "__main__":
    main()
# Made by : Harshil Prajapati
