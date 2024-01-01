import csv

def header():
    csv_file = open("library.csv", "w")
    fields = ['Book Id', 'Book Title', 'Book Price']
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(fields)
    csv_file.close()

# writes the header only if the file is empty(does not have fieldnames to begin with)
def write_header():
    csv_file = open("library.csv", "r")
    csv_reader = csv.reader(csv_file)
    i = 0 # track if csv_reader is empty
    for line in csv_reader:
        i += 1
        csv_file.close()
        break
    if i == 0:
        header()


def add_record():
    print("Current Operation : Add Record")
    csv_file = open("library.csv", "a")
    csv_writer = csv.writer(csv_file)
    book_id = input("Enter Book-Id :")
    book_title = input("Enter Book Title :")
    book_price = input("Enter Book Price :")
    record = [book_id, book_title, book_price]
    csv_writer.writerow(record)
    print("Record added successfully!\n")
    csv_file.close()


def display_records():
    csv_file = open("library.csv", "r")
    csv_reader = csv.reader(csv_file)
    print("Id=============Title============Price")
    for line in csv_reader:
        if line != []:
            print(line[0],"\t", line[1],"\t\t", line[2])
def display_menu():
    print("=" * 50,)
    print("="*15, "MAIN MENU", "=" * 15)
    print('''
              Choose 1-5
              ----------
            1. Add Record
            2. Modify Record
            3. Delete Record
            4. Search Record
            5. Display All Records
            6. Quit\n''')


write_header()
display_menu()

command = 0

while command != 6:
    command = int(input(">>>"))
    if command == 1:
        add_record()
    elif command == 5:
        display_records()