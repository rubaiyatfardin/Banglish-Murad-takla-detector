import wget
wget.download('http://0xhosts.com/words.txt')
wget.download('http://0xhosts.com/translate.txt')
my_input=str(raw_input("Enter Your Sentence:"))
from pyavrophonetic import avro
import codecs
spit_it=my_input.split()
check=spit_it
print check
print "Total Words",len(check)
if len(check)==4:
  if check[0] and check[1] and check[2] and check[3] in open("words.txt").read().split():
    print ("False")
  else:
    s1=avro.parse(check[0])
    s2=avro.parse(check[1])
    s3=avro.parse(check[2])
    s4=avro.parse(check[3])
    p=codecs.open('translate.txt','r+','utf-8')
    p.write("%s.Translation : %s %s %s %s" %(s1,s2,s3,s4))
    p.close()
    print("Translation Completed.Saved to translate.txt")
    
    if s1 and s2 and s3 and s4 in codecs.open('words.txt','r','utf-8').read().split():
      print "Banglish Style"
    else:
      print "Murad Takla Style"
else:
    print ("Sorry max/min 4 words")
