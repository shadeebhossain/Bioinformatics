#to open the file BRCA1 BA that contains the nucleotide for breast cancer and
# downloaded from BRCA1 "nucleotide" section number 53 with over 15k
#nucleotide.
# It is saved as text file and r for read
gene =open("BRCA1.BA.txt","r")
#set the values to zero since all the nucleotides are labelled as
# G, A , C, T
g=0;
a=0;
c=0;
t=0;
#skip the first line of header
gene.readline()
for line in gene:
    line =line.lower()
    for char in line:
        if char == "g":
            g+=1
        if char == "a":
            a+=1
        if char == "c":
           c+=1
        if char == "t":
           t+=1
print "number of g's " +str(g)
print "number of a's " +str(a)
print "number of c's " +str(c)
print "number of t's " +str(t)
# 0. = convert to floating points
gc=(g+c+0.)/(a+t+c+g+0.)
print "number of gc content is  " +str(t)
