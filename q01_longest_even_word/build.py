def q01_longest_even_word(sentence):
    even_list = [x for x in sentence.split() if len(x) % 2 == 0]
    output = max(even_list, key=len) if even_list else 0
    return output
sentence='mya namea ias bhavesh'
q01_longest_even_word(sentence)


