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

    $ flake8chart --help

.. code-block:: console

    Usage: flake8chart [OPTIONS]

    Options:
      --chart-type [PIE|BAR]  type of chart (default: 'PIE')
      --chart-title TEXT      title of chart (default: 'flake8 stats')
      --chart-output TEXT     name of SVG file to export (default:
                              'flake8_stats.svg')
      --csv-output TEXT       name of CSV file to export
      --help                  Show this message and exit.

Usage
-----
``flake8chart`` takes the output of ``flake8`` as an input. Make sure the ``--statistics`` flag is on with ``flake8``.

.. code-block:: console

    $ flake8 --statistics ~/devel/projs/fn.py | \
    > flake8chart \
    > --chart-type=PIE --chart-output=stats_pie.svg \
    > --csv-output=stats.csv

Chart Examples
--------------
* `pie chart`_
* `bar graph`_

Versions Tested
---------------
* Python 2.7
* Python 3.4
* Python 3.5

License
-------
MIT

.. _pie chart: https://rawgit.com/microamp/flake8-chart/master/output/svg/stats_pie.svg
.. _bar graph: https://rawgit.com/microamp/flake8-chart/master/output/svg/stats_bar.svg
