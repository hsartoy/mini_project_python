import optparse
import re


if __name__ == '__main__':
    parser = optparse.OptionParser('usage%prog -F <CC file>')
    parser.add_option('-F', dest="ccFile", type="string", help = 'Specify file with CC numbers')
    (options, args) = parser.parse_args()
    ccFile = options.ccFile

    if ccFile == None:
        print(parser.usage)
        exit(0)
        
    '''
        1) Open the file with potential credit card numbers, one on each line
        2) For each number, remove any trailing whitespace
        3) Create a regular expression to identify a valid credit card number
        4) Go through the file and print the total number of valid credit card numbers that you've found
    '''
    #### YOUR CODE HERE #####
    data = open("ccnumbers.txt", "r")    #1)Open the file with potential credit card numbers, one on each line
    total = 0
    for x in data:
        data.readline(())                   #1)Open the file with potential credit card numbers, one on each line
        data = data.replace(/[ -]/g,'');    #2) For each number, remove any trailing whitespace
        #3) Create a regular expression to identify a valid credit card number
        total++                             
    print(total)                            #4) Go through the file and print the total number of valid credit card numbers that you've found
    
    ###https://www.regular-expressions.info/creditcard.html
    ##https://docs.python.org/2/howto/regex.html
    ### Reference ^
