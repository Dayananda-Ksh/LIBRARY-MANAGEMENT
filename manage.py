import csv
import os

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
    print("-"*33)
    csv_file = open("library.csv", "a")
    csv_writer = csv.writer(csv_file)
    book_id = input("Enter Book-Id :")
    book_title = input("Enter Book Title :")
    book_price = input("Enter Book Price :")
    record = [book_id, book_title, book_price]
    csv_writer.writerow(record)
    print("Record added successfully!\n")
    csv_file.close()


def update_record():
    print("Current Operation : Update Record")
    print("-"*33)
    book_id = input("Book Id : ")
    csv_file = open("library.csv", "r", newline="\r\n")
    csv_reader = csv.reader(csv_file)
    temp_file = open("temp.csv", "a")
    temp_writer = csv.writer(temp_file)
    for line in csv_reader:
        if line[0] == book_id:
            print("\nCurrent Record :")
            print("Id".ljust(20), "Title".ljust(40), "Price")
            print("="*80)
            print(line[0].ljust(20), line[1].ljust(40), line[2])
            print("\nUpdating...")
            book_title = input("Enter new Book Title : ")
            book_price = input("Enter new Book Price : ")
            new_book_id = input("Enter new Book Id : ")
            data = [new_book_id, book_title, book_price]
            temp_writer.writerow(data)
            print("The updated record is : ")
            print("Id".ljust(20), "Title".ljust(40), "Price")
            print("="*80)
            print(data[0].ljust(20), data[1].ljust(40), data[2])
        else:
            temp_writer.writerow(line)
    csv_file.close()
    temp_file.close()
    os.remove("library.csv")
    os.rename("temp.csv", "library.csv")


def delete_record():
    print("Current Operation : Delete Record")
    print("-"*33)
    book_id = input("Book Id : ")
    csv_file = open("library.csv", "r", newline="\r\n")
    csv_reader = csv.reader(csv_file)
    temp_file = open("temp.csv", "a")
    temp_writer = csv.writer(temp_file)
    for line in csv_reader:
        if line[0] == book_id:
            print("\nSelected Record :")
            print("Id".ljust(20), "Title".ljust(40), "Price")
            print("="*80)
            print(line[0].ljust(20), line[1].ljust(40), line[2])
            print("\nDeleting...")
            print("Record deleted successfully.")
        else:
            temp_writer.writerow(line)
    csv_file.close()
    temp_file.close()
    os.remove("library.csv")
    os.rename("temp.csv", "library.csv")


def search_record():
    print("Current Operation : Search Record")
    print("-"*33)
    book_id = input("Book Id : ")
    csv_file = open("library.csv", "r", newline="\r\n")
    csv_reader = csv.reader(csv_file)
    found = False
    for line in csv_reader:
        if line[0] == book_id:
            print("\nFound Record :")
            print("Id".ljust(20), "Title".ljust(40), "Price")
            print("="*80)
            print(line[0].ljust(20), line[1].ljust(40), line[2])
            found = True
    if found == False:
        print("\nNo record found❌")


def display_records():
    print("Current Operation: Display Records")
    print("-"*35)
    csv_file = open("library.csv", "r", newline='\r\n') #newline='\r\n' removes empty line
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    print("Id".ljust(20), "Title".ljust(40), "Price")
    print("="*80)
    for line in csv_reader:
        print(line[0].ljust(20), line[1].ljust(40), line[2])


def display_menu():
    print("=" * 50,)
    print("="*15, "MAIN MENU", "=" * 15)
    print('''
              Choose 1-5
              ----------
            1. Add Record
            2. Update Record
            3. Delete Record
            4. Search Record
            5. Display All Records
            6. Exit\n''')


write_header()
display_menu()

command = 0

while command != 6:
    command = input("\n>>>")
    print("\n")
    if command == '1':
        add_record()
    elif command == '2':
        update_record()
    elif command == '3':
        delete_record()
    elif command == '4':
        search_record()
    elif command == '5':
        display_records()
    elif command == '6':
        print("Library Exited Successfully.\n")
        print("Thank You. Please  Visit Again🙏\n\n")
    else:
        print("Invalid Input!❌\n")