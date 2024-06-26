# teachingSchedule

A simple script to automatically put together a teaching schedule based on a few parameters and skipping reserved days (like holidays).

For example, running
```Python
./getDates.py  --start 20240923 --block 20241223..20250103 "Recesso de fim de ano" --annotate 20241030 "Help" --format short
```
yields
```
 1: 23/09 (Mon)
 2: 25/09 (Wed)
 3: 30/09 (Mon)
 4: 02/10 (Wed)
 5: 07/10 (Mon)
 6: 09/10 (Wed)
 7: 14/10 (Mon)
 8: 16/10 (Wed)
 9: 21/10 (Mon)
10: 23/10 (Wed)
11: 28/10 (Mon)
12: 30/10 (Wed) (Help)
13: 04/11 (Mon)
14: 06/11 (Wed)
15: 11/11 (Mon)
16: 13/11 (Wed)
17: 18/11 (Mon)
18: 20/11 (Wed)
19: 25/11 (Mon)
20: 27/11 (Wed)
21: 02/12 (Mon)
22: 04/12 (Wed)
23: 09/12 (Mon)
24: 11/12 (Wed)
25: 16/12 (Mon)
26: 18/12 (Wed)
--: 23/12 (Mon) (Blocked: Recesso de fim de ano)
--: 25/12 (Wed) (Holiday: Natal)
--: 30/12 (Mon) (Blocked: Recesso de fim de ano)
--: 01/01 (Wed) (Holiday: Ano novo)
27: 06/01 (Mon)
28: 08/01 (Wed)
29: 13/01 (Mon)
30: 15/01 (Wed)
```
