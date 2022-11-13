
import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []

MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []

AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []

DOC_FILES = []
DOCX_FILES = []
TXT_FILES = []
PDF_FILES = []
XLSX_FILES = []
PPTX_FILES = []

MY_OTHER = []
TAR_ARCHIVES = []
GZ_ARCHIVES = []
ZIP_ARCHIVES = []

REGISTER_EXTENSIONS = {
    'JPEG': JPEG_IMAGES,
    'PNG': PNG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_FILES,
    'DOCX': DOCX_FILES,
    'TXT': TXT_FILES,
    'PDF': PDF_FILES,
    'XLSX': XLSX_FILES,
    'PPTX': PPTX_FILES,
    'ZIP': ZIP_ARCHIVES,
    'GZ': GZ_ARCHIVES,
    'TAR': TAR_ARCHIVES
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    # перетворюємо розширення файлу на назву папки .jpg -> JPG
    return Path(filename).suffix[1:].upper()


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        # Якщо це папка то додаємо її зі списку FOLDERS і переходимо до наступного елемента папки
        if item.is_dir():
            # перевіряємо, щоб папка не була тією, в яку ми складаємо вже файли.
            if item.name not in ('archives', 'video', 'audio', 'files', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                # скануємо цю вкладену папку - рекурсія
                scan(item)
            # перейти до наступного елемента в сканованій папці
            continue

        # Робота з файлом
        ext = get_extension(item.name)  # взяти розширення
        fullname = folder / item.name  # взяти повний шлях до файлу
        if not ext:  # якщо файл не має розширення додати до невідомих
            MY_OTHER.append(fullname)
        else:
            try:
                # взяти список куди покласти повний шлях до файлу
                container = REGISTER_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                container.append(fullname)
            except KeyError:
                # Якщо ми не реєстрували розширення у REGISTER_EXTENSIONS, то додати до іншого
                UNKNOWN.add(ext)
                MY_OTHER.append(fullname)


if __name__ == '__main__':

    folder_for_scan = sys.argv[1]
    print(f'Start in folder {folder_for_scan}')

    scan(Path(folder_for_scan))
    print(f'Images jpeg: {JPEG_IMAGES}')
    print(f'Images jpg: {JPG_IMAGES}')
    print(f'Images svg: {SVG_IMAGES}')
    print(f'Images png: {PNG_IMAGES}')
    print(f'Audio mp3: {MP3_AUDIO}')
    print(f'Audio ogg: {OGG_AUDIO}')
    print(f'Audio wav: {WAV_AUDIO}')
    print(f'Audio amr: {AMR_AUDIO}')
    print(f'Video avi: {AVI_VIDEO}')
    print(f'Video mp4: {MP4_VIDEO}')
    print(f'Video mov: {MOV_VIDEO}')
    print(f'Video mkv: {MKV_VIDEO}')
    print(f'Files doc: {DOC_FILES}')
    print(f'Files docx: {DOCX_FILES}')
    print(f'Files txt: {TXT_FILES}')
    print(f'Files pdf: {PDF_FILES}')
    print(f'Files xlsx: {XLSX_FILES}')
    print(f'Files pptx: {PPTX_FILES}')
    print(f'Archives_zip: {ZIP_ARCHIVES}')
    print(f'Archives_gz: {GZ_ARCHIVES}')
    print(f'Archives_tar: {TAR_ARCHIVES}')

    print(f'Types of files in folder: {EXTENSIONS}')
    print(f'Unknown files of types: {UNKNOWN}')

    print(FOLDERS[::-1])
