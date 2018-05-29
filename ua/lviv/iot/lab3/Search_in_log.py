
# Вивести всі неуспішні запити (містять статус код в діапазоні 400-499)  з лог файлу, які відбувались в проміжку 22/Mar/2009:19:25:21
#  До 29/Mar/2009:12:00:00, наприклад:
# 83.198.250.175 - - [22/Mar/2009:07:40:07 +0100] "GET /favicon.ico HTTP/1.1" 404
#
# Лог файл:
# http://igm.univ-mlv.fr/~cherrier/download/L1/access.log
import zipfile
import re

def search_in_log():
    zip_file = zipfile.ZipFile('access.log.zip')
    file = zip_file.open('access.log.txt')
    for line in file:
        if re.search('.*[[22-30/]Mar/2009:1[2-9]:2[0-5]:[0-2][0-1] .* [4-5][0-9][4-9]', str(line)):
            print(line)
    zip_file.close()


if __name__ == "__main__":
    search_in_log()