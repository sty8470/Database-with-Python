#Tae Young Kevin Shin
#Dr. Garrett's COSC 330A
#Introduction to Database
#1st Assignment Submission

#importing csv module
import csv

#defining class storing csv data as OrderedDict format
class SalesReader:
    def __init__(self,filename):
        self.__data=[]
        self.__keys=[]
        with open(filename, encoding = 'utf8') as receipt_file:
            csvreader = csv.DictReader(receipt_file)
            self.__data = list(csvreader)
            self.__keys = csvreader.fieldnames

    def __iter__(self):
        return iter(self.__data)

#Storing specific customer's expenditure information
def customer():
    reader = SalesReader('bakery.csv')
    recepit_num = input("Enter a customer's receipt number: ")
    lst = []
    for row in reader:
        if row['receiptno'] == recepit_num:
            lst.append(row)

    return lst
            
customer_data = customer()

#defining final_receipt format and printing values
def final_receipt():
    new_lst = []

    #storing necessary data in new_lst
    #printing customer's personal information
    for case in customer_data:
        new_lst.append((case['prodno'], case['itemno'], case['flavor'], case['unitprice']))
    new_lst.sort(key=lambda x:x[1])
    print("-----------------------------------------")
    print("Customer:   {} {}". format(case['first'], case['last']))
    print("Date:       {}". format(case['receiptdate']))
    print("Receipt No: {}". format(case['receiptno']))
    print("\n")

    #printing customer's consumption information
    total = []
    for item in new_lst:
        print ("{:<20} {:<14} {:>5}". format(item[0],item[2], item[3]))
        total.append(float(item[3]))    
    print("                                  ","------")
    print("Total:                            $",sum(total))
    print("-----------------------------------------")
    
final_receipt()
    
    
