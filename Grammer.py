#한줄 주석은 #한개

"""
여러줄
주석은
큰따옴표 또는 작은따옴표
3개
"""

'''
변수
타입별로 변수 키워드는 없다. 데이터를 저장한 변수를 어떻게 부를지만 존재한다. : 변수이름 = 데이터
변수명은 일반적으로 소문자로 시작한다. 특수문자나 숫자로 시작할 수 없다.
부울리안 참 거짓은 첫 문자가 대문자인 True / False 이다.

정수
메모리가 허용하는 한도에서 무한크기로 사용가능. 
정수 변수하나에 담을 수 있는 크기가 42억 이상(메모리가 허용한다면)

실수
8바이트 내에서 사용가능
8바이트 이후 데이터는 손실됨(부분손실)
ex) 1.2345678901234567     => 1.2345678901234567
    1.2345678901234567890  => 1.2345678901234567

문자 
문자/문자열 , 큰따옴표/작은따옴표 구분하지 않는다.
'''

myInt = 1234

myStr = 'Hello Python'

myFloat = 3.14

myChar = 'a'

myBool = True

myBool2 = False

"""
print 함수
"""
print('================ print함수 ================')
print(myInt)

print("myInt = ", myInt)

print('myInt = ', myInt)

"""
계산
초기화 부분에서 바로 계산한다.
+, -, *, /, % 동일
//연산자 => 몫만 구하는 연산
"""
print('================ 계산 ================')
myCal = 10 + 10
myCal2 = 30 // 3
print('덧셈 연산 : ', myCal)
print('몫만 구하는 연산 : ', myCal2)
"""
type 함수 
변수의 데이터 타입을 반환한다.
"""
print('================ type함수 ================')
print('Int type = ', type(myInt))

"""
형변환
서로 다른 타입은 합해지지 않는다.
알파벳은 숫자로 변환되지 않는다. 아스키 코드 적용되지 않음.

print(myInt + myStr) -> error
myStr = 'Hello Python'
print(int(myStr)) -> error

int() -> 문자를 정수로 변환하는 함수
str() -> 정수를 문자로 변환하는 함수

"""
print('================ 형변환 ================')
mystr1 = 'hello'
myChar2 = '123'
myInt2 = 456
#문자 -> 정수
print(int(myChar2))
#정수 -> 문자
print(str(myInt))

print(int(myChar2) + myInt2)

print(myChar2 + str(myInt2))
#리스트->튜플
print(tuple([1, 2]))
#튜플->리스트
print(list((1, 2)))
#리스트->집합
print(set([1,2]))
#집합->리스트
print(list({1,2}))
#리스트->딕셔너리 , 키:밸류 쌍으로 이루어져야 함
print(dict([[1,2], [3,4]]))
print(dict([[1,2]]))

"""
리스트 []
리스트 길이 반환 : len(리스트)
리스트 요소 추가 : 리스트.append(데이터) , 마지막에 추가됨
리스트 요소 삭제 : 리스트.pop()-> 마지막 삭제 , 리스트.pop(3) -> 인덱스 3 삭제 , 스택 팝과 같은 기능, 리스트에서 삭제 후 값 반환
리스트 연장 : 리스트.extend([ 리스트 내용 ]) 리스트 덧셈
데이터 삽입 : 리스트.insert(인덱스, 데이터)
특정 데이터 삭제 : 리스트.remove(데이터)
전체 데이터 삭제 : 리스트.clear()
데이터 정렬 : 리스트.sort(reverse=False) : 오름차순(생략가능) , 리스트.sort(reverse=True) : 내림차순
데이터 역순 : 리스트.reverse()
데이터 슬라이싱 : 리스트[1:3]

"""
students = ['홍길동', "오용석", '장영실', 123, 3.14, -1, True, False]
print('================ 리스트 ================')
print('요소 하나 출력 : ', students[0])
print('전체 출력 : ', students)
print('길이 출력 : ', len(students))

#수정 작업은 함수내에서 사용 불가한 것 같다.
students.append('추가됨!')
print('요소추가 : ', students)
print('기본 삭제 반환 값: ', students.pop())
print('기본 삭제 후 상태', students)

students.insert(0, '인덱스0 삽입')
print('인덱스 삽입 : ', students)

students.extend(['연장1', '연장2', '연장3'])
print('리스트 연장 : ', students)

students.remove('인덱스0 삽입')
print('특정 데이터 삭제 : ', students)

students.clear()
print('전체 데이터 삭제 : ', students)

list = [4, 3, 2, 1]

list.sort()
print('리스트 오름차순 정렬 : ', list)
list.sort(reverse=True)
print('리스트 내림차순 정렬 : ', list)

list.reverse()
print('리스트 역순 : ', list)
#슬라이싱 [ 인덱스부터 : 인덱스 앞까지(해당 인덱스는 포함되지 않음) ]
print('리스트 슬라이싱 : ', list[0:0])
print('리스트 슬라이싱 : ', list[0:1])
print('리스트 슬라이싱 : ', list[:4])
print('리스트 슬라이싱 : ', list[1:3])

"""
튜플  ()
리스트와 같은 구조이지만 수정이 불가능한 자료형, 참조용도
튜플 길이 : len
튜플 결합 : +
튜플 슬라이싱 : [n:m]
튜플 인덱스 검색 : index(찾고자하는 데이터) 인덱스 값 반환
튜플 포함 데이터 갯수 : count()
"""
print('================ 튜플 ================')
readOnly = (1, 2, 3, 4, 4, 4)

print('결합 : ', readOnly + ('a', 'b', 'c'))
print('길이 : ', len(readOnly))
print('슬라이싱 : ', readOnly[0:1])
print('인덱스 : ', readOnly.index(4)) #존재하는 데이터 중 처음으로 발견된 인덱스 반환
print('데이터 갯수 : ', readOnly.count(4))

"""
딕셔너리 (해시)  {}
키:밸류 로 구성됨 
키중복을 허용하지 않음

길이 : len(딕셔너리)
참조 : 딕셔너리[키값]
삭제 : del 딕셔너리[키값]
"""
print('================ 딕셔너리 ================')
dictionary1 = {10:'a', 20:'b', 30:'c', 40:'d'}
dictionary2 = {'a', 'b', 'c', 'd'}
print('길이 : ', len(dictionary1))
print('참조 : ', dictionary1[10])
#키설정을 해두지 않으면 전체 참조만 가능
print('참조 : ', dictionary2)

del dictionary1[10]
print('삭제 : ', dictionary1)

"""
비교연산자

비교연산 시에는 문자/문자열 을 아스키코드 값으로 비교한다. 형변환과 다름.

논리연산자
xor은 존재하지 않는다.

"""
print('================ 비교연산자 ================')
num1 = 10
num2 = 20

print(num1 >= num2)
print('a' >= 'b')
print('abc' == 'cba')
print('abc' == 'abc')

print('================ 논리연산자 ================')
print(True and True)
print(True or False)
print(not False)
print((3>1) and (5>3))

"""
조건문
if(조건문) :
    내용
반드시 if문 다음줄에 들여쓰기를 해야만 적용된다.
else if는 elif 로 쓴다.

"""
print('================ 조건문 ================')
num3 = 10
num4 = 20
score = 10
if(num3 < num4) :
    print('{0} < {1}'.format(num3, num4))

if(score >= 90) :
    print('수')
elif(score >= 80) :
    print('우')
elif (score >= 70) :
    print('미')
else :
    print('가')

"""
반복문
for
for문에서 사용되는 i는 foreach와 비슷하게 사용된다.
또한 for문에서 사용되는 i는 지역변수 i이다.
밖에서 따로 생성한 변수 i와 다른 변수이다.
foreach(Object o : Object Set)

들여쓰기된 문장들이 같이 반복된다.
들여쓰기가 끝나는 시점이 반복 한번이 끝나는 시점

range문
range(시작, 끝, 단계)
ex) range(1, 10, 2) -> 1부터 10까지 진행하면서 단계마다 실행
= 1, 3, 5, 7, 9 

while문
while 조건문 :
    반복내용

break, continue 존재



"""

print('================ 반복문 ================')

list = ['a', 'hello', 3, -4, 5.0]
tuple = ('a', 'hello', 3, -4, 5.0)
dictionary3 = {10:'홍길동', '장영실': 20, -3:30, 6:40}
i = 123547
print('== for == ')
for i in list :
    print(i)
for i in tuple :
    print(i)
for i in dictionary3 :
    print('key :', i)
    print('value : ', dictionary3[i])

    print('키 : {0}, 밸류 : {1}'.format(i, dictionary3[i]))
print('== range == ')
for i in range(10) :
    print(i)
print(' ')
for i in range(1, 10, 2) :
    print(i)

count = 0
target = 100
sum = 0
print('== while == ')
while count <= target :
    sum += count
    count += 1
print('sum : ', sum)

print('== continue == ')
for i in range(10) :
    if(i % 2 == 0) :
        continue
    print(i)
print('== break == ')
for i in range(10) :
    if(i > 5) :
        break;
    print(i)

"""
함수

def 함수명 (매개변수) :
    내용
    내용
    return 내용 -> (끝)
함수명(매개변수) -> 함수 사용

매개변수는 지역변수 = 함수내에서만 사용가능
함수 밖 변수 = 전역변수 
다른언어와 지역 전역 변수간 규칙 동일함.
함수 내에 같은 이름 => 지역변수 우선 사용
없으면 전역변수 사용

반드시 return값을 할당할 필요 없음
return 키워드가 함수 내에 있어도
void 함수처럼 사용할 수 있음

"""
def addFunc(x, y) :
    print('in addFunc : ', x, y)
    return x+y
result = addFunc(1, 3)
print('result addFunc: ', result)

def isglobal() :
    result = 'no'
    print('global var?: ', result)
    print('this is voidFunc')
isglobal()

result = 'yes'
def islocal() :
    print('global var?: ', result)
islocal()
"""
클래스
클래스 이름은 일반적으로 대문자로 시작한다.
속성 :  def __init__() 메서드에 정의한다.
기능 : 함수와 동일하게 정의한다.

"""
class Bike :
    def __init__(self):
        self.color = 'black'
        self.weight = 3
    def sell(self):
        print('sell')
    def drive(self):
        print('drive')
    def brake(self):
        print('brake')
    def gear(self):
        print('gear')
myBike = Bike()
friendBike = Bike()
myBike.color = 'red'
print(myBike.color)
print(myBike.drive()) # drive함수 실행 후 아무것도 없고 아무것도 없는데 출력하려해서 none이 출력됨
myBike.brake()


