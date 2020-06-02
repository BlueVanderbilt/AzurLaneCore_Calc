import datetime, math

x = datetime.datetime.now()
if x.year % 4 == 0 and (x.year % 100 != 0 or x.year % 400 == 0): leap = "true"
else: leap = "false"
    
def core_calc(month, event, event_days, core):
    if month == 2 and leap == "true": total = 29
    elif month == 2 and leap == "false": total = 28
    elif month in (4, 6, 9, 11): total = 30
    elif month in (1, 3, 5, 7, 8, 10, 12): total = 31
    else: print("Invalid month.")
    if event == 1:
        left = total - event_days; week_core = math.floor(total/7); print((core * 3 * left) + (core * 3 * event_days * 3) + total * 5 + week_core * 15)
    else: week_core = math.floor(total/7); print(core * 3 * total + total * 5 + week_core * 15)

'''
Instructions on how to use:

1st argument is Month, any number ranging from 1 to 12
2nd argument is event, 1 means yes and any other number means no
3rd argument is event_days, how many days the 3x core event lasts for
4th argument is core, means how many core data do you get per clear, e.g: Chapter 8 would be 20 core data per clear

Lastly, this code is 100% accurate. 

'''

core_calc(6, 1, 9, 20) #This here is a template, change these numbers to fit your needs. 
         #1, 2, 3, 4
