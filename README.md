flake8-chart
============

TODO

Help
----
```bash
$ python flake8charts.py --help
```
```
Usage: flake8charts.py [OPTIONS]

Options:
  --chart-type [PIE|BAR]  type of chart (default: PIE)
  --chart-output TEXT     name of SVG file to export (default:
                          flake8_stats.svg)
  --csv-output TEXT       name of CSV file to export
  --help                  Show this message and exit.
```

Usage
-----
`flake8-chart` takes the output of `flake8` as the input. Make sure the `--statistics` flag is on when `flake8` is executed.
```bash
$ flake8 --quiet --statistics /path/to/some/repo | python flake8chart.py --chart-type=BAR --chart-output=stats_bar.svg --csv-output=stats.csv
```

Examples
--------
* [pie chart](https://github.com/microamp/flake8-chart/blob/master/output/svg/stats_pie.svg)
* [bar graph](https://github.com/microamp/flake8-chart/blob/master/output/svg/stats_bar.svg)

License
-------
MIT
