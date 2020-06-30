class book_b:
    def plusmenu(self,book_contents):
        book_name = str(input("추가할 도서의 도서명 저자 출판연도 출판사명 장르 입력 : "))
        book_b.plusbook(self,book_name,book_contents)
        return (book_contents)

    def plusbook(self,book_name,book_contents):
        print(book_name)
        a = int(input("추가하시겠습니까? yes = 1 (다른걸 누르시면 취소됩니다.): "))
        if a == 1: #1 누를 경우
           book_contents.append(book_name+'\n') #추가
           print("추가완료")
           for i in range (len(book_contents)):
               print (i)
               print (book_contents[i])
        else: # 그 외 숫자
            print("취소")

    def fixmenu(self,book_contents):
        for i in range(0, len(book_contents), 1):
            print(i)
            print(book_contents[i]) #입력되어 있는 책 정보 출력
        a = int(input("수정할 책의 번호를 고르세요 : "))
        self.fix_book(book_contents, a)
        return (book_contents)

    def fix_book(self,book_contents, book_num):
        fix_temp = str(input("수정할 도서의 도서명/저자/출판연도/출판사명/장르 입력 : "))
        book_contents.pop(book_num)
        book_contents.append(fix_temp + '\n')
        print(book_contents)
        print("수정되었습니다.") 