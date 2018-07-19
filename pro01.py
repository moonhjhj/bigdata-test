# def bank_program():
balance = 0
print("---------------------------------")
print(" 1.예금 | 2.출금 | 3.잔고 | 4.종료")
print("---------------------------------")
# flag = true
while True:
    select_no = int(input("선택>"))
    if select_no == 1:
        deposit = int(input("예금액>"))
        balance = balance + deposit
    elif select_no == 2:
        withdraw = int(input("출금액>"))
        balance = balance - withdraw
    elif select_no == 3:
        print(balance)
    elif select_no == 4:
        # exit()
        print("프로그램 종료")
        break
    else :

        print("다시 입력해주세요")




# bank_program()