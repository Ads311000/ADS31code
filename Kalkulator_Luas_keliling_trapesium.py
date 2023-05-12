# -*- coding: utf-8 -*-
"""
Created on Thu May 11 11:30:25 2023
@author: ASUS
"""

from tkinter import *

root=Tk()
root.config(background='light blue')

label1= Label(text="Kalkulator", font="Normal 25", background="light blue")
label1.grid(row=0, column=3)
label2= Label(text="Luas dan Keliling Trapesium", font="Normal 12", background="light blue")
label2.grid(row=2, column=3)

#spasi
spasi1= Label(text=" ", font="Normal 12", background="light blue")
spasi1.grid(row=3, column=0)
spasi2= Label(text=" ", font="Normal 12", background="light blue")
spasi2.grid(row=4, column=0)

#input Nama Npm kelas
nama= Label(text="Nama : Ari Dwi Saputra", font="Normal 12", background="light blue")
nama.grid(row=5, column=3)
npm= Label(text="NPM : 240110180011", font="Normal 12", background="light blue")
npm.grid(row=6, column=3)
kelas= Label(text="Kelas : Alsin", font="Normal 12", background="light blue")
kelas.grid(row=7, column=3)

spasi3= Label(text=" ", font="Normal 12", background="light blue")
spasi3.grid(row=8, column=0)

#keliling trapesium
Keliling= Label(text="Keliling Trapesium", font="Normal 12", background="light blue")
Keliling.grid(row=9, column=0)
rumus_Keliling= Label(text="Keliling Trapesium = a+b+c+d", font="Normal 12", background="light blue")
rumus_Keliling.grid(row=10, column=0)
Masukan_Keliling= Label(text="Masukan Nilai", font="Normal 12", background="light blue")
Masukan_Keliling.grid(row=11, column=0)
a_Keliling= Label(text="a =", font="Normal 12", background="light blue")
a_Keliling.grid(row=12, column=0)
input_a_Keliling= Entry(font = "Normal 10", bd = 5)
input_a_Keliling.grid(row=12, column=1)
b_Keliling= Label(text="b =", font="Normal 12", background="light blue")
b_Keliling.grid(row=13, column=0)
input_b_Keliling= Entry(font = "Normal 10", bd = 5)
input_b_Keliling.grid(row=13, column=1)
c_Keliling= Label(text="c =", font="Normal 12", background="light blue")
c_Keliling.grid(row=14, column=0)
input_c_Keliling= Entry(font = "Normal 10", bd = 5)
input_c_Keliling.grid(row=14, column=1)
d_Keliling= Label(text="d =", font="Normal 12", background="light blue")
d_Keliling.grid(row=15, column=0)
input_d_Keliling= Entry(font = "Normal 10", bd = 5)
input_d_Keliling.grid(row=15, column=1)

def perintah_keliling():
    input_hasil_Keliling.delete(0,END)
    K_trapesium=int (input_a_Keliling.get()) + int (input_b_Keliling.get())+int (input_c_Keliling.get())+int (input_d_Keliling.get())
    
    input_hasil_Keliling.insert(0,K_trapesium)

button_keliling = Button(text = "Hitung", font = "Normal 10", activebackground = "Blue", command=perintah_keliling)
button_keliling.grid(row=17, column=1)

hasil_Keliling= Label(text="Keliling =", font="Normal 12", background="light blue")
hasil_Keliling.grid(row=18, column=0)
input_hasil_Keliling= Entry(font = "Normal 10", bd = 5)
input_hasil_Keliling.grid(row=18, column=1)

#luas trapesium
luas= Label(text="Luas Trapesium", font="Normal 12", background="light blue")
luas.grid(row=9, column=4)
rumus_luas= Label(text="Luas Trapesium = 1/2 x (a+b) x t", font="Normal 12", background="light blue")
rumus_luas.grid(row=10, column=4)
Masukan_luas= Label(text="Masukan Nilai", font="Normal 12", background="light blue")
Masukan_luas.grid(row=11, column=4)
sisi_a_luas= Label(text="a =", font="Normal 12", background="light blue")
sisi_a_luas.grid(row=12, column=4)
input_a_luas= Entry(font = "Normal 10", bd = 5)
input_a_luas.grid(row=12, column=5)
sisi_b_luas= Label(text="b =", font="Normal 12", background="light blue")
sisi_b_luas.grid(row=13, column=4)
input_b_luas= Entry(font = "Normal 10", bd = 5)
input_b_luas.grid(row=13, column=5)
tinggi_luas= Label(text="Tinggi =", font="Normal 12", background="light blue")
tinggi_luas.grid(row=14, column=4)
input_tinggi_luas= Entry(font = "Normal 10", bd = 5)
input_tinggi_luas.grid(row=14, column=5)


def perintah_luas():
    input_hasil_luas.delete(0,END)
    K_trapesium=0.5*(int (input_a_luas.get()) + int (input_a_luas.get()))*int (input_tinggi_luas.get())
    
    input_hasil_luas.insert(0,K_trapesium)

button_keliling = Button(text = "Hitung", font = "Normal 10", activebackground = "Blue", command=perintah_luas)
button_keliling.grid(row=17, column=5)

hasil_luas= Label(text="Keliling =", font="Normal 12", background="light blue")
hasil_luas.grid(row=18, column=4)
input_hasil_luas= Entry(font = "Normal 10", bd = 5)
input_hasil_luas.grid(row=18, column=5)

def clear():
    input_a_Keliling.delete(0, END)
    input_b_Keliling.delete(0, END)
    input_c_Keliling.delete(0, END)
    input_d_Keliling.delete(0, END)
    input_hasil_Keliling.delete(0, END)
    input_a_luas.delete(0, END)
    input_b_luas.delete(0, END)
    input_tinggi_luas.delete(0, END)
    
clear_all = Button(text = "Clear", font = "Normal 15", activebackground = "Blue", command=clear)
clear_all.grid(row=19, column=3)



# def perintah():
#     print(data.get())
#     data.delete(0,END)
# button = Button(text = "Tekan", font = "Normal 25", activebackground = "Blue", command=perintah)
# button.grid(row=1, column=1)

# teks = Text(width = 33, height = 10, bd = 10, font = "Normal 15")
# teks.grid(row=2, column=0)

# l_trapesium=0.5*(sisi_a+sisi_b)*t
# K_trapesium=a+b+c+d

root.mainloop()