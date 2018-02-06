#coding: UTF-8
import pigpio
import time
#RGBのポート番号の設定
GPIO_R = 13 
GPIO_G = 26
GPIO_B = 19

def main():
    #ホワイトバランスの設定
    max_val = 255.0
    col = [max_val/ 4, max_val / 3, max_val / 2]

    #pigpioの初期化
    pi = pigpio.pi()

    #周波数の設定
    pi.set_PWM_frequency(GPIO_R,200)
    pi.set_PWM_frequency(GPIO_G,200)
    pi.set_PWM_frequency(GPIO_B,200)

    #PWMの設定("白"に設定)
    pi.set_PWM_dutycycle(GPIO_R,col[0])
    pi.set_PWM_dutycycle(GPIO_G,col[1])
    pi.set_PWM_dutycycle(GPIO_B,col[2])

if __name__ =='__main__':
    main()    
