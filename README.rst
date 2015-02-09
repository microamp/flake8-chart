flake8-chart
============

flake8 stats visualised

Installation
------------
.. code-block:: console

    $ pip install flake8-chart

Dependencies
------------
* click
* pygal

Help
----
.. code-block:: console

    $ python flake8charts.py --help

.. code-block:: console

    Usage: flake8charts.py [OPTIONS]

    Options:
      --chart-type [PIE|BAR]  type of chart (default: PIE)
      --chart-output TEXT     name of SVG file to export (default:
                              flake8_stats.svg)
      --csv-output TEXT       name of CSV file to export
      --help                  Show this message and exit.

Usage
-----
`flake8-chart` takes the output of `flake8` as an input. Make sure the `--statistics` flag is on with `flake8`.

.. code-block:: console

    $ flake8 --statistics ~/devel/projs/fn.py | \
    > python flake8chart.py --chart-type=PIE --chart-output=stats_pie.svg --csv-output=stats.csv

Chart Examples
--------------
* [pie chart](https://github.com/microamp/flake8-chart/blob/master/output/svg/stats_pie.svg)
* [bar graph](https://github.com/microamp/flake8-chart/blob/master/output/svg/stats_bar.svg)

Versions Tested
---------------
* Python 2.7
* Python 3.4

License
-------
MIT
