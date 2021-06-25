'''
Created on : May 31, 2021  10:41:42

@author: ThamDinh
'''

import math
import time
import numpy as np

#Ham f
def fx(x1, x2):
    return 100*pow((x2 - x1*x1), 2) + pow((1 - x1), 2)

#dao ham bac 1 theo x1
def dfx1(x1, x2):
    return -400*x1*x2 + 400*pow(x1, 3) + 2*x1 -2

#dao ham bac 1 theo x2
def dfx2(x1, x2):
    return 200*x2 -200*pow(x1, 2)

#dao ham bac 2 theo x1x1
def dfx1x1(x1, x2):
    return -400*x2 + 1200*x1*x1 +2

#dao ham bac 2 theo x1x2 = dao ham theo x2x1
def dfx1x2(x1, x2):
    return -400*x1

#dao ham bac 2 theo x2x2
def dfx2x2():
    return 200

#binh phuong chuan 2
def enclide(dfx1, dfx2):
    return dfx1*dfx1 + dfx2*dfx2

def gradien(x):
    df1 = dfx1(x[0], x[1])
    df2 = dfx2(x[0], x[1])
    return np.array([[df1], [df2]])

#matran Hessian
def hessian(x):
    df11 = dfx1x1(x[0], x[1])
    df12 = dfx1x2(x[0], x[1])
    df22 = dfx2x2()
    return np.array([[df11, df12], [df12, df22]])


def newBack(t, alpha, beta, x):
    
    count = 0
    gra = gradien(x) #mt2-1
    hes = hessian(x) #mt2-2
    invHes = np.linalg.inv(hes) #mt2-2
    detax = -invHes @ gra #mt2-1
    lamda = (np.transpose(gra) @ invHes @ gra) /2#so

    while count < 1000 or lamda[0,0] > 0.0001:
        # print(count, x)
        
        f = fx(x[0], x[1])
        gra = gradien(x) #mt2-1
        hes = hessian(x) #mt2-2
        invHes = np.linalg.inv(hes) #mt2-2
        detax = -invHes @ gra #mt2-1

        dk1_x0 = x[0] + t*detax[0, 0]
        dk1_x1 = x[1] + t*detax[1, 0]
        dk1 = [dk1_x0, dk1_x1]

        dk2_0 = np.transpose(gra) @ detax
        dk2 = f + alpha*t*dk2_0

        while fx(dk1[0], dk1[1]) > dk2:
            t = beta*t

            dk1_x0 = x[0] + t*detax[0, 0]
            dk1_x1 = x[1] + t*detax[1, 0]
            dk1 = [dk1_x0, dk1_x1]

            dk2_0 = np.transpose(gra) @ detax
            dk2 = f + alpha*t*dk2_0
        
        x = dk1
        count += 1
        lamda = ((np.transpose(gra) @ invHes) @ gra) / 2 #so
        
    return x, count

if __name__ == '__main__':
    x01 = [1.2, 1.2]
    x02 = [-1.2, 1] 

    alpha = 0.2
    beta = 0.5
    t = 1

    print('PP Newton with Backtracking line search')
    timeStart1 = time.time()
    back1 = newBack(t, alpha, beta, x01)
    timeEnd1 = time.time()
    time1 = timeEnd1 - timeStart1
    print(
        "Diem cuc tieu voi x0 = ", x01, " là ", back1[0], ", thời gian: ", time1, " giay, so vòng lặp: ", back1[1])

    timeStart2 = time.time()
    back2 = newBack(t, alpha, beta, x02)
    timeEnd2 = time.time()
    time2 = timeEnd2 - timeStart2
    print(
        "Diem cuc tieu voi x0 = ", x02, " là ", back2[0], ", thời gian: ", time2, " giay, so vòng lặp: ", back2[1])

