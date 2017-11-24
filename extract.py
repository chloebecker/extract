from random import randint

#our stack will just be a list- .append() = push, .pop() = pop!
stack = []
content = []
extract = ['pour', 'pull', 'filter', 'scoop', 'grind', 'brew', 
           '(|)', 'stir', 'price', 'lightRoast', 'darkRoast', 
           'makeLatte', 'roast', 'new']

def GetText(fileName) :
    #opens file with name of "sample.txt"
    file = open(fileName+".txt", "r")
    #reads the whole file at once 
    readFile = file.read()
    #returns a list, ie: ['pour', '1', '2', 'pull', '5', '2', ...etc]
    content = readFile.split();
    file.close()
      
    print(content)

def Main():
    GetText("sample")
    #go through each word/item in the list
    for item in content:
        #if it's equal to something in the dictionary, proceed
        if item in extract:
            # a bunch of ifelse blocks for the functions like so:
            # if word = pour
                # push the next two values onto the 
        #else, return error: "Error: *word* is not a valid function call."
        else: 
            print("Error: "+item+" is not a valid function call.")


Main()