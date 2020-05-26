import pandas as pd
import yfinance as yf

asx_data = pd.read_csv('ASXListedCompanies.csv')

print(asx_data.head())

output_df = pd.DataFrame(columns=['Ticker', 'Date', 'Div Amount'])
for index, row in asx_data.iterrows():

    ticker = row['ASX code'] + '.AX'
    print(ticker)
    afi = yf.Ticker(ticker)
    start_date = '2015-01-01'
    end_date = '2019-12-31'

    history = afi.history(start=start_date)

    for index, row in history.iterrows():
        dividend = row['Dividends']
        if dividend > 0.00:
            output_df.loc[-1] = [ticker, index, dividend]
            output_df.index = output_df.index+1
            output_df = output_df.sort_index()
            print('found dividend for' + ticker)


output_df.to_csv('ASXDividendCompaniesLatest.csv')
print('Finished')

