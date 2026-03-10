from typing import List
class Solution:
    
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)

        
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
            
        countS, countT = {}, {}
        
        for i in range(len(s)):
            # dict.get() lay gia mac dinh == 0 dau tien sau do tang dan len 1
            countS[s[i]] =  1 + countS.get(s[i], 0)
            countT[t[i]] =  1 + countT.get(t[i], 0)

            
        return countS == countT
            

            

    def isAnagram(self, s: str,  t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] *26  # create list 26 phan tu == 0 
        for i in range(len(s)):
            # lap cung luc 2 chuoi :  neu s co thi tang, con t thi co giam. neu cung atn suat thi ket qua tat ca bang 0 het || nguoc lai thi co su khac nhau va tan suat
            count[ord(s[i]) - ord('a')]  += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0: 
                return False
        return True

        
        
