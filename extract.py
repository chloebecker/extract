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
    index = 0
    while index < content.len():
        item = content[index]
        #if it's equal to something in the dictionary, proceed
        if item in extract:
            if item == "pull":
                #subtract, ie: [...,pull,10,2,pull,...] -> 10 - 2 -> will set quotient = 8 
                #       then move on to next function (which is another pull in this case)
                quotient = content[index+1] - content[index+2]
                #move on to next function call in content
                index += 2
            
        #else, return error: "Error: *word* is not a valid function call."
        else: 
            print("Error: "+item+" is not a valid function call.")


Main()