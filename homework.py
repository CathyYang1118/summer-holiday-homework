def text_to_words(the_text): 
    """删除符号"""
    my_substitutions = the_text.maketrans(
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      "abcdefghijklmnopqrstuvwxyz                                          ")
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds

def open_file(filename): #相对路径：当前文件夹./上一层../
    """读取文件"""
    f=open(filename,'r')
    data = f.readlines()
    data2=[]
    for words in data:
        words_2 = words.strip()
        data2.append(words_2)
    data2=str(data2)
    #return data2
    return text_to_words(data2)

def test_words(file_be_tested,file_test):
    """二分测试"""
    mid = len(file_be_tested)
    if len(file_be_tested) == 0:
        return False
    else:
        mid = len(file_be_tested) // 2
        if file_test == file_be_tested[mid]:
            return True
        else:
            if file_test <= file_be_tested[mid]:
                return test_words (file_be_tested[0:mid],file_test)
            else:
                return test_words (file_be_tested[mid+1:],file_test)    

story_open = open_file('爱丽丝.txt')
story_open.sort()
list_open = open_file('单词表.txt')
 
#打开，排序

count = 0
list_words = []
for word_criterion in list_open:
    list_words.append(word_criterion)
for words in story_open:
    result = test_words(list_words,words)
    if result == False:
        count += 1
#测试超纲单词数量
        
print('书中一共有{0}个单词，其中超纲单词有{1}个，其占比为{2}'.format
      (len(story_open),count,round(count/len(story_open),2)))
