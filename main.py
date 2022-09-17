import wordcloud
f = open(r"path/to/file","r")

uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just","words"]
    
l = f.read().lower()
l1 = []
l2=[]
for x in l.split():
    if x.isalpha() and x not in uninteresting_words:
        l1.append(x)
'''
for y in l1:
    if y not in l2:
        l2.append(y)
'''
l2 = set(l1)
print(l2)
dic = {a:l1.count(a) for a in l2}
print(dic)

cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(dic)
cloud.to_file("freq.jpg")

#print(l1)
