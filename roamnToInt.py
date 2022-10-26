def romanToInt(s: str) -> int:
        romanDictionary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        oldRoman = 0
        romanInt = 0
        for romanStr in s:
            if romanDictionary[romanStr] > oldRoman:
                romanInt +=  abs(oldRoman * 2 - romanDictionary[romanStr])
            else:
                romanInt += romanDictionary[romanStr]
            oldRoman = romanDictionary[romanStr]
        return romanInt
        
print(romanToInt(input()))