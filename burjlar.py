# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 09:40:58 2022

@author: User
"""

oy=input("Tug`ilgan oyingizni kiriting: ").lower()
kun=int(input("Tug`ilgan kuningizni kiriting: "))
if oy=="mart":
    if kun>=22:
        print("Xamal(Qo`y)")
    elif kun<22:
        print("Xut(Baliq)")
if oy=="aprel":
    if kun<=20:
        print("Xamal(Qo`y)")
    elif kun>20:
        print("Savr(Sigir)")
if oy=="may":
    if kun<=20:
        print("Savr(Sigir)")
    elif kun>20:
        print("Javzo(Egizak)")
if oy=="iyun":
    if kun<=21:
        print("Javzo(Egizak)")
    elif kun>21:
        print("Saraton(Qisqichbaqa)")
if oy=="iyul":
    if kun<=22:
        print("Saraton(Qisqichbaqa)")
    elif kun>22:
        print("Asad(Arslon)")
if oy=="avgust":
    if kun<=22:
        print("Asad(Arslon)")
    elif kun>22:
        print("Sunbula(Boshoq)")
if oy=="sentabr":
     if kun<=23:
         print("Sunbula(Boshoq)")
     elif kun>23:
         print("Mezon(Tarozi)")
if oy=="oktabr":
     if kun<=22:
         print("Mezon(Tarozi)")
     elif kun>22:
         print("Aqrab(Chayon)")
if oy=="noyabr":
     if kun<=22:
         print("Aqrab(Chayon)")
     elif kun>22:
         print("Qavs(O`qotar)")
if oy=="dekabr":
    if kun<=21:
        print("Qavs(O`qotar)")
    elif kun>21:
        print("Jadiy(Tog` echkisi)")
if oy=="yanvar":
    if kun<=19:
        print("Jadiy(Tog` echkisi)")
    elif kun>19:
        print("Dalv(Qovg`a)")
if oy=="fevral":
    if kun<=18:
        print("Dalv(Qovg`a)")
    elif kun>18:
        print("Xut(Baliq)")