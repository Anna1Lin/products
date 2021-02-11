products = []
while True:
    name = input("please input product name: ")
    if name == "q":
        break
    price = input("please input product price: ")
    price = int(price)
    products.append([name, price])
print(products)

print(products[0][0])
print(products[1][0])

for p in products:
    print(p[0], "cost", p[1])

with open ("products.csv", "w", encoding="utf-8") as f:
    f.write("The product name, The price \n")
    for p in products:
        f.write(p[0] + "," + str(p[1]) + "\n")