from flask import Blueprint, request, render_template, redirect, url_for, flash, Response, jsonify, session
import logging
import argostranslate.package
import argostranslate.translate
from argostranslatefiles.argostranslatefiles import argostranslatefiles
import tempfile
import os

actions = Blueprint('actions', __name__, template_folder='templates')

# Cấu hình logging
logging.basicConfig(filename='logfile.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info('#################################################')
logging.info('#                 Start APP                     #')
logging.info('#################################################')


@actions.route('/')
def index():
    return render_template('index.html')


@actions.route('/translate', methods=['POST'])
def translate():
    print("## [translate] ##")
    try:
        if request.method == 'POST':
            # Lấy dữ liệu từ form
            from_text = request.form['from_text']
            from_code = request.form['from_code']
            to_code = request.form['to_code']

            base_dir = os.getcwd()
            # dịch từ việt sang nhật cần qua trung gian là ANH
            if (from_code == "vi" and to_code == "ja") or (from_code == "ja" and to_code == "vi"):
                to_code_temp = "en"
                from_code_temp = "en"

                file_name_temp = "translate-" + from_code + "_" + to_code_temp + ".argosmodel"
                download_path_temp = os.path.join(base_dir, "translate_data_model", file_name_temp)
                argostranslate.package.install_from_path(download_path_temp)
                # Translate
                installed_languages_temp = argostranslate.translate.get_installed_languages()

                from_lang = list(filter(
                    lambda x: x.code == from_code,
                    installed_languages_temp))[0]

                lang_temp = list(filter(
                    lambda x: x.code == from_code_temp,
                    installed_languages_temp))[0]

                translation_temp = from_lang.get_translation(lang_temp)
                to_text_temp = translation_temp.translate(from_text)

                file_name = "translate-" + to_code_temp + "_" + to_code + ".argosmodel"
                download_path = os.path.join(base_dir, "translate_data_model", file_name)
                argostranslate.package.install_from_path(download_path)
                installed_languages = argostranslate.translate.get_installed_languages()
                to_lang = list(filter(
                    lambda x: x.code == to_code,
                    installed_languages))[0]

                translation = lang_temp.get_translation(to_lang)
                to_text = translation.translate(to_text_temp)
            else:

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
                to_text = translation.translate(from_text.strip())

            return jsonify({'status': 'success', 'data': to_text})
            # return render_template('index.html', from_text=from_text, to_text=to_text)

    except Exception as e:
        # Xảy ra lỗi khi kết nối
        print('Connection error: ' + str(e))
        return jsonify({'status': 'error', 'message': str(e)})


@actions.route('/translate-file', methods=['POST'])
def translate_file():
    print("tranlsate_file")
    try:
        file = request.files['filepond']
        print(file)
        from_code = "en"
        to_code = "vi"
        file_name = "translate-" + from_code + "_" + to_code + ".argosmodel"
        base_dir = os.getcwd()
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

        isExist = os.path.exists("output_translate")
        if not isExist:
            os.makedirs("output_translate")

        argostranslatefiles.translate_file(translation, file)

    except Exception as e:
        # Xảy ra lỗi khi kết nối
        print('Error: ' + str(e))
        return jsonify({'status': 'error', 'message': str(e)})
