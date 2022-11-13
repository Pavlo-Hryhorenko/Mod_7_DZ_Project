from pathlib import Path
import shutil
import sys
import file_parser as parser
from normalize import normalize


def handle_media(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_other(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_archive(filename: Path, target_folder: Path):
    # Створюємо папку для архівів
    target_folder.mkdir(exist_ok=True, parents=True)
    # Створюємо папку куди розпакуємо архіви
    # Беремо суфікс у файла і видаляємо replace(filename.suffix, '')
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))
    # folder_for_file = target_folder / filename.replace(filename.suffix, '')
    # Створюємо папку для архіву з іменем файлу
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()),
                              str(folder_for_file.resolve()))
    except shutil.ReadError:
        print(f'Це не архів {filename}!')
        folder_for_file.rmdir()
        return None
    filename.unlink()


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Помилка видалення папки {folder}')


def main(folder: Path):
    parser.scan(folder)
    for file in parser.JPEG_IMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in parser.JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in parser.PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in parser.SVG_IMAGES:
        handle_media(file, folder / 'images' / 'SVG')
    for file in parser.MP3_AUDIO:
        handle_media(file, folder / 'audio' / 'MP3')
    for file in parser.OGG_AUDIO:
        handle_media(file, folder / 'audio' / 'OGG')
    for file in parser.WAV_AUDIO:
        handle_media(file, folder / 'audio' / 'WAV')
    for file in parser.AMR_AUDIO:
        handle_media(file, folder / 'audio' / 'AMR')
    for file in parser.AVI_VIDEO:
        handle_media(file, folder / 'video' / 'AVI')
    for file in parser.MP4_VIDEO:
        handle_media(file, folder / 'video' / 'MP4')
    for file in parser.MOV_VIDEO:
        handle_media(file, folder / 'video' / 'MOV')
    for file in parser.MKV_VIDEO:
        handle_media(file, folder / 'video' / 'MKV')
    for file in parser.DOC_FILES:
        handle_media(file, folder / 'files' / 'DOC')
    for file in parser.DOCX_FILES:
        handle_media(file, folder / 'files' / 'DOCX')
    for file in parser.TXT_FILES:
        handle_media(file, folder / 'files' / 'TXT')
    for file in parser.PDF_FILES:
        handle_media(file, folder / 'files' / 'PDF')
    for file in parser.XLSX_FILES:
        handle_media(file, folder / 'files' / 'XLSX')
    for file in parser.PPTX_FILES:
        handle_media(file, folder / 'files' / 'PPTX')
    for file in parser.ZIP_ARCHIVES:
        handle_media(file, folder / 'archives' / 'ZIP')
    for file in parser.GZ_ARCHIVES:
        handle_media(file, folder / 'archives' / 'GZ')
    for file in parser.TAR_ARCHIVES:
        handle_media(file, folder / 'archives' / 'TAR')

    for file in parser.MY_OTHER:
        handle_other(file, folder / 'MY_OTHER')


    # Виконуємо реверс списку для того щоб видалити всі папки
    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)


def path_function():
    try:
        folder = sys.argv[1]
    except IndexError:
        print('Enter valid path to the folder')
    else:
        folder_for_scan = Path(folder)
        print(f'Start in folder {folder_for_scan.resolve()}')
        main(folder_for_scan.resolve())


if __name__ == '__main__':
    path_function()
#
# if __name__ == '__main__':
#     if sys.argv[1]:
#         folder_for_scan = Path(sys.argv[1])
#         print(f'Start in folder {folder_for_scan.resolve()}')
#         main(folder_for_scan.resolve())


# TODO: запускаємо:  python3 main.py `назва_папки_для_сортування`