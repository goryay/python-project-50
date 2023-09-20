### Hexlet tests and linter status:
[![Actions Status](https://github.com/goryay/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/goryay/python-project-50/actions)
<a href="https://codeclimate.com/github/goryay/python-project-lvl1/maintainability"><img src="https://api.codeclimate.com/v1/badges/614a3f8511bdb84b3258/maintainability" /></a>
<a href="https://codeclimate.com/github/goryay/python-project-lvl1/test_coverage"><img src="https://api.codeclimate.com/v1/badges/614a3f8511bdb84b3258/test_coverage" /></a>


# Генератор отличий
### Выполняет сравнение документов в форматах *.json, *.yml, *.yaml, содержащих словарь словарей. Находит различия в ключах и их значениях и выводит их в заданном формате.
### Вы можете использовать пакет python или вызвать его из командной строки.


## Форматы вывода

* stylish - используется по умолчанию. Выводит результат в виде многострочного текста с древовидной структурой словаря.
* plain - выводит результат в виде многострочного текста в форме:
  * Свойство ... было добавлено ...
  * Свойство ... было удалено ...
  * Свойство ... было обновлено ...
* json - Выводит результат в виде json-объекта.


## Установка и удаление пакета:

* mmake build - сборка пакета.
* make package-install - установка пакета.
* make package-uninstal-hc - удаление пакета. Включение встроенной папки пакета.


## Опции пакета:
* -h, --help - показать сообщение справки и выйти.
* -f, --format - возможность указать выбор формата. Возможные форматы см. выше.


# Пример


