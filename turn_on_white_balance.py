#coding: UTF-8
import pigpio
import time
#RGB�̃|�[�g�ԍ��̐ݒ�
GPIO_R = 13 
GPIO_G = 26
GPIO_B = 19

def main():
    #�z���C�g�o�����X�̐ݒ�
    max_val = 255.0
    col = [max_val/ 4, max_val / 3, max_val / 2]

    #pigpio�̏�����
    pi = pigpio.pi()

    #���g���̐ݒ�
    pi.set_PWM_frequency(GPIO_R,200)
    pi.set_PWM_frequency(GPIO_G,200)
    pi.set_PWM_frequency(GPIO_B,200)

    #PWM�̐ݒ�("��"�ɐݒ�)
    pi.set_PWM_dutycycle(GPIO_R,col[0])
    pi.set_PWM_dutycycle(GPIO_G,col[1])
    pi.set_PWM_dutycycle(GPIO_B,col[2])

if __name__ =='__main__':
    main()    
