test = {   'name': 'q3b',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> df_1972_to_2016_clean.shape == (51, 12)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> df_1972_to_2016_clean.index.name == 'State'\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> all(df_1972_to_2016_clean.columns == [str(x) for x in np.arange(1972, 2017, 4)])\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> df_1972_to_2016_clean.index[-1] == 'Wyoming'\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.all(df_1972_to_2016_clean.applymap(lambda x: str(x) in ['D', 'R']))\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
