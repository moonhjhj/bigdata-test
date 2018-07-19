# num = int(input("숫자를 , 로 구분하여 입력하세요"))


def average_num():
    num = list(map(int, input("숫자를 ,로 구분하여 입력하세요").split(",")))
    # print(num)
    print("평균은", sum(num)/len(num), "입니다.")

average_num()