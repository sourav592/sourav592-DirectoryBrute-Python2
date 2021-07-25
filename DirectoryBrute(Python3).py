import requests , sys

url = sys.argv[1]
wordlist = sys.argv[2]

def write(word):
    f1 = open("I_Found.txt" ,"a")
    f1.write(word +"\n")

fo = open(wordlist,"r+")
for i in range (200000):
    word = fo.readline(10).strip()
    surl = url+word

    response = requests.get(surl)

    if (response.status_code == 200):
        print ("[+] Found :- ", surl)
        write(word)

    else:
        print("[-] Not Found :-", surl)
        pass
