# -*- coding: utf-8 -*-

"""flake8chart: flake8 stats visualised
"""

import sys
import string
import itertools
import time
import pprint
import csv

try:
    import click
    import pygal
except ImportError as e:
    print("error: {0}".format(e))
    sys.exit(1)

if sys.version_info[0] == 3:
    import functools
    reduce = functools.reduce

# ref: http://flake8.readthedocs.org/en/latest/warnings.html
CODES = {"E1": "Indentation",
         "E2": "Whitespace",
         "E3": "Blank line",
         "E4": "Import",
         "E5": "Line length",
         "E7": "Statement",
         "E9": "Runtime",
         "W1": "Indentation",
         "W2": "Whitespace",
         "W3": "Blank line",
         "W6": "Deprecation",
         "F4": "Module",
         "F8": "Name"}
CHART_TYPE_PIE = "PIE"
CHART_TYPE_BAR = "BAR"
CHART_TYPES = (CHART_TYPE_PIE, CHART_TYPE_BAR,)


def split_str(s, sep=None, maxsplit=2):
    return (s.split(sep=sep, maxsplit=maxsplit)
            if sys.version_info[0] == 3 else
            string.split(s, sep=sep, maxsplit=maxsplit))


def is_stat(items):
    return len(items) == 3 and items[0].isdigit() and len(items[1]) == 4


def pipe(*fns):
    def _pipe(*args, **kwargs):
        return reduce(lambda r, g: g(r),
                      fns[1:],
                      fns[0](*args, **kwargs))

    return _pipe


def dict_rows(rows):
    for r in rows:
        split = split_str(r)

        if not is_stat(split):
            continue

        yield {"count": int(split[0]),
               "code": split[1],
               "desc": split[2]}


def group_by_code(rows):
    return itertools.groupby(sorted(rows, key=lambda r: r["code"]),
                             key=lambda r: r["code"][:2])


def calc_sum(rows):
    return ({"code": "{code}: {desc}".format(code=code,
                                             desc=CODES.get(code, "?")),
             "count": sum(r["count"] if isinstance(r["count"], int) else
                          int(r["count"]) for r in iterable)}
            for code, iterable in rows)


def sort_by_count(rows):
    return sorted(rows, key=lambda r: r["count"], reverse=True)


def get_total(rows):
    return sum(r["count"] for r in rows)


def chart_pie(rows, title="Title", filename="pie_chart.svg"):
    chart = pygal.Pie()
    chart.title = title

    for row in rows:
        chart.add(row["code"], row["count"])

    return chart.render_to_file(filename)


def chart_bar(rows, title="Title", filename="bar_chart.svg"):
    chart = pygal.Bar()
    chart.title = title

    for row in rows:
        chart.add(row["code"], row["count"])

    return chart.render_to_file(filename)


def elapsed(f):
    def _elapsed(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        click.echo("time elapsed: %.2f seconds" % (time.time() - start,))
        return result

    return _elapsed


@click.command()
@click.option("--chart-type",
              default=CHART_TYPE_PIE,
              type=click.Choice(CHART_TYPES),
              help="type of chart (default: {0})".format(CHART_TYPE_PIE))
@click.option("--chart-output",
              default="flake8_stats.svg",
              help=("name of SVG file to export (default: {0})"
                    "".format("flake8_stats.svg")))
@click.option("--csv-output",
              help="name of CSV file to export")
@elapsed
def flake8chart(chart_type, chart_output, csv_output):
    click.echo("chart-type: {0}".format(chart_type))
    click.echo("chart_output: {0}".format(chart_output))
    click.echo("csv-output: {0}".format(csv_output))

    # sort stats by count
    stats = sorted([r for r in sys.stdin.read().split("\n")
                    if is_stat(split_str(r))],
                   key=lambda r: int(r.split()[0]),
                   reverse=True)
    if not stats:
        click.echo("error: no stats found")
        return
    click.echo("stats:")
    click.echo(pprint.pformat(stats))

    # aggregate stats
    pipeline = pipe(dict_rows,
                    group_by_code,
                    calc_sum,
                    sort_by_count,)
    stats_summary = pipeline(stats)

    click.echo("stats summary:")
    click.echo(pprint.pformat(stats_summary))

    # export chart (svg)
    if stats_summary:
        if chart_type.upper() == "PIE":
            chart_pie(stats_summary,
                      title="flake8 stats (%)",
                      filename=chart_output)
            click.echo("pie chart exported: '{0}'".format(chart_output))
        else:
            chart_bar(stats_summary,
                      title=("flake8 stats "
                             "(total: {0})".format(get_total(stats_summary))),
                      filename=chart_output)
            click.echo("bar chart exported: '{0}'".format(chart_output))

    # export stats summary (csv)
    if csv_output:
        with open(csv_output, "w") as file:
            writer = csv.DictWriter(file, fieldnames=["code", "count"])
            writer.writeheader()
            writer.writerows(stats_summary)
            click.echo("csv output exported: '{0}'".format(csv_output))


if __name__ == "__main__":
    flake8chart()
