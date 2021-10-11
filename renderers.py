from typing import List, Dict, AnyStr
from copy import deepcopy
from colorbewer import colors
from re import findall


class CustomRenderer:

    wells_outline = {
        'style': 'esriSLSSolid',
        'type': 'esriSLS',
        'color': [0, 0, 0, 120],
        'width': .5
    }

    wells_renderer = {
        'type': 'classBreaks',
        'visualVariables': [],
        'rotationType': 'arithmetic',
        'minValue': 0,
        'field': 'nitr_ran',
        'defaultSymbol': {
            'type': 'esriSMS',
            'style': 'esriSMSCircle',
            'color': [255, 255, 255, 165],
            'size': 2,
            'angle': 0,
            'xoffset': 0,
            'yoffset': 0,
            'outline': wells_outline
        },
        'defaultLabel': 'Other',
        'classificationMethod': 'EsriClassifyNaturalBreaks',
        'classBreakInfos':
            [
                {
                    'classMaxValue': 2,
                    'label': '0 - 2 mg/L',
                    'description': '0 - 2 mg/L',
                    'symbol': {
                        'type': 'esriSMS',
                        'style': 'esriSMSCircle',
                        'color': [255, 255, 255, 165],
                        'size': 2,
                        'angle': 0,
                        'xoffset': 0,
                        'yoffset': 0,
                        'outline': wells_outline
                    }
                },
                {
                    'classMaxValue': 6,
                    'label': '3 - 6 mg/L',
                    'description': '3 - 6 mg/L',
                    'symbol': {
                        'type': 'esriSMS',
                        'style': 'esriSMSCircle',
                        'color': [255, 255, 255, 165],
                        'size': 4,
                        'angle': 0,
                        'xoffset': 0,
                        'yoffset': 0,
                        'outline': wells_outline
                    }
                },
                {
                    'classMaxValue': 10,
                    'label': '7 - 10 mg/L',
                    'description': '7 - 10 mg/L',
                    'symbol': {
                        'type': 'esriSMS',
                        'style': 'esriSMSCircle',
                        'color': [255, 255, 255, 165],
                        'size': 6,
                        'angle': 0,
                        'xoffset': 0,
                        'yoffset': 0,
                        'outline': wells_outline
                    }
                },
                {
                    'classMaxValue': 14,
                    'label': '11 - 14 mg/L',
                    'description': '11 - 14 mg/L',
                    'symbol': {
                        'type': 'esriSMS',
                        'style': 'esriSMSCircle',
                        'color': [255, 255, 255, 165],
                        'size': 8,
                        'angle': 0,
                        'xoffset': 0,
                        'yoffset': 0,
                        'outline': wells_outline
                    }
                },
                {
                    'classMaxValue': 18,
                    'label': '14 - 18 mg/L',
                    'description': '14 - 18 mg/L',
                    'symbol': {
                        'type': 'esriSMS',
                        'style': 'esriSMSCircle',
                        'color': [255, 255, 255, 165],
                        'size': 10,
                        'angle': 0,
                        'xoffset': 0,
                        'yoffset': 0,
                        'outline': wells_outline
                    }
                }
            ]
    }
    
    point_renderer = {  
   "type": "simple",
   "symbol": 
   {
    "type": "esriSMS",
    "style": "esriSMSCircle",
    "color": [43, 140, 190, 255],
    "size": 2,
    "angle": 0,
    "xoffset": 0,
    "yoffset": 0,
    "outline": {
     "color": [255, 255, 255, 255],
     "width": .5
    }
   },
   "label": "Well Locations",
   "description": "Renders single point locations",
    }

    county_boundary_renderer = {
                 'type': 'Simple',
                'visualVariables': [],
                'symbol': {
                    'type': 'esriSFS',
                    'style': 'esriSFSSolid',
                    'color': [0, 0, 0, 0],
                    'outline': {
            'style': 'esriSLSSolid',
            'type': 'esriSLS',
            'color': [0, 0, 0, 255],
            'width': .75
            }
        }
    }

    tract_boundary_renderer = deepcopy(county_boundary_renderer)
    tract_boundary_renderer['symbol']['outline']['width'] = .5

    def __init__(self):
        self.outline_base = {
            'style': 'esriSLSSolid',
            'type': 'esriSLS',
            'width': .5
        }

        self.outline_color = [128, 128, 128]

        self.class_breaks_base = {
            'classMaxValue': 0,
            'label': '',
            'description': '',
            'symbol': {
                'type': 'esriSFS',
                'style': 'esriSFSSolid',
                'color': [],
                'outline': {}
            }
        }

        self.polygon_renderer_base = {
            'type':
                'classBreaks',
            'visualVariables': [],
            'rotationType': 'arithmetic',
            'minValue': 0,
            'field': '',
            'defaultSymbol': {
                'type': 'esriSFS',
                'style': 'esriSFSSolid',
                'color': [0, 0, 0, 255],
                'outline': {}
            },
            'defaultLabel': 'Other',
            'classificationMethod': 'esriNaturalBreaks',
            'classBreakInfos': []
        }

        self.st_dev_break_infos = [
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
        {
            'classMaxValue': -1.5,
            'label': '-2.5 to -1.5 St. Dev',
            'description': '-2.5 to -1.5 St. Dev',
            'symbol': {
                'type': 'esriSFS',
                'style': 'esriSFSSolid',
                'color': [],
                'outline': {}
                    }
         },
            {
            'classMaxValue': -.5,
            'label': '-1.5 to -.5 St. Dev',
            'description': '-1.5 to -.5 St. Dev',
            'symbol': {
                'type': 'esriSFS',
                'style': 'esriSFSSolid',
                'color': [],
                'outline': {}
                    }
         },
            {
                'classMaxValue': .5,
                'label': '-.5 to .5 St. Dev',
                'description': '.5 to 1.5 St. Dev',
                'symbol': {
                    'type': 'esriSFS',
                    'style': 'esriSFSSolid',
                    'color': [],
                    'outline': {}
                }
            },
            {
                'classMaxValue': 1.5,
                'label': '1.5 - 2.5 St. Dev',
                'description': '1.5 - 2.5 St. Dev',
                'symbol': {
                    'type': 'esriSFS',
                    'style': 'esriSFSSolid',
                    'color': [],
                    'outline': {}
                }
            },
            {
                'classMaxValue': 10,
                'label': '> 2.5 St. Dev',
                'description': '> 2.5 St. Dev',
                'symbol': {
                    'type': 'esriSFS',
                    'style': 'esriSFSSolid',
                    'color': [],
                    'outline': {}
                }
            }
        ]

    def generate(self,
                 color_ramp_selection: AnyStr,
                 outline: bool,
                 values: List,
                 field: str,
                 label_unit: str,
                 ) -> Dict:

        def get_color(
                ramp: List[str],
                index: int
        ):
            color_string = ramp[index]
            this_color = findall('[0-9]+', string=color_string)
            this_color = [int(color_value) for color_value in this_color]
            this_color.append(255)
            return this_color

        length = len(values)

        outline_color = deepcopy(self.outline_color)

        if outline:
            outline_color.append(255)
        else:
            outline_color.append(0)

        outline_base = deepcopy(self.outline_base)
        outline_base['color'] = outline_color

        class_break_infos = []
        this_renderer = deepcopy(self.polygon_renderer_base)


        if values != ['st_dev']:
            color_ramp = colors[color_ramp_selection][length]

            for i, maximum in enumerate(values):
                this_break = deepcopy(self.class_breaks_base)

                this_color = get_color(
                    ramp=color_ramp,
                    index=i
                )

                this_break['classMaxValue'] = maximum
                # if using percentages, convert max for labeling after assignment
                if label_unit == "%" and maximum < 1.1:
                    maximum = int(maximum * 100)
                    minimum = int(values[i - 1] * 100) + 1
                else:
                    minimum = values[i - 1]

                minimum = 0 if i <= 0 else minimum + 1

                if i+1 < length:
                    label = f"{minimum} - {maximum}{label_unit}"
                else:
                    label = f"{minimum}{label_unit} +"

                this_break['label'] = label
                this_break['description'] = label
                this_break['symbol']['color'] = this_color
                this_break['symbol']['outline'] = outline_base
                class_break_infos.append(this_break)

        elif values == ['st_dev']:
            this_renderer['classificationMethod'] = 'esriClassifyStandardDeviation'
            print(this_renderer['classificationMethod'])
            class_break_infos = deepcopy(self.st_dev_break_infos)
            color_ramp = colors[color_ramp_selection][7]

            for i, this_break in enumerate(class_break_infos):
                this_color = get_color(ramp=color_ramp, index=i)
                this_break['symbol']['color'] = this_color
                this_break['symbol']['outline'] = outline_base

        this_renderer['field'] = field
        this_renderer['defaultSymbol']['outline'] = outline_base

        this_renderer['classBreakInfos'] = class_break_infos

        return this_renderer

if __name__ == "__main__":
    renderer = CustomRenderer()

    new_renderer = renderer.generate(
        color_ramp_selection="BuGn",
        outline=False,
        values=[2, 4, 6, 8, 10],
        field="canrate",
        label_unit=r'%'
    )
    print(new_renderer)

    std_dev_renderer = renderer.generate(
        color_ramp_selection='BuGn',
        outline=True,
        values=['st_dev'],
        field="stdresid",
        label_unit="St. Dev"
    )

    print(std_dev_renderer)