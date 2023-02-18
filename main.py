import requests


def get_info():
    response = requests.get(url='https://yobit.net/api/3/info')

    with open('info.txt', 'w') as file:
        file.write(response.text)
    return response.text


def get_ticker():
    response = requests.get(url=f'https://yobit.net/api/3/ticker/btc_usd-eth_usd?ignore_invalid=1')

    with open('ticket.txt', 'w') as file:
        file.write(response.text)
    return response.text


def get_depth(coin1="btc", coin2="eth", valute="usd", limit=150):
    response = requests.get(
        url=f'https://yobit.net/api/3/depth/{coin1}_{valute}-{coin2}_{valute}?limit={limit}&ignore_invalid=1')

    with open('depth.txt', 'w') as file:
        file.write(response.text)
    bids_btc = response.json()[f'{coin1}_{valute}']['bids']
    bids_eth = response.json()[f'{coin2}_{valute}']['bids']

    total_bids_amount_btc = 0
    total_bids_amount_eth = 0
    for item_bids in bids_btc:
        price = item_bids[0]
        coin_amount = item_bids[1]

        total_bids_amount_btc += price * coin_amount
    for item_bids in bids_eth:
        price = item_bids[0]
        coin_amount = item_bids[1]

        total_bids_amount_eth += price * coin_amount

    return f'Total bids btc: {round(total_bids_amount_btc, 3)} $\nTotal bids eth: {round(total_bids_amount_eth, 3)} $'


def get_trades_many(coin1="btc", coin2="eth", valute="usd", limit=150):
    response = requests.get(
        url=f'https://yobit.net/api/3/trades/{coin1}_{valute}-{coin2}_{valute}?limit={limit}&ignore_invalid=1')

    with open('get_trades_many.txt', 'w') as file:
        file.write(response.text)

    total_trade_ask_btc = 0
    total_trade_bid_btc = 0
    total_trade_ask_eth = 0
    total_trade_bid_eth = 0

    for item in response.json()[f'{coin1}_{valute}']:
        if item['type'] == 'ask':
            total_trade_ask_btc += item['price'] * item['amount']
        else:
            total_trade_bid_btc += item['price'] * item['amount']

    for item in response.json()[f'{coin2}_{valute}']:
        if item['type'] == 'ask':
            total_trade_ask_eth += item['price'] * item['amount']
        else:
            total_trade_bid_eth += item['price'] * item['amount']

    info = f'[-] TOTAL {coin1} SELL: {round(total_trade_ask_btc, 3)} $\n[+] TOTAL {coin1} BUY: {round(total_trade_bid_btc, 3)} $\n' \
           f'[-] TOTAL {coin2} SELL: {round(total_trade_ask_eth, 3)} $\n[+] TOTAL {coin2} BUY: {round(total_trade_bid_eth, 3)} $'

    return info


def get_trades(coin1="btc", valute="usd", limit=150):
    response = requests.get(
        url=f'https://yobit.net/api/3/trades/{coin1}_{valute}?limit={limit}&ignore_invalid=1')

    with open('get_trades_many.txt', 'w') as file:
        file.write(response.text)

    total_trade_ask_btc = 0
    total_trade_bid_btc = 0

    for item in response.json()[f'{coin1}_{valute}']:
        if item['type'] == 'ask':
            total_trade_ask_btc += item['price'] * item['amount']
        else:
            total_trade_bid_btc += item['price'] * item['amount']

    info = f'[-] TOTAL {coin1} SELL: {round(total_trade_ask_btc, 3)} $\n[+] TOTAL {coin1} BUY: {round(total_trade_bid_btc, 3)} $'

    return info


def main():
    print(get_info())
    print(get_ticker())
    print(get_depth())
    print(get_trades())


if __name__ == '__main__':
    main()
