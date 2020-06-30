
import Library_manage
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'input.txt')
f = open(my_file,'r')

class user1:
    def __init__(self):
        self.book_class = Library_manage.book_b()
        self.Library_class = Library_manage.Library_x()

    def menu(self,book_contents):
        print("1. 도서추가")
        print("2. 도서검색")
        print("3. 도서 정보 수정")
        print("4. 도서삭제")
        print("5. 도서 목록 출력")
        print("6. 저장")
        print("7. 종료")
        selected_menu = int(input("메뉴를 선택하세요:")) #1-7중 선택

        if selected_menu == 1:
            book_Contents = self.book_class.plusbook(book_contents)
            self.menu(book_contents)

        elif selected_menu == 2:
            matching_list = self.Library_class.find_book_kind(book_contents)
            if len(matching_list) == 0: #입력 내용과 비교하여 일치하는 부분이없을 때(0일 경우)
                print("일치하는 책이 없습니다.")
            else:
                for i in range(0, len(matching_list), 1):
                    print(i)
                    print(matching_list[i]) #일치하는 값에 해당하는 도서 정보 출력
            find_book = self.Library_class.find_book_name(matching_list)
            if len(find_book) == 0:
                print("일치하는 책이 없습니다.")
            else:
                for i in range(0, len(find_book), 1):
                    print(i)
                    print(find_book[i])
            self.menu(book_contents)

        elif selected_menu == 3:
            book_contents = self.book_class.fixmenu(book_contents)
            self.menu(book_contents)

        elif selected_menu == 4:
            book_contents = self.Library_class.delete_book(book_contents)
            self.menu(book_contents)

        elif selected_menu == 5:
            for i in range(0, len(book_contents), 1):
                print(i)
                print(book_contents[i]) #저장된 도서 정보 출력
            self.menu(book_contents)

        elif selected_menu == 6:
            self.Library_class.input_list(book_contents)
            print("저장완료")
            self.menu(book_contents)

        elif selected_menu == 7:
            self.Library_class.input_list(book_contents)
            print("종료합니다")
        else:
            print("1~7사이의 값을 입력하세요.")
            self.menu(book_contents)


book_contents = f.readlines()
a = user1()
a.menu(book_contents)  