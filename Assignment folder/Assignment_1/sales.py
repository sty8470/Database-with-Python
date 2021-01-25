import csv
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



