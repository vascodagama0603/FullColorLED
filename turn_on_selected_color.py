# coding: UTF-8
import pigpio
import time
from enum import Enum

# RGBのポート番号の設定
GPIO_R = 13
GPIO_G = 26
GPIO_B = 19


# 列挙型のクラスを定義
class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3
    YELLOW = 4
    MAZENTA = 5
    SYAN = 6
    WHITE = 7

# 色の設定を呼び出す関数を定義
def main():
    #色の設定を呼び出す
    #引数は(列挙型の色の設定値,秒数[sec])
    set_led_color(Color.RED,1)
    set_led_color(Color.BLUE,1)
    set_led_color(Color.GREEN,1)
    set_led_color(Color.YELLOW,1)
    set_led_color(Color.MAZENTA,1)
    set_led_color(Color.SYAN,1)
    set_led_color(Color.WHITE,1)

# 色を設定する関数を定義
def set_led_color(Target, sec):
    # pigpioの初期化
    pi = pigpio.pi()

    # 周波数の設定
    pi.set_PWM_frequency(GPIO_R, 200)
    pi.set_PWM_frequency(GPIO_G, 200)
    pi.set_PWM_frequency(GPIO_B, 200)

    # ホワイトバランスの設定
    max_val = 255.0
    zero = (max_val-1)
    base_col = [max_val / 4, max_val / 3, max_val / 2]

    # 色をすべてOFFに設定
    red = zero
    blue = zero
    green = zero

    # 着色の場合分け
    if Color.RED == Target:
        red = base_col[0]
    elif Color.BLUE == Target:
        blue = base_col[1]
    elif Color.GREEN == Target:
        green = base_col[2]
    elif Color.YELLOW == Target:
        red = base_col[0]
        green = base_col[2]
    elif Color.MAZENTA == Target:
        red = base_col[0]
        blue = base_col[1]
    elif Color.SYAN == Target:
        blue = base_col[1]
        green = base_col[2]
    elif Color.WHITE == Target:
        red = base_col[0]
        blue = base_col[1]
        green = base_col[2]
    else:
        print("No Setting Color!")

    # Targetの色にPWMの設定
    pi.set_PWM_dutycycle(GPIO_R, red)
    pi.set_PWM_dutycycle(GPIO_G, blue)
    pi.set_PWM_dutycycle(GPIO_B, green)
    time.sleep(sec)

if __name__ == '__main__':
    main()
