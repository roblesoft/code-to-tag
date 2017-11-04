code = open('code.txt', 'w')
all_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
limits = '()[]{}.,;1234567890'
signs = '-+*/=<>'
ind = 0
caracter = '() =.\t[]{};+-,'
ends = '() = \t{};-+'
reserver_words = ['for', 'if', 'new', 'import', 'while', 'do', 'JOptionpane', 'else', 'int', 'String', 'float', 'public', 'static', 'void', 'class', 'null']
code.write("<!--code by roblesoft, github.com/roblesoft-->\n")
code.write("<style>.tab{color: #222526} .reserver{color: #FC4349 } .limits{color:#FFF} .var{color:#ADD96C} .func{color:#00E4ED} .signs{color:#FC4349} .string{color:#EAFF11} .codigo{background-color: #222526; padding: 10%; border-radius: 10px} .ind{color:grey} .coment{color:grey}</style>\n")
tag = "<code>\n"
code.write(tag)
tag = '\t<div class="codigo">\n'
code.write(tag)
rel = False
for line in open('input.txt'):
    end = 0
    line_of_code = line.replace("\n","")
    char = line_of_code
    ind += 1
    if ind == 1:
        indi = '\t\t<span class="ind">{}</span>'. format(ind)
    else:
        indi = '<span class="ind">{}</span>'. format(ind)
    code.write(indi)
    word = '---'
    tag = "<span class ='tab'>{}</span>". format(word)
    code.write(tag)
    for j in range(len(line_of_code)):        
        if char[j] == '\t':
            word = "----"
            tag = "<span class ='tab'>{}</span>". format(word)
            code.write(tag)
        elif char[j] == '/' and char[j+1] == '/':
            coment = True
            tag = "<span class = 'coment'>{}</span>". format(line_of_code)
            code.write(tag)
        elif char[j] in limits and rel == False and coment == False:
            word = char[j: j+1]
            tag = "<span class ='limits'>{}</span>". format(word)
            code.write(tag)
        elif char[j] == ' ' and rel == False and coment == False:
            word = ' '
            tag = "<span class ='tab'>{}</span>". format(word)
            code.write(tag)
        elif char[j] in signs and rel == False and coment == False:
            word = char[j: j+1]
            tag = "<span class ='signs'>{}</span>". format(word)
            code.write(tag)
        elif char[j] == '"':
            gat = 0
            rel = True
            if char[j+1] == ';' or char[j+1] == ')' or char[j+1] == '+' or char[j+1] == ' ':
                rel = False
                continue
            for w in range(j, len(line_of_code)):
                if char[w] == '"' and char[w + 1] in ends:
                    word = line_of_code[j:j+gat+1]
                    tag = "<span class ='string'>{}</span>". format(word)
                    code.write(tag)
                    break
                gat += 1        
        elif char[j] in all_letters and rel == False and coment == False:
            end = 0
            if char[j-1] in all_letters:
                continue
            for i in range(j, len(line_of_code)):
                if char[i] in caracter:
                    string = line_of_code[j:j+end]
                    if string in reserver_words:
                        word = string
                        tag = "<span class ='reserver'>{}</span>". format(word)
                    elif line_of_code[j+end] == '(':
                        word = string
                        tag = "<span class ='func'>{}</span>". format(word)
                    else:
                        word = string
                        tag = "<span class ='var'>{}</span>". format(word)
                    code.write(tag)
                    break
                end += 1
        elif char[j] == ' ':
            continue
        if j + 1 == len(line_of_code):
            coment = False
            tag = "<br>"
            code.write(tag)
tag = "\n\t</div>\n"
code.write(tag)
tag = "</code>"
code.write(tag)
code.close()
