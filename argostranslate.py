import argostranslate.package
import argostranslate.translate
import json
import os

os.environ["ARGOS_DEVICE_TYPE"] = "auto"

from_code = "ja"
to_code = "en"

argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(
    filter(
        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
    )
)
argostranslate.package.install_from_path(package_to_install.download())

with open('1.0.json', 'r', encoding="utf8") as data_file:
    json_data = data_file.read()
data = json.loads(json_data)

iterator = 0
size = len(data)
dict = {}
for k, v in data.items():
    iterator+=1
    translatedText = argostranslate.translate.translate(v, from_code, to_code)
    dict[k] = translatedText
    print(str(iterator) + "/" + str(size), end="\r")

json_object = json.dumps(dict,ensure_ascii=False)
 
with open("1.0_translated.json", "w", encoding="utf8") as outfile:
    outfile.write(json_object)
