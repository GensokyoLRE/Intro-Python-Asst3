"""
Program: theProgramThatMadeMeDieInside2.py
Author: Phillip "Hifumi" Cuesta
Last Mod: 9/23/18
Purpose: Assignment for week 5. But... whyyyyyyyyyyyy doe.
"""
import random

tL, theRand, mD, avg, mdPt = [2], random.randint(5, 8), 0, 2, 0
while len(tL) != theRand:
    tL.append(random.randint(tL[-1], (tL[-1] * 2))); mD = len(tL)//2; avg += tL[-1]; mdP = int((tL[mD-1] + tL[mD]) / 2)
print("List: %s  - Sum: %i - Median: %f - Avg: %f" % (tL, sum(tL), tL[mD] if (len(tL) % 2 == 1) else tL[mdP], avg/2))
