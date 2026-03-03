file = open('song.txt', 'r')

song = file.read()

file.close

song = song.split()
unique_words = {}

for i in range(len(song)):
    if(song[i] in unique_words):
        unique_words[song[i]]+=1
    else:
        unique_words[song[i]] = 1


for key in unique_words.keys():
    if(unique_words[key] == 1):
        print(key, ': ', unique_words[key])
        count+=1
