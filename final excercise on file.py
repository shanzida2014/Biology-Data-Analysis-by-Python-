#name:Shanzida Jahan Siddique
#BIFX:502
#HW 6
# This program get the file from the users and analyses DNA sequences with diferent properties.
num_sequences = 0
num_CTATA = 0
num_over_1000 = 0
num_high_GC = 0
num_over_2000_high_GC =0

#open the file
#Count the total number of DNA sequences
for line in open(input("Please enter the file name")):
    seq=line.rstrip()
    num_sequences=num_sequences+1
#count the CTATA pattern contining sequences:
    if "CTATA" in seq:
        num_CTATA=num_CTATA+1 
    if len(seq) > 1000:  # count the sequences which over 1000 base pair
        num_over_1000=num_over_1000 + 1
        GC_content = (seq.count("G") + seq.count("C")) / float(len(seq))
         
    if GC_content > 0.5:# count the sequences which have more than 50%GC content
        num_high_GC=num_high_GC + 1
            
    
    if len(seq) > 2000 and GC_content > 0.6:# count the sequences which have 2000 base and more than 50 % sequences
        num_over_2000_high_GC=num_over_2000_high_GC + 1
            

print (num_sequences, "sequences")
print (num_CTATA, "with the pattern CTATA")
print (num_over_1000, "have over 1000 bases")
print (num_high_GC, "have over 50% GC")
print (num_over_2000_high_GC, "have over 2000 bases and over 50% GC")
