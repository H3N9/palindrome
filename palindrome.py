"""
    Longest palindrom
    accept only alphbet A-z and cutting all punctuation marks.

"""
def palindrome(s):
    if(len(s) < 3):
        return s
    covertStr = ''.join([x.lower() for x in s if x.isalpha()])
    #transform to lower case and cutting all punctuation marks.
    resultStr = ''
    halfStr = len(s)//2 + 1 #half string
    for mainStr in range(1,halfStr):
      for shiftStr in range(0,len(s) - mainStr):
        if(shiftStr+mainStr*2-1 >= len(covertStr)):
          break
        leftStr = covertStr[shiftStr:shiftStr+mainStr]
        rightStr = covertStr[shiftStr+mainStr*2-1:shiftStr+mainStr-1:-1]
        skipStr = covertStr[shiftStr+mainStr*2:shiftStr+mainStr:-1]
        if(leftStr == skipStr and shiftStr+mainStr*2 < len(covertStr)):
          resultStr = covertStr[shiftStr:shiftStr+mainStr*2+1]
          break
        if(leftStr == rightStr):
          resultStr = covertStr[shiftStr:shiftStr+mainStr*2]
          
    return resultStr

inputStr = palindrome(input())
    
print('{result} is {found}palindrome.'.format(result = inputStr if inputStr else 'it', found='' if inputStr else 'not '))
