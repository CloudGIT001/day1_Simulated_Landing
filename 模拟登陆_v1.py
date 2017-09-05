#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:xieshengsen


"""
模拟登陆：
1. 用户输入帐号密码进行登陆
2. 用户信息保存在文件内
3. 用户密码输入错误三次后锁定用户
"""

import os
import sys
import json
import time
import datetime


def logout():
    exit("logout now".center(40, "-"))


def register():
    ex_flag = True
    while ex_flag:
        username = input("\033[32;1mPlease input your register name[b=back]\033[0m>>>:")
        account_file = "%s.json" % username
        if os.path.isfile(account_file):
            print("\033[31;1mUser already exists\033[0m")
            continue
        elif username == "b":
            main()
        else:
            password1 = input("\033[32;1mPlease input your register password\033[0m>>>:")
            password2 = input("\033[32;1mPlease input your register password again\033[0m>>>:")
            if password1 == password2:
                password = password1
                today = datetime.datetime.now().strftime('%Y-%m-%d')
                account_data = {"enroll_date": today, "password": password, "username": username, "time": 0}
                # account_file = "%s.json" % username
                with open(account_file, "w", encoding="utf-8") as f2:
                    json.dump(account_data, f2)
                    return True
            else:
                print("\033[31;1m password is not identical,please again~\033[0m")


def login():
    username = input("\033[32;1mPlease input Your username\033[0m>>>:")
    account_file = "%s.json" % username
    if os.path.isfile(account_file):
        with open(account_file, "r", encoding="utf-8") as f3:
            account_data = json.load(f3)
            print(account_data)
            timeit = timeit = account_data["time"]
            if timeit > 3:
                print("\n\033[41;1mToo many login errors, accounts have been locked\033[0m")
                exit("bye")
            else:
                password = input("\033[32;1mPlease input Your password\033[0m>>>:")
                if account_data["password"] == password:
                    for i in range(10):
                        sys.stdout.write("--> ")
                        print ("\033[34;1mWELCOME TO LOGIN\033[0m")
                        sys.stdout.flush()
                        time.sleep(0.2)
                    time.sleep(5)
                    return True
                else:
                    print ("\033[31;1m password is error\033[0m")
                    timeit += 1
                    account_data["time"] = timeit
                    print (timeit)
                    with open(account_file, "w+", encoding="utf-8") as f4:
                        json.dump(account_data, f4)
    else:
        print("\033[31;1mUser does not exist. Please register\033[0m")


def main():
    print("\033[32;1mwelcone to simulated landing test~\033[0m\n")

    menu ="""\033[33;1m
        0. logout
        1. register
        2. login
        \033[0m"""

    flag = False
    while not flag:
        print(menu)
        user_choice = input("\033[32;1mplease input user chioce\033[0m[0=exit]>>>:").strip()
        if user_choice == "0":
            logout()

        if user_choice == "1":
            register()

        if user_choice == "2":
            login()

        else:
            print("\033[31;1mYour input error,please again\033[0m")


if __name__ == "__main__":
    main()