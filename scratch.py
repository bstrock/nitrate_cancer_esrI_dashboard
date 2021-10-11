renderer = {'type': 'classBreaks',
            'visualVariables': [],
            'rotationType': 'arithmetic',
            'minValue': 0,
            'field': 'canrate',
            'defaultSymbol': {
                'type': 'esriSFS',
                'style': 'esriSFSSolid',
                'color': [0, 0, 0, 255],
                'outline': {
                    'style': 'esriSLSSolid',
                    'type': 'esriSLS',
                    'width': 0.5,
                    'color': [128, 128, 128, 0]
                }
            },
            'defaultLabel': 'Other',
            'classificationMethod': 'esriNaturalBreaks',
            'classBreakInfos': [
                {'classMaxValue': 8,
                 'label': '0 - 8%',
                 'description': '0 - 8%',
                 'symbol': {
                     'type': 'esriSFS',
                     'style': 'esriSFSSolid',
                     'color': [237, 248, 251, 255],
                     'outline': {
                         'style': 'esriSLSSolid',
                         'type': 'esriSLS',
                         'width': 0.5,
                         'color': [128, 128, 128, 0]
                     }
                 }
                 },
                {
                    'classMaxValue': -2.5,
                    'label': '> 2.5 St. Dev',
                    'description': '> 2.5 St. Dev',
                    'symbol': {
                        'type': 'esriSFS',
                        'style': 'esriSFSSolid',
                        'color': [],
                        'outline': {}
                    }
                },
                {'classMaxValue': -1.5, 'label': '-2.5 - -1.5 St. Dev', 'description': '-2.5 - -1.5 St. Dev',
                 'symbol': {
                     'type': 'esriSFS', 'style': 'esriSFSSolid', 'color': [],
                     'outline': {'style': 'esriSLSSolid', 'type': 'esriSLS', 'width': 0.5,
                                 'color': [128, 128, 128, 0]}}},
                {'classMaxValue': 61, 'label': '41 - 61%', 'description': '41 - 61%',
                 'symbol': {'type': 'esriSFS', 'style': 'esriSFSSolid', 'color': [44, 162, 95, 255],
                            'outline': {'style': 'esriSLSSolid', 'type': 'esriSLS', 'width': 0.5,
                                        'color': [128, 128, 128, 0]}}},
                {'classMaxValue': 110, 'label': '63% +', 'description': '63% +',
                 'symbol': {'type': 'esriSFS', 'style': 'esriSFSSolid', 'color': [0, 109, 44, 255],
                            'outline': {'style': 'esriSLSSolid', 'type': 'esriSLS', 'width': 0.5,
                                        'color': [128, 128, 128, 0]}}}]}

tracts_outline = {
    'style': 'esriSLSSolid',
    'type': 'esriSLS',
    'color': [0, 0, 0, 120],
    'width': .5
}
tracts_renderer = {
    'type': 'classBreaks',
    'visualVariables': [],
    'rotationType': 'arithmetic',
    'minValue': 0,
    'field': 'canrate',
    'defaultSymbol': {
        'type': 'esriSFS',
        'style': 'esriSFSSolid',
        'color': [27, 141, 102, 255],
        'outline': tracts_outline
    },
    'defaultLabel': 'Other',
    'classificationMethod': 'esriNaturalBreaks',
    'classBreakInfos':
        [
            {
                'classMaxValue': 0.08,
                'label': '0 - 8%',
                'description': '0 - 8%',
                'symbol': {
                    'type': 'esriSFS',
                    'style': 'esriSFSSolid',
                    'color': [240, 249, 232, 255],
                    'outline': tracts_outline
                }
            },
            {
                'classMaxValue': .22,
                'label': '9 - 22%',
                'description': '9 - 22%',
                'symbol': {
                    'type': 'esriSFS',
                    'style': 'esriSFSSolid',
                    'color': [186, 228, 188, 255],
                    'outline': tracts_outline
                }
            },
            {
                'classMaxValue': .39,
                'label': '23 - 39%',
                'description': '23 - 39%',
                'symbol': {
                    'type': 'esriSFS',
                    'style': 'esriSFSSolid',
                    'color': [123, 204, 196, 255],
                    'outline': tracts_outline
                }
            },
            {
                'classMaxValue': .61,
                'label': '40 - 61%',
                'description': '40 - 61%',
                'symbol': {
                    'type': 'esriSFS',
                    'style': 'esriSFSSolid',
                    'color': [67, 162, 202, 255],
                    'outline': tracts_outline
                }
            },
            {
                'classMaxValue': 1.1,
                'label': '62% +',
                'description': '62% +',
                'symbol': {
                    'type': 'esriSFS',
                    'style': 'esriSFSSolid',
                    'color': [8, 104, 172, 255],
                    'outline': tracts_outline
                }
            }
        ]
}

stdev = {'type': 'classBreaks',
         'visualVariables': [],
         'rotationType': 'arithmetic',
         'minValue': 0,
         'field': 'stdresid',
         'defaultSymbol': {'type': 'esriSFS', 'style': 'esriSFSSolid', 'color': [0, 0, 0, 255],
                           'outline': {'style': 'esriSLSSolid', 'type': 'esriSLS', 'width': 0.5,
                                       'color': [128, 128, 128, 255]}},
         'defaultLabel': 'Other',
         'classificationMethod': 'esriNaturalBreaks',
         'classBreakInfos': [
        {'classMaxValue': -2.5, 'label': '< 2.5 St. Dev', 'description': '< 2.5 St. Dev',
         'symbol': {'type': 'esriSFS', 'style': 'esriSFSSolid', 'color': [237, 248, 251, 255],
                    'outline': {'style': 'esriSLSSolid', 'type': 'esriSLS', 'width': 0.5,
                                'color': [128, 128, 128, 255]}}},
        {'classMaxValue': -1.5, 'label': '-2.5 to -1.5 St. Dev', 'description': '-2.5 to -1.5 St. Dev',
         'symbol': {'type': 'esriSFS', 'style': 'esriSFSSolid', 'color': [204, 236, 230, 255],
                    'outline': {'style': 'esriSLSSolid', 'type': 'esriSLS', 'width': 0.5,
                                'color': [128, 128, 128, 255]}}},
        {'classMaxValue': -0.5, 'label': '-1.5 to -.5 St. Dev', 'description': '-1.5 to -.5 St. Dev',
         'symbol': {'type': 'esriSFS', 'style': 'esriSFSSolid', 'color': [153, 216, 201, 255],
                    'outline': {'style': 'esriSLSSolid', 'type': 'esriSLS', 'width': 0.5,
                                'color': [128, 128, 128, 255]}}},
        {'classMaxValue': 0.5, 'label': '-.5 to .5 St. Dev', 'description': '.5 to 1.5 St. Dev',
         'symbol': {'type': 'esriSFS', 'style': 'esriSFSSolid', 'color': [102, 194, 164, 255],
                    'outline': {'style': 'esriSLSSolid', 'type': 'esriSLS', 'width': 0.5,
                                'color': [128, 128, 128, 255]}}},
        {'classMaxValue': 1.5, 'label': '1.5 - 2.5 St. Dev', 'description': '1.5 - 2.5 St. Dev',
         'symbol': {'type': 'esriSFS', 'style': 'esriSFSSolid', 'color': [65, 174, 118, 255],
                    'outline': {'style': 'esriSLSSolid', 'type': 'esriSLS', 'width': 0.5,
                                'color': [128, 128, 128, 255]}}},
        {'classMaxValue': 999, 'label': '> 2.5 St. Dev', 'description': '> 2.5 St. Dev',
         'symbol': {'type': 'esriSFS', 'style': 'esriSFSSolid', 'color': [35, 139, 69, 255],
                    'outline': {'style': 'esriSLSSolid', 'type': 'esriSLS', 'width': 0.5,
                                'color': [128, 128, 128, 255]}}}]}
