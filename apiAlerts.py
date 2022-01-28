import argparse, requests, json, statistics, datetime

currency = 'btcusd'
deviation = 1
lvl = 'INFO'

# Getting CLI arguments
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--deviation", help="standard deviation threshold. eg. 1", type = float)
parser.add_argument("-c", "--currency", help="The currency trading pair", type = str)
args = parser.parse_args()
if args.deviation:
    deviation = args.deviation

if args.currency:
    currency = args.currency

try:
    # Calling REST API
    base_url = "https://api.gemini.com/v2"
    response = requests.get(base_url + f"/ticker/{currency}")
    r_data = response.json()

    # Getting data in a dict
    last_price = float(r_data['close'])
    changes = [float(i) for i in r_data['changes']]
    average = statistics.mean(changes)
    change = last_price-average
    sdev = statistics.stdev(changes)

    data = {}
    data['last_price'] = last_price
    data['average'] = average
    data['change'] = change
    data['sdev'] = sdev
    
except:
    lvl = 'ERROR'
    data = {}
    sdev = 0
    
# Prepare final output
res = {}
my_date = datetime.datetime.now()
res['timestamp'] = my_date.isoformat()
res['level'] = lvl
res['trading_pair'] = currency
res['deviation'] = (sdev > deviation)
res['data'] = data

print(json.dumps(res))
