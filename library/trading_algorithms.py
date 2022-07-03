import numpy as np
import pandas as pd


def BBands(df_close, w=20, k=2):
    """
        w: 이동평균선 기간 값 (20)
        k: 승수 (2)
        std 함수는 '표준편차를 구하기 위한' numpy 패키지에 포함되어 있는 내장 함수입니다.
        DATAFRAME[-1:] 마지막 row
        DATAFRAME[:-1] index 0부터 마지막 row 제외한 rows
        DATAFRAME[-20:] 뒤에서부터 20개의 rows
        DATAFRAME[:20] index 0부터 20개의 rows
        DATAFRAME[20:] index 20부터 끝까지 rows
    """
    # 고가, 저가, 종가의 평균을 이용하는 경우 정수로 변환이 필요
    df_close = df_close.astype(int)
    # 표준편차
    std = df_close[:w].std()[0]
    std_1 = df_close[1:w].std()[0]
    std_2 = df_close[2:w].std()[0]
    std_3 = df_close[3:w].std()[0]
    std_4 = df_close[4:w].std()[0]
    std_5 = df_close[5:w].std()[0]
    std_6 = df_close[6:w].std()[0]
    std_7 = df_close[7:w].std()[0]
    std_8 = df_close[8:w].std()[0]
    std_9 = df_close[9:w].std()[0]
    std_10 = df_close[10:w].std()[0]
    std_11 = df_close[11:w].std()[0]
    std_12 = df_close[12:w].std()[0]
    std_13 = df_close[13:w].std()[0]
    std_14 = df_close[14:w].std()[0]
    std_15 = df_close[15:w].std()[0]
    std_16 = df_close[16:w].std()[0]
    std_17 = df_close[17:w].std()[0]
    std_18 = df_close[18:w].std()[0]
    std_19 = df_close[19:w].std()[0]
    std_20 = df_close[20:w].std()[0]
    # mean() 함수는 '평균을 구하기 위한' numpy 패키지에 포함되어 있는 내장 함수입니다.
    # 20일 이평선이자 볼린저밴드 중앙선
    mbb = df_close[:w].mean()[0]
    mbb_1 = df_close[1:w].mean()[0]
    mbb_2 = df_close[2:w].mean()[0]
    mbb_3 = df_close[3:w].mean()[0]
    mbb_4 = df_close[4:w].mean()[0]
    mbb_5 = df_close[5:w].mean()[0]
    mbb_6 = df_close[6:w].mean()[0]
    mbb_7 = df_close[7:w].mean()[0]
    mbb_8 = df_close[8:w].mean()[0]
    mbb_9 = df_close[9:w].mean()[0]
    mbb_10 = df_close[10:w].mean()[0]
    mbb_11 = df_close[11:w].mean()[0]
    mbb_12 = df_close[12:w].mean()[0]
    mbb_13 = df_close[13:w].mean()[0]
    mbb_14 = df_close[14:w].mean()[0]
    mbb_15 = df_close[15:w].mean()[0]
    mbb_16 = df_close[16:w].mean()[0]
    mbb_17 = df_close[17:w].mean()[0]
    mbb_18 = df_close[18:w].mean()[0]
    mbb_19 = df_close[19:w].mean()[0]
    mbb_20 = df_close[20:w].mean()[0]
    #모멘텀 지표
    mom = (mbb / mbb_10) * 100
    mom_1 = (mbb_1 / mbb_11) * 100
    mom_2 = (mbb_2 / mbb_12) * 100
    mom_3 = (mbb_3 / mbb_13) * 100
    mom_4 = (mbb_4 / mbb_14) * 100
    mom_5 = (mbb_5 / mbb_15) * 100
    mom_6 = (mbb_6 / mbb_16) * 100
    mom_7 = (mbb_7 / mbb_17) * 100
    mom_8 = (mbb_8 / mbb_18) * 100
    mom_9 = (mbb_9 / mbb_19) * 100
    mom_10 = (mbb_10 / mbb_20) * 100
    mom_sig = (mom + mom_1 + mom_2 + mom_3 + mom_4 + mom_5 + mom_6 + mom_7 + mom_8 + mom_9) / 10
    mom_sig_1 = (mom_1 + mom_2 + mom_3 + mom_4 + mom_5 + mom_6 + mom_7 + mom_8 + mom_9 + mom_10) / 10
    # 종가
    close = df_close[0][0]
    close_1 = df_close[0][1]

    '''
        std (표준편차 값)과 mbb(중앙선)을 이용하여 볼린저밴드
        1. ubb (상한선)
        2. lbb (하한선)
        3. perb (%b: 볼린저밴드에서의 종가 위치)
        4. bw (밴드폭)
        4개의 값을 구하는 수식을 01)볼린저밴드 개념에 안내되어 있는 [볼린저 밴드 계산방법]을 참고하여 구현해주세요.
        변수 이름은 ubb, lbb, perb, bw로 통일하여 주시기 바랍니다.
    '''

    ## blank ###########################
    ubb = mbb + std * k
    ubb_1 = mbb_1 + std_1 * k
    ubb_2 = mbb_2 + std_2 * k
    ubb_3 = mbb_3 + std_3 * k
    ubb_4 = mbb_4 + std_4 * k
    ubb_5 = mbb_5 + std_5 * k
    ubb_6 = mbb_6 + std_6 * k
    ubb_7 = mbb_7 + std_7 * k
    ubb_8 = mbb_8 + std_8 * k
    ubb_9 = mbb_9 + std_9 * k
    ubb_10 = mbb_10 + std_10 * k
    ubb_11 = mbb_11 + std_11 * k
    ubb_12 = mbb_12 + std_12 * k
    ubb_13 = mbb_13 + std_13 * k
    ubb_14 = mbb_14 + std_14 * k
    ubb_15 = mbb_15 + std_15 * k
    ubb_16 = mbb_16 + std_16 * k
    ubb_17 = mbb_17 + std_17 * k
    ubb_18 = mbb_18 + std_18 * k
    ubb_19 = mbb_19 + std_19 * k
    ubb_20 = mbb_20 + std_20 * k
    lbb = mbb - std * k
    lbb_1 = mbb_1 - std_1 * k
    lbb_2 = mbb_2 - std_2 * k
    lbb_3 = mbb_3 - std_3 * k
    lbb_4 = mbb_4 - std_4 * k
    lbb_5 = mbb_5 - std_5 * k
    lbb_6 = mbb_6 - std_6 * k
    lbb_7 = mbb_7 - std_7 * k
    lbb_8 = mbb_8 - std_8 * k
    lbb_9 = mbb_9 - std_9 * k
    lbb_10 = mbb_10 - std_10 * k
    lbb_11 = mbb_11 - std_11 * k
    lbb_12 = mbb_12 - std_12 * k
    lbb_13 = mbb_13 - std_13 * k
    lbb_14 = mbb_14 - std_14 * k
    lbb_15 = mbb_15 - std_15 * k
    lbb_16 = mbb_16 - std_16 * k
    lbb_17 = mbb_17 - std_17 * k
    lbb_18 = mbb_18 - std_18 * k
    lbb_19 = mbb_19 - std_19 * k
    lbb_20 = mbb_20 - std_20 * k
    ####################################

    if ubb > lbb:
        ## blank ###########################
        perb = (close - lbb) / (ubb - lbb)
        perb_1 = (close_1 - lbb_1) / (ubb_1 - lbb_1)
        bw = (ubb - lbb) / mbb
        bw_1 = (ubb_1 - lbb_1) / mbb_1
        bw_2 = (ubb_2 - lbb_2) / mbb_2
        bw_3 = (ubb_3 - lbb_3) / mbb_3
        bw_4 = (ubb_4 - lbb_4) / mbb_4
        bw_5 = (ubb_5 - lbb_5) / mbb_5
        bw_6 = (ubb_6 - lbb_6) / mbb_6
        bw_7 = (ubb_7 - lbb_7) / mbb_7
        bw_8 = (ubb_8 - lbb_8) / mbb_8
        bw_9 = (ubb_9 - lbb_9) / mbb_9
        bw_10 = (ubb_10 - lbb_10) / mbb_10
        bw_11 = (ubb_11 - lbb_11) / mbb_11
        bw_12 = (ubb_12 - lbb_12) / mbb_12
        bw_13 = (ubb_13 - lbb_13) / mbb_13
        bw_14 = (ubb_14 - lbb_14) / mbb_14
        bw_15 = (ubb_15 - lbb_15) / mbb_15
        bw_16 = (ubb_16 - lbb_16) / mbb_16
        bw_17 = (ubb_17 - lbb_17) / mbb_17
        bw_18 = (ubb_18 - lbb_18) / mbb_18
        bw_19 = (ubb_19 - lbb_19) / mbb_19
        bw_20 = (ubb_20 - lbb_20) / mbb_20
        bw_m_1 = bw_1
        bw_m_r = (bw_1 + bw_2 + bw_3 + bw_4 + bw_5 + bw_6 + bw_7 + bw_8 + bw_9 + bw_10 + bw_11 + bw_12 + bw_13 + bw_14 + bw_15 + bw_16 + bw_17 + bw_18 + bw_19 + bw_20) / 20
        bw_m = (bw_1 + bw_2 + bw_3 + bw_4 + bw_5) / 5
        bw_m20 = (bw_1 + bw_2 + bw_3 + bw_4 + bw_5 + bw_6 + bw_7 + bw_8 + bw_9 + bw_10 + bw_11 + bw_12 + bw_13 + bw_14 + bw_15 + bw_16 + bw_17 + bw_18 + bw_19 + bw_20) / 20
        ####################################
        return mom, mom_1, mom_sig, mom_sig_1, mbb, ubb, lbb, perb, perb_1, bw, bw_m
    else:
        return False
