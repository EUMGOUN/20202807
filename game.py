#딕셔너리, 리스트, 함수
def player(name, age, school):
    print(name, school)
 
player(age=21, name="이름은 Eum", school="지금 다니는 학교는 kit")

game = {'name':'갤러그', 'level':'쉬움', 'ph' : '01075267311'}

print("갤러그 게임 시작")
# 반복시작
for i in range(3) :
    print("적 비행기 발생")
    print("1. 발사 2. 오른쪽이동 3. 왼쪽이동")
    number = input("숫자를 입력하세요: ")
    print("당신의 입력값?", number)
    # 만약에 1번을 누르면 총알 발사
    if number == "1":
        print("총알 발사")
    # 만약에 2번을 누르면 오른쪽
    if number == "2":
        print("오른쪽")
    # 만약에 3번을 누르면 왼쪽
    if number == "3":
        print("왼쪽")



#반복끝