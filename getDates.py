#!/usr/bin/env python3

import argparse

from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

holidays = {2022 : [
  "20220101",
  "20220228",
  "20220301",
  "20220302",
  "20220415",
  "20220421",
  "20220501",
  "20220616",
  "20220815",
  "20220907",
  "20221012",
  "20221028",
  "20221102",
  "20221115",
  "20221208",
  "20221225"],
            2023 : [
              "20230101",
              "20230220",
              "20230221",
              "20230222",
              "20230407",
              "20230421",
              "20230501",
              "20230608",
              "20230609",
              "20230815",
              "20230907",
              "20231012",
              "20231028",
              "20231102",
              "20231115",
              "20231208",
              "20231225"          ]

}

def nextWeekday(d, weekday):
    daysAhead = weekday - d.weekday()
    if daysAhead <= 0: # Target day already happened this week
        daysAhead += 7
    return d + timedelta(daysAhead)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--start', dest="start", help='Start date (in format YYYYMMDD)')
    parser.add_argument('--format', dest="format", choices = ["long", "short"],
                        default="long", help='Format in which to print dates (def. long: YYYY-MM-DD day)')
    parser.add_argument('--regularity', dest="regularity",
                        default=2, help='Interval between entries (def. 2)')
    parser.add_argument('--per-week', dest="per_week",
                        default=2,
                        help='How many entries per week (def. 2). Next week will start on same day of start date')
    parser.add_argument('--max', dest="max",
                        default=30, help='Generate up to max entries (def. 30)')
    parser.add_argument('--block', dest="blocked", action='append', default=[],
                        help="Add date to block (YYYYMMDD)")
    parser.add_argument('--add', dest="added", action='append', default=[],
                        help="Add ad-hoc date to consider (YYYYMMDD)")

    args = parser.parse_args()

    if not args.start:
      print("Need start date")
      quit()

    added = sorted([datetime.strptime(x, '%Y%m%d') for x in args.added])

    curr = datetime.strptime(args.start, '%Y%m%d')
    lastRegular = curr
    startDay = curr.weekday()
    formatDate = "%Y-%m-%d %a" if args.format == "long" else "%d/%m (%a)"
    count = 0
    weekly = 0
    fromAdded = False
    while count < args.max:
      # get date in format in holidays set
      printedDate = curr.strftime("%Y%m%d")
      # skip holidays and blocked dates
      if not (printedDate in holidays[curr.year] or printedDate in args.blocked):
        if fromAdded:
          print("*{0:2d}: {1}".format(count + 1, curr.strftime(formatDate)))
          fromAdded = False
        else:
          print("{0:3d}: {1}".format(count + 1, curr.strftime(formatDate)))
        count += 1
      else:
        print(" --: {1}".format(count + 1, curr.strftime(formatDate)))

      weekly += 1
      assert not added or added[0] > curr
      # if there is an added entry between curr and the next entry, consider the added one first
      if added and added[0] - curr < timedelta(days=7) and \
      ((weekly == args.per_week and nextWeekday(curr, startDay) > added[0]) \
       or (curr + timedelta(days=args.regularity) > added[0])):
        if (weekly == args.per_week and nextWeekday(curr, startDay) > added[0]):
          weekly -= 1
        curr = added[0]
        # remove current head
        added = added[1:]
        fromAdded = True
        continue

      # reset to initial weekday if completed entries per week
      if weekly == args.per_week:
        curr = nextWeekday(curr, startDay)
        weekly = 0
      # otherwise get next entry this week
      else:
        curr = lastRegular + timedelta(days=args.regularity)
      lastRegular = curr
