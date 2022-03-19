f = open("words5.txt")

words = []
for w in f:
    words.append(w)

attempt = 0


has = [{},{},{},{}]
not_have = [[],[],[],[]]
must_be = [{},{},{},{}]

while (attempt  < 9) :
    attempt=attempt+1
    print (f"Attempt :  {attempt}:")
    word = input()
    
    puzzle =0
    while (puzzle<4):

        print (f"Result for {word}x (wrong) y (yellow) g (green) : {puzzle+1} {attempt}:")
        result = input()
        position = 0
        while position <5:
            if result[position] == "x":
                if word[position] in has[puzzle]:
                    positions = has[puzzle][word[position]]
                    positions.append(position)
                    has[puzzle][word[position]] = positions
                else:
                    not_have[puzzle].append(word[position])
            if result[position] == "y":
                positions = []
                if word[position] in has[puzzle]:
                    positions = has[puzzle][word[position]]
                positions.append(position)
                has[puzzle][word[position]] = positions
            if result[position] == "g":
                must_be[puzzle][position] = word[position]
            position=position + 1

        print (f"The word cannot contain: {not_have[puzzle]}" )
        print (f"The word has letter but not in this position: {has[puzzle]}")
        print (f"The word has in the specified position, this letter: {must_be[puzzle]}")

        candidate_words = []
        for candidate_word in words:
            skip_word = False
            for not_letter in not_have[puzzle] :
                if not_letter in candidate_word:
                    skip_word =True
                    next
            for must in must_be[puzzle]:
                if must_be[puzzle][must] !=candidate_word[must]:
                    skip_word =True
                    next
            for must_have in has[puzzle]:
                if must_have not in candidate_word:
                    skip_word =True
                    next
                else:
                    for must_not_be_position in has[puzzle][must_have]:
                        if candidate_word[must_not_be_position]==must_have:
                            skip_word=True
                            next
            if skip_word==False:
                candidate_words.append(candidate_word)

        print(f"Candidate words: {candidate_words}")
        puzzle=puzzle+1