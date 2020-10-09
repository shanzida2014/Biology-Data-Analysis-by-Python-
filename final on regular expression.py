# Shanzida Jahan Siddique
#BIFX502
#HW 8
#This program will print only the accession names that satisfy the following criteria


# accession name 

accs = ['xkn59438', 'yhdck2', 'eihd39d9',
'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
print(accs)
#Contain the letter a
import re
for acc in accs:
    if re.search(r"a", acc):
        print("\t" + acc)
        
#Contain the number 3 or 8

for acc in accs:
    if re.search(r"(3|8)", acc):
        print ("\t" + acc)
            
#Contain the letters d and e in that order
        
for acc in accs:
    if re.search(r"d.*e", acc):
        print ("\t" + acc) 
                
# Contain the letters d and e in that order with a single letter between them
for acc in accs:
    if re.search (r"(d.e)", acc):
        print ("\t" + acc)
#Contain both the letters d and e in any order
for acc in accs:
    if re.search(r"d.*e", acc) or re.search(r"e.*d", acc):
        print ("\t" + acc)
#Start with c or h
for acc in accs:
    if re.search(r"^(c|h)", acc):
        print("\t" + acc)
#Start with c or h and end with 5
for acc in accs:
    if re.search(r"^(c|h).*5$", acc):
        print ("\t" + acc)
        
# Start with x and j and end with e
for acc in accs:
    if re.search(r"^(x.*j).*e$", acc):
        print ("\t" + acc)
# End with 7 or 9
for acc in accs:
    if re.search(r"(7|9)$", acc):
        print ("\t" + acc)
#End with d followed by either a, r, or p
for acc in accs:
    if re.search(r"d[arp]$", acc):
        print ("\t" + acc)
       
        
