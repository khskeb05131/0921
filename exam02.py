a = int(input("숫자 입력 :")) #input은 입력을 문자열로 인식함

if a % 2 == 0:
    print("{}는 짝수입니다.".format(a))
else:
    print("{}는 홀수입니다.".format(a))