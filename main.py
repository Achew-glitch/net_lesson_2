import csv

with open('csv_file.csv') as f_n:
    f_n_reader = csv.reader(f_n)
    print(f'Headers: {next(f_n_reader)}')
    for row in f_n_reader:
        print(row)

with open('csv_file.csv') as f_n:
    f_n_reader = csv.DictReader(f_n)
    for row in f_n_reader:
        print(row)
        print(row['hostname'], row['model'])


data = [['hostname', 'vendor', 'model', 'location'],
        ['kp1', 'Cisco', '2960', 'Moscow, str'],
        ['kp2', 'Cisco', '2960', 'Novosibirsk, str'],
        ['kp3', 'Cisco', '2960', 'Kazan, str'],
        ['kp4', 'Cisco', '2960', 'Tomsk, str']]

with open('writing_data.csv', 'w') as f_n:
    csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC).writerows(data)

with open('writing_data.csv') as f_n:
    print(f_n.read())

with open('writing_dict_data.csv', 'w') as f_n_w:
    f_n_dictwriter = csv.DictWriter(f_n_w, fieldnames=data[0], quoting=csv.QUOTE_NONNUMERIC)
    f_n_dictwriter.writeheader()
    with open('csv_file.csv') as f_n_r:
        f_n_reader = csv.DictReader(f_n_r)
        f_n_dictwriter.writerows(f_n_reader)

with open('writing_dict_data.csv') as f_n:
    print(f_n.read())