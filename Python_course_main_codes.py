## DAY=2 ####################################
'''
0.30
int
1, 2, 3, -1, -2, -3

0.50
float
1.1, 1.7, 3.14, 3.0

1.10
str
'Hello, world!'

1.35
list
[1, 3.14, 'Hello']

2.00
dict
{ 'alex' : '123', 'anna' : '321'}

2.35
tuple
(1, 3.14, 'Hello')

3.10
set
{'a', 'b', 'c'}

3.33
bool
True
False
'''
x = 1
print(x)
print(type(x))
''' 
result::
1
<class 'int'>
'''
x = float(x)
print(x)
print(type(x))
''' 
result::
1.0
<class 'float'>
'''


###   DAY=3 ########################################################
x = 3
print(x)
x = 5
print(x)
y = 4
print(x + y)
print(y + y)
print(x + x)
print(type(x))
z = 'text123'
print(type(z))
# print(x + z) ERROR
print(z + ' ' + z)
x = None
print(type(x))
''' 
result::
3
5
9
8
10
<class 'int'>
<class 'str'>
text123 text123
<class 'NoneType'>
'''



x = 1+1   #2
x = 2+2   #4
x = 3-2   #1
x = 3-5   # -2
x = 9/3   # 3.0
x = 1/1   #1.0
x = 7/2   #3.5
x = 3.0+1   #4.0
x = 3*2   #6
x = 1.2*3   #3.599999999999996
x = round(1.2*3, 2)   #3.6
print(x)
'''
boldi
'''


x = 3%2   #1
x = 4%2==0   #True
x = 9%2==0   #False
x = 2*2*2*2   #16
x = 2**4    #16
print(x)
'''
boldi
'''
x = 2+2*2   #6
x = (2+2)*2    #8
x = (2+2)*2+3*(6/2)   #17.0
x = 3**36   #150,094,635,296,999,121
x = 2**62   #4,611,686,018,427,387,904
print(x)
'''
boldi
'''
import math
a = 15
b = 11
c = 9
p = (a+b+c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(s)
''' 
result::
49.16490109824284
'''


###      DAY=4   ####################################################
y = int(False)
print(y)
''' 
result::
0
'''
a = []
b = [1, 2, 3]
x = bool(a)
print(x)   #False
y = bool(b)
print(y)    #True

a = True
print(a)    #True
print(type(a))    #<class 'bool'>
'''
'''
b = true    #Error
'''
'''

print(2>3)   #False
print(3<2)   #False
print(2>1)   #True

print(2>=2)    #True
print(3>=2)    #True
print(2>=3)    #False
print(1!=1)    #False
print(2!=1)    #True
print(1==1)    #True
print(2==1)    #False
print('text' == 'text') #True
print('text' == 'text 2') #false
print('text' == 'TEXT') #false
print(1<2<3<4) #True
print(1<2<3>4) #false
print(1<2 and 2<3) #True
print(1>2 and 2<3) #false
print(1>2 or 2<3) #True
print(1>2 or 2>3) #false



###    DAY=5  ######################################################


x = 'Alex'
print(x)    #Alex

y = "Some text 123"
print(y)   #Some text 123

z = 'Some 'long' text'   #Error

z = "Some 'long' text"
print(z)    #Some 'long' text

x = "Some 'long', and 'awesome' text"
print(x)    #Some 'long', and 'awesome' text

x = "Some \'long\', and \'awesome\' text"
print(x)    #Some 'long', and 'awesome' text

y = 'C:\\Users\\dell\\Desktop\\Py_lesson'
print(y)    #C:\Users\dell\Desktop\Py_lesson

z = r'C:\Users\dell\Desktop\Py_lesson'
print(z)    #C:\Users\dell\Desktop\Py_lesson

x = 'some long text \nand new string \nand new string \nand new string'
print(x)
'''
some long text
and new string
and new string
and new string
'''

text = str('hello world')
print(text)    #hello world
print(text[0])    #h
print(text[0]+text[1])    #he
print(text[-1]+text[1])    #dh
print(text[6:]+text[1])    #worlde
print(text[6:]+' '+text[:6])    #world hello
print(text[6:8])    #wo
print(text[::1])    #hello world
print(text[::2])    #hlowrd
x = 'hello'
y = 'world'
print(x + ' ' + y)    #hello world
print('%s %s' % (x, y))    #hello world
print('{} {}'.format(x, y))    #hello world
z = 'text '
print(z*6)    #text text text text text text



###     DAY=6 #######################################################
x = 'some long and awesome TEXT'
print(len(x))    #26
print(x[len(x)-1])    #T
print(x[len(x)-4:len(x)])     #TEXT
print(x.count('o'))     #3
print(x.find('a'))     #10
print(x.find('o'))     #1
print(x.find('o'))    #1
print(x.find('o', 3, 7))    #6
print(x.find('o', 7))     #18
print(x.find('and'))     #10
print(x.find('TEXT'))     #22
print(x.find('abc'))     #-1
print(x.capitalize())    #Some long and awesome text
print(x.upper())     #SOME LONG AND AWESOME TEXT
print(x.lower())     #some long and awesome text
print('Old text: '+x)    #Old text: some long and awesome TEXT

upper_cased = x.upper()
lower_cased = x.lower()
print(upper_cased.isupper())    #True
print(lower_cased.islower())    #True
print(x.isupper())     #False
print(x.islower())     #False

print('xxx777'.isalnum())    #True //bu hammasida yo harf yo raqam bolsa
print('xxx777!'.isalnum())    #False //chunki betda undov ! belgisi bor
print('xxx777'.isalpha())    #False // bu hammasi harf bolsagina turi.
print('xxx'.isalpha())    #True  //bu hammasi harf
print('   '.isspace())    #True // agarda bosh joy bolsa bu rost boladi.
print(''.isspace())    #False  // agarda bosh joy bolmasa bu yolg'on boladi
empty_string = ''
print(empty_string == '') #true  //chunki bu yerda hech narsa yoq, boshliq
print(empty_string == ' ')  #false   //xato, chunki bu yerda bosh koringani bilan "probel" bor

////////////////////////////////////////////////////////////////////////////

print(empty_string.strip(' ') == '')    #true   //
empty_string = ' '
print(empty_string.strip() == '')

empty_string = ''
if not empty_string:
	print('not empty')
else:
	print('empty')

/////////////////////////////////////////////////////////////////////////////////

x = str('hello')
print(x.startswith('he'))     #True  //chunki "hello" bosh harflari "he..." dan boshlanadi
print(x.endswith('lo'))     #True   // chunki "hello oxirgi harflari "...lo" bilan tugaydi

'''
'''
x = str('hello')
split = x.split('l')
print(type(split))     #<class 'list'>
print(split)     #yozilgan harfni olib tashlaydi
'''
result:
<class 'list'>
['he', '', 'o']  
'''
split = x.split('e')
print(split)
'''
['h', 'llo']
'''
some_data = '4;8;15;16;23;42'
separated_data = some_data.split(';')     #biron listdan osha belgini olib tashlab vergul bilan list yasab beradi
print(separated_data)     #belgini obtashlab vergul bilan list yasab berdi
print(separated_data[3])     #listdagi indeksi boyicha osha sonni chiqarib berdi.(0:4,1:8,2:15,3:16)
'''
['4', '8', '15', '16', '23', '42']
16
'''



###      DAY=7 ###########################################################################

x = '10'
y = 'cold'
print('Weather: temperature +{} and it\'s {}'.format(x, y)     #Weather: temperature +10 and it's cold
print('Weather: temperature +{1} and it\'s {0}'.format(x, y))     #Weather: temperature +cold and it's 10
print(f'Weather: temperature +{x} and it\'s {y}')      #Weather: temperature +10 and it's cold
pi = 3.141532
print(pi)
print(f'pi equals {pi:0.2f}')
print(f'pi equals {pi:0.5f}')

################# Uy ishi ##########################################
"""
Задание на строки
Работа со строками
1) Задайте переменные: имя фамилия и возраст.
 Выведите в консоль: Привет, меня зовут ‘имя’, ‘фамилия’ и мне ‘возраст’ лет.
2) Выведите на экран текст детского стихотворения ‘Почему лето короткое’:
— Почему для всех ребят
Лета не хватает?
— Лето, словно шоколад,
Очень быстро тает!
Используйте специальные операторы для переноса текста на новую строку.

3) Выведите в консоль индекс буквы ‘W’ фразы ‘Hello World’

4) Из строки ‘abrakadabra’ удалите, с помощью метода срез все сочетания ‘ab’.
и выведите результат на экран

5) Путём конкатенации (присоединения/сложения) строк и срезов соберите строку ‘barbara’ из из строки ‘abrakadabra’.
6) Преобразуйте строку ‘barbara’ выведя её с заглавной буквы.
7) Выведите строку ‘win! win! win!’ с помощью умножения.
Преобразуйте строку  ‘win! win! win!’ так чтобы все буквы были заглавными.


"""

name = 'Анна'
surname = 'Иванова'
age = 19

print(f'Привет меня зовут {name} {surname}, мне {age} лет.')

print('— Почему для всех ребят\nЛета не хватает?\n— Лето, словно шоколад,\nОчень быстро тает!')

#Из строки ‘abrakadabra’ удалите все сочетания ‘ab’.
text = 'abrakadabra'
index_letter_ab_1 = text.find('ab')
index_letter_ab_2 = text.find('ab', 1)

#Зная индексы подстроки ab делаем срезы
new_text = text[index_letter_ab_1+2:index_letter_ab_2] + text[index_letter_ab_2+2:-1]

print(new_text)

#Путём конкатенации (присоединения/сложения) строк и срезов соберите строку ‘barbara’ из из строки ‘abrakadabra’.

text = 'abrakadabra'
new_text = text[text.find('b')] + text[0] + text[text.find('r')] + text[text.find('b')] + text[0] + text[text.find('r'):text.find('r')+2]
print(new_text)

capitalize_text = new_text.capitalize()
print(capitalize_text)

text = 'win! '
new_text = text*3
print(new_text)
upper_text = new_text.upper()
print(upper_text)

#################################################################################





###     DAY = 8 ############################################################################

new_list = [1,2,3,4]
mix_list = [12, 3.14, 'text']
print(len(new_list))    #4   //list uzunligi 4 ga teng
print(new_list[0])    #1   //chunki 0 indeksida faqat 1 soni turubdi
print(new_list[-1])    #4   // -1 raqam bu noldan oldin turadi, yani listdan orqaga qaytadigan bolsa 4 turubdi.
print(new_list[2:])    #[3, 4]   //listda 2 indeksida 3 turubdi, va 2 indeksidan keyin 4 soni ham bor oxirida.

# delete


list_1 = ['anna', 'alex', 'max']
list_2 = ['john', 'nicolas', 'vlad']
print(list_1 + list_2)     #['anna', 'alex', 'max', 'john', 'nicolas', 'vlad']

list_1[0] = 'artur'     #//0 indeksidagi ismni ozgartirdi.
print(list_1)     #['artur', 'alex', 'max'] not ['anna', 'alex', 'max']

list_1.append('anna')     #// qoshib qoyadi list oxiriga osha sozni
print(list_1)     #['artur', 'alex', 'max', 'anna']

list_1.insert(1, 'john')       #//1 indeksi boyicha joyga osha yangi sozni qoshib qoyadi
print(list_1)     #['artur', 'john', 'alex', 'max', 'anna']
print(list_1.index('max'))     #//'max' sozi qaysi indexda turganini korsatib beradi

list_1.index('max', start=0, stop=10) #OR list_1.index('vlad', 0, 10)   //qaysi yacheykada turganini etib beradi
pop_del = list_1.pop()    #   //listdagi eng oxirgi sozni udalit qiladi
print(pop_del)     #anna
print(list_1)    #['artur', 'john', 'alex', 'max']

list_1.pop(0)    #//indeksi boyicha 1chi elementni udalit qildi
print(list_1)     #['john', 'alex', 'max']

list_1.clear()     #// polniy listni udalit qilib pustoy qiladi
print(list_1)    # []


# delete


list_3 = ['33', '22', '11', '44']
print(list_3)    #['33', '22', '11', '44']
list_3.sort()    #//kattarish boyicha qib beradi
print(list_3)    #['11', '22', '33', '44']
list_3.sort(reverse=True)    #listni kamayish boyicha qib beradi
print(list_3)     #['44', '33', '22', '11']


# delete


list_4 = ['abcde', 'bcb', 'da', 'cde',  'ser', 'q']
print(list_4)     #['abcde', 'bcb', 'da', 'cde',  'ser', 'q']
list_4.sort()     #//1chi harfiga qarab sorting qib tashlaydi.
print(list_4)     #['abcde', 'bcb', 'cde', 'da', 'q', 'ser']
list_4.sort(key=len)    #//len* funksiya sabab sozlarni uzunligi boyicha list qib beradi
print(list_4)    #['q', 'da', 'bcb', 'cde', 'ser', 'abcde']
list_4.reverse()    #royhatni shunchaki orqaga aylantirib chappacha qib beradi
print(list_4)     #['abcde', 'ser', 'cde', 'bcb', 'da', 'q']


#### UY ISHI ##################################################################
#java download, commandda javac. acrosoft download, kitobdan yejini java ni faylarini, tomcat download., maven download










