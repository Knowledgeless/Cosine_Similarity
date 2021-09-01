import math

class Similarity:
    # creating constructor and taking strings
    def __init__(self, string1, string2):
        self.user1 = string1.split()
        self.user2 = string2.split()
        
    def wordList(self):
        words = []
        for i,j in zip(self.user1, self.user2):
            if i not in words:
                words.append(i)
            if j not in words:
                words.append(j)
            else:
                pass
        return words
    
    def get_similarities(self):
        count1 = []
        count2 = []
        s1xs2 = 0
        s1_magnitude = 0
        s2_magnitude = 0
        
        for i in self.wordList():
            data1 = self.user1.count(i)
            data2 = self.user2.count(i)
            count1.append(data1)
            count2.append(data2)
            
        for k, l in zip(count1,count2):
            c = k*l
            s1xs2 +=c
            s1_magnitude += (k**2)
            s2_magnitude += (l**2)
            
        result = s1xs2/(math.sqrt(s1_magnitude)*math.sqrt(s2_magnitude))
        return round(result, 3)
    def thetaValue(self):
        return round(math.cos(self.get_similarities()), 3)        
        
        
if __name__ == "__main__":
    user1 = input("First String: ")
    user2 =input("Second String: ")
    obj = Similarity(user1, user2)
    print("""
        Given Texts Are:
        1.{} 
        2.{} \n
        The Similarity Result Is: {}\n
    """.format(user1, user2, obj.get_similarities()))
    choose = input("Need Theta Value? (Y/n): ")
    if choose.lower() == "y":
      print("The Value of the Theta is: {} radian".format(obj.thetaValue()))
    else:
     pass
    print("\nHappy Coding\n")
