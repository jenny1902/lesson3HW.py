import random
num = random.randint(1 , 10)
time = 1
while time < 6:
    gus = (int(input("請猜一個1~10的數字: ")))
    if num > gus:
       print("你猜得太小了!")   
       time = time + 1   
    elif num < gus:
       print("你猜對了!你用了" ,time, "次猜對")
       break
    else:
       print("你猜得太大了!")
       time = time + 1
while time == 6:
  print("猜的次數超過上限!")
  break
