# TCP-IP_project
Title: 숫자야구 프로그램<br>
학번이름 : 201744080 박중원<br>

채팅 기능을 이용하여 숫자야구 프로그램을 구현 <br>
<br>
 (개요, 목적, 설계 및 기능, 차이점등, 실행화면 이미지)<br>
 
 
목적 <br>
-유저 여럿이 들어와서 채팅을 통해 숫자야구를 풀어내는 것<br>

교안에 있는 내용과 차이점 <br>
GUI를 이용하여 상대방이 보낸 내용과 내가 보낸 내용을 한눈에 구별이 가능하며 숫자야구 기능을 추가하였다.<br.

사용기능 및 언어 <br>
1.Python <br>
2.GUI <br>
3.Socket 통신 <br>
4.멀티 쓰레드

기능 <br>
1. 기존 채팅방 기능에서 숫자야구 맞추는 기능을 추가함 <br>
2. 숫자야구 숫자는 서버에서 랜덤으로 값을 정합니다.<br>
<br>
3. 맨 처음 입력하는 것은 닉네임 입력<br>
<br>
5. 일반적인 문자열을 치면 일반적인 채팅이 뜨고<br>
<br>
6. 서로다른 숫자 4자리 입력시 숫자야구를 결과값이 뜸 <br>
<br>
7. 4스트라이크가 나오면 우승자가 나오고 서버가 종료됨 <br>

구현화면 <br>
1. 초기화면(설명) <br>
![image](https://user-images.githubusercontent.com/71125201/122163666-7eb09600-ceb0-11eb-8678-31d6820d7a30.png)<br>
2. 각클라이언트가 박중원 박성원을 입력 하여 닉네임 등록(왼쪽: 박중원 오른쪽: 박성원)<br> 
![image](https://user-images.githubusercontent.com/71125201/122165706-8de51300-ceb3-11eb-99bc-85af92142c0c.png)
<br>
3. 일반적인 채팅 입력시 화면<br>
![image](https://user-images.githubusercontent.com/71125201/122165829-ba009400-ceb3-11eb-9d89-9fde36757832.png)
<br>
5. 서로다른 숫자 4자리 입력시 숫자야구 결과 출력<br>
![image](https://user-images.githubusercontent.com/71125201/122166065-08159780-ceb4-11eb-89f3-56806a78dc91.png)
<br>

6. 겹치는 숫자 4자리 입력시 일반적인 채팅<br>
![image](https://user-images.githubusercontent.com/71125201/122166278-562a9b00-ceb4-11eb-98e4-33f3262acd7c.png)
<br>
7. 4스트라이크가 나오면 우승자가 나오고 서버가 종료됨 <br>
![image](https://user-images.githubusercontent.com/71125201/122166635-dc46e180-ceb4-11eb-905f-e59aa3b53664.png)





