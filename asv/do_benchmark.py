# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst

# This file, unlike all others, must be compatible with as many
# versions of Python as possible and have no external dependencies.
# This is the only bit of code from asv that is actually loaded into
# the benchmarking process.

import sys
import time
import timeit
import unittest


if __name__ == '__main__':
    benchmark_dir = sys.argv[-2]
    test_id = sys.argv[-1]
    sys.path.insert(0, benchmark_dir)

    test = list(unittest.defaultTestLoader.loadTestsFromName(test_id))[0]

    timefunc = timeit.default_timer
    number = 0
    repeat = timeit.default_repeat
    timefunc = time.time

    timer = timeit.Timer(
        stmt=test.run, setup=test.setUp, timer=timefunc)

    if number == 0:
        # determine number so that 0.2 <= total time < 2.0
        number = 1
        for i in range(1, 10):
            if timer.timeit(number) >= 0.2:
                break
            number *= 10
    all_runs = timer.repeat(repeat, number)
    best = min(all_runs) / number
    print(best)
