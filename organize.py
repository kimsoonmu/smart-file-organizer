import os
import shutil
import sys

# 파일 확장자별 분류 기준
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx", ".csv", ".hwp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
    "Audio": [".mp3", ".wav", ".flac", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
}


def get_category(extension):
    extension = extension.lower()
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return "Others"


def organize_folder(target_folder):
    if not os.path.isdir(target_folder):
        print(f"폴더를 찾을 수 없습니다: {target_folder}")
        return

    moved_count = 0

    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)

        # 하위 폴더는 건너뛰기
        if os.path.isdir(file_path):
            continue

        _, extension = os.path.splitext(filename)
        category = get_category(extension)

        category_folder = os.path.join(target_folder, category)
        os.makedirs(category_folder, exist_ok=True)

        destination = os.path.join(category_folder, filename)
        shutil.move(file_path, destination)
        moved_count += 1
        print(f"이동: {filename} -> {category}/")

    print(f"\n총 {moved_count}개 파일을 정리했습니다.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python organize.py [정리할 폴더 경로]")
        sys.exit(1)

    target = sys.argv[1]
    organize_folder(target)
