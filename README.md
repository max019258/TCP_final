# TCP-IP_project
Title: O<br>
학번이름 : 201744080 박중원<br>

채팅 기능을 이용하여 숫자야구 프로그램을 구현 <br>
<br>
 (개요, 목적, 설계 및 기능, 차이점등, 실행화면 이미지)

사용기능 및 언어 <br>
1.Python <br>
2.GUI <br>
3.Socket 통신 <br>
4.멀티 쓰레드

개요 <br>
1. 기존 채팅방 기능에서 숫자야구 맞추는 기능을 추가함 <br>
<br>
2. 숫자야구 숫자는 서버에서 랜덤으로 값을 정합니다.<br>
<br>
3. 맨 처음 입력하는 것은 닉네임 입력<br>
<br>
4. 일반적인 문자열을 치면 일반적인 채팅이 뜨고<br><br>
5. 서로다른 숫자 4자리 입력시 숫자야구를 결과값이 뜸 <br><br>
6. 4스트라이크가 나오면 우승자가 나오고 서버가 종료됨 <br>
![image](https://user-images.githubusercontent.com/71125201/122163666-7eb09600-ceb0-11eb-8678-31d6820d7a30.png)

목적 <br>
-유저 여럿이 들어와서 채팅을 통해 숫자야구를 풀어내는 것



실행화면<br>
처음 클라이언트를 실행했을때의 화면 입니다.<br>
이상태에서 아무것도 입력하지 않고 엔터를 치면 127.0.0.1로 연결됩니다.<br>
(포트는 코드에서 2500으로 설정되었습니다.)<br>
![image](https://user-images.githubusercontent.com/71188378/122154468-0e9a1400-cea0-11eb-860c-1da8f5f07424.png)


서버를 실행하고 한유저가 접속했을때의 상황입니다.유저가 <br>
두명이상일 때만 퀴즈가 시작되기 때문에 한명의 유저는 채팅을 치는 상황입니다.<br>
![image](https://user-images.githubusercontent.com/71188378/122154506-207bb700-cea0-11eb-9168-0267cda186b5.png)

유저 수가 두명이 되자마자 퀴즈가 시작됩니다.<br>
![image](https://user-images.githubusercontent.com/71188378/122154554-34bfb400-cea0-11eb-9682-1dbc76dcef65.png)

<br>'O' , 'X'를 입력하여 정답을 제출할 수 있습니다. <br>
정답입니다 혹은 오답입니다 메세지는 답을 제출한 본인에게만 보여지게끔 설계되었습니다.<br>
다른 유저는 상대가 O 또는 X를 쓴것 만 보입니다. <br>
![image](https://user-images.githubusercontent.com/71188378/122154593-4b660b00-cea0-11eb-9407-f9315624693a.png)

4개의 퀴즈를 풀고난 상황입니다.<br>
퀴즈의 제한시간을 늘려야 한다면 Time.sleep()의 시간을 늘리면 해결됩니다.<br>
![image](https://user-images.githubusercontent.com/71188378/122156150-5ff7d280-cea3-11eb-9c3e-fd744bd3a693.png)
