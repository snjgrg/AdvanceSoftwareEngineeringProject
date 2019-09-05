from collections import Counter, defaultdict

    
f=open("1661.txt","r")
def getTotalNumberOfWords():
    
    #f=open("1661.txt","r")
    f=open("1661.txt","r")
    count=0
    for line in f:
        for word in line.split():
            count+=1
    print("total number of words:",count)


def getTotalUniqueWords():
    #f=open("1661.txt","r")
    d=defaultdict(int)
    for line in f:
        for word in line.split():
            d[word]+=1
    print("total unique numbers is",len(d))


def get20MostFrequentWords():
    f=open("1661.txt","r")
    dict={}
    for line in f:
        for word in line.split():
            dict[word]=dict.get(word,0)+1
            k=Counter(dict)
        high=k.most_common(20)
    print("Dictionary with 20 frequent words:")
    print("keys:  Values")
    for i in high:
        print('[',i[0],', ',i[1],']')




def get20MostInterestingFrequentWords():
    f=open("1661.txt","r")
    g=open("1-1000.txt","r")
    dict={}
    
    for line in f:
        for word in line.split():
            
           
                
            dict[word]=dict.get(word,0)+1
            k=Counter(dict)
        high=k.most_common(20)
            
            

# result=filter(lambda x: x%200!=0,k)
    
    print("Dictionary with 20 Interesting frequent words:")
    print("keys:  Values")
    for i in high:
        print('[',i[0],', ',i[1],']')




getTotalNumberOfWords()
getTotalUniqueWords()
#get20MostFrequentWords()
get20MostInterestingFrequentWords()











