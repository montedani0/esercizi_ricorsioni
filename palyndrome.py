def palindrome(word):
    if len(word)<=1:
      return True
    else:
        return word[0] == word[-1] and palindrome(word[1:-1])


if __name__ == "__main__":
    print(palindrome('casa'))
    print(palindrome('civic'))