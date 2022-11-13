from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1.0',
    description='Сортує задану папку- перевіряє внутрішні вкладення/ Форматує утворюючи нові папки і розархивовує архіви, також переіменовує.',
    author='Pavlo_Hryhorenko',
    entry_points={'console_scripts': ['clean-folder = clean_folder.main:path_function']},
    packages = find_packages(),
    include_package_data = True
)

