with open("speed_tests_results", 'r') as f:

    statistics = {
        "<class 'pure_python.Fate'>": [],
        "<class 'pure_cython.Fate'>": [],
        "<class 'pyx_cython.Fate'>": [],
        "<class 'mypy_python.Fate'>": []
    }

    for test in f:
        a = test.split()
        if a == []:
            continue
        statistics[f'{a[0]} {a[1]}'].append(float(a[3]))

    for key in statistics.keys():
        print(f'{key} middle time is {sum(statistics[key]) / 10}')
