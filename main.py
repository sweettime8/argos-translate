import argostranslate.package
import argostranslate.translate

from argostranslatefiles.argostranslatefiles import argostranslatefiles
import os

from_code = "en"
to_code = "vi"

available_packages = argostranslate.package.get_available_packages()
# print("############# available_packages ##########################")
# for item in available_packages:
#     print(item)
available_package = list(
    filter(
        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
    )
)[0]

base_dir = os.getcwd()
file_name = "translate-" + from_code + "_" + to_code + ".argosmodel"
download_path = os.path.join(base_dir, "translate_data_model", file_name)
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
text_eng = f"""
My biggest weakness is that I sometimes get so caught up in the details. 
I’ve been trying to improve in this aspect by checking in with myself regularly and reminding myself to refocus on the big picture. 
This way I can still ensure the quality of my work without impacting my productivity.
"""

text_vi = f"""
Điểm yếu lớn nhất của tôi là đôi khi tôi bị cuốn vào các chi tiết. 
Tôi đã cố gắng cải thiện trong phương diện này bằng cách tự kiểm tra bản thân thường xuyên và nhắc nhở bản thân trung lại vào tổng quan công việc. 
Bằng cách này, tôi vẫn có thể đảm bảo chất lượng công việc mà không ảnh hưởng đến năng suất của mình
"""
translatedText = translation.translate(text_eng)
print("############# translatedText ##########################")
print(translatedText)

argostranslatefiles.translate_file(translation, os.path.abspath('datatest/test.txt'))
