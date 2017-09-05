# -*- coding:utf-8 -*-
# Author:xieshengsen

username = {}
with open("loginfile","r",encoding="utf-8") as f:
    for line in f:
        username_list = line.strip().split("|")
        print (username_list)
        username[username_list[0]] = {"name":username_list[0],"pwd":username_list[1],"times":username_list[2]}

with open("lockfile","r",encoding="utf-8") as f1:
    black_list = []
    for line in f1:
        black_list.append(line.strip())
        # print (black_list)
while True:
    user_name = input("please input your username:").strip()
    pass_word = input("pleasw input your password:").strip()

    if user_name in black_list:
        print ("The user has been locked and no landing is allowed~")
        break

    elif user_name in username:
        username[user_name]["times"] = int(username[user_name]["times"])
        if username[user_name]["times"] < 3 and pass_word == username[user_name]["pwd"]:
            print ("welcome to login~")
            break
        else:
            username[user_name]["times"] += 1
            print ("Password error, login failed~")
            with open("loginfile","w",encoding="utf-8") as f2:
                for i in username:
                    f2.write(i + "|" + username[i]["pwd"] + "|" + str(username[i]["times"]) + "\n")

        if username[user_name]["times"] == 3:
            print ("Login error has more than three times, account password is locked~")
            with open("lockfile","w",encoding="utf-8") as f3:
                for k in black_list:
                    f3.write(k + "\n")
                break
    else:
        print ("Login account not registered~")
        continue
