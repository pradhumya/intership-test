import csv

with open('input/main.csv', 'r') as file:
    reader = csv.reader(file)
    with open("output/filteredCountry.csv", "w") as fc_file:
        fc_writer = csv.writer(fc_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        header = next(reader, None)
        print(header)
        fc_writer.writerow(header)
        for row in reader:
            if ('USA' in row[8]):
                fc_writer.writerow(row)

print("Please check output/filteredCountry.csv")