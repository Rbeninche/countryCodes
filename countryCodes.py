def get_country_codes(prices):
    price_list = prices.split(" ")
    country_code = ''
    result = ""
    for each_price in price_list:
        country_code += each_price[:2] + ', '
    return country_code.rstrip(', ')


print(get_country_codes("NZ$300, KR$1200, DK$5"))
