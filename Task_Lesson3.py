# Домашнее задание:
# https://drive.google.com/open?id=15fBsTB1ZU_BzEw5SJmlOMX2uuyi1xN1-
# В файле содержится текст. Считать/скопировать текст из файла и выполнить следующую последовательность действий:
file = open("text.txt", 'r', encoding="utf-8")
text = file.read()
# LIGHT:

# 1) методами строк очистить текст от знаков препинания;
text_no_punct = text.replace('.','').replace(',','').replace('-',' ').replace('«','').replace('»','').replace('!','').replace('?','').replace('—','').replace(';','').replace(':','').replace('(','').replace(')','').replace('\n',' ')
print ('Текст без знаков препинания:', text_no_punct)

# 2) сформировать list со словами (split);
text_list = list(text_no_punct.split())
print('Список всех слов текста:', text_list)

# 3) привести все слова к нижнему регистру (map);
# text_lower = text_no_punct.lower()
text_lower = list(map(lambda x: str(x).lower(), text_list))
print('Список слов в нижнем регистре:', text_lower)

# провести лемматизацию текста;
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
text_normalized = str()
for word in text_lower:
    word = morph.parse(word)[0]
    text_normalized += word.normal_form + " "
text_lower = list(text_normalized.split())
print('Список нормализованных слов:', text_lower)

# 4) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
text_dict = {}
for i in range (len(text_lower)):
    text_dict[text_lower[i]] = text_lower.count(text_lower[i])
print('Сколько раз встречаются слова:', text_dict)

# 5) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).
text_top_list = list(text_dict.items())
text_top_list.sort(key = lambda i: i[1], reverse=True)
print('TOP-5 часто встречающихся слов:', text_top_list[:5])
# print('Всего в тексте', len(text_dict),'разных слов')
print('Всего в тексте', len(set(text_lower)),'разных слов')

