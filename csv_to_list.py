import os

csvlist = os.listdir("files")

csv_list = {}

for csvs in csvlist:
    if csvs.__contains__(".csv"):
        csplit = csvs.split('_')
        x = csv_list.get(str(csplit[0]))
        if x is None:
            csv_list[str(csplit[0])] = []
            csv_list[str(csplit[0])].append(csplit[1].replace(".csv",""))
        else:
            csv_list[str(csplit[0])].append(csplit[1].replace(".csv",""))
for csvv in csv_list:
	csv_list[csvv].sort()

for csvv in csv_list:
    fp = open(os.path.join("manifestslist", csvv + '.txt'), 'w')
    fp.write(str(csv_list[csvv]))
    fp.close()

print("Done!")    
