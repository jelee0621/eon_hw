import Library_manage
import os

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
        selected_menu = int(input("메뉴를 선택하세요:"))

        if selected_menu == 1:
            book_list = self.book_class.plusmenu(book_contents)
            self.menu(book_contents)

        elif selected_menu == 2:
            matching_list = self.Library_class.find_book_kind(book_contents)
            if len(matching_list) == 0:
                print("일치하는 장르의 책이 없습니다.")
            else:
                i=0
                while i < len(matching_list):
                    print(matching_list[i])
                    i+=1
            find_book = self.Library_class.find_book_author(matching_list)
            if len(find_book) == 0: #일치하는 길이가 0일때, 일치x
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
                print(book_contents[i])
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

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'input.txt')
f = open(my_file,'r')
book_contents = f.readlines()
a = user1()
a.menu(book_contents)