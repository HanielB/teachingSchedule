# teachingSchedule

A simple script to automatically put together a teaching schedule based on a few parameters and skipping reserved days (like holidays).

For example, running
```Python
./getDates.py --start 20220822 --block 20220905 --block 20221031 --add 20221015 --add 20221022 --add 20221203 --format short
```
yields 
```
 1: 22/08 (Mon)
 2: 24/08 (Wed)
 3: 29/08 (Mon)
 4: 31/08 (Wed)
 5: 12/09 (Mon)
 6: 14/09 (Wed)
 7: 19/09 (Mon)
 8: 21/09 (Wed)
 9: 26/09 (Mon)
10: 28/09 (Wed)
11: 03/10 (Mon)
12: 05/10 (Wed)
13: 10/10 (Mon)
14: 15/10 (Sat)
15: 17/10 (Mon)
16: 19/10 (Wed)
17: 22/10 (Sat)
18: 24/10 (Mon)
19: 26/10 (Wed)
20: 07/11 (Mon)
21: 09/11 (Wed)
22: 14/11 (Mon)
23: 16/11 (Wed)
24: 21/11 (Mon)
25: 23/11 (Wed)
26: 28/11 (Mon)
27: 30/11 (Wed)
28: 03/12 (Sat)
29: 05/12 (Mon)
30: 07/12 (Wed)
```
