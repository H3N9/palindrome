def longestCommonPrefix(strs):
    maximumStr = 0
    prefix = ''
    oldStr = ''
    for str in strs:
        if(len(str) > maximumStr):
            maximumStr = len(str)
    for i in range(maximumStr):
        token = False
        
        if token:
            break
        for j in range(len(strs)):
            text = strs[j][0:i+1]
            if j == 0:
                oldStr = text
            if len(strs[j]) < i:
                token = True
                break
            if text != oldStr:
                token = True
            oldStr = text
            
        if(not token):
            prefix = oldStr

    print(prefix)

longestCommonPrefix(input().split(" "))