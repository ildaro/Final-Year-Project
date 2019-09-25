import gzip
import shutil
import os
import sys
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

sys.setrecursionlimit(2500)

#function to convert a number to any base from base 2 to base16
def convert_to_base(n,base):
   convert = "0123456789ABCDEF"
   if n < base:
      return convert[n]
   else:
      return convert_to_base(n//base,base) + convert[n%base]


# asks user what file to convert
file = input("Which file would you like to convert? e.g. powers2.txt :")

#file stats before conversion to other bases

#compress original numbers file
with open(file, 'rb') as f_in:
    with gzip.open(file + '.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

uncomp_size_test = os.path.getsize(file)
comp_size_test = os.path.getsize(file + ".gz")
reduced_test = 100 - ((comp_size_test/uncomp_size_test)*100)

print("Stats of ", file)
print("File size is", uncomp_size_test, "bytes.")
print("Compressed file size is", comp_size_test, "bytes.")
print("Compressing the file reduced its size by", str(round(reduced_test,2)),"percent.")

performance = []

for num in range(2, 17):
    #read from file, convert to base num, and write to file
    with open(file,'r') as file1:
        with open('conversion.txt','w') as file2:
            for numbers in file1:
                numbs = numbers.split(',')
                for i in numbs:
                    x = int(i)
                    converted = convert_to_base(x,num)
                    file2.write(converted + ',')

    #compress converted numbers file
    with open('conversion.txt', 'rb') as f_in:
        with gzip.open('conversion.txt.gz', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    
    #compression comparsion (converted files)
    uncomp_size_converted = os.path.getsize("conversion.txt")
    comp_size_converted = os.path.getsize("conversion.txt.gz")
    reduced_converted = 100 - ((comp_size_converted/uncomp_size_converted)*100)

    print("\n====== BASE" + str(num) + " ======")
    print("Converted file size is", uncomp_size_converted, "bytes.")
    print("Compressed converted file size is", comp_size_converted, "bytes.")
    print("Compressing the converted file reduced its size by", str(round(reduced_converted,2)),"percent.")

    performance.append(reduced_converted)

objects = ('base2', 'base3', 'base4', 'base5', 'base6', 'base7', 'base8','base9', 'base10', 'base11', 'base12', 'base13', 'base14', 'base15', 'base16')
y_pos = np.arange(len(objects))
 
plt.bar(y_pos, performance, align='center', alpha=1)
plt.xticks(y_pos, objects)
plt.ylabel('Percentage of size reduced')
plt.title('Size Reduction after compression of ' + str(file))
 
plt.show()