import argostranslate.package
import argostranslate.translate
import os

from_code = "en"
to_code = "ja"

# Download and install Argos Translate package
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
available_package = list(
    filter(
        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
    )
)[0]
# download_path = available_package.download()
base_dir = os.getcwd()
file_name = "translate-" + from_code + "_" + to_code + ".argosmodel"
download_path = os.path.join(base_dir, "translate_data_model", file_name)
print(download_path)
argostranslate.package.install_from_path(download_path)

# Translate
installed_languages = argostranslate.translate.get_installed_languages()
from_lang = list(filter(
    lambda x: x.code == from_code,
    installed_languages))[0]
to_lang = list(filter(
    lambda x: x.code == to_code,
    installed_languages))[0]
translation = from_lang.get_translation(to_lang)
text = f"""
        Click on the Manage Packages menu item.
        Click on the Install package file button.
        Navigate to where you downloaded the new language pairs, click on the .argosmodel file, and click on the Open button.
        Repeat the last two steps until you have all of the language pairs that you want.
        Click on the X in the top right to close the Manage Packages window. 
"""
translatedText = translation.translate(text)
print("############# available_packages ##########################")
for item in available_packages:
    print(item)
print(translatedText)

# '¡Hola Mundo!'
