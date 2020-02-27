#1.Given a list, url = [www.annauniv.edu, www.google.com, www.ndtv.com, www.website.org, www.bis.org.in, www.rbi.org.in]; Sort the list based on the top level domain (edu, com, org, in) using custom
url = ['www.annauniv.edu', 'www.google.com', 'www.ndtv.com', 'www.website.org', 'www.bis.org.in', 'www.rbi.org.in']
topDomainList = ["edu", "com", "org", "in"]
urlList = ["www.annauniv.edu", "www.google.com", "www.ndtv.com", "www.website.org", "www.bis.org.in", "www.rbi.org.in"]

def sortDomainNames(domainList, urlList):
    tempDomainList = domainList
    tempUrlList = urlList
    sortedUrlList = []

    for i, v in enumerate(tempDomainList):
        for i1, v1 in enumerate(tempUrlList):
            if v1.endswith(v):
                sortedUrlList.append(v1)

    print sortedUrlList

sortDomainNames(topDomainList, urlList)

#2.	Given a list of strings, return the count of the number of strings where the string length is 2 or more and the first and last chars of the string are the same.

# i.	['axa', 'xyz', 'gg', 'x', 'yyy']
# ii.	['x', 'cd', 'cnc', 'kk']
# iii.	['bab', 'ce', 'cba', 'syanora']

def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['axa', 'xyz', 'gg', 'x', 'yyy']))
print(match_words(['x', 'cd', 'cnc', 'kk']))

#3
a=['bbb', 'ccc', 'axx', 'xzz', 'xaa']
a1=['mix', 'xyz', 'apple', 'xanadu', 'aardvark']

def start_with_x(list1):
    new_list=[]
    for nlst in list1:
        #print(nlst)
        if nlst[0]=='x':
            new_list.append(nlst)
            list1.remove(nlst)
    print sorted(new_list) + sorted(list1)
# start_with_x(a)
# start_with_x(a1)

#4
def last(n):
    return n[-1]
def sort_tup(tuples):
    return sorted(tuples,key=last)
t1=[(1, 3), (3, 2), (2, 1)]
t2=[(1, 7), (1, 3), (3, 4, 5), (2, 2)]
print (sort_tup(t1))
print (sort_tup(t2))

#5
def list_new(list2):
    nw_list=[]
    for n in list2:
        if n not  in nw_list:
            nw_list.append(n)
    return nw_list
l3=[1,2,2,3,3,3]
print(list_new(l3))

#6
bookstore = {"New Arrivals":{"COOKING":["Everyday Italian","Giada De Laurentiis","2005","30.00"],"CHILDREN":["Harry Potter","J K.Rowling","2005","29.99"],"WEB":["Learning XML","Erik T. Ray","2003","39.95"]}}
for dic1 in bookstore.values():
    for lst in dic1.values():
	    d1=str(lst)
	    d1=d1[1:len(d1)-1]
	    print d1

#7
str1="Python is a widely used high-level programming language for general-purpose programming"
examp_dt={}
word_list=str1.split()
for word in word_list:
    examp_dt[word]=str1.count(word)
values=examp_dt.values()
values.sort()
values.reverse()
topfive_wrd=values[0:5]
cnt=0
for v in topfive_wrd:
    for word in examp_dt:
        if examp_dt[word]==v:
            print word, "\t\t", examp_dt[word]
            cnt+=1
            if cnt==5:
                break
    if cnt==5:
        break
print "\n\n\n"

#8
def getDic(str2):
	dic={}
	wordList=str2.split()
	length=len(wordList)
	for index,word in enumerate(wordList):
		if dic.has_key(word):
			continue
		tmpList=[]
		for i in range(index,length):
			if index==length-1:
				break
			if word==wordList[i]:
				nextWord=wordList[i+1]
				tmpList.append(nextWord)
		#print word,tmpList

		dic[word]=tmpList
	return dic

def predict(str2,word):
	wordDictionary=getDic(str2)
	print "in the given string, the word ' ",word,"' is likely followed by the list of words",wordDictionary[word]
#call the function
predict(str1,"Python")

#9
import re
str3 = """Interface		IP-Address	OK? 	Method Status	Protocol

FastEthernet0/0	192.168.1.242	YES 	manual up	up 
FastEthernet1/0        unassigned	YES 	unset		down 
Serial2/0              	192.168.1.250	YES 	manual up	up 
Serial3/0              	192.168.1.233	YES 	manual up	up 
FastEthernet4/0        unassigned	YES 	unset  		down	
FastEthernet5/0        unassigned	YES        unset 		down"""

for line in str3.splitlines():
    #print line
    matchObj = re.match(r'(\w+\d\/\d)\s+[.0-9a-z]+\s+\w+\s+(\w+\s?\w+?)\s+\w+', line, re.M | re.I)

    if matchObj:
        print  matchObj.group(1), ",", matchObj.group(2), "\n"

#10
def reachTarget(target):
    # Handling negatives by symmetry
    target = abs(target)

    # Keep moving while sum is
    # smaller or difference is odd.
    sum = 0
    step = 0
    while (sum < target or (sum - target) % 2 != 0):
        step = step + 1
        sum = sum + step

    return step


# Driver code
target = 3
print(reachTarget(target))
