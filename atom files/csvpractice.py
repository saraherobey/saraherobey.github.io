import csv
# # importing csv package --give me the code in the csv library. Give it to me.
#
# with open("csvs/basic.csv", "r") as csvfile:
# #open a csv file for me that is at csvs/basic.csv, get ready to read it (r), small variable name csvfile
#
#     our_reader = csv.reader(csvfile)
#     # go inside csv library and find the reader (using the aforementioned file)/prepare file to be opened
#
#     names = [row for row in our_reader]
#     #loop for each row and create names list/knows it will be a list because of []
#
# print(names[2][3])
#     #print item in names list
#
# # find the length of each first name
# for row in names:
#     print(len(row[2]))
#
# # find the longest first name
# longest = ""
# for row in names:
#     if len(row[2]) > len(longest):
#         longest = row[2]
# print(longest)
#
# # construct a new list consisting of only the first names we have here.
# last_names = [row[2] for row in names]
# last_names.reverse()
# print(last_names)
#
# new_row = [2,'wayne','graham','meh']
# names.append(new_row)
# print(names)
#
# a_row = [3,'fox','eliza','SO COOL']
# print(names + a_row)

with open('csvs/practice.csv', 'w') as fout:
    csvwriter = csv.writer(fout)
    for i in range(0, 100, 10):
        csvwriter.writerow([i, i + 5, i + 10, i + 15, i + 20, i + 25, i + 30])
