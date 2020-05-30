def core_calc(month, event, event_days, core):
    if month == 2: total = 28
    elif month in (4, 6, 9, 11): total = 30
    elif month in (1, 3, 5, 7, 8, 10, 12): total = 31
    else: print("Invalid month.")
    if event == 1:
        left = total - event_days; week_core = round(total/7); print((core * 3 * left) + (core * 3 * event_days * 3) + total * 5 + week_core * 15)
    else: week_core = round(total/7); print(core * 3 * total + total * 5 + week_core * 15)

'''
Instructions on how to use:

1st argument is Month, any number ranging from 1 to 12
2nd argument is event, 1 means yes and any other number means no. 
3rd argument is event_days, pretty self explainable
4th argument is core, just means how many core data do you get per clear, F.E: Chapter 8 would be 20 core data per clear

Lastly, this code is 100% accurate for non leap years as 28/7 = 4, 30/7 = 4.28 (Rounded to 4), 31/7 = 4.42 (Rounded to 4)
If calculating core data for leap year and the month of February, just +5 core data to the output.

'''

core_calc(6, 1, 9, 20)
         #1, #2, #3, #4
