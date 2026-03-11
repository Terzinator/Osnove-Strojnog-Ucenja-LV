file = open('SMSSpamCollection.txt', 'r')

contents = file.read()

file.close

string = contents.splitlines()

spam = []
ham = []
print(string)
for i in len(string):
    if(string[i].startswith("spam")):
        spam.append(string[i])
    if(string[i].startswith("ham")):
        ham.append(string[i])

averageWordsHam = float(sum(len(ham.split()))/len(ham))
print('Average length of ham: ', averageWordsHam)
averageWordsSpam = float(sum(len(spam.split()))/len(spam))
print('Average length of spam: ', averageWordsSpam)

