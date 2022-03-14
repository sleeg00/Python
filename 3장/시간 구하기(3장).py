import time
ti=time.time()//60
minute = ti%60
hour = ti //60%24
print("현재 시간(영국 그리니치 시각):",int(hour),"시",int(minute),"분",int(ti),"초")

#time 모듈 쓰는 법
#secs=time.time() #초를 나타냄

#tm=time.gmtime(13434234234.3232)
#tm.tm_year, tm.tm_mon,tm.tm_mday등등
