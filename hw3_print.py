document_num = int(input("작업 문서의 수 : ")) 
wokrk_num = int(input("작업번호 : ")) 
priority = list(map(int,input("우선순위 ").split())) 

print_num = list(range(len(priority))) 
time_count = 0 

while True : 
    if priority[0] == max(priority): 
        time_count+=1 #시간 증가
        if print_num[0] == wokrk_num: 
            print(time_count, "분") 
            break 
        else : 
            priority.pop(0) #제거
            print_num.pop(0) 
    else: 
        priority.append(priority.pop(0)) #뒤에넣어준다.
        print_num.append(print_num.pop(0)) 
