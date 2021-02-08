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

for p in products:
    print(p[0], "cost", p[1])

with open ("products.csv", "w") as f:
    for p in products:
        f.write(p[0] + "," + p[1] + "\n")