f = open("words5.txt")

words = []
for w in f:
    words.append(w)

attempt = 0

has = {}
not_have = []
must_be = {}

while (attempt  < 9) :
    attempt=attempt+1
    print (f"Attempt :  {attempt}:")
    word = input()
    print (f"Result x (wrong) y (yellow) g (green) :  {attempt}:")
    result = input()
    position = 0
    while position <5:
        if result[position] == "x":
            if word[position] in has:
                positions = has[word[position]]
                positions.append(position)
                has[word[position]] = positions
            else:
                not_have.append(word[position])
        if result[position] == "y":
            positions = []
            if word[position] in has:
                positions = has[word[position]]
            positions.append(position)
            has[word[position]] = positions
        if result[position] == "g":
            must_be[position] = word[position]
        position=position + 1

    print (f"The word cannot contain: {not_have}" )
    print (f"The word has letter but not in this position: {has}")
    print (f"The word has in the specified position, this letter: {must_be}")

    candidate_words = []
    for word in words:
        skip_word = False
        for not_letter in not_have :
            if not_letter in word:
                skip_word =True
                next
        for must in must_be:
            if must_be[must] !=word[must]:
                skip_word =True
                next
        for must_have in has:
            if must_have not in word:
                skip_word =True
                next
            else:
                for must_not_be_position in has[must_have]:
                    if word[must_not_be_position]==must_have:
                        skip_word=True
                        next
        if skip_word==False:
            candidate_words.append(word)

    print(f"Candidate words: {candidate_words}")