from argostranslate.translate import ITranslation

from argostranslatefiles.argostranslatefiles.abstract_file import AbstractFile
import os

class Txt(AbstractFile):
    supported_file_extensions = ['.txt']

    def translate(self, underlying_translation: ITranslation, file):
        #outfile_path = self.get_output_path(underlying_translation, file_path)
        # infile = open(file_path, "r", encoding='utf-8')
        # outfile = open(outfile_path, "w", encoding='utf-8')
        # translated_text = underlying_translation.translate(infile.read())
        # outfile.write(translated_text.strip())
        # infile.close()
        # outfile.close()
        # return outfile_path


        outfile_path = os.getcwd()
        infile = file.read()

        translated_text = underlying_translation.translate(infile.decode('utf-8'))
        with open(outfile_path +"/output_translate/"+ file.filename, 'w', encoding='utf-8') as outfile:
            outfile.write(translated_text)

        return outfile_path
