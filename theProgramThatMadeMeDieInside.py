"""
Program: theProgramThatMadeMeDieInside.py
Author: Phillip "Hifumi" Cuesta
Last Mod: 9/23/18
Purpose: Assignment for week 5. But... whyyyyyyyyyyyy doe.
"""
import random

tL, theRand = [2], random.randint(5, 8)
while len(tL) != theRand:
    tL.append(random.randint(tL[-1], (tL[-1] * 2)))
print('List: %s - Sum: %i - Median: %.0f - Avg: %.2f' % (', '.join(map(str, tL)), sum(tL), tL[len(tL)//2] if len(tL) % 2 == 1 else (tL[(len(tL) // 2) - 1] + tL[len(tL) // 2]), sum(tL) / 2))
