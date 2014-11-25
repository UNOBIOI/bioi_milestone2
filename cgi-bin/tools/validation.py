from Bio.Seq import Seq

#Function checks to make sure the sequence only contains G,A,T or C
def contentCheck():
    f = open('sequence.fasta', 'r')
    fline = f.readline()
    secline = f.readline()
    f.close()
    seq = Seq(secline)
    Gcount = seq.count('G')
    Ccount = seq.count('C')
    Acount = seq.count('A')
    Tcount = seq.count('T')
    sum = Gcount + Ccount + Acount + Tcount

    if '\n' in seq:
        if sum == len(seq) - 1:
            print 'Sequence contains proper characters'
        else:
            print 'Sequence countains improper characters'
    else:
        if sum == len(seq):
            print 'Sequence contains proper characters'
        else:
            print 'Sequence contains improper characters'

#Function checks to makes sure the sequence is atleast 30 nucleotides in length
def sizeCheck():
    f = open('sequence.fasta', 'r')
    fline = f.readline()
    secline = f.readline()
    f.close()

    if len(secline) >= 30:
        print 'valid'
    else:
        print 'invalid'

#Function checks to make sure there are no more than 2 new lines.  
def newlineCheck():
    num_lines = sum(1 for line in open('sequence.fasta'))
    
    if num_lines > 2:
        print 'Too many new lines'
    else:
        print 'Valid amount of lines' 

#Fuctions checks the first line of the fasta file.
def firstlineCheck():
    f = open('sequence.fasta', 'r')
    fline = f.readline()
    f.close()

    if fline[0] == '>':
        print 'The first line is valid'
    else:
        print ' The first line is Invalid'

