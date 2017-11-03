code = open('code.txt', 'w')
all_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
limits = '()[]{}.;1234567890'
signs = '-+*/='
caracter = '() =.\t[]{}'
reserver_words = ['for', 'if', 'import', 'while', 'do', 'JOptionpane', 'else', 'int', 'String', 'float', 'public', 'static', 'void', 'class']
for line in open('hola.txt'):
    end = 0
    line_of_code = line.replace("\n","")
    char = line_of_code
    for j in range(len(line_of_code)):        
        if char[j] == '\t':
            word = "----"
            tag = "<span class ='tab'>{}</span>\n". format(word)
            code.write(tag)
        elif char[j] in limits:
            word = char[j: j+1]
            tag = "<span class ='limits'>{}</span>\n". format(word)
            code.write(tag)
        elif char[j] in signs:
            word = char[j: j+1]
            tag = "<span class ='signs'>{}</span>\n". format(word)
            code.write(tag)
        elif char[j] == '"':
            gat = 0
            for w in range(j, len(line_of_code)):
                if char[w] == '"':
                    word = line_of_code[j:j+gat+1]
                    tag = "<span class ='signs'>{}</span>\n". format(word)
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
                        tag = "<span class ='reserver'>{}</span>\n". format(word)
                    elif line_of_code[j+end] == '(':
                        word = string
                        tag = "<span class ='func'>{}</span>\n". format(word)
                    else:
                        word = string
                        tag = "<span class ='var'>{}</span>\n". format(word)
                    code.write(tag)
                    break
                end += 1
        elif char[j] == ' ':
            continue
        if j + 1 == len(line_of_code):
            tag = "<br>\n"
            code.write(tag)
code.close()
