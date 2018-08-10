import textract

BIBLE_DICT = {'Genesis':1,'Exodus':2,'Leviticus':3,'Numbers':4,'Deuteronomy':5,'Joshua':6,'Judges':7,'Ruth':8,'Samuel':'check9',
              'Kings':'check11','Chronicles':'check13','Ezra':15,'Nehemiah':16,'Esther':17,'Job':18,'Psalms':19,'Proverbs':20,
              'Ecclesiastes':21,'Solomon':22,'Isaiah':23,'Jeremiah':24,'Lamentations':25,'Ezekiel':26,'Daniel':27,
              'Hosea':28,'Joel':29,'Amos':30,'Obadiah':31,'Jonah':32,'Micah':33,'Nahum':34,'Habakkuk':35,'Zephaniah':36,
              'Haggai':37,'Zechariah':38,'Malachi':39,'Matthew':40,'Mark':41,'Luke':42,'John':'check43','Acts':44,'Romans':45,
              'Corinthians':'check46','Galatians':48,'Ephesians':49,'Philippians':50,'Colossians':51,'Thessalonians':'check52',
              'Timothy':'check54','Titus':56,'Philemon':57,'Hebrews':58,'James':59,'Peter':'check60','Jude':65,'Revelation':66}
              
def listWords(textIn):
    key = "Home Church Questions"
    page1 = textIn.split(key)
    page1 = page1[0]
    wordList = []
    beg = 0
    pos = 0
    while pos < len(page1):
        if ord(page1[pos]) > 122 or ord(page1[pos]) < 44 or ord(page1[pos])==46:
            wordList.append(page1[beg:pos])
            beg = pos+1
        pos = pos+1
    return wordList

def listBiblePassages(wordListIn):
    bibleVerses = []
    for i in range(0,len(wordListIn)):
        check = BIBLE_DICT.get(wordListIn[i])
        if check != None:
            if isinstance(check, int):
                bibleVerses.append('{0} {1}'.format(wordListIn[i],wordListIn[i+1]))
    return bibleVerses
   
    

text = textract.process("2018-01-28-1112-notes.pdf")
words = listWords(text)
BP = listBiblePassages(words)      
print(BP)
