import csv

with open('output/filteredCountry.csv', 'r') as input_file:
    file_reader = csv.reader(input_file)
    next(file_reader, None)
    csv_header = ['SKU', 'FIRST_MINIMUM_PRICE', 'SECOND_MINIMUM_PRICE']
    with open('output/lowestPrice.csv', 'w') as lp_file:
        lp_writer = csv.writer(lp_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        lp_writer.writerow(csv_header)
        dict_sku = {}
        for row in file_reader:
            price = row[5]
            try:
                price = float(price[1:])
            except ValueError:
                print ("Error : " + price + " can't be converted.")
                continue
            # print(price)
            if (row[0] in dict_sku.keys()):
                dict_sku[row[0]].append(price)
            else:
                dict_sku[row[0]] = [price]
        # print(dict_sku)

        for key, value in dict_sku.items():
            new_row = []
            new_row.append(key)
            value.sort()
            # print(value[0])
            new_row.append(value[0])
            if (len(value) > 1):
                # print("2nd val -> " + str(value[1]))
                new_row.append(value[1])
            else:
                new_row.append("NO 2nd Item")
            lp_writer.writerow(new_row)

print("Please check output/lowestPrice.csv")