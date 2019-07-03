import re
import urllib.request


headers = {'User-Agent':
"Mozilla/4.0 (\
compatible;\
MSIE 6.0;\
Windows NT 5.1;\
SV1;\
.NET CLR 1.1.4322;\
.NET CLR 2.0.50727;\
.NET CLR 3.0.04506.30\
)"}


def clean_text(text):
    if text == '':
        return ''

    return text.replace(' ', '%20')


def make_get_request(tl='auto', sl='auto', text=''):
    _request = """http://translate.google.com/m?hl={target_lang}&sl={source_lang}&q={text}"""

    cleaned_text = clean_text(text)

    _built_request = _request.format(source_lang=sl, target_lang=tl, text=cleaned_text)

    _urllib_request = urllib.request.Request(_built_request, headers=headers)

    _response = urllib.request.urlopen(_urllib_request).read()

    return _response


def parse_response(response):
    _raw_response = response.decode('utf-8')
    _matches = re.findall(r'class="t0">(.*?)<', _raw_response)

    if _matches is None or len(_matches) == 0:
        print("Could not find anything...")
    else:
        print(_matches[0])


if __name__ == "__main__":
    supported_langs = ['es', 'en', 'de']
    print("""es->Spanish, en->English, de->German""")
    src_l = input("Specify source language: ")
    while src_l not in supported_langs:
        print("Invalid entry..")
        src_l = input("Specify source language: ")
    dst_l = input("Specify target language: ")
    while dst_l not in supported_langs:
        print("Invalid entry:")
        dst_l = input("Specify target language: ")

    corpora = input("Enter text to translate: ")

    parse_response(make_get_request(sl=src_l, tl=dst_l, text=corpora))