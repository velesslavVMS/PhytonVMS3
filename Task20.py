'''Задача 20: * В настольной игре Скрабл (Scrabble) 
каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко; 
D, G – 2 очка; 
B, C, M, P – 3 очка; 
F, H, V, W, Y – 4 очка; 
K – 5 очков; 
J, X – 8 очков; 
Q, Z – 10 очков. 
А русские буквы оцениваются так: 
    А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
    Д, К, Л, М, П, У – 2 очка; 
    Б, Г, Ё, Ь, Я – 3 очка; 
    Й, Ы – 4 очка; 
    Ж, З, Х, Ц, Ч – 5 очков; 
    Ш, Э, Ю – 8 очков; 
    Ф, Щ, Ъ – 10 очков. 
Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
Будем считать, что на вход подается только одно слово, 
которое содержит либо только английские, либо только русские буквы.'''

word = str(input('Введите слово: '))
word1=list(word.upper())
print(word1)
count = 0
n1 =0
n2 =0
n3 =0
n4 =0
n5 =0
n6 =0
n7 =0
N = 0
for i in range(len(word1)):
    if word1[i] == 'A'or'E'or 'I'or 'O'or 'U'or 'L'or 'N'or 'S'or 'T'or 'R':
        count = 1
        n1= n1+count
        print (f"i= {i} word1[i]={word1[i]} n1= {[n1]}")
    elif word1[i] == 'D'or'G':
        count = 2 
        n2= n2+count
        print (f"i= {i} word1[i]={word1[i]} n2= {[n2]}")
    elif word1[i] == 'B'or 'C'or 'M'or 'P':
        count = 3   
        n3= n3+count
        print (f"i= {i} word1[i]={word1[i]} n3= {[n3]}")
    elif word1[i] == 'F'or 'H'or 'V'or 'W'or 'Y':
        count = 4 
        n4= n4+count
        print (f"i= {i} word1[i]={word1[i]} n4= {[n4]}")
    elif word1[i] == 'K':
        count = 5 
        n5= n5+count
        print (f"i= {i} word1[i]={word1[i]} n5= {[n5]}")
    elif word1[i] == 'J'or 'X':
        count = 8
        n6= n6+count
        print (f"i= {i} word1[i]={word1[i]} n6= {[n6]}")
    elif word1[i] == 'Q'or 'Z':
        count = 10 
        n7= n7+count
        print (f"i= {i} word1[i]={word1[i]} n7= {[n7]}")
        
    N = N + count
print (f"Слово {word} стоит {N} очков")