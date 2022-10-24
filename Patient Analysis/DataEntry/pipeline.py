
# Import writer class from csv module
from csv import writer

# List that we want to add as a new row
List = [6, 'William', 5532, 1, 'UAE']

# Open our existing CSV file in append mode
# Create a file object for this file
with open('patient.csv', 'a') as f_object:

    # Pass this file object to csv.writer()
    # and get a writer object
    writer_object = writer(f_object)

    qlist = []

    print("Simplirwse tis 30 erwthseis tou erwtimatologiou")
    for i in range(30):
        print('questione', i+1)
        q = input('Enter')
        qlist.append(q)

    print("Dimografika stoixia kia noshleia")
    for i in range(11):
        print('questione', i+1)
        q = input('Enter')
        qlist.append(q)

    writer_object.writerow(qlist)

    # Pass the list as an argument into
    # the writerow()

    # Close the file object
    f_object.close()
