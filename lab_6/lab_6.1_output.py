def calculate_total_price(product_prices, discount, tax_rate=0):
    total_price = sum(price * 0.9 if discount else price for price in product_prices)
    total_price *= (1 + tax_rate)
    return total_price
