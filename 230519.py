def calc_total_price(price, quantity):
    total = price * quantity
    return total

item_price = float(input("물품 가격: "))
item_quantity = int(input("물품 수량: "))

total_price = calc_total_price(item_price, item_quantity)

print(f"물품의 가격은 {total_price}원입니다.")