import operator
import sys




def readFile(filename):
    data = {}
    f = open(filename, 'r')
    for line in f:
        (name, count) = line.split();
        data[name]=int(count)
    return data

def computePrior(dict):
    prior = {}
    #print sum(dict.values)
    for (name, count) in dict.iteritems():
        prior[name] = float(count)/float(sum(dict.itervalues()))

    return prior
def guessWord(evidence):
    if evidence == "0": return

def checkChar(string, letter, position):
    if string.find(letter) != -1:
       if position in [pos for pos, char in enumerate(string) if char == letter]:
           return 1


    return 0

def main():
   #  data = readFile("hw1_word_counts_05.txt")
   #  prior = computePrior(data)
   #
   #  i=0;
   #
   #  for pair in sorted(prior.items(), key=operator.itemgetter(1), reverse = True):
   #      if i<15:
   #          print pair
   #      i+=1
   #  print "\n"
   #  i=0;
   #  for pair in sorted(prior.items(), key=operator.itemgetter(1), reverse = False):
   #      if i<14:
   #          print pair
   #      i+=1
   #
   # #for line in sys.stdin:
   #
   #
   print checkChar("ABA", 'A',0)
   return 0




if __name__ == "__main__":
    main()