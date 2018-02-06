#coding: UTF-8
import pigpio
import time

#RGBのポート番号の設定
GPIO_R = 13 
GPIO_G = 26
GPIO_B = 19

#刻み幅の設定
STEP = 100

#スリープ時間の設定
SEC = 0.01

#pigpioの設定
pi = pigpio.pi()

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
    
    

    #周波数の設定
    pi.set_PWM_frequency(GPIO_R,200)
    pi.set_PWM_frequency(GPIO_G,200)
    pi.set_PWM_frequency(GPIO_B,200)

    #PWMの設定(初期の色を"白"に設定)
    pi.set_PWM_dutycycle(GPIO_R,white[0])
    pi.set_PWM_dutycycle(GPIO_G,white[1])
    pi.set_PWM_dutycycle(GPIO_B,white[2])
    
    #グラデーション（赤→緑）
    change_color_gradation(red,green)
    #グラデーション（緑→赤）
    change_color_gradation(green,red)

#RGBごとの刻み幅の算出
def get_rgb_incriment(col1,col2):
    rgb_inc = []
    for i in range(3):
        rgb_inc.append(float(col2[i] - col1[i])/STEP)
    return rgb_inc

#col1からcol2へ徐々に色を変更
def change_color_gradation(col1,col2):
    #刻み幅の算出
    rgb_inc = get_rgb_incriment(col1, col2)
    for i in range(STEP):
        for color, GPIO in enumerate([GPIO_R,GPIO_G,GPIO_B]):
            #PWMの設定
            pi.set_PWM_dutycycle(GPIO,col1[color] + (i) * rgb_inc[color])
            #スリープ
            time.sleep(SEC)

if __name__ =='__main__':
    main()
