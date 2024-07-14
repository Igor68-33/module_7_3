# # "Оператор "with"

class WordsFinder:
    """
    WordsFinder('file1.txt, file2.txt', 'file3.txt', ...)

    """
    file_names = []

    def __init__(self, *files_names):
        self.file_names = [x for x in files_names]

    def get_all_words(self):
        """
        get_all_words - подготовительный метод
        :return: словарь {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4']}
         'file.txt':
         ['word1', 'word1']
        """
        all_words = dict()
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                file_string = file.read().lower()
            file_string = file_string.replace(',', ' ')
            file_string = file_string.replace('.', ' ')
            file_string = file_string.replace('=', ' ')
            file_string = file_string.replace('!', ' ')
            file_string = file_string.replace('?', ' ')
            file_string = file_string.replace(';', ' ')
            file_string = file_string.replace(':', ' ')
            file_string = file_string.replace(' — ', ' ')
            file_string = file_string.replace('\n', ' ')
            file_string = file_string.replace('  ', ' ')
            all_words.update({file_name: file_string.split()})
        return all_words

    def find(self, word):
        """
        find(self, word)
        :param word: - искомое слово
        :return: словарь {название файла: позиция первого такого слова в списке слов
        """
        word = word.lower()
        result = dict()
        for name, words in self.get_all_words().items():
            if word in words:
                result.update({name: words.index(word) + 1})
                continue
        return result

    def count(self, word):
        """

        :param word:  - искомое слово
        :return: словарь, где ключ - название файла, значение - количество слова word в списке слов
        """
        word = word.lower()
        result = dict()
        for name, words in self.get_all_words().items():
            if word in words:
                result.update({name: words.count(word)})
                continue
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

# Вывод на консоль:
# {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки',
# 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
# {'test_file.txt': 3}
# {'test_file.txt': 4}