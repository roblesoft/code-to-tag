code = open('code.txt', 'w')
all_letters = 'abcdefghijklmnopqrstuvwxyzSJO'
limits = '()[]{}.;'
signs = '-+*/='
coin = 0
caracter = '() =.\t[]{}'
reserver_words = ['for', 'if', 'import', 'while', 'do', 'JOptionpane', 'else', 'int', 'String', 'float', 'public', 'static', 'void', 'class']
for line in open('hola.txt'):
    coin = 0
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
        elif char[j] in all_letters:
            end = 0
            if char[j-1] in all_letters:
                continue
            for i in range(coin, len(line_of_code)):
                if char[i] in caracter:
                    string = line_of_code[coin:coin+end]
                    if string in reserver_words:
                        word = string
                        tag = "<span class ='reserver'>{}</span>\n". format(word)
                    else:
                        word = string
                        tag = "<span class ='var'>{}</span>\n". format(word)
                    code.write(tag)
                    break
                end += 1
            coin += end - 1
        elif char[j] == ' ':
            coin += 1
            continue
        if coin + 2>= len(line_of_code) or char[j] == ';':
            tag = "<br>\n"
            code.write(tag)
        coin += 1
code.close()
