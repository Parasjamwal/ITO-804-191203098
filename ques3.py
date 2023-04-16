import csv
# Initialize an empty dictionary for each stock symbol
symbols = {}

# Open the CSV file and read in the data
with open('stock_prices.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader) # skip header row
    
    # Loop through each row of data
for row in csv_reader:
        symbol, date, price = row
        
        # If the symbol isn't already in the dictionary, add it
        if symbol not in symbols:
            symbols[symbol] = {'highest': float(price), 'lowest': float(price)}
        else:
            # If the price is higher than the current highest, update the dictionary
            if float(price) > symbols[symbol]['highest']:
                symbols[symbol]['highest'] = float(price)
            
            # If the price is lower than the current lowest, update the dictionary
            if float(price) < symbols[symbol]['lowest']:
                symbols[symbol]['lowest'] = float(price)
                
# Print out the results
for symbol, data in symbols.items():
    print(symbol)
    print('Highest price:', data['highest'])
    print('Lowest price:', data['lowest'])
    print('')
