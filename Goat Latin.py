class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel = ['a', 'e', 'i', 'o' , 'u', "A" , "E" , "I", "O", "U"]
        sentence = [i for i in sentence.split()]
        print(sentence)
        for i in range(len(sentence)):
            #print(sentence[i])
            if sentence[i][0] in vowel:
                sentence[i] = sentence[i]+"ma" + (i+1)*"a"
            else:
                sentence[i] = sentence[i][1:] + sentence[i][0] + "ma" + (i+1)*"a"


        return  (" ".join(sentence))



obj = Solution()

str = "Each word consists of lowercase and uppercase letters only"

print(obj.toGoatLatin(str))
