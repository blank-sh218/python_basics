# 문자열 포매팅 연습

## 1. 숫자 바로 대입
a = "I eat %d apples." % 3
print(a) # I eat 3 apples.

## 1-1
a = "I eat {0} apples".format(3)
print(a) 

## 2. 문자열 바로 대입
a = "I eat %s apples." % "five"
print(a) # I eat five apples.

## 2-1
a = "I eat {0} apples".format("five")
print(a) # I eat five apples.

## 3. 숫자 값을 나타내는 변수로 대입
number = 3
a = "I eat %d apples." % number
print(a) # I eat 3 apples.

## 4. 2개 이상의 값 넣기
number = 10
day = "three"
a = "I ate %d apples. so I was sick for %s days." % (number, day)
print(a) # I ate 10 apples. so I was sick for three days.

