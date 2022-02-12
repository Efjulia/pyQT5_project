from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QAction, QFileDialog, QComboBox, \
    QMessageBox, QColorDialog, QTextEdit, QLineEdit
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QMouseEvent, QFont
from PyQt5.QtCore import Qt, QPoint
from functools import partial
import os
import datetime
import sys


# Класс для выбора параметров расшифрования
class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle('Расшифрование')
        self.setMinimumWidth(300)
        self.setMinimumHeight(500)
        # Значения для расшифрования по умолчанию.
        self.count = 1
        self.file_path = 'start.bmp'
        self.file_path2 = 'result.txt'
        self.txt_len = 10
        # управляющие элементы для выбора параметров расшифрования.
        self.combo1 = QComboBox(self)
        self.combo1.setGeometry(50, 50, 200, 50)
        list1 = [
            self.tr('Выбрать степень шифрования'),
            self.tr('Степень шифрования 2'),
            self.tr('Степень шифрования 4'),
            self.tr('Степень шифрования 8'),
        ]
        self.combo1.clear()
        for t in list1:
            self.combo1.addItem(t)
        self.combo1.show()
        # self.statusBar()
        self.combo1.currentIndexChanged.connect(self.index_changed)

        # Выбор файла куда расшифровываем
        self.button = QPushButton(self)
        self.button.setGeometry(50, 150, 200, 50)
        self.button.setText('Выбрать текстовый файл\n для расшифрования')
        self.button.show()
        self.button.clicked.connect(self.find_encrypt_txt)
        #
        # выбор изображения для расшифрования
        self.button2 = QPushButton(self)
        self.button2.setGeometry(50, 250, 200, 50)
        self.button2.setText('Выбрать изображение\n для расшифрования')
        self.button2.show()
        self.button2.clicked.connect(self.find_encrypt_image)
        #
        # Поле ввода длины
        self.pb_txt_len = QLineEdit(self)
        self.pb_txt_len.setGeometry(50, 350, 200, 50)
        self.pb_txt_len.setText('10')
        self.pb_txt_len.show()
        self.pb_txt_len.textChanged[str].connect(self.on_changed)

        #
        # кнопка для запуска расшифрования
        self.button3 = QPushButton(self)
        self.button3.setGeometry(50, 450, 200, 50)
        self.button3.setText('Расшифрование')
        self.button3.show()
        self.button3.clicked.connect(self.encrypt_image)
        # self.button3.clicked.connect(txt_file, input_file_image, output_file_image, count)

    def on_changed(self, text):
        if all([c.isdigit() for c in text]):
            self.txt_len = int(text)
        else:
            self.show_exception(-3)

    # Получаем степень шифрования - расшифрования
    def index_changed(self, index):
        self.count = 2 ** index
        # print(self.count)

    # Процедура для выбора графического файла
    def find_encrypt_image(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, 'Открыть файл', "", 'BMP(*.bmp)')
        if self.file_path == "":
            return
        file_name = self.file_path.split('/')
        # print(self.file_path)
        self.button2.setText("Файл " + file_name[-1] + " выбран")

    # Процедура для выбора текстового файла
    def find_encrypt_txt(self):
        self.file_path2, _ = QFileDialog.getOpenFileName(self, 'Открыть файл', "", 'Text Files (*.txt)')
        if self.file_path2 == "":
            return
        file_name2 = self.file_path2.split('/')
        # print(self.file_path2)
        self.button.setText("Файл " + file_name2[-1] + " выбран")

    # Вызывается функция расшифрования
    def encrypt_image(self):
        # формат вызова Crypt.encrypt('result.txt', 'result7.bmp', 4, 1000)
        result = Crypt.encrypt(self.file_path2, self.file_path, self.count, self.txt_len)
        self.show_exception(result)

        # Проверка исходов работы функции, вывод исключений
    def show_exception(self, result):
        if result == -1:
            self.show_dialog("Степень шифрования должна быть равна 1, 2, 4 или 8")
        elif result == -2:
            self.show_dialog("Слишком длинный текст")
        elif result == -3:
            self.show_dialog
        elif result:
            self.show_dialog("Символов: " + str(result))
        else:
            self.show_dialog("Неизвестная ошибка" + str(result))

    # Вывод сообщений о норм работе и исключениях
    def show_dialog(self, text):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(text)
        msg_box.setWindowTitle("Выполнено")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()


# Класс для выбора параметров шифрования
class Window1(QWidget):
    def __init__(self):
        super(Window1, self).__init__()
        self.setWindowTitle('Шифрование')
        self.setMinimumWidth(300)
        self.setMinimumHeight(500)
        # Значения для шифрования по умолчанию.
        self.count = 1
        self.file_path = 'start.bmp'
        self.file_path2 = 'sample.txt'
        # управляющие элементы для выбора параметров шифрования
        self.combo1 = QComboBox(self)
        self.combo1.setGeometry(50, 50, 200, 50)
        list1 = [
            self.tr('Выбрать степень шифрования'),
            self.tr('Степень шифрования 2'),
            self.tr('Степень шифрования 4'),
            self.tr('Степень шифрования 8'),
        ]
        self.combo1.clear()
        for t in list1:
            self.combo1.addItem(t)
        self.combo1.show()
        self.combo1.currentIndexChanged.connect(self.index_changed)

        self.button = QPushButton(self)
        self.button.setGeometry(50, 150, 200, 50)
        self.button.setText('Выбрать текстовый файл\n для шифрования')
        self.button.show()
        self.button.clicked.connect(self.find_crypt_txt)

        self.button2 = QPushButton(self)
        self.button2.setGeometry(50, 250, 200, 50)
        self.button2.setText('Выбрать изображение\n для шифрования')
        self.button2.show()
        self.button2.clicked.connect(self.find_crypt_image)

        self.button3 = QPushButton(self)
        self.button3.setGeometry(50, 350, 200, 50)
        self.button3.setText('Шифрование')
        self.button3.show()
        self.button3.clicked.connect(self.crypt_image)
        # self.button3.clicked.connect(txt_file, input_file_image, output_file_image, count)

    def index_changed(self, index):
        self.count = 2 ** index
        # print(self.count)

    # Процедура для выбора графического файла - источника
    def find_crypt_image(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, 'Открыть файл', "", 'BMP(*.bmp)')
        if self.file_path == "":
            return
        file_name = self.file_path.split('/')
        # print(self.file_path)
        self.button2.setText("Файл " + file_name[-1] + " выбран")

    # Процедура для выбора текстового файла - источника
    def find_crypt_txt(self):
        self.file_path2, _ = QFileDialog.getOpenFileName(self, 'Открыть файл', "", 'Text Files (*.txt)')
        if self.file_path2 == "":
            return
        file_name2 = self.file_path2.split('/')
        # print(self.file_path2)
        self.button.setText("Файл " + file_name2[-1] + " выбран")

    def crypt_image(self):
        result = Crypt.crypt(self.file_path2, self.file_path, 'result.bmp', self.count)
        # print(result)
        if result == -1:
            self.show_dialog("Степень шифрования должна быть равна 1, 2, 4 или 8")
        elif result == -2:
            self.show_dialog("Слишком длинный текст")
        elif result:
            self.show_dialog("Символов: " + str(result))
        else:
            self.show_dialog("Неизвестная ошибка" + str(result))

    def show_dialog(self, text):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(text)
        msg_box.setWindowTitle("Выполнено")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()


# Гл.форма приложения
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # self.setupUi(self)

        top = 400
        left = 400
        width = 800
        height = 600

        self.setWindowTitle("CryptPaint")
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QIcon('icons/icon program.png'))
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.drawing = False
        self.brush_size = 8
        self.brush_color = Qt.red
        self.lastPoint = QPoint()
        self.about_window = QWidget()
        # текстовка в "О программе"
        self.text_about = "Программа для стеганографического сокрытия текста в изображение и обратного расшифрования." \
                          "Используеются латинские буквы."
        self.text_about_encrypt = "По умолчанию расшифровывается 10 символов из файла start.bmp в текстовый файл" \
                                  " result.txt со степенью шифрования 1"
        self.text_about_crypt = "Сохраните файл перед шифрованием, если Вы этого не сделали, то" \
                                " по умолчанию шифруется sample.txt в start.bmp со степенью 1"
        # данные для создания меню
        menu_items = {'Файл': [{'name': 'Сохранить', 'icon': 'icons/save.png',
                                's_cut': "Ctrl+S", 'act': self.save},
                               {'name': 'Очистить лист', 'icon': 'icons/paper clean.png',
                                's_cut': "Ctrl+C", 'act': self.clear},
                               {'name': 'Ластик', 'icon': 'icons/eraser.png',
                                's_cut': "Ctrl+L", 'act': partial(self.color_pixels, Qt.white)}],
                      'Размер кисти': [
                          {'name': 'Размер 8', 'icon': 'icons/blue 8.png',
                           's_cut': "Ctrl+1", 'act': partial(self.size_pixels, 8)},
                          {'name': 'Размер 10', 'icon': 'icons/red 10.png',
                           's_cut': "Ctrl+2", 'act': partial(self.size_pixels, 10)},
                          {'name': 'Размер 12', 'icon': 'icons/green 12.png',
                           's_cut': "Ctrl+3", 'act': partial(self.size_pixels, 12)},
                          {'name': 'Размер 14', 'icon': 'icons/yellow 14.png',
                           's_cut': "Ctrl+4", 'act': partial(self.size_pixels, 14)}],
                      'Цвет кисти': [
                          {'name': 'Черный', 'icon': 'icons/black pencil.png',
                           's_cut': "Ctrl+V", 'act': partial(self.color_pixels, Qt.black)},
                          {'name': 'Красный', 'icon': 'icons/red pencil.png',
                           's_cut': "Ctrl+R", 'act': partial(self.color_pixels, Qt.red)},
                          {'name': 'Зеленый', 'icon': 'icons/green pencil.png',
                           's_cut': "Ctrl+G", 'act': partial(self.color_pixels, Qt.green)},
                          {'name': 'Желтый', 'icon': 'icons/yellow pencil.png',
                           's_cut': "Ctrl+Y", 'act': partial(self.color_pixels, Qt.yellow)},
                          {'name': 'Синий', 'icon': 'icons/blue pencil.png',
                           's_cut': "Ctrl+B", 'act': partial(self.color_pixels, Qt.blue)}],
                      'Заливка цветом': [
                          {'name': 'Черный', 'icon': 'icons/black bucket.png',
                           's_cut': "Ctrl+T", 'act': partial(self.fore_color, Qt.black)},
                          {'name': 'Красный', 'icon': 'icons/red bucket.png',
                           's_cut': "Ctrl+F", 'act': partial(self.fore_color, Qt.red)},
                          {'name': 'Зеленый', 'icon': 'icons/green bucket.png',
                           's_cut': "Ctrl+A", 'act': partial(self.fore_color, Qt.green)},
                          {'name': 'Желтый', 'icon': 'icons/yellow bucket.png',
                           's_cut': "Ctrl+D", 'act': partial(self.fore_color, Qt.yellow)},
                          {'name': 'Синий', 'icon': 'icons/blue bucket.png',
                           's_cut': "Ctrl+E", 'act': partial(self.fore_color, Qt.blue)},
                          {'name': 'Белый', 'icon': 'icons/white bucket.png',
                           's_cut': "Ctrl+W", 'act': partial(self.fore_color, Qt.white)}],
                      'Фоновое изображение': [
                          {'name': 'Открыть файл', 'icon': 'icons/document-image.png',
                           's_cut': "Ctrl+Q", 'act': self.fore_picture}],
                      'Стеганография': [
                          {'name': 'Шифровать', 'icon': 'icons/sha-256.png',
                           's_cut': "Ctrl+N", 'act': self.crypt_image},
                          {'name': 'Расшифровать', 'icon': 'icons/sha-256(1).png',
                           's_cut': "Ctrl+M", 'act': self.encrypt_image}],
                      'О программе': [
                          {'name': 'Помощь', 'icon': 'icons/blue info.png', 's_cut': "Ctrl+H",
                           'act': partial(self.about, self.text_about)},
                          {'name': 'Про шифрование', 'icon': 'icons/green info.png', 's_cut': "Ctrl+I",
                           'act': partial(self.about, self.text_about_crypt)},
                          {'name': 'Про расшифрование', 'icon': 'icons/red info.png', 's_cut': "Ctrl+J",
                           'act': partial(self.about, self.text_about_encrypt)}]
                      }

        self.build_menu(menu_items)

    # Форма для шифрования
    def show_window_1(self):
        self.win1 = Window1()
        self.win1.show()

    # Форма для расшифрования
    def show_window_2(self):
        self.win2 = Window2()
        self.win2.show()

    # Собираем меню
    def build_menu(self, menu_dict):
        menu_bar = self.menuBar()
        for menu in menu_dict.keys():
            menu_list = menu_bar.addMenu(menu)
            for menu_item in menu_dict[menu]:
                this_menu_item = QAction(QIcon(menu_item['icon']), menu_item['name'], self)
                this_menu_item.setShortcut(menu_item['s_cut'])
                menu_list.addAction(this_menu_item)
                this_menu_item.triggered.connect(menu_item['act'])

    # Обработка события нажатия клавиши мыши
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()
        # Смена цвета кисти через контекстное меню
        if event.buttons() == Qt.RightButton:
            dialog = QColorDialog(self)
            dialog.setCurrentColor(self.brush_color)
            # print(self.brush_color)
            if dialog.exec():
                self.brush_color = dialog.currentColor()
                self.update()

    # Обработка события движения мыши
    def mouseMoveEvent(self, event: QMouseEvent):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    # Обработка события отпускания клавиши мыши
    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False

    # Рисование
    def paintEvent(self, event):
        canvas_painter = QPainter(self)
        canvas_painter.drawImage(self.rect(), self.image, self.image.rect())

    # Диалог для сохранения файла картинки
    def save(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "BMP(*.bmp)")
        if file_path == "":
            return
        self.image.save(file_path)
        file = open(file_path, 'r')
        file.close()
        if not self.image.save(file_path):
            raise Exception('Не удалось сохранить в "{}"'.format(file_path))

    # Обработка нажатия иконки закрытия
    def closeEvent(self, event):
        reply = QMessageBox.warning(self, "Закрытие....", "Файл был изменён\n Хотите сохранить изменения?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            self.save()

    # Смена цвета фона
    def fore_color(self, color_fore):
        self.image.fill(color_fore)
        self.update()

    # Картинка на фон
    def fore_picture(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Открыть файл', "", 'BMP(*.bmp)')
        if file_path == "":
            return
        self.image = QImage(file_path).scaled(self.size())
        self.update()

    # Пока не сделала,через ООП для рисования линии
    def line_draw(self):
        pass

    # Смена размера кисти
    def size_pixels(self, count):
        self.brush_size = count

    # Смена цвета кисти через меню
    def color_pixels(self, color):
        self.brush_color = color

    # Очистка фона
    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    # Вызов формы для выбора параметров шифрования
    def crypt_image(self):
        self.show_window_1()

    # Вызов формы для выбора параметров расшифрования
    def encrypt_image(self):
        self.show_window_2()

    # Вывод инфы "О программе"
    def about(self, text):
        self.about_window.text_b = QTextEdit(self.centralWidget())
        self.about_window.text_b.setWindowTitle("О программе")
        self.about_window.text_b.setGeometry(500, 500, 400, 100)
        font = QFont()
        font.setPixelSize(16)
        self.about_window.text_b.setText(text)
        self.about_window.text_b.setFont(font)
        self.about_window.text_b.show()


# Класс для реализации функций шифрования и расшифрования
class Crypt:
    # Вес информационных битов изображения, которые не шифруются, чтобы не поломать файл
    BEGIN_SIZE = 54

    # Функция шифрования, параметы: текстовый файл, исходный граф.файл,
    #                               результирующий граф.файл, глубина шифрования
    @staticmethod
    def crypt(txt_file, input_file_image, output_file_image, count):
        if count not in [1, 2, 4, 8]:
            # print("Степень шифрования должна быть равна 1, 2, 4 или 8")
            return -1
        # print(txt_file, input_file_image, output_file_image, count)

        text_len = os.stat(txt_file).st_size
        img_len = os.stat(input_file_image).st_size
        current_datetime = datetime.datetime.now()
        str_hour = str(current_datetime.hour)
        str_minute = str(current_datetime.minute)
        # Меняем название итогового файла, новое название содержит: глубину шифрования,
        # длину зашифрованного текста, время создания и название от пользователя.
        # тогда при выборе файла легко взять данные для параметров расшифрования
        output_file_image = str(count) + '_' + str(
            text_len) + '_' + str_hour + "_" + str_minute + "_" + output_file_image
        input_file = open(input_file_image, 'rb')
        output_file = open(output_file_image, 'wb')
        text_file = open(txt_file, 'r')

        if text_len >= img_len * count / 8 - Crypt.BEGIN_SIZE:
            # print("Слишком длинный текст")
            return -2
        # Пропускаем служебные символы,читаем и перезаписываем в результирующий файл без изменений
        bmp_header = input_file.read(Crypt.BEGIN_SIZE)
        output_file.write(bmp_header)
        # Получаем маску для шифрования в зависимости от выбранной глубины шифрования
        text_mask, image_mask = Crypt.count_crypt_mask(count)

        # Пока не кончился текст
        while True:
            txt_sym = text_file.read(1)
            if not txt_sym:
                break
            # Получаем двоичное представление символа
            txt_sym = ord(txt_sym)

            # Для каждого бита изображения читаем, накладываем маску с текстом,
            # записываем в итоговый графический файл
            for _ in range(0, 8, count):
                img_byte = int.from_bytes(input_file.read(1), sys.byteorder) & image_mask
                bits = txt_sym & text_mask
                bits >>= (8 - count)
                img_byte |= bits
                output_file.write(img_byte.to_bytes(1, sys.byteorder))
                txt_sym <<= count
        output_file.write(input_file.read())
        # закрываем файлы
        text_file.close()
        input_file.close()
        output_file.close()
        # print(text_len)
        # возвращаем длину текста для проверки корректности шифрования и расшифрования
        return text_len

    # Функция расшифрования, параметы: итоговый текстовый файл, исходный граф.файл,
    #                                  глубина шифрования, длина зашифрованного текста
    @staticmethod
    def encrypt(txt_file, input_file_image, count, text_len):
        # print("дешифрование")
        # Проверка на значение глубины шифрования
        if count not in [1, 2, 4, 8]:
            # print("Степень шифрования должна быть равна 1, 2, 4 или 8")
            return -1
        img_len = os.stat(input_file_image).st_size
        if text_len >= img_len * count / 8 - Crypt.BEGIN_SIZE:
            # print("Слишком длинный текст")
            return -2
        text_file = open(txt_file, 'w', encoding='utf-8')
        input_file = open(input_file_image, 'rb')

        # Пропускаем служебные символы
        input_file.seek(Crypt.BEGIN_SIZE)

        # Получаем маску для шифрования в зависимости от выбранной глубины шифрования
        text_mask, image_mask = Crypt.count_crypt_mask(count)
        # Накладываем маску на бит изображения
        image_mask = ~image_mask
        count_read = 0

        # Пока не расшифровали весь текст
        while count_read <= text_len:
            txt_sym = 0
            # читаем каждый бит, накладываем маску и сдвигаем для получения итогового символа текста
            for _ in range(0, 8, count):
                img_byte = int.from_bytes(input_file.read(1), sys.byteorder) & image_mask
                txt_sym <<= count
                txt_sym |= img_byte
            # print("Символ {0} {1:c}".format(count_read, txt_sym))
            if chr(txt_sym) == '\n' and len(os.linesep) == 2:
                count_read += 1
                # print(ord(txt_sym))
            count_read += 1
            # расшифровав символ пишем его в файл
            text_file.write(chr(txt_sym))
        # закрываем файлы
        text_file.close()
        input_file.close()
        # возвращаем длину текста для проверки корректности шифрования и расшифрования
        return text_len

    @staticmethod
    def count_crypt_mask(count):
        # Получаем маску для шифрования и расшифрования
        text_mask = 0b11111111
        image_mask = 0b11111111
        # Сдвигаем маску на глубину шифрования
        text_mask <<= (8 - count)
        text_mask %= 256
        image_mask >>= count
        image_mask <<= count
        return text_mask, image_mask


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m_window = MainWindow()
    m_window.show()
    sys.exit(app.exec_())
