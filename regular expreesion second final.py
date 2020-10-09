#Shanzida Jahan Siddique
#BIFX 502
#HW 8(2)

# this program predict the fragment length if we digest the sequence with the AbcI restriction enzyme
#whose recognition site is ANT/AAT
# open the dna txt file and read this.
import re
dna = open("dna.txt").read().rstrip("\n")
print(str(len(dna)))
all_cuts = [0]

# add cut positions for AbcI
for match in re.finditer(r"A[ATGC]TAAT", dna):
    all_cuts.append(match.start() + 3)


# add the final position

all_cuts.append(len(dna))
sorted_cuts = sorted(all_cuts)
print(sorted_cuts)
for i in range(1,len(sorted_cuts)):
    this_cut_position = sorted_cuts[i]
    previous_cut_position = sorted_cuts[i-1]
    fragment_size = this_cut_position - previous_cut_position
    print("one fragment size is " + str(fragment_size))
    
    
    
    
