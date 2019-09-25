# Guessing the next number in the sequence by analysing file compression ratios

## Objectives
The objectives of this project were to write a program in Python which would take an increasing sequence of num-bers  in  base-10  and  another  base  as  input,  and  convert the sequence to the given fixed base. Then write the converted sequence to a file, compress the file using standard compression utilities and analyse the compression ratio.
After converting to fixed bases, the aim was to do the same for varying bases. Essentially, the end goal was to ask the user for a sequence of numbers, with no apparent pattern in base-10, convert it to a varying base with the highest compression ratio and use the varying base to find the next number in the sequence.

## Conversion to bases and varying bases
Before running convertBase.py or varying.py make sure you have Python v3, Numpy and matplotlib installed.

convertBase.py converts the specified .txt files to each base from base-2 to base-16 and compresses it using GZIP compression, it then creates a bar chart which shows by how much percent the file size reduced for each base. New files are created and compressed for each base, these files have a .txt.gz extension.

varying.py **attempts** to convert Sequence.txt to all varying bases from [2,2,2,2,2,2,2,2,2,2] to [9,9,9,9,9,9,9,9,9,9], compressing the file and writing the percentage reduction of file size along with the corresponding varying bases to a dictionary. This is quite inefficient and likely will not finish running before crashing. A detailed explanation and potential solution to this problem can be found in the **[report](https://drive.google.com/file/d/1DT9DBk-Aer4pare-Vizsyq0Sy48QCobP/view?usp=sharing)** from page 23 onwards.

If you would like to learn more, a report detailing my research and findings can be found at https://drive.google.com/file/d/1DT9DBk-Aer4pare-Vizsyq0Sy48QCobP/view?usp=sharing