# Display my name,class and homework number.
print('Shanzida Jahan Siddique')
print('BIFX 502')
print('LAB 2')

#ask user to enter the DNA sequence

dna_sequence=input("please enter the dna sequence")

#count the number of A in sequence
adenine_A=dna_sequence.count("A")

#count the number of T in sequence
thiamine_T=dna_sequence.count("T")

#count the number of G in sequence
guanine_G=dna_sequence.count("G")

#count the number of C in sequence
cytocine_C=dna_sequence.count("C")


#Display the presence and count of nucleotides in the sequence.

if "A" in dna_sequence :
    print("The number of adenine,"+str(adenine_A))
else:
    print('"A"is not in the sequence')
if "T" in dna_sequence:
    print("The number of thiamine,"+str(thiamine_T))
else:
    print('"T"is not in the sequence')
    
if "G" in dna_sequence:
    print("The number of guanine,"+str(guanine_G))
else:
    print('"G"is not in the sequence')
if "C" in dna_sequence :
    print("The number of cytocine,"+str(cytocine_C))
else:
    print('"C"is not in the sequence')


        
 

    
    


