


# Display my name,class and homework number.
print('Shanzida Jahan Siddique')
print('BIFX 502')
print('Homework 1')

#This program gets the DNA sequence  from the user.
#Calculate the the length and number of nucleotides.

#Get the DNA sequence from the user.
dna_sequence=input("Please enter the DNA sequence:")

# get the length of the sequence
length_sequence=len(dna_sequence)

#count the number of A in sequence
adenine_A=dna_sequence.count("A")
#count the nuber of a in sequence
adenine_a=dna_sequence.count("a")
#Get the number of total adenine.
total_adenine= adenine_A+adenine_a

#count the number of T in sequence
thiamine_T=dna_sequence.count("T")
#count the number of t in sequence
thiamine_t=dna_sequence.count("t")
#Get the number of total thiamine.
total_thiamine=thiamine_T+thiamine_t 

#count the number of G in sequence
guanine_G=dna_sequence.count("G")
#count the nuber of g in sequence
guanine_g=dna_sequence.count("g")
#Get the number of total guanine.
total_guanine= guanine_G+guanine_g

#count the number of C in sequence
cytocine_C=dna_sequence.count("C")
#count the nuber of c in sequence
cytocine_c=dna_sequence.count("c")
#Get the number of total cytocine.
total_cytocine= cytocine_C+cytocine_c

#Display the length of the sequence and number of nucleotides.
print("The length of the sequence is,"+str(length_sequence))
print("The number of adenine,"+str(total_adenine))
print("The number of thiamine,"+str(total_thiamine))
print("The number of guanine,"+str(total_guanine))
print("The number of cytocine,"+str(total_cytocine))
        
 


