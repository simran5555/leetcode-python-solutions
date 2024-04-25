# Isomorphic string

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        stot = {} #maps from s to t (s :t)
        ttos = {} #maps from t to s (t :s)
        for i, j in zip(s, t): #simultaneous loop using zip
            if i in stot and stot[i]!=j or j in ttos and ttos[j]!=i:  #checking if key : value is being changed
                return False
            else :  #keep mapping
                stot[i] = j
                ttos[j] = i
        return True
