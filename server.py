import socket, threading
import random
import sys


def isNumber(s): #숫자로 바꿀수있는지 여부를 아는 함수
    try:
        int(s)
        return True
    except ValueError:
        return False


class Room:  # 채팅방 클래스 선언
    def __init__(self):
        self.clients = [] #채팅방 클라이언트 리스트 생성
        self.allChat=None #

    def addClient(self, c):  # c: 텔레마케터 . 클라이언트 1명씩 전담하는 쓰레드
        self.clients.append(c) #리스트에 쓰레드를 올림

    def delClient(self, c):
        self.clients.remove(c) #리스트에 쓰레드 제거

    def sendMsgAll(self, msg):  # 채팅방에 있는 모든 사람(클라이언트)한테 메시지 전송
        for i in self.clients: #클라이언트 리스트들을 i에 넣어서 반복
            print(i)    # 넣은 i값(클라이언트 리스트원소)를 출력
            i.sendMsg(msg)  #해당 클라이언트에게 메시지 전송


class ChatClient:  # 클라이언트 클래스 선언
    def __init__(self, r, soc ,nb):
        self.room = r  # 채팅방. romm
        self.id = None  # 사용자 id
        self.soc = soc  # 사용자와 1:1 통신할 소켓
        self.nb=numberBaseball() #숫자야구 객체선언
        #self.nb.computer=nb #숫자야구 배열
        self.nb.computer = [1,2,3,4]  # 숫자야구 배열

    def readMsg(self): # 메시지 읽어들이기
        self.id = self.soc.recv(1024).decode() # 해당 클라이언트의 소켓의 데이터를 받고 문자열로 변환하기 위해 디코딩하여 id에 저장
        msg = self.id + '님이 입장하셨습니다' # msg = 사용자 id + 님이 입장하셨습니다.
        self.room.sendMsgAll(msg) # 클라이언트의 채팅방에있는 모든 사람들에게 메시지 전송

        while True: #무한 반복
            msg = self.soc.recv(1024).decode()  # 사용자가 전송한 메시지 읽음
            listMsg = list(msg) #msg 한글자씩 리스트에 넣기
            trueCnt = 0 #Ture개수
            falseCnt = 0 #Flse개수
            result='' #result는 스트라이크 볼 아웃 여부 결과 문자열
            overlapCnt=0 #중복개수

            for i in listMsg: #리스트Msg를 i에 넣고 반복
                if isNumber(i) == True: # i를 숫자로 바꿀수 있으면
                    trueCnt += 1 # 1증가
                else: #아니면
                    falseCnt += 1  #1증가

            if msg == '종료':  # 종료 메시지이면
                self.soc.sendall(msg)  # 이 메시지를 보낸 한명에게만 전송
                self.room.delClient(self) # 채팅방에서 해당 클라이언트를 삭제
                break #루프 종료
            elif trueCnt==4 and falseCnt==0 :#숫자개수 4개, 나머지타입이 0개이면
                for i in range(len(listMsg)): #litMsg길이만큼 반복
                    listMsg[i]=int(listMsg[i]) #리스트 원소들 int형으로 전환

                for i in listMsg:
                    for j in listMsg:
                        if i==j:
                            overlapCnt+=1
                if overlapCnt==4:
                    result='\n '+msg+' ='+self.nb.matchBaseball(listMsg) # 스트라이크 아웃 볼 여부 반환

            msg = self.id+' : '+ msg + result# 사용자 id : 입력한 내용
            if self.nb.matchBaseball(listMsg) == ' strike : 4/ ball : 0':  # 만약 4스트라이크면
                msg+='\n 축하합니다.'+str(self.id)+'님이 우승하셨습니다.\n 서버를 종료합니다.'
                self.room.sendMsgAll(msg)  # 모든 사용자에 메시지 전송
                quit() #강제종료

            self.room.sendMsgAll(msg)  # 모든 사용자에 메시지 전송


        self.room.sendMsgAll(self.id + '님이 퇴장하셨습니다.') # ~~가 퇴장했다고 알림

    def sendMsg(self, msg): #메시지 보내는 함수
        print(type(msg)) #msg 타입 확인해보기
        self.soc.sendall(msg.encode(encoding='utf-8'))  #이 메시지를 보낸 클라이언트 에게 인코딩하여 보냄


class ChatServer: #채팅 서버 선언
    ip = 'localhost'  # or 본인 ip or 127.0.0.1
    port = 8082 # 포트를 8082지정

    def __init__(self):
        self.server_soc = None  # 서버 소켓
        self.room = Room() #  # 해당 서버.room = Room 객체

    def open(self):
        self.server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET,SOCK_STREAM 생성 (주소체계 IPV4, 소켓타입 TCP)
        self.server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #winError10048 에러해결
        self.server_soc.bind((ChatServer.ip, ChatServer.port)) #소켓을 특정 네트워크 인터페이스와 포트번호에 연결
        self.server_soc.listen() #서버가 클라이언트의 접속을 허용

    def run(self):
        self.open() # open메소드 실행
        print('서버 시작') # 서버시작을 알림
        nb=numberBaseball()
        nb.randomBaseball()

        while True: # 무한반복
            client_soc, addr = self.server_soc.accept() # 대기하다가 클라이언트가 접속하면 새로운 소켓 리턴
            print(addr, '접속') # 접속한 클라이언트 주소 +접속 출력
            c = ChatClient(self.room, client_soc,nb.computer) # 클래스 선언 ( Room, 들어온 소켓,숫자야구)
            self.room.addClient(c) # 클라이언트 room에 추가
            print('클라:',self.room.clients) # 클라: 클라이언트 출력
            th = threading.Thread(target=c.readMsg) #readMsg를 스레드가 실행
            th.start() # 스레드 시작


        self.server_soc.close() # 소켓 닫기

class numberBaseball():

    def __init__(self):
        self.computer = []  # 서버 소켓

    def randomBaseball(self):
        for i in range(4):
            r = random.randint(0, 10)
            while r in self.computer:
                r=random.randint(0, 10)
            self.computer.append(r)

    def matchBaseball(self,user):
        strike=0
        ball=0
        for i in range(4):
            if self.computer[i] == user[i]:
                strike += 1
                ball -= 1
            for j in range(4):
                if self.computer[i]==user[j]:
                    ball+=1
        if strike==0 and ball==0:
            return 'out'
        else:
            result=' strike : '+str(strike)+ '/ ball : '+str(ball)
            return result






def main():
    cs = ChatServer() # cs=채팅서버
    cs.run() # 파일 실행

main()