#!/usr/bin/python
# -*- coding:utf-8 -*-

i = int(raw_input("请输入净利润："))
arr = [1000000,600000,400000,200000,100000,0]
rate = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0

for idx in  range(0,6):
    if i > arr[idx]:
        r += (i-arr[idx])*rate[idx]
        print (i-arr[idx])*rate[idx]
        i = arr[idx]

print r
