import datetime

x = datetime.datetime.now()
leap = 1 if x.year % 4 == 0 and (x.year % 100 != 0 or x.year % 400 == 0) else 0

def core_calc(month, event, days, core):
    total = 29 if month == 2 and leap == 1 else 28 
    if month in (4, 6, 9, 11): total = 30
    elif month in (1, 3, 5, 7, 8, 10, 12): total = 31
    left = total - days; print((core * 3 * left) + (core * 9 * days) + total * 5 + 60) if event == 1 else print(core * 3 * total + total * 5 + 60)
        
'''
Instructions on how to use)

1st argument is month: any number ranging from 1 through 12
2nd argument is event: 1 means yes and any other number means no 
3rd argument is days: refers to how many days the 3x core event lasts for
4th argument is core: how much core data you get per clear, e.g: Chapter 8 would be 20 core data per clear
'''

#core_calc(6, 1, 9, 20)
          #1, 2, 3, 4 
