import copy

try:
    f = open("C:/Users/ADmin/Desktop/eonhw/TrainList.txt", 'r')  
    TrainList = []
    indlist = []

    while True:
        tl = f.readline().split()
        if not tl: break
        TrainList.append(tl)
except FileNotFoundError:
    print("열차정보 파일이 존재하지 않습니다.")
    exit()
finally:
    f.close()

# 첫줄 삭제
del TrainList[0]

# 열차정보 리스트 복사
modyTrainList = copy.deepcopy(TrainList)
reservation_list = []
ind = None

for i in range(20):  # 열차정보 개수만큼 반복
    del modyTrainList[i][2] # -> 삭제
    modyTrainList[i][0] = modyTrainList[i][0].replace(":", "") # : 문자열 제거
    modyTrainList[i][0] = int(modyTrainList[i][0]) # 시간정보 문자열를 숫자형으로 형변환


def close_time(my_time, time_list):  # 가까운 시간 찾기
    mt = my_time # 예매시간
    tl = time_list.copy() # 시간 리스트
    real_time_list = [605, 635, 715, 842] # 열차시간(분으로 환산한 시간이 아님)
    gap_list = [] # 예매시간과 열차시간의 시간차(분)
    for i in range(len(tl)):
        gap_list.append(abs(mt - tl[i]))
    idx = gap_list.index(min(gap_list)) # 시간차 리스트에서 최소값을 찾고, 해당 최소값의 인덱스를 찾음
    return real_time_list[idx] # 인덱스를 사용해서 열차시간 리턴


class TRAIN:
    def menu1(self):  # 기차 검색 , 예매
        des_train = list(input(
            "\n====== 원하는 시간(YY:MM), 출발역, 도착역, 열차종류 입력 ('빈칸'으로 구분) ======\n※ 뒤로가기 : 아무키 입력 ※\n※  입력이 잘못되면 뒤로갑니다 ※\n입력 : ").split())
        tmp_TrainList = copy.deepcopy(modyTrainList)

        for i in range(20):
            tmp_TrainList[i].pop()

        # 열차시간을 분으로 환산한 리스트
        time_list = [365, 395, 435, 522]

        # 예매시간에서 : 제거
        tmp_mytime = int(des_train[0].replace(":", ""))
        a, b = divmod(tmp_mytime, 100)  # a,b 몫, 나머지
        mytime = a * 60 + b
        des_train[0] = close_time(mytime, time_list)
        closed_T = []

        for i in range(20):
            if tmp_TrainList[i] == des_train:
                closed_T = tmp_TrainList[i].copy()
                closed_T.append(TrainList[i][5])
                ind = i
                print('\n===== 가장 가까운 시간의 기차 정보 =====\n|  시간  | 출발 | 도착 | 열차종류 | 잔여석 수 |')

        # 숫자 시간을 다시 시:분으로 표현
        a, b = divmod(closed_T[0], 100)
        a = str(a)
        b = str(b)
        if int(b) // 10 == 0:
            closed_T[0] = ''.join(['0', a, ':', '0', b])
        else:
            closed_T[0] = ''.join(['0', a, ':', b])
        print('|', end=' ')
        for a in closed_T:
            print(a, end=' | ')

        while True:
            reservation = input('\n해당 기차표를 예매하시겠습니까? [Y/N]\n입력 : ')
            if reservation == 'Y':
                if TrainList[ind][5] != '매진':
                    reservation_list.append(TrainList[ind])
                    TrainList[ind][5] = int(TrainList[ind][5]) - 1  # 예매를 완료하면 표를 하나 줄여나간다
                    print('\n예매가 완료되었습니다.')
                    indlist.append(ind)
                    if TrainList[ind][5] == 0:  # 남아있는 표의 수가 0이 되면
                        TrainList[ind][5] = '매진'  # 매진
                    break
                else:
                    print('\n해당 표는 매진되었습니다. 초기메뉴로 돌아갑니다.')
                    break
            elif reservation == 'N':  # 예매하지 않음
                print('\n처음 화면으로 돌아갑니다.')
                break
            else:
                print('Y 또는 N을 입력해주세요.')
        return ind

    def menu2(self):  # 전체 기차리스트를 출력
        print('\n= 기차 시간표 =', '시간_출발_도착_열차종류_잔여좌석수', '--', sep='\n')
        i = 0
        while i < len(TrainList):
            a, b, c, d, e, f = TrainList[i]
            print(a, b, c, d, e, f)
            i += 1

    def menu3(self):
        if ind == None:  # 예매내역 없음
            print('\n예매된 기차가 없습니다.')
        elif reservation_list == []:
            print('\n예매된 기차가 없습니다.')
        else:
            print('\n[ 예매 완료 ]\n', '======== 기차 정보 ========', sep='\n')
            i = 0
            while i < len(reservation_list):
                a, b, c, d, e, f = reservation_list[i]
                print(a, b, c, d, e)  # 예약된 순번까지 하나씩 프린트
                i += 1
            cancle = input('\n예매를 취소하시겠습니까? [Y/N]\n※ 뒤로가기 : 아무키나 입력 ※\n입력 : ')
            if cancle == 'Y':
                if TrainList[indlist[len(indlist) - 1]][5] == '매진':
                    TrainList[indlist[len(indlist) - 1]][5] = 1
                    reservation_list.pop()
                else:
                    TrainList[indlist[len(indlist) - 1]][5] = TrainList[indlist[len(indlist) - 1]][5] + 1  # 취소되어 표 증가
                    reservation_list.pop()
                indlist.pop()
                print('\n취소가 완료되었습니다.')
            else:
                print('\n처음 화면으로 돌아갑니다.')


while True:
    print('\n======메뉴======')
    print('1. 빠른시간 기차 검색 및 예매')
    print('2. 전체 기차 리스트 출력')
    print('3. 나의 예매 현황 출력 및 예매 취소')
    print('4. 프로그램 종료')

    number = input("수를 입려해 주세요 ")
    train = TRAIN()
    try:
        if number == '1':
            ind = train.menu1()
        elif number == '2':
            train.menu2()
        elif number == '3':
            train.menu3()
        elif number == '4':
            print('프로그램을 종료합니다.')
            break
        elif number == '5':
            number = 5
            print('최상위 메뉴입니다.')
        else:
            print('없는 메뉴 번호입니다.')
    except:
        print('처음 화면으로 돌아갑니다.')