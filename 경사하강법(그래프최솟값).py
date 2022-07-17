import numpy as np #numpy 모듈
import matplotlib.pyplot as plt #plot 모듈
import sympy as sym #sympy 모듈

#여러 값 입력
print("[finding minimum]")
print("추천: x**2/-3/3/1/0.05/1")
IE=input("식:") #입력식
range1=float(input("최소 x범위")) #범위(무작위점,그래프 한정)
range2=float(input("최대 x범위"))
간격=float(input("간격:")) #무작위점 간격
rate=float(input("학습률:")) #학습률
c=int(input("소숫점 표현 정도")) #소숫점 반올림 반환


#최소가능점 리스트 생성
list_x_s=[] #극소가 될 가능성이 있는 x값들
list_y_s=[] #극소값일 수 있는 y값들


# 여러 시작점/끝나면 최소값 출력
for i in range(0,10*10):
  x_s=range1+i*간격 #특정 점 하나씩 일정간격으로 떨어뜨리기
  if x_s>=range2: #무작위점이 range2보다 커지기 전까지 반복
    a=min(list_y_s) #극소값중 가장작은 값->최솟값
    b=list_y_s.index(a) #리스트내 첫번째 최소값의 위치
    print("x값은",list_x_s[b]) #그 위치에(최소값) 대응하는 x값 출력
    print("y값은",a) #y값(최소값) 출력
    print("Please click [show file] and check some graphs")
    break
      

  #미분
  x=sym.Symbol('x') #심볼함수
  de=sym.diff(IE,x) #입력식의 도함수
  DE=str(de) #코드->문자


  #경사하강하고 최소가능점 찾기
  while True:
    x=x_s #eval에 집어넣기 위해 문자 x로 치환
    G=eval(DE) #미분계수
    x_s=x_s-rate*G #경사하강(x_s값 이동)
    x=x_s #eval에 집어넣기 위해 문자 x로 치환
    y_s=eval(IE) #경사하강(x_s에 대응하는 y_s값 이동)
  
    if -0.00001<G<0.00001: #미분계수가 0쯤되는 지점
      list_x_s.append(round(x_s,c)) #극소값의 x값 일수 있는 x_s값 리스트에 추가
      list_y_s.append(round(y_s,c)) #극소값 리스트에 추가
      break

    if range1-0.1<=x_s<=range1+0.1 or range2-0.1<=x_s<=range2+0.1: #범위 끝에 이동정이 닿았을때
      list_x_s.append(round(x_s)) #극소값의 x값 일수 있는 x_s값 리스트에 추가
      list_y_s.append(round(y_s)) #극소값 리스트에 추가
      break


#전체그래프
fig = plt.figure(figsize=(5,5))
x1=np.arange(-50,50,0.2) #넘파이로 -50에서50범위 재배열
x=x1 #eval에 집어넣기 위해 문자 x로 치환
y1=eval(IE) #재배열된 x값을 식에 대입해 대응하는 y값 얻기
plt.plot(x1,y1,c="r",lw=1, label="whole graph") #색:빨강, 두께:0.5, 이름:whole graph

#부분그래프

x1=np.arange(range1,range2+0.2,0.2) #넘파이로 범위내 재배열
x=x1 #eval에 집어넣기 위해 문자 x로 치환
y1=eval(IE) #재배열된 x값을 식에 대입해 대응하는 y값 얻기
plt.xlim(range1-5,range2+5) #그래프 ㅌ범위:(range1-5)~(range2+5)
plt.ylim(a-3,a+15) #그래프 y범위:(최솟값-3)~(최댓값+15)
plt.plot(x1,y1,c='b',lw=3,label="range graph") #색:파랑, 두께:2, 이름:range graph

#최솟값

x = list_x_s[b] #최솟값일떄 x값
y = a #최솟값
plt.scatter(x,y,c="g",s=20, label="min point") #색:초록, 크기:20, 이름:min point

plt.grid() 
plt.legend()
plt.show()