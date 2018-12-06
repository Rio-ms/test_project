# -*- coding: utf-8 -*-
import gspeech
import time
import os

def main():
    gsp = gspeech.Gspeech()
    while True:
        # 음성 인식 될때까지 대기 한다.
        stt = gsp.getText()
        if stt is None:
            break
        print(stt)

        gsp.text_to_speech(stt)

        time.sleep(0.01)
        #끝내자는 명령이 들어오면 프로그램 종료
        if ('그만' in stt):
            break

if __name__ == '__main__':
    main()