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


