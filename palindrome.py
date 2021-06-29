# #palindrome
print("PALINDROME CHECK")
print("Welcome, let's check if your word is a palindrome")
is_entry = input("input any word: ")
is_entlist = list(is_entry)
is_entcopy = is_entlist.copy()
is_entlist.reverse()

if is_entlist == is_entcopy:
      print("your entry is a palindrome!\n\n")
else: print("try again!, this isn't a palindrome\n\n")