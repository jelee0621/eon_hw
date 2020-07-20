import os
class TUSHUGUAN:   
    def delete_book(self, book_List):
        i = 1
        while i < len(book_List):
            print(i,book_List[i])
            i += 1
        delete_num = int(input("삭제할 책의 번호를 고르세요(취소하시려면 00) : "))
        if delete_num == 00:
            print("취소")
            return book_List
        else:
            try:
                self.delete_b(book_List,delete_num)
            except:
                print("삭제 실패")
                self.delete_book(book_List)
            return book_List

    def delete_b(self,book_List,delete_num):
        book_List.pop(delete_num)
        print("삭제 완료")


    def find_book_genere(self,book_List):
        d_book_info = str(input("write down genere of the book : "))
        matching = self.find_book_book(d_book_info,book_List)
        return matching

    def find_book_author(self,book_contents):
        d_book_info = str(input("write down author of the book : "))
        matching = self.find_book_book(d_book_info,book_contents)
        return matching        

    def find_book_book(self, find_text, book_List):
        matching = []
        for s in book_List:
            if find_text in s:
                matching.append(s)
        if len(matching) == 0:
            print("fail")
            return matching
        else:
            return matching
    
    def input_list(self,book_List):
        new_book_List = ' '.join(book_List)
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'input.txt')
        d = open(my_file,'w')
        d.write(new_book_List)
        d.close()


class book_b:
    def plusmenu(self,book_List):
        book_name = str(input("추가할 도서의 도서명 저자 출판연도 출판사명 장르 입력 : "))
        book_b.plusbook(self,book_name,book_List)
        return (book_List)
        
    def plusbook(self,book_name,book_List):
        print(book_name)
        a = int(input("추가하시려면 1을 눌러주세요: "))
        if a == 1:
           book_List.append(book_name+'\n')
           print("추가완료")
           for i in range (len(book_List)):
               print (i, book_List[i])

        else:
            print("취소")

    def fixmenu(self,book_List):
        i=1
        while i<len(book_List):
            print(i, book_List[i])
            i+=1
        a = int(input("수정할 책의 번호를 고르세요 : "))
        self.fix_book(book_List, a)
        return (book_List)

    def fix_book(self,book_List, book_num):
        fix_temp = str(input("수정할 도서의 도서명 저자 출판연도 출판사명 장르를 입력 : "))
        book_List.pop(book_num)
        book_List.append(fix_temp + '\n')
        print(book_List)
        print("수정.")