class books:
    def __init__(self, chapter_1, chapter_2, chapter_3):
        self.chapter_1 = chapter_1
        self.chapter_2 = chapter_2
        self.chapter_3 = chapter_3

    def say_chapters(self):
        print('В первой главе рассказывается о ' + self.chapter_1)
        print('Во второй главе рассказывается о ' + self.chapter_2)
        print('В третьей главе рассказывается о ' + self.chapter_3)

class part_2_books(books):
    def __init__(self, chapter_1, chapter_2, chapter_3, chapter_1_p2, chapter_2_p2, chapter_3_p2):
        super().__init__(chapter_1, chapter_2, chapter_3)
        self.chapter_1_p2 = chapter_1_p2
        self.chapter_2_p2 = chapter_2_p2
        self.chapter_3_p2 = chapter_3_p2

    def say_p2_chapters(self):
        print('В четвертой главе рассказывается о ' + self.chapter_1_p2)
        print('В пятой главе рассказывается о ' + self.chapter_2_p2)
        print('В шестой главе рассказывается о ' + self.chapter_3_p2)

arkanum_books = part_2_books('поездке сусликов в Чехию',  'войне за бублики в столовке', 'том, как бургер кинг стал лучше макональдса', 'жоской битве двух арабов', 'Чечня на связи', 'Даирбек дышит')
print('Серия книг BRUH:')
arkanum_books.say_chapters()
arkanum_books.say_p2_chapters()

