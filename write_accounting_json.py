import json

with open('accounting_clean.txt', 'r') as f:
    buf = f.readlines()

accounting_keys = [buf[idx] for idx in range(0,len(buf)) if idx%2 == 0]
accounting_vals = [buf[idx] for idx in range(0,len(buf)) if idx%2 != 0]

accounting_list = []
for elem in zip(accounting_keys, accounting_vals):
    accounting_list.append(elem)

with open('accounting_data.json', 'w') as f:
    f.write(json.dumps(accounting_list))

with open('accounting_data.json', 'r') as f:
    data = json.load(f)

data_split = [[elem[0], elem[1].strip().split('.')] for elem in data]

data_split_cleaned = []
for elem in data_split:
    if('' in elem[1]):
        elem[1].remove('')
        data_split_cleaned.append([elem[0].strip(), elem[1]])
    else:
        data_split_cleaned.append([elem[0].strip(), elem[1]])

with open('accounting.json', 'w') as f:
    f.write(json.dumps(data_split_cleaned))
