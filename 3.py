flag = True;
while flag:
    temp = input("请输入一个数字:");
    guess = int(temp)
    if guess == 8:
        print("bingo")
        flag = False;
    elif guess > 8:
        print("垃圾,猜大了")
    else:
        print("垃圾,猜小了")
print("游戏结束")
        
