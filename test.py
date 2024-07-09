s = input()
s_list = list(s)
spaces = list(map(int, input().split()))
word_spaces = []
for i in range(len(s_list)):
        if i in spaces:
            word_spaces.append(' ')
            word_spaces.append(s_list[i])
        else:
            word_spaces.append(s_list[i])

print(word_spaces)