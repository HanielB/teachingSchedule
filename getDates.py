#!/usr/bin/env python3

import argparse, codecs

from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

contents = []

holidays = {
    2022 :
    {
        "20220101": "Ano novo",
        "20220228": "Carnaval",
        "20220301": "Carnaval",
        "20220302": "Carnaval",
        "20220415": "Paixão de Cristo",
        "20220421": "Tiradentes",
        "20220501": "Dia do Trabalho",
        "20220616": "Corpus Christi",
        "20220617": "Imprensado",
        "20220815": "Assunção de Nossa Senhora",
        "20220907": "Independência do Brasil",
        "20221012": "Padroeira do Brasil",
        "20221028": "Dia do Servidor Público",
        "20221102": "Finados",
        "20221115": "Proclamação da República",
        "20221208": "Imaculada Conceição",
        "20221225": "Natal"
    },
    2023 :
    {
        "20230101": "Ano novo",
        "20230220": "Carnaval",
        "20230221": "Carnaval",
        "20230222": "Carnaval",
        "20230407": "Paixão de Cristo",
        "20230421": "Tiradentes",
        "20230501": "Dia do Trabalho",
        "20230608": "Corpus Christi",
        "20230609": "Imprensado",
        "20230815": "Assunção de Nossa Senhora",
        "20230907": "Independência do Brasil",
        "20231012": "Padroeira do Brasil",
        "20231028": "Dia do Servidor Público",
        "20231102": "Finados",
        "20231115": "Proclamação da República",
        "20231208": "Imaculada Conceição",
        "20231225": "Natal"
    },
    2024 :
    {
        "20240101": "Ano novo",
        "20240212": "Carnaval",
        "20240213": "Carnaval",
        "20240214": "Carnaval",
        "20240329": "Paixão de Cristo",
        "20240421": "Tiradentes",
        "20240501": "Dia do Trabalho",
        "20240530": "Corpus Christi",
        "20240531": "Imprensado",
        "20240815": "Assunção de Nossa Senhora",
        "20240907": "Independência do Brasil",
        "20241012": "Padroeira do Brasil",
        "20241028": "Dia do Servidor Público",
        "20241102": "Finados",
        "20241115": "Proclamação da República",
        "20241208": "Imaculada Conceição",
        "20241225": "Natal"
    },
    2025 :
    {
        "20250101": "Ano novo",
        "20250303": "Carnaval",
        "20250304": "Carnaval",
        "20250305": "Carnaval",
        "20250418": "Paixão de Cristo",
        "20250421": "Tiradentes",
        "20250501": "Dia do Trabalho",
        "20250619": "Corpus Christi",
        "20250620": "Imprensado",
        "20250815": "Assunção de Nossa Senhora",
        "20250907": "Independência do Brasil",
        "20251012": "Padroeira do Brasil",
        "20251028": "Dia do Servidor Público",
        "20251102": "Finados",
        "20251115": "Proclamação da República",
        "20251208": "Imaculada Conceição",
        "20251225": "Natal"
    },
}

def printDate(count, formatDate, fromAdded, printLatex):
  global contents
  if printLatex:
    while True:
      loop = False
      content = contents[count] if count < len(contents) else ""
      if content.startswith("*"):
        loop = True
        content = content[1:]
        contents = contents[:count] + contents[count + 1:]
      print("{0}{1} & {2} & {3} \\\\".format("*" if fromAdded else "", "{0:2d}".format(count + 1) if not loop else "--",
                                              curr.strftime(formatDate), content))
      if not loop:
        break
  else:
    print("{0}{1:2d}: {2}".format("*" if fromAdded else "", count + 1, curr.strftime(formatDate)))



def nextWeekday(d, weekday):
    daysAhead = weekday - d.weekday()
    if daysAhead <= 0: # Target day already happened this week
        daysAhead += 7
    return d + timedelta(daysAhead)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--start', dest="start", help='Start date (in format YYYYMMDD)')
    parser.add_argument('--format', dest="format", choices = ["long", "short", "latex"],
                        default="long", help='Format in which to print dates (def. long: YYYY-MM-DD day)')
    parser.add_argument('--regularity', dest="regularity",
                        default=2, help='Interval between entries (def. 2)')
    parser.add_argument('--per-week', dest="per_week",
                        default=2,
                        help='How many entries per week (def. 2). Next week will start on same day of start date')
    parser.add_argument('--max', dest="max",
                        default=30, help='Generate up to max entries (def. 30)')
    parser.add_argument('--block', dest="blocked", action='append', default=[],
                        help="Add date to block (YYYYMMDD[..YYYYMMDD])")
    parser.add_argument('--add', dest="added", action='append', default=[],
                        help="Add ad-hoc date to consider (YYYYMMDD)")

    parser.add_argument('-c', dest="content", default=[],
                        help="Read file with contents (one per line)")

    args = parser.parse_args()

    if not args.start:
      print("Need start date")
      quit()

    blocked = []
    for block in args.blocked:
      if not ".." in block:
        lb = datetime.strptime(block, '%Y%m%d')
        blocked += [(lb, lb)]
        continue
      split = block.split("..")
      lb = datetime.strptime(split[0], '%Y%m%d')
      ub = datetime.strptime(split[1], '%Y%m%d')
      blocked += [(lb, ub)]

    added = sorted([datetime.strptime(x, '%Y%m%d') for x in args.added])

    if args.content:
      with open(args.content,"rb") as readContents:
        contents = list(codecs.iterdecode(readContents, 'utf-8'))
        contents = [c.replace("\n","") for c in contents]

    curr = datetime.strptime(args.start, '%Y%m%d')
    lastRegular = curr
    startDay = curr.weekday()
    formatDate = "%Y-%m-%d %a" if args.format == "long" else "%d/%m (%a)"
    printLatex = args.format == "latex"
    count = 0
    weekly = 0
    fromAdded = False
    while count < args.max or count < len(contents):
      # get date in format in holidays set
      printedDate = curr.strftime("%Y%m%d")
      # skip holidays and blocked dates
      if not (printedDate in holidays[curr.year] or list(filter(lambda x : curr >= x[0] and curr <= x[1], blocked))):
        printDate(count, formatDate, fromAdded, printLatex)
        if fromAdded:
          fromAdded = False
        count += 1
      else:
        if printLatex:
          print("-- & {0} & {1} \\\\".format(curr.strftime(formatDate), holidays[curr.year][printedDate] if printedDate in holidays[curr.year] else "Blocked"))
        else:
          print("--: {0}".format(curr.strftime(formatDate)))

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
