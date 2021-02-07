products = []
while True:
    name = input("please input product name: ")
    if name == "q":
        break
    price = input("please input product price: ")
    p = [name, price]
    products.append(p)
print(products)

print(products[0][0])
print(products[1][0])