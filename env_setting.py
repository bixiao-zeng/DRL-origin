class Setting(object):
    def __init__(self):
        # a = [1.5]*5
        # b = [0.2,0.4,0.6,0.8,1]
        # c = [a[i]/b[i] for i in range(5)]
        self.V = {
            'relationship': [
                [0.11, 0.0, 0.11, 0.11, 0.11, 0.0, 0.22, 0.11, 0.22, 0.0, ],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
                [0.11, 0.0, 0.11, 0.11, 0.11, 0.0, 0.22, 0.11, 0.22, 0.0, ],
                [0.11, 0.0, 0.11, 0.11, 0.11, 0.0, 0.22, 0.11, 0.22, 0.0, ],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
                [0.22, 0.0, 0.22, 0.22, 0.22, 0.0, 0.44, 0.22, 0.44, 0.0, ],
                [0.11, 0.0, 0.11, 0.11, 0.11, 0.0, 0.22, 0.11, 0.22, 0.0, ],
                [0.33, 0.0, 0.33, 0.33, 0.33, 0.0, 0.67, 0.33, 0.67, 0.0, ],
            ],
            'cost': [1]*5,
            'R': 10000,
            'prob': [0.2, 0.4, 0.3, 0.4],
            'task_num': 1,
            'user_battery_budget': [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50,
                                    50, 50, 50, 50, 50, 50, 50, 50, 50],
            'datasize':[4750]*2,
            'uni_quality':[0.3]*4+[1]
        }
