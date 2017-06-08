import csv
# with open("csvs/ripper.csv", "r") as csvfile:
#     our_reader = csv.reader(csvfile)
#     names = [row for row in our_reader]
# print(names[0])

#column 4 for rows 0 300

with open("csvs/ripper.csv", "r") as csvfile:
    our_reader = csv.reader(csvfile)
    all_texts = [row[4] for row in our_reader]

all_texts



with open("csvs/practice.csv", "w") as fout:
    csvwriter = csv.writer(fout)
    csvwriter.writerow(map(str.lower, all_texts))
print(all_texts)
