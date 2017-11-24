from random import randint

#our stack will just be a list- .append() = push, .pop() = pop!
stack = []
extract = ["pour", "pull", "filter", "scoop", "grind", "brew", "(|)", "stir", "price", "lightRoast", "darkRoast", "makeLatte", "roast", "new"]

def GetText(fileName) :
    #opens file with name of "sample.txt"
    file = open(fileName+".txt", "r")
    #reads the whole file at once 
    readFile = file.read()
    #returns a list, ie: ['pour', '1', '2', 'pull', '5', '2', ...etc]
    global content 
    content = readFile.split();
    file.close()
      
    print(content)#TEMP

def Main():
    GetText("sample")
    #go through each word/item in the list
    index = 0
    print(index)#TEMP
    print(len(content))
    while index < len(content):
        item = content[index]
        print(item)#TEMP
        #if it's equal to something in the dictionary, proceed
        if item in extract:
            if item == "pull":
                if IsInt(content[index+1]) and IsInt(content[index+2]):
                    #subtract, ie: [...,pull,10,2,pull,...] -> 10 - 2 -> will set quotient = 8 
                    #       then move on to next function (which is another pull in this case)
                    quotient = int(content[index+1]) - int(content[index+2])
                    print(content[index+1],"-",content[index+2],"=",quotient)
                else:
                    print("Error: you can only perform pull on integers")
                #move on to next function call in content
                index += 2
            elif item == "brew":
                print(content[index+1])
                index += 1
            elif item == "(|)":
                index += 1
                while content[index] != "(|)":
                    index += 1
                    if index > 100:
                        print("Error: your comment is either over 100 words or you are missing the ending '(|)' ")
            elif item == "stir":
                if isinstance(content[index+1], str) and isinstance(content[index+2], str):
                    concat = content[index+1] + content[index+2]
                else:
                    print("Error: one or both of the values you are trying to concatenate is not a string")
                index += 1
            elif item == "makeLatte":
                if IsInt(content[index+1]):
                    fact = Factorial()
                    print(fact)
                else:
                    print("Error: you can only perform makeLatte on integers")
                index += 1
            elif item == "roast":
                if IsInt(content[index+1]) and IsInt(content[index+2]):
                    rand = randint(content[index+1], content[index+2])
                    print("random number is: "+rand)
                else:
                    print("Error: you can only perform roast on integers")
                index += 2
            #temporary, until we get all the functions in here ^
            else:
                print("Function not yet available, sorry!")
                index += 1
        #else, return error: "Error: *word* is not a valid function call."
        else: 
            print("Error: "+item+" is not a valid function call.")
            index += 1

def Factorial(num):
    if num == 0:
        return 1
    else:
        return num * Factorial(num-1)
    
def IsInt(num):
    try:
        num = float(num)
        return num.is_integer()
    except:
        return False
    
Main()


