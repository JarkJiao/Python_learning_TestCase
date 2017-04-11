#!/usr/bin/python
# -*- coding: UTF-8 -*-


for i in range(1,10):
    print
    for j in range (1,i+1):
        print '%7ld * %7ld=%7ld' % (i,j,i*j)