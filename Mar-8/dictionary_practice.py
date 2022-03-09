# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 19:04:04 2022

@author: mrobbins
"""

populations = { "New York":8.17, "Chicago":2.7, "Rome":2.87 }
print(populations)

status = { 404: "Not Found", 418: "I'm a teapot" }
print(status)

teapot = status[418]
print(teapot)

NYC = populations["New York"]
print(NYC)

# This throws an error because it cannot find the key 0
# NYC_2 = populations["0"]
# print(NYC_2)
