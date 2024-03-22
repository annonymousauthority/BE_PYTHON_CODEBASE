def unscramble_word(unscrambled_list, target_word):
    scrambled_word = ""
    letter_found = False
    for letter in target_word:
        for scrambled_letter in unscrambled_list:
            if letter.lower() == scrambled_letter.lower():
                scrambled_word += scrambled_letter
                letter_found = True
                break
        if letter_found != True:
            return "Target word doesn't exist in the unscrambled_list"
        letter_found = False
    return scrambled_word

print(unscramble_word(["e","g","h","u"], "Hue"))