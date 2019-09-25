import gzip
import shutil
import os
import sys
import operator
import time

#the function convert_alt_bases, takes a number x and a list of bases
#and converts x to a the varying base representation of that number
def convert_alt_bases(x, bases):
    result = []
    for i in range(len(bases)):
        y = x % bases[-i]
        z =  x // bases[-i]
        result.append(y)
        x = z
    r = result[::-1]
    return r

#convert list to int to use as key for dict
def list_to_int(numList):
    s = ''.join(map(str, numList))
    return int(s)


#ask the user to input a sequence of numbers and set the sequence to the variable seq
seq = input("Enter a sequence of numbers, seperated by commas: ")

# using the with keyword saves me closing files as they automatically close once the file the code in
# the scope has been executed
# writes the sequence seq to a file called Sequence.txt
with open('Sequence.txt', 'w') as sfile:
    sfile.write(seq)

# the following code compresses the Sequence.txt file and creates a compressed file Sequence.txt.gz
with open('Sequence.txt', 'rb') as f_in:
    with gzip.open('Sequence.txt' + '.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)



uncomp_size_test = os.path.getsize('Sequence.txt')
comp_size_test = os.path.getsize('Sequence.txt' + ".gz")
reduced_test = 100 - ((comp_size_test/uncomp_size_test)*100)

baseperc = dict()

#loops through all the possibile of bases from [2,2,2,2,2,2,2,2,2,2] to [9,9,9,9,9,9,9,9,9,9]
#uses the baselist to convert the sequence.txt file and adds the compression percentage to the dictionary
for a in range(2,10):
    for b in range(2,10):
        for c in range(2,10):
            for d in range(2,10):
                for e in range(2,10):
                    for f in range (2,10):
                        for g in range(2,10):
                            for h in range(2,10):
                                for i in range(2,10):
                                    for j in range(2,10):
                                        blist = [a,b,c,d,e,f,g,h,i,j]
                                        key = list_to_int(blist)
                                            
                                        with open('Sequence.txt','r') as file1:
                                            with open('conversion.txt','w') as file2:
                                                for numbers in file1:
                                                    numbs = numbers.split(',')
                                                    for k in numbs:
                                                        x = int(k)
                                                        converted = convert_alt_bases(x, blist)
                                                        str1 = ''.join(str(s) for s in converted)
                                                        file2.write(str1 + ',')

                                        #compress converted numbers file
                                        with open('conversion.txt', 'rb') as f_in:
                                            with gzip.open('conversion.txt.gz', 'wb') as f_out:
                                                shutil.copyfileobj(f_in, f_out)
                                                
                                        #compression comparsion (converted files)
                                        uncomp_size_converted = os.path.getsize("conversion.txt")
                                        comp_size_converted = os.path.getsize("conversion.txt.gz")
                                        reduced_converted = 100 - ((comp_size_converted/uncomp_size_converted)*100)
                                        
                                        
                                        baseperc.update({key : reduced_converted})

#prints the key that corresponds to the varying base list which reduces the size of conversion.txt the most
#i.e. the one thats most likely to have a pattern in the the certain varying base
#this key can then be used to work back to a base-10 number, could potentially be the next number in the sequence
print(max(baseperc.items(), key=operator.itemgetter(1))[0]) 