import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",#创建一个叫X的类，他是Y的一种
    "class %%%(object):\n\tdef __init__(self,***)":
        "class %%% has-a __init__ that tales self and *** params.",#类X有一个__init__，他接收self，和J作为参数
    "class %%%(object):\n\tdef ***(self,@@@)":
        "class %%% has-a function *** that takes self and @@@ params.",#类X有一个名为M的函数，他接收self和J作为参数
    "*** = %%%()":
        "Set *** to an instance of class %%%.",#将foo设置为类X的一个实例
    "***.***(@@@)":
        "From *** get the *** function,call it with params self,@@@.",#从foo中找到M函数，并使用self和J参数调用它
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."#从foo中获取K属性，并将其设置为Q
}

#do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True
else:
    PHRASES_FIRST = False

#load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(),encoding="utf-8"))


def convert(snippet,phrase):
    class_names = [w.capitalize() for w in
                    random.sample(WORDS,snippet.count("%%%"))]
    other_names = random.sample(WORDS,snippet.count("***"))
    results = []
    params_names = []

    for i in range(0,snippet.count("@@@")):
        param_count = random.randint(1,3)
        params_names.append(', '.join(
            random.sample(WORDS,param_count)))

    for sentence in snippet,phrase:
        result = sentence[:]

        #fake class name
        for word in class_names:
            result = result.replace("%%%",word,1)

        #fake other class_names
        for word in other_names:
            result = result.replace("***",word,1)

        #fake parameter lists
        for word in params_names:
            result = result.replace("@@@",word,1)

        results.append(result)

    return results


#keep going until they hit ctrl-d
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question,answer = convert(snippet,phrase)
            if PHRASES_FIRST:
                question,answer = answer,question#右边给左边赋值

            print(question)

            input("> ")
            print(f"ANSWER:{answer}\n\n")
except EOFError:
    print("\nBye")
