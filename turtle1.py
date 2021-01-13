#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle
turtle.shape('turtle')
turtle.speed(100)
x = 0
for x in range(60):
  for i in range(4):
    turtle.forward(100)
    turtle.right(90)
  turtle.right(5)

