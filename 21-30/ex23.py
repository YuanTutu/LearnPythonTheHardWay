import sys
script,encoding,error = sys.argv


def main(language_file,encoding,errors):
    print(">>>> main",repr(language_file),encoding,errors)
    line = language_file.readline()

    if line:
        print(">> there's a line",repr(line))
        print_line(line,encoding,errors)#调用print_line函数
        print(">>>> calling main again")
        return main(language_file,encoding,errors)#重新调用main
    print("<<<< exit main")#最后结束时候才会输出


def print_line(line,encoding,errors):
    print(">>>> print_line",repr(line),encoding,errors)
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding,errors = errors)
    cooked_string = raw_bytes.decode(encoding,errors = errors)

    print(raw_bytes,"<===>",cooked_string)
    print("<<<< exit print_line")


languages = open("languages.txt",encoding = "utf-8")

main(languages,encoding,error)
