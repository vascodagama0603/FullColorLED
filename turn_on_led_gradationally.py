#coding: UTF-8
import pigpio
import time

#RGB�̃|�[�g�ԍ��̐ݒ�
GPIO_R = 13 
GPIO_G = 26
GPIO_B = 19

#���ݕ��̐ݒ�
STEP = 100

#�X���[�v���Ԃ̐ݒ�
SEC = 0.01

#pigpio�̐ݒ�
pi = pigpio.pi()

def main():
    #�z���C�g�o�����X�̐ݒ�
    max_val = 255
    zero = (max_val-1) 
    base_col = [max_val/3, max_val/4 , max_val/2]
    
    #�F�̒�`
    red = [base_col[0],zero,zero]
    green = [zero,base_col[1],zero]
    blue = [zero,zero,base_col[2]]
    yellow = [base_col[0],base_col[1],zero]
    mazenta = [base_col[0],zero,base_col[2]]
    sian = [zero,base_col[1],base_col[2]]
    white = base_col
    
    

    #���g���̐ݒ�
    pi.set_PWM_frequency(GPIO_R,200)
    pi.set_PWM_frequency(GPIO_G,200)
    pi.set_PWM_frequency(GPIO_B,200)

    #PWM�̐ݒ�(�����̐F��"��"�ɐݒ�)
    pi.set_PWM_dutycycle(GPIO_R,white[0])
    pi.set_PWM_dutycycle(GPIO_G,white[1])
    pi.set_PWM_dutycycle(GPIO_B,white[2])
    
    #�O���f�[�V�����i�ԁ��΁j
    change_color_gradation(red,green)
    #�O���f�[�V�����i�΁��ԁj
    change_color_gradation(green,red)

#RGB���Ƃ̍��ݕ��̎Z�o
def get_rgb_incriment(col1,col2):
    rgb_inc = []
    for i in range(3):
        rgb_inc.append(float(col2[i] - col1[i])/STEP)
    return rgb_inc

#col1����col2�֏��X�ɐF��ύX
def change_color_gradation(col1,col2):
    #���ݕ��̎Z�o
    rgb_inc = get_rgb_incriment(col1, col2)
    for i in range(STEP):
        for color, GPIO in enumerate([GPIO_R,GPIO_G,GPIO_B]):
            #PWM�̐ݒ�
            pi.set_PWM_dutycycle(GPIO,col1[color] + (i) * rgb_inc[color])
            #�X���[�v
            time.sleep(SEC)

if __name__ =='__main__':
    main()
