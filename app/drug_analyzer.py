from ast import parse
from random import weibullvariate
import re
from tkinter.messagebox import NO


class DrugAnalyzer:
    # TODO: Part 1 - Add method(s) necessary to fulfill the requirements.
    def __init__(self, data=[]):
        self.data = data
        self.results = []
    
    def __add__(self, data):
        if len(data) == 4:
            if all(isinstance(i, float) for i in data[1:]) and isinstance(data[0], str):
                self.data += [data]
                return self
            else:
                raise ValueError('Improper type on list added.')
        else:
            raise ValueError('improper length of the added list.')


    def verify_series(self, series_id: str, act_subst_wgt: float, act_subst_rate: float, allowed_imp: float) -> bool:
        
        # TODO: Part 2 - Implement this method.
        pills=[]
        for series in self.data:
            if series[0][:3] == series_id[:3]:
                pills += [series]
            if series_id[:3] not in [series[0][:3] for series in self.data]:
                raise ValueError(f'{series_id} series is not present within the dataset.')
        
        for series in pills:
            pill_weight = sum(p[1] for p in pills)
            total_active_substances = sum(p[2] for p in pills)
            total_impurities = sum(p[3] for p in pills)    
        
            if act_subst_wgt*(1+act_subst_rate) < series[2] or series[2] < act_subst_wgt*(1-act_subst_rate):
                return False
            
            if ((len(pills) * act_subst_wgt)*(1 + act_subst_rate)) < total_active_substances or total_active_substances < ((len(pills) * act_subst_wgt)*(1 - act_subst_rate)):
                return False
        
            if float(allowed_imp * pill_weight) < total_impurities:
                return False
            
        return True