
import csv
class ReusableReader:
    def __init__(self,filename):
        self.__data=[]
        self.__keys=[]
        with open(filename, encoding = 'utf8') as mfile:
            csvreader = csv.DictReader(mfile)
            self.__data = list(csvreader)
            self.__keys = csvreader.fieldnames

    def __iter__(self):
        return iter(self.__data)

