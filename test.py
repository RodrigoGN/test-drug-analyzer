from app.drug_analyzer import DrugAnalyzer

my_drug_data = [
                ['L01-10', 1000.02, 102.88, 1.00100],
                ['L01-06', 999.90, 96.00, 2.00087],
                ['G02-03', 1000, 96.50, 3.00100],
                ['G03-06', 989.01, 119.00, 4.00004]
]
my_analyzer = DrugAnalyzer(my_drug_data)
print(my_analyzer.data)
print(DrugAnalyzer().data)
my_new_analyzer = my_analyzer + ['G03-01', 789.01, 129.00, 0.00008]
print(my_new_analyzer.data)
# my_new_analyzer = my_analyzer + ['G03-01', 129.00, 0.00008]

# testes para executar
print(my_new_analyzer.verify_series(series_id = 'L01', act_subst_wgt = 100, act_subst_rate = 0.05, allowed_imp = 0.001))
print(my_new_analyzer.verify_series(series_id = 'L01', act_subst_wgt = 100, act_subst_rate = 0.05, allowed_imp = 0.01))
print(my_analyzer.verify_series(series_id = 'B03', act_subst_wgt = 100, act_subst_rate = 0.05, allowed_imp = 0.001))