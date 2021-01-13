#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle
turtle.shape("turtle")
turtle.speed(100)
scale = 0
for i in range(60):
    scale += 5
    for x in range(4):
        turtle.forward(25+scale)
        turtle.right(90)
    turtle.right(5)

