import requests, urllib2, sys
print """
 .__.___             .__.      .__._________
 |--|\--\            |--|      |--|_________\\
 |--| \--\           |--|      |--|         \\\                             ________________    ________________
 |--|  \--\          |--|      |--|          \\\    |--|             |--|  |_____________   |  |_____________   |
 |--|   \--\         |--|      |--|           \\\   |--|             |--|               /--/                 /--/
 |--|    \--\        |--|      |--|           | |  |--|             |--|              /--/                 /--/
 |--|     \--\       |--|      |--|           //   |--|             |--|             /--/                 /--/
 |--|      \--\      |--|      |--|          //    |--|             |--|            /--/                 /--/
 |--|       \--\     |--|      |--|_________//     |--|             |--|           /--/                 /--/
 |--|        \--\    |--|      |--|_________/      |--|             |--|          /--/                 /--/
 |--|         \--\   |--|      |--|                |--|             |--|         /--/                 /--/
 |--|          \--\  |--|      |--|                |--|             |--|        /--/                 /--/
 |--|           \--\ |--|      |--|                |--|             |--|       /--/                 /--/
 |--|            \--\|--|      |--|                |--|             |--|      /--/                 /--/
 |--|             \--\--|      |--|                |--|             |--|     /--/                 /--/
 |--|              \--\-|      |--|                \--\             |--|    /--/                 /--/
 |--|               \--\|   _  |--|                 \--\===========/--/    /--/_____________    /--/_____________
 |__|                \__\  |_| |__|                  \__\=========/--/     |________________|   |________________|
 

                       """
#tool manual

print "                                       CODED IN PYTHON BY \'Entroboy\'                                  "
print "\n"
print "             -URL     :     https://example.com/        "+"\n"+"             -WORDLIST:     *list file path* or (w1 : .php / w2 : files or dirs / w3 : doted dirs / w4 : dirs )"

#built-in wordlists

w1 = "wordlists/PHP.wordlist"
w2 = "wordlists/Filenames_or_Directories_All.wordlist"
w3 = "wordlists/Filenames_Doted_All.wordlist"
w4 = "wordlists/Directories_All.wordlist"

#loading external or built-in wordlist

def load_words(file):
    wordlist = list()
    with open(file) as f :
        for line in f:
            wordlist.append(line.rstrip('\n'))
    return wordlist
wordlist = load_words(input("wordlist = "))

#Entering target url and choosing search type
            
dirlist = wordlist
m = raw_input("insert url:")
search_type = raw_input("Type:normal[N] /CSRF mining[CSRF]/both ?")
if search_type == "N" or search_type == "normal":
    word = raw_input('search in source code for :')    
    for x in dirlist :
        r = requests.get(m+x)
        sys.stdout.write('\r'+"trying"+">>>"+x)
    
        if r.status_code == 200 :
            html = urllib2.urlopen(m+x)
            source_code = html.read()
            if word in source_code: 
                print('\r'+"[*]FOUND"+">>>"+m+x+"  "+"&"+"  "+'[*]'+word+'\'S FOUND')
        
            else:
                print ('\r'+"[*]FOUND"+">>>"+m+x)                
            
elif search_type == "CSRF" or search_type == "CSRF mining" :
    session = requests.Session()
    session.cookies.get_dict()
    {}
    response = session.get(m)
    ses = session.cookies.get_dict()


    for x in dirlist :
        r = requests.get(m+x)
        sys.stdout.write('\r'+"trying"+">>>"+x)
    
        if r.status_code == 200 :
            html = urllib2.urlopen(m+x)
            source_code = html.read()
            if "<input" in source_code or "submit" in source_code or "post" in source_code and "token" in source_code: 
                print('\r'+"[*]FOUND"+">>>"+m+x)
        
            elif "<input" in source_code or "submit" in source_code or "post" in source_code and "token" not in source_code and "token" not in ses :
                print ('\r'+"[*]FOUND"+">>>"+m+x+"  "+"&"+"  "+'[*]Vulnerable to CSRF')                       
else :
    session = requests.Session()
    session.cookies.get_dict()
    {}
    response = session.get(m)
    ses = session.cookies.get_dict()
    word = raw_input('search in source code for :')    
    for x in dirlist :
        r = requests.get(m+x)
        sys.stdout.write('\r'+"trying"+">>>"+x)
    
        if r.status_code == 200 :
            html = urllib2.urlopen(m+x)
            source_code = html.read()
            if "<input" in source_code or "submit" in source_code or "post" in source_code and "token" in source_code: 
                print('\r'+"[*]FOUND"+">>>"+m+x) 
            elif word in source_code: 
                print('\r'+"[*]FOUND"+">>>"+m+x+"  "+"&"+"  "+'[*]'+word+'\'S FOUND')    
        
            elif "<input" in source_code or "submit" in source_code or "post" in source_code and "token" not in source_code and word in source_code and "token" not in ses:
                print ('\r'+"[*]FOUND"+">>>"+m+x+"  "+"&"+"  "+'[*]Vulnerable to CSRF'+"  "+"&"+"  "+'[*]'+word+'\'s found')
                
            elif "<input" in source_code or "submit" in source_code or "post" in source_code and "token" not in source_code and "token" not in ses :
                print ('\r'+"[*]FOUND"+">>>"+m+x+"  "+"&"+"  "+'[*]Vulnerable to CSRF')    
               
    
