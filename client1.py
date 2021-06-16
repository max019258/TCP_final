import threading
import socket
import tkinter as tk #tkinter -> tk 로 줄여 표현


class UiChatClient:
    # class 변수 / static 변수 : 모든 객체가 공유
    ip = 'localhost'
    port = 8082

    def __init__(self):
        self.conn_soc = None  # 서버와 연결된 소켓
        self.win = None # TK
        self.chatCont = None # 채팅 label
        self.myChat = None #  채팅 입력 entry
        self.sendBtn = None # 전송 버튼
        self.allChat ='' #  모든 챗 내역
        self.chatlist=None #모든 챗 내역 한줄씩 리스트로 나누기
        self.cnt=0 # id를 받기위한 카운트 변수
        self.id='' # id변수

    def conn(self):
        self.conn_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET,SOCK_STREAM 생성 (주소체계 IPV4, 소켓타입 TCP)
        self.conn_soc.connect((UiChatClient.ip, UiChatClient.port)) #포트 ip를 통한 연결

    def setWindow(self):
        self.win = tk.Tk() # Tk선언
        self.win.title('숫자야구프로그램') # 창 제목
        #self.win.geometry('800x500') # 크기 지정
        self.chatCont = tk.Label(self.win,borderwidth = 2, relief="ridge", width=50, height=30, text='',background='white',justify='right') #라벨 크기 선언
        self.chatCont2 = tk.Label(self.win, borderwidth = 2, relief="ridge",width=50, height=30,background='white',justify='left',text=' 1.맨처음 입력하는 것은 닉네임입니다.\n\n2. 숫자야구를 풀고 싶으시다면 \n서로다른 숫자 4자리를 입력해주세요.\n\n'
                                                                                                                                       '3. 채팅기능도 구현되어있습니다\n\n4. 4strike가 발생시 자동으로 서버가 꺼집니다.')
        self.lbl_log2 = tk.Label(self.win, borderwidth=2, relief="ridge", width=50, height=1, text='자신이 보낸 내용입니다',background='gray')  # 라벨 크기 선언
        self.lbl_log = tk.Label(self.win, borderwidth=2, relief="ridge", width=50, height=1, text='다른사람이 보낸 내용입니다.',background='gray')  # 라벨 크기 선언


        self.myChat = tk.Entry(self.win, width=40,text='닉네임을 입력해주세요') # 입력창 선언
        self.sendBtn = tk.Button(self.win, width=10, text='전송',command=self.sendMsg_btn) # 전송버튼 선언

        self.lbl_log.grid(row=0, column=0)  # 배치
        self.lbl_log2.grid(row=0, column=1)  # 배치
        self.chatCont2.grid(row=1, column=0)  # 배치
        self.chatCont.grid(row=1, column=1) # 배치
        self.myChat.grid(row=2, column=0,columnspan=2,sticky='ew')# 배치
        self.sendBtn.grid(row=2, column=2,sticky="ew") # 배치

        self.myChat.bind('<Return>', self.sendMsg) #엔터 누를시 sendMsg 실행

    def sendMsg_btn(self):  # 키보드 입력 받아 상대방에게 메시지 전송
        if self.cnt==0: # 만약 cnt가 0이면
            msg = self.myChat.get()  # 입력 값을 받아서 msg에 넣는다
            self.id=msg # self.id는 msg
            self.cnt+=1 # cnt에 1추가
            self.myChat.delete(0, tk.END)
            self.myChat.config(text='')  # entry 값 초기화
            print(type(msg))  # msg 타입 확인
            msg = msg.encode(encoding='utf-8')  # 한글값을 위한 인코딩
            print(self.conn_soc)  # 소켓 확인
            self.conn_soc.sendall(msg)  # 메시지 서버로 보내기
        else:
            msg = self.myChat.get() #입력 값을 받아서 msg에 넣는다
            self.myChat.delete(0, tk.END)
            self.myChat.config(text='')  #entry 값 초기화
            print(type(msg)) # msg 타입 확인
            msg = msg.encode(encoding='utf-8') #한글값을 위한 인코딩
            print(self.conn_soc) #소켓 확인
            self.conn_soc.sendall(msg) # 메시지 서버로 보내기
        print('전송완료')


    def sendMsg(self, e):  # 키보드 입력 받아 상대방에게 메시지 전송
        if self.cnt==0: # 만약 cnt가 0이면
            msg = self.myChat.get()  # 입력 값을 받아서 msg에 넣는다
            self.id=msg # self.id는 msg
            self.cnt+=1 # cnt에 1추가
            self.myChat.delete(0, tk.END)
            self.myChat.config(text='')  # entry 값 초기화
            print(type(msg))  # msg 타입 확인
            msg = msg.encode(encoding='utf-8')  # 한글값을 위한 인코딩
            print(self.conn_soc)  # 소켓 확인
            self.conn_soc.sendall(msg)  # 메시지 서버로 보내기
        else:
            msg = self.myChat.get() #입력 값을 받아서 msg에 넣는다
            self.myChat.delete(0, tk.END)
            self.myChat.config(text='')  #entry 값 초기화
            print(type(msg)) # msg 타입 확인
            msg = msg.encode(encoding='utf-8') #한글값을 위한 인코딩
            print(self.conn_soc) #소켓 확인
            self.conn_soc.sendall(msg) # 메시지 서버로 보내기
        print('전송완료')

    def recvMsg(self):  # 서버에서 보낸 메시지 읽어서 화면에 출력

        while True:
            print('read start')# 읽어왔는지 확인
            msg = self.conn_soc.recv(1024) #msg는 서버에서 받아온 값
            print(msg)
            msg = msg.decode()+'\n' # msg디코딩
            self.allChat += msg # msg를 allchat(전체 채팅 목록에 추가)
            allchat=self.allChat
            #print(allchat) #전체 채팅

            # self.chatCont2.config(text=self.allChat) # allchat을 label에 출력

            self.chatlist=allchat.split('\n')  #문자열을 리스트로 바꿔준다.  # 한줄 씩 리스트에 넣는다
            print(self.chatlist)
            msg2=''
            msg3=''
            for i in self.chatlist: #채팅 리스트를 i에 넣는다.
                if i.startswith(self.id): #만약 id로 시작하면
                    msg2=msg2+'\n\n'+i
                    self.chatCont.config(text=msg2)  # allchat을 label에 출력
                else:
                    msg3=msg3+'\n\n'+i
                    self.chatCont2.config(text=msg3)  # allchat을 label에 출력


    def run(self): #작동 함수
        self.conn()  # 서버 연결
        self.setWindow() # GUI

        th2 = threading.Thread(target=self.recvMsg) # recvMsg를 스레드가 실행
        th2.start() # "
        self.win.mainloop() # GUI용

    def close(self):
        self.conn_soc.close() # 소켓 닫기
        print('종료되었습니다')


def main():
    conn = UiChatClient() #conn 객체 지정
    conn.run() #작동함수


main()