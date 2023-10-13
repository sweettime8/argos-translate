from argostranslate.translate import ITranslation

from argostranslatefiles.argostranslatefiles.formats.html import Html
from argostranslatefiles.argostranslatefiles.formats.opendocument.odp import Odp
from argostranslatefiles.argostranslatefiles.formats.opendocument.odt import Odt
from argostranslatefiles.argostranslatefiles.formats.openxml.docx import Docx
from argostranslatefiles.argostranslatefiles.formats.openxml.pptx import Pptx
from argostranslatefiles.argostranslatefiles.formats.txt import Txt
from argostranslatefiles.argostranslatefiles.formats.epub import Epub


def get_supported_formats():
    return [
        Txt(),
        Odt(),
        Odp(),
        Docx(),
        Pptx(),
        Epub(),
        Html()
    ]


def translate_file(underlying_translation: ITranslation, file):
    """Translate a file.

    Args:
        underlying_translation (argostranslate.translate.ITranslation): Argos Translate Translation
        file_path (str): file path

    Returns:
        file_path: Translated file
    """

    for supported_format in get_supported_formats():
        if supported_format.support(file.filename):
            return supported_format.translate(underlying_translation, file)

    return False
