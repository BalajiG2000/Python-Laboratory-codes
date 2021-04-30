def sortedSentence(Sentence): 
	words = Sentence.split(" ") 
	words.sort() 
	newSentence = " ".join(words) 
	return newSentence 

Sentence = input()
print(sortedSentence(Sentence)) 
 

