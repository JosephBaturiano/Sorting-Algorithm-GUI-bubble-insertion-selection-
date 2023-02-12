import tkinter
from tkinter import *

root = Tk()
root.title("SORTING ALGORITHMS")
root.geometry("449x500")
root.config(bg="gray58")

random_num = [66, 35, 88, 93, 28, 59, 97, 69, 62, 9]

# BUBBLE SORT


def bubble_sort():
    print("\n\t\tTHE NUMBERS ARE SORTED NOW USING BUBBLE SORT\n")
    for i in range(len(random_num)-1, 0, -1):
        for j in range(i):
            if random_num[j] > random_num[j+1]:
                swap = random_num[j]
                random_num[j] = random_num[j+1]
                random_num[j+1] = swap
                print(random_num)
                result.insert(tkinter.END, random_num)
                result.insert(tkinter.END, ('\n'))

# INSERTION SORT


def insertion_sort():
    print("\n\t\tTHE NUMBERS ARE SORTED NOW USING INSERTION SORT\n")
    for i in range(1, len(random_num)):
        anchor = random_num[i]
        j = i - 1
        while j >= 0 and anchor < random_num[j]:
            random_num[j+1] = random_num[j]
            j = j - 1
        random_num[j+1] = anchor
        print(random_num)
        result.insert(tkinter.END, random_num)
        result.insert(tkinter.END, ('\n'))
