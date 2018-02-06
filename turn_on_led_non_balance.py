#coding: UTF-8
import pigpio
import time
GPIO_R = 13 
GPIO_G = 26
GPIO_B = 19

def main():
    max_val = 255.0
    col = [max_val / 10, max_val / 10, max_val / 10]
    pi = pigpio.pi()
    pi.set_PWM_frequency(GPIO_R,200)
    pi.set_PWM_frequency(GPIO_G,200)
    pi.set_PWM_frequency(GPIO_B,200)

    pi.set_PWM_dutycycle(GPIO_R,col[0])
    pi.set_PWM_dutycycle(GPIO_G,col[1])
    pi.set_PWM_dutycycle(GPIO_B,col[2])

if __name__ =='__main__':
    main()  