print "******************************Script By Osman Malik***********************************\n\n\n "
print "Enter Name Of Word List To Make Combinations from .( should be in the same directory )\n The combinations made will be saved in the file Wordlist.txt"

filne = raw_input()
PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" 
words=[]
with open(filne, 'r+') as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
        line = lines[i]
        line = "".join(c for c in line if c in PERMITTED_CHARS)
        words.insert(i+1,line)
first=0
firstcount=len(lines)
secound=len(lines)
secoundcount=0
fo = open("wordlist.txt", "wb")
i=1
print "\n\n\n******************************* Done ***********************************\n "
print "They Are : \n\n\n"

while (firstcount != first):
  while (secound != secoundcount):
      w = words[first]+words[secoundcount]
      fo.write(w+"\n")
      print '\n                  '+w
      secoundcount=secoundcount+1
      i=i+1
  secoundcount=0
  secound=len(lines)
  first=first+1
print "\n "
print "Total number :"
print i

# Close opend file
fo.close()
