# ==============================
# CHƯƠNG TRÌNH QUẢN LÝ PLAYLIST NHẠC (CLI)
# Lập trình thủ tục - Python
# ==============================

playlist = []  # Danh sách bài hát


# ==============================
# 1. Thêm bài hát
# ==============================
def add_song():
    name = input("Nhập tên bài hát: ")
    artist = input("Nhập tên ca sĩ: ")
    song = {"name": name, "artist": artist}
    playlist.append(song)
    print("✅ Đã thêm bài hát vào playlist!\n")


# ==============================
# 2. Xóa bài hát
# ==============================
def remove_song():
    name = input("Nhập tên bài hát muốn xóa: ")
    for song in playlist:
        if song["name"].lower() == name.lower():
            playlist.remove(song)
            print("🗑️ Đã xóa bài hát!\n")
            return
    print("❌ Không tìm thấy bài hát cần x
def view_playlist():
    """
    Hiển thị toàn bộ bài hát trong danh sách songs.
    """
    if not songs:
        print("Danh sách phát hiện đang trống.")
        return
    
    print("=== Danh sách phát ===")
    for i, song in enumerate(songs, start=1):
        print(f"{i}. {song['title']} - {song['artist']} ({song['duration']} giây)")

def search_by_artist():
    """
    Tìm bài hát theo ca sĩ.
    """
    artist_name = input("Nhập tên ca sĩ muốn tìm: ")
    found = [song for song in songs if song['artist'].lower() == artist_name.lower()]
    
    if not found:
        print(f"Không tìm thấy bài hát nào của ca sĩ {artist_name}.")
    else:
        print(f"Bài hát của {artist_name}:")
        for i, song in enumerate(found, start=1):
            print(f"{i}. {song['title']} ({song['duration']} giây)")

