def readin_fasta(string):
    data = open(string, 'r')
    dnadata = data.readlines()
    for line in dnadata:
        for ch in line:
            if ch[0] == '>':
                dnadata.pop(0)
    dnastring = ''.join(str(i) for i in dnadata).replace('\n', '')
    return dnastring

def CG_edge(string):
    if string[-1] == 'A' or string[-1] == 'T' or string[0] == 'A' or string[0] == 'T':
        return False
    else:
        return True

def CG_count(string):
    CG=0
    i = 0
    while i<len(string):
        if string[i] == 'C':
            CG += 1
        elif string[i] == 'G':
            CG += 1
        i += 1
    return CG

def reverse_complement(x):
    x = x[::-1]
    x = x.replace('C', "g").replace('G',"C").replace('T', "a").replace('A',"T").replace('a',"A").replace('g',"G")
    return x


def complement5(string1, string2):
    string2 = reverse_complement(string2)
    count = 0
    for x in range(len(string1)):
        for y in range(len(string2)):
            i = 0
            while ((x + i) < len(string1)) and ((y + i) < len(string2)) and (string1[x + i] == string2[y + i]):
                i += 1

            count = max(i, count)
    if count >= 5:
        return True
    else:
        return False


dnaseq = input("Please input the name of the fasta file you would like to run the program on: \n")
    
positions = input("Please input 2 integer numbers in increasing order and separated by a blank space, representing positions in the DNA sequence: \n")
positions = positions.split()
position1 = int(positions[0])
position2 = int(positions[1])
    
fullstrand = readin_fasta(dnaseq)
    
long_sprimer = fullstrand[:(position1+20)]
long_rprimer = fullstrand[(position2 - 20):]
    
rev_long_sprimer = reverse_complement(long_sprimer)
                              
sprimer = rev_long_sprimer[0:20]
rprimer = long_rprimer[0:20]                          
                         
i = 0
correct_sprimer = False
while ((i<len(rev_long_sprimer)) and (correct_sprimer == False)):
    sprimer = rev_long_sprimer[i:i+20]
    if ((CG_edge(sprimer) == True) and (CG_count(sprimer)<13) and (CG_count(sprimer)>7) and (complement5(sprimer[:10],sprimer[10:]) == False)):
        correct_sprimer = True
        print('Start primer sequence : ', sprimer)
        
    else:
        sprimer = ''
        i += 1
if sprimer == '':
    print('Start primer sequence : ')
                          
j = 0
correct_rprimer = False
while ((j<len(long_rprimer)) and (correct_rprimer == False)):
    rprimer = long_rprimer[j:j+20]
    if ((CG_edge(rprimer) == True) and (CG_count(rprimer)<13) and (CG_count(rprimer)>7) and (complement5(rprimer[:10],rprimer[10:]) == False) and (complement5(sprimer,rprimer) == False)):
        correct_rprimer = True
        print('Reverse primer sequence : ', rprimer)
        
    else:
        rprimer = ''
        j += 1
if rprimer == '':
    print('Reverse primer sequence : ')