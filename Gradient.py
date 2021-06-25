'''
Created on : May 27, 2021  00:41:42

@author: ThamDinh
'''

import math
import time
#Ham f
def fx(x1, x2):
    return 100*pow((x2 - x1*x1), 2) + pow((1 - x1), 2)
#dao ham bac 1 theo x1
def dfx1(x1, x2):
    return -400*x1*x2 + 400*pow(x1, 3) + 2*x1 -2
#dao ham bac 1 theo x2
def dfx2(x1, x2):
    return 200*x2 -200*pow(x1, 2)
#binh phuong chuan 2
def enclide(dfx1, dfx2):
    return dfx1*dfx1 + dfx2*dfx2

def grtBack(t, alpha, beta, x):
    count = 0
    df1 = dfx1(x[0], x[1])
    df2 = dfx2(x[0], x[1])
    enSqrt = math.sqrt(enclide(df1, df2))

    while count < 1000 or enSqrt >= 0.0001:
        # print(count, x)
        f = fx(x[0], x[1])
        df1 = dfx1(x[0], x[1])
        df2 = dfx2(x[0], x[1])
        en = enclide(df1, df2)
        enSqrt = math.sqrt(enclide(df1, df2))
        
        dk1_x0 = x[0] - t*df1
        dk1_x1 = x[1] - t*df2
        dk1 = [dk1_x0, dk1_x1]
        dk2 = alpha*t*en

        while fx(dk1[0], dk1[1]) > (f - dk2):
            t = beta * t
            dk1_x0 = x[0] - t*df1
            dk1_x1 = x[1] - t*df2

            dk1 = [dk1_x0, dk1_x1]
            dk2 = alpha*t*en

        x = dk1
        count += 1

    return x, count

if __name__ == '__main__':
    x01 = [1.2, 1.2]
    x02 = [-1.2, 1] 

    alpha = 0.2
    beta = 0.5
    t = 1

    print('PP Gradient descent with backtracking line search')
    timeStart1 = time.time()
    back1 = grtBack(t, alpha, beta, x01)
    timeEnd1 = time.time()
    time1 = timeEnd1 - timeStart1
    print(
        "Diem cuc tieu voi x0 = ",x01," là ",back1[0],", thời gian: ",time1," giay, so vòng lặp: ", back1[1])

    timeStart2 = time.time()
    back2 = grtBack(t, alpha, beta, x02)
    timeEnd2 = time.time()
    time2 = timeEnd2 - timeStart2
    print(
        "Diem cuc tieu voi x0 = ", x02, " là ", back2[0], ", thời gian: ", time2, " giay, so vòng lặp: ", back2[1])

