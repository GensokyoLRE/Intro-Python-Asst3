"""
Program: theProgramThatMadeMeDieInside.py
Author: Phillip "Hifumi" Cuesta
Last Mod: 9/22/18
Purpose: Assignment for week 5. But... whyyyyyyyyyyyy doe.
"""
import random

theList, theRand = [2], random.randint(5, 8)
while len(theList) != theRand:
    theList.append(random.randint(theList[-1], (theList[-1] ** 2)))
print(f'List: {theList}  - Sum: {sum(theList)} - Median: {theList[(len(theList)) // 2]} - Avg: {sum(theList) /2}')
