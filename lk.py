filename = "E:\data.csv"
def read_from_file(filename):
    with open(filename, 'r') as file:
        columns = tuple(file.readline().split(','))
        data = []
        for line in file:
            line = line.split(',')
            data.append((int(line[0]),line[1],line[2],int(line[3]),int(line[4]),int(line[5])))
        return columns, data
def write_to_file(filename):
    with open(filename,  'w') as file:
        file.write(','.join(columns))
        for line in data:
            line = [str(i) for i in line]
            file.write(','.join(line)+'\n')
def print_data():
    m = max([len(i) for i in columns])
    for i in columns:
        print(str(i).ljust(m+2, ' '), end='')
    print()
    for line in data:
        for i in line:
           print(str(i).ljust(m+2, ' '), end='')
        print()
def insert(line):
    if line not in data:
       data.append(line)
def get_value():
    line = list(input().split())
    return (int(line[0]),line[1],line[2],int(line[3]),int(line[4]),int(line[5]))
global columns, data
columns, data = read_from_file(filename)
insert(get_value())
print_data()
write_to_file(filename)