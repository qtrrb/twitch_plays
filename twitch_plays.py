import socket
import sys
import pyautogui

server= "irc.chat.twitch.tv"
port = 6667
token = ""
nickname= ""
channel = "#"
sock = socket.socket()
input = [
"up",
"down",
"left",
"right",
"a",
"b",
"start",
"select"
]
output = [
"up",
"down",
"left",
"right",
"x",
"z",
"enter",
"backspace"
]

def main():
    connect()
    run()

def run():
    while True:
        try:
            recv = sock.recv(1024).decode()
        except:
            recv = ""
        for line in recv.split('\n'):
            ping(line)
            if line == "":
                continue
            else:
                message = read(line)
                print(message)
                control(message)

#taken from:
#https://www.learndatasci.com/tutorials/how-stream-text-data-twitch-sockets-python/
def connect():
    sock.connect((server, port))
    sock.send(f"PASS {token}\n".encode())
    sock.send(f"NICK {nickname}\n".encode())
    sock.send(f"JOIN {channel}\n".encode())

def read(line):
    try:
        message = (line.split(":", 2))[2]
    except:
        message = ""
    return message

def ping(line):
    if line.startswith("PING"):
        sock.send(line.replace("PING", "PONG").encode())
        print("PING PONG!")

def control(message):
    for x in range(0,8):
        if message.lower() == input[x]:
            pyautogui.keyDown(output[x])
            message = ""
            pyautogui.keyUp(output[x])
        else:
            pass

if __name__ == "__main__":
    main()
