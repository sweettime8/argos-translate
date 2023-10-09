import argostranslate.package
import argostranslate.translate
import os

from_code = "vi"
to_code = "en"

available_packages = argostranslate.package.get_available_packages()
print("############# available_packages ##########################")
for item in available_packages:
    print(item)
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
Open-source offline translation library written in Python

Argos Translate uses OpenNMT for translations and can be used as 
either a Python library, command-line, or GUI application. Argos 
Translate supports installing language model packages which are zip 
archives with a ".argosmodel" extension containing the data needed for 
translation. LibreTranslate is an API and web-app built on top of Argos Translate.

Argos Translate also manages automatically pivoting through intermediate 
languages to translate between languages that don't have a direct translation 
between them installed. For example, if you have a es → en and en → fr translation
 installed you are able to translate from es → fr as if you had that translation
  installed. This allows for translating between a wide variety of languages at 
  the cost of some loss of translation quality.

"""

text_vi = f"""Dường như ngày ấy Trên xe buýt có ai đã khóc nức nở 
Tiếng nức nở Hòa cùng cơn mưa rơi trên đường về Góc phố quen nhuộm màu cô đơn Hàng cây giờ có thêm lá héo Đã xa thật rồi Ôi kỷ niệm, đừng trở thành quá khứ... 
Dường như ngày ấy Trên xe buýt, ai đó đã khóc lớn Mặt trời dường như ngừng hát Khi thiếu người ngồi bên cạnh Điểm dừng chân tiếp theo Tự hỏi liệu chúng ta có gặp lại nhau Hay màu sắc sẽ phai theo thời gian Những năm tháng ấy dần tan biến Nhưng dù sao, trên xe buýt, bạn không nên khóc to...
Dường như ngày ấy Trên xe buýt có ai đã khóc nức nở 
Tiếng nức nở Hòa cùng cơn mưa rơi trên đường về Góc phố quen nhuộm màu cô đơn Hàng cây giờ có thêm lá héo Đã xa thật rồi Ôi kỷ niệm, đừng trở thành quá khứ... 
Dường như ngày ấy Trên xe buýt, ai đó đã khóc lớn Mặt trời dường như ngừng hát Khi thiếu người ngồi bên cạnh Điểm dừng chân tiếp theo Tự hỏi liệu chúng ta có gặp lại nhau Hay màu sắc sẽ phai theo thời gian Những năm tháng ấy dần tan biến Nhưng dù sao, trên xe buýt, bạn không nên khóc to..."""
translatedText = translation.translate(text_vi)
print("############# translatedText ##########################")
print(translatedText)

# '¡Hola Mundo!'