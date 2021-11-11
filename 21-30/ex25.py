def break_words(stuff):#stuff填充
    """this function will break up words for us."""
    words = stuff.split(' ')#Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
    print(">>> words:",repr(words))
    return words

def sort_words(words):#从break_words返回的结果放进去
    """sorts the words."""
    print(">>> sorted:",repr(sorted))
    return sorted(words)#排序操作

def print_first_word(words):
    """prints the first word after popping it off."""
    word  = words.pop(0)#Python 字典 pop() 方法删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
    print(">>> word:",repr(word))
    print(word)

def print_last_word(words):
    """prints the last word after poping it off."""
    word = words.pop(-1)
    print(">>> word:",repr(word))
    print(word)

def sort_sentence(sentence):
    """takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    print(">>> word:",repr(words))
    return sort_words(words)

def print_first_and_last(sentence):
    """print the first and last words of the sentence."""
    words = break_words(sentence)
    print(">>> +++++word:",repr(words))
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print(">>> +++++word:",repr(words))
    print_first_word(words)
    print_last_word(words)
