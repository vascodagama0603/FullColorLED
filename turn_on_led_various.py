#coding: UTF-8
import pigpio
import time
#RGBのポート番号の設定
GPIO_R = 13
GPIO_G = 26
GPIO_B = 19

def main():
    #ホワイトバランスの設定
    max_val = 255
    zero = (max_val-1) 
    base_col = [max_val/3, max_val/4 , max_val/2]
    
    #色の定義
    red = [base_col[0],zero,zero]
    green = [zero,base_col[1],zero]
    blue = [zero,zero,base_col[2]]
    yellow = [base_col[0],base_col[1],zero]
    mazenta = [base_col[0],zero,base_col[2]]
    sian = [zero,base_col[1],base_col[2]]
    white = base_col

    #pigpioの設定
    pi = pigpio.pi()
    
    #周波数の設定
    pi.set_PWM_frequency(GPIO_R,200)
    pi.set_PWM_frequency(GPIO_G,200)
    pi.set_PWM_frequency(GPIO_B,200)

    #各色を2回分ループ
    for i in range(2):
        for col in [red,green,blue,yellow,mazenta,white]:
            #PWMの設定
            pi.set_PWM_dutycycle(GPIO_R,col[0])
            pi.set_PWM_dutycycle(GPIO_G,col[1])
            pi.set_PWM_dutycycle(GPIO_B,col[2])
            #スリープ
            time.sleep(1)

if __name__ =='__main__':
    main()
