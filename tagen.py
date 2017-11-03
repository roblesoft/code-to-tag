code = open('code.txt', 'w')
all_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
limits = '()[]{}.;1234567890'
signs = '-+*/='
caracter = '() =.\t[]{}'
reserver_words = ['for', 'if', 'import', 'while', 'do', 'JOptionpane', 'else', 'int', 'String', 'float', 'public', 'static', 'void', 'class']
code.write("<style>.tab{color: #222526} .reserver{color: #FC4349 } .limits{color:#FFF} .var{color:#B2FF55} .func{color:#00E4ED} .signs{color:#FC4349} .string{color:#EAFF11} .codigo{background-color: #222526; padding: 10%;}</style>\n")
tag = "<code>\n"
code.write(tag)
tag = '\t<div class="codigo">\n'
code.write(tag)
for line in open('input.txt'):
    end = 0
    line_of_code = line.replace("\n","")
    char = line_of_code
    for j in range(len(line_of_code)):        
        if char[j] == '\t':
            word = "----"
            tag = "\t\t<span class ='tab'>{}</span>\n". format(word)
            code.write(tag)
        elif char[j] in limits:
            word = char[j: j+1]
            tag = "\t\t<span class ='limits'>{}</span>\n". format(word)
            code.write(tag)
        elif char[j] in signs:
            word = char[j: j+1]
            tag = "\t\t<span class ='signs'>{}</span>\n". format(word)
            code.write(tag)
        elif char[j] == '"':
            gat = 0
            for w in range(j, len(line_of_code)):
                if char[w] == '"':
                    word = line_of_code[j:j+gat+1]
                    tag = "\t\t<span class ='string'>{}</span>\n". format(word)
                    code.write(tag)
                gat += 1
            j += gat
        
        elif char[j] in all_letters:
            end = 0
            if char[j-1] in all_letters:
                continue
            for i in range(j, len(line_of_code)):
                if char[i] in caracter:
                    string = line_of_code[j:j+end]
                    if string in reserver_words:
                        word = string
                        tag = "\t\t<span class ='reserver'>{}</span>\n". format(word)
                    elif line_of_code[j+end] == '(':
                        word = string
                        tag = "\t\t<span class ='func'>{}</span>\n". format(word)
                    else:
                        word = string
                        tag = "\t\t<span class ='var'>{}</span>\n". format(word)
                    code.write(tag)
                    break
                end += 1
        elif char[j] == ' ':
            continue
        if j + 1 == len(line_of_code):
            tag = "\t\t<br>\n"
            code.write(tag)
tag = "\t</div>\n"
code.write(tag)
tag = "</code>"
code.write(tag)
code.close()
