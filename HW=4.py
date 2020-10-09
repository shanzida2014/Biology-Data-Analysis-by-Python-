def get_count_substring(dna,substring): 
    length = len(dna) 
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    c_count =  dna.upper().count('C')
    atc_content = (a_count + t_count+c_count) / length 
    return round(at_content, 3)
