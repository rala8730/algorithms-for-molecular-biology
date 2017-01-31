#!/usr/bin/env/python

import sys, getopt, math, os.path, string,collections

def readInput(inFile):
    File=open(inFile,'r')
    sequence_name=[]
    sequences=[]
    output=[]
    index=0
    for line in File:
        if line.startswith('>'):
			if index >=1:
				sequence_name.append(name)
				sequences.append(seq)
			index+=1
			name=line[1:].rstrip('\n')
			seq=' '
        else:
            seq+=line.rstrip('\n')
	for i in range(len(sequence_name)):
		output.append((sequence_name[i],sequences[i]))
    return output


def usage():
	# print the usage of the application
    #print 'python Rasmi_lamichhane_hw1.py -F <filename> -S <seq-name> -K <kmer>'
    #print "where -F specifies the .txt fasta file to be read and analyzed,"
    #print "-K is the size of kmer to search for"
    #print "and -S is the Sequence."
    print "-----------------------------------------"
def main(argv):

    try:
        opts, args = getopt.getopt(argv, "H:F:K:S:")
    except getopt.GetoptError:
        #print "ERROR! An input file (-F) and a length of a kmer (-K) must be specified. Correct usage:"
        usage()
        sys.exit(2)
    for opt, arg in opts:
        # process each input parameter
        if opt == '-H':
            #print "Correct usage is:"
            usage()
            sys.exit()
        if opt == '-F':
            if os.path.isfile(arg):
                inputFile = arg
            # If the input file given does not exist, print an error message and exit the program
            else:
                #print "ERROR! Input file must exist. Correct usage:"
                usage()
                sys.exit(2)
        if opt == '-K':
            kmer = arg

        if opt =='-S':
            usage()
            seqname=arg

    # Run the readInput function to format the input file. Store the returned
    # list in the variable sequences

    #store the array
    id = "ID"

    sequences=readInput(inputFile)
    foundseq = searchseq(seqname,sequences)

    splitseq=splitedfoundseq(foundseq)
    GCcount=GC_content(splitseq)

    kmermatch=k_mermatch(kmer, foundseq)

    revseq=reverse_seq(foundseq)

    comp=compliment(kmer,revseq)

    rev_kmermatch=revkmatch(kmer,revseq)

    print "File:", inputFile
    print "Seq:", foundseq
    print "rev comp:",comp
    print "seq length:", len(foundseq)
    print "Kmer:",kmer
    print "kmermatchpos:",kmermatch,rev_kmermatch
    print "GC count is :", GCcount,"%"
    #print "seqname", "foundseq", "kmermatch", "kmer", "forward", "id"


    for match in range(0,len(kmermatch)):
        print seqname,foundseq,kmermatch[match],kmer,"+",id
    for match in range(0,len(rev_kmermatch)):
        print seqname,foundseq,rev_kmermatch[match],kmer,"-",id

def searchseq(seqname,sequences):
    for lines in sequences:
        if(lines[0]==seqname):
            return lines[1]

def splitedfoundseq(foundseq):
        split=foundseq.split()[0]
        return split

def GC_content(splitseq):
    count=0
    for pos in range(len(splitseq)-1):
        if (splitseq[pos]=="G" and splitseq[pos+1]=="C") or (splitseq[pos]=="C" and splitseq[pos+1]=="G"):
           count=count+1
        elif (splitseq[pos]=="T" and splitseq[pos+1]=="A") or (splitseq[pos]=="A" and splitseq[pos+1]=="T"):
            count = count+1
    count=count -1 +0.0
    G_Ccount=(float(count) *100.0)/len(splitseq)
    return G_Ccount

#possible longest length of the string
def k_mermatch(kmer, foundseq):
    index=0
    matchpos=[]
    for pos in range(len(foundseq)-len(kmer)+1):
        if kmer==foundseq[index:index+len(kmer)]:
            matchpos.append(index)
        index=index+ 1

    return matchpos

def reverse_seq(foundseq):
    for seq in foundseq:
        reverse=foundseq[::-1]
        print reverse,
        return reverse

def compliment(kmer,revseq):
    compliment=""
    for seq in revseq:
        if seq=="G":
            seq="C"
            compliment=compliment+seq
        elif seq=="C":
            seq="G"
            compliment=compliment+seq
        elif seq=="A":
            seq="T"
            compliment=compliment+seq
        elif seq=="T":
            seq=="A"
            compliment=compliment+seq
        else:
            compliment=compliment+seq
            print"finish converting to compliment not a single A, T, C, or G"
    print compliment,"------compliment"
    print revseq,"+++++reverseseq"
    return compliment

def revkmatch(kmer,comp):

    return k_mermatch(kmer,comp)


#seq name 2) position match
def Gffformat(seqname,foundsed,kmermatch,kmer,forward,id):
    #gff= seqname,foundsed, kmermatch, kmer, forward, id
    return 0


if __name__== '__main__':
    main(sys.argv[1:])







