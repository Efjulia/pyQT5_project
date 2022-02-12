#CryptPaint
##Назначение
Программа для создания изображения и стеганографического сокрытия текстовой информации в изображении. 

##Функционал
1. Создание изображения.
2. Шифрование текста в изображение.
3. Расшифрование текста из изображения.
4. Информация о программе.

###Создание изображения 
Изображение создается по принципу элементарного Paint.

Рисование происходит при нажатой левой клавиши мыши и при её перемещении. Завершается рисование после отпускания левой клавиши мыши.

Правая клавиша мыши используется для выбора цвета кисти из палитры.

   
Для <b>создания</b> изображения используются пункты следующие меню:

 - <b>Заливка фона</b>
   
   Цвет фона можно поменять на один из 6 вариантов: белый, синий, красный, желтый, зеленый, черный.
   По умолчанию при запуске программы установлен фон белого цвета.
   
 - <b>Цвет кисти</b>
   
   Цвет кисти можно поменять на один из 5 вариантов: синий, красный, желтый, зеленый, черный.
   По умолчанию при запуске программы цвет кисти установлен в красный.
   
 - <b>Размер кисти</b>
   
   Пользователь может поменять размер кисти на 8 пикселей, 10 пикселей, 12 и 14 пикселей.
   По умолчанию при запуске программы размер кисти равен 8.
 - <b>Фоновое изображение</b>
   
   В диалоговом режиме пользователь может выбрать произвольное изображение для заполнения фона.
 - <b>Ластик</b>
   
   Стирает точку изображения, равную установленному размеру кисти.
 - <b>Очистить лист</b>
   
   Полностью удаляет нарисованное изображение.
   
Для <b>сохранения</b> изображения используются пункты меню:

 - <b>Сохранить</b>
   
   В диалоговом режиме пользователь сохраняет изображение в формате *.bmp. При закрытии программы пользователю также предлагается сохранить изображение.


###Шифрование текста в изображение

Процесс закрытия текстовой информации в изображение запускается из пункта меню "Стенография" - "Шифрование".

В папке проекта располагается файл sample.txt с информацией для шифрования и start.bmp в качестве примера изображения. 
Название результирующего файла - переменное.

Для шифрования необходимо выбрать <b>степень шифрования</b>, <b>текстовый документ</b> с исходным текстом, <b>графический файл</b> , в который "закрывается" информация.
Важным параметром является степень шифрования, которая означает количество используемых битов в каждом пикселе изображения.
Чем выше степень шифрования, тем сильнее изменяется исходный цвет пикселя.
После выбора всех параметров шифрования, по нажатию кнопки "Шифровать", генерируется результирующий текстовый файл с сокрытой в изображении информацией. 
При этом файл получает название, состоящее из следующих параметров: степень шифрования, количество фактически зашифрованных символов, время его создания.
Количество фактически зашифрованных символов используется при обратной расшифровке сообщения.
По умолчанию, если пользователь не выбрал в форме параметры, шифруется sample.txt в start.bmp со степенью 1.

###Расшифрование текста из изображения
Процесс обратного расшифрования текстовой информации из изображения запускается из пункта меню "Стенография" - "Расшифрование".

В папке проекта располагается файл result.txt для расшифрования в него информации, 
название файла для расшифровки меняется в зависимости от выбранных параметров и времени его получения программой.

Для расшифрования используется <b>текстовый файл</b>, полученный на этапе шифрования, его легко определить - в названии имеются цифры.
Выбираются параметры, использованные при шифровании: <b>степень шифрования</b> и <b>количество зашифрованных символов</b>.
Кроме того, пользователь указывает текстовый файл, в который сохраняется расшифрованная информация.
По умолчанию, если пользователь не выбрал в форме параметры, расшифровывается 10 символов из файла start.bmp 
в текстовый файл result.txt со степенью шифрования 1.

###Информация  о программе
Пункт меню "О программе" содержит краткую информацию для пользователя о назначении программы и принципах её использования.