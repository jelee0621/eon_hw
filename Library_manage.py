import os
class Library_x:   
    def delete_book(self, book_contents):
        for i in range(0, len(book_contents), 1):
            print(i)
            print(book_contents[i])
        delete_num = int(input("삭제할 책의 번호를 고르세요(0 = 취소) : "))
        if delete_num == 0:
            print("취소") #취소
            return book_contents
        else:
            try:
                self.delete_b(book_contents,delete_num)
            except:
                print("삭제 실패")
                self.delete_book(book_contents)
            return book_contents

    def delete_b(self,book_contents,delete_num):
        book_contents.pop(delete_num)
        print("삭제 완료")

    def find_book_name(self,matching_list):
        d_book_info = str(input("찾을 책의 정보를 입력하세요(아무 정보나 입력) : "))
        matching = self.find_book_book(d_book_info,matching_list)
        return matching

    def find_book_kind(self,book_contents):
        d_book_info = str(input("찾을 책의 장르를 입력하세요 : "))
        matching = self.find_book_book(d_book_info,book_contents)
        return matching

    def find_book_book(self, find_text, book_contents):
        matching = []
        for s in book_contents:
            if find_text in s:
                matching.append(s)
        if len(matching) == 0:
            print("검색 실패")
            return matching
        else:
            return matching
    
    def input_list(self,book_contents):
        new_book_List = ' '.join(book_contents)
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'input.txt')
        d = open(my_file,'w')
        d.write(new_book_List)
        d.close()



class book_b:
    def plusmenu(self,book_contents):
        book_name = str(input("추가할 도서의 도서명 저자 출판연도 출판사명 장르를 입력 : "))
        book_b.plusbook(self,book_name,book_contents)
        return (book_contents)
        
    def plusbook(self,book_name,book_contents):
        print(book_name)
        a = int(input("추가하시려면 1을 눌러주세요 (다른걸 누르면 취소): "))
        if a == 1:
           book_contents.append(book_name+'\n')
           print("추가완료")
           for i in range (len(book_contents)):
               print (i)
               print (book_contents[i])
        else:
            print("취소")

    def fixmenu(self,book_contents):
        for i in range(0, len(book_contents), 1):
            print(i)
            print(book_contents[i])
        a = int(input("수정할 책의 번호를 고르세요 : "))
        self.fix_book(book_contents, a)
        return (book_contents)

    def fix_book(self,book_contents, book_num):
        fix_temp = str(input("수정할 도서의 도서명 저자 출판연도 출판사명 장르를 입력하세요 : "))
        book_contents.pop(book_num)
        book_contents.append(fix_temp + '\n')
        print(book_contents)
        print("수정완료.")