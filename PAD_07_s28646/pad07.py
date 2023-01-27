import pandas as pd
from scipy import stats
import plotly.express as px
import statsmodels.formula.api as smf

df = pd.read_csv('wyniki.csv')

dff = df[df['plec'] == 'F'].reset_index()
dfm = df[df['plec'] == 'M'].reset_index()

test_data = pd.DataFrame(data={'sex': ['M', 'F'], 'mean': [dfm['ocena_koncowa'].mean(), dff['ocena_koncowa'].mean()],
                                'std': [dfm['ocena_koncowa'].std(), dff['ocena_koncowa'].std()],
                                'nobs': [dfm['ocena_koncowa'].count(), dff['ocena_koncowa'].count()]})

ttest = stats.ttest_ind_from_stats(
    test_data.iloc[0][1], test_data.iloc[0][2], test_data.iloc[0][3], test_data.iloc[1][1],
    test_data.iloc[1][2], test_data.iloc[1][3])

print(f'T = {ttest[0]}, p-value = {ttest[1]}')
alpha = 0.05
if alpha > ttest[1]:
    print('Odrzucamy H0')
else:
    print('Nie orzucamy H0')

# zad 2
print("\nZAD 2\n")
df = pd.read_csv('ZyskiFirmyX.csv')
fig = px.scatter(df, "Rok", "Zysk", title="ZyskiFirmyX")
fig.show()
print('Nie jest zauważalny trend liniowy')

model = smf.ols(formula="Zysk ~ Rok", data=df).fit()
print(model.summary())
