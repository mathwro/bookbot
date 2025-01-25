import os

def remove_nonalpha(content):
  cleaned_contents = ""
  for i in content:
    if i.isalnum():
      cleaned_contents += i
  return cleaned_contents

def char_counter(contents):
  lower_contents = contents.lower().replace("\n", "").replace(" ", "")
      
  counter_dict = {}
  for i in remove_nonalpha(lower_contents):
    if not i in counter_dict:
      counter_dict[i] = 1
    else:
      counter_dict[i] += 1

  return(dict(sorted(counter_dict.items(), key=lambda item: item[1], reverse=True)))

def word_counter(contents):
  return(len(contents.split()))

def main():
  # Open file
  book_name = "frankenstein.txt"
  script_dir = os.path.dirname(__file__)
  with open(script_dir + "/books/" + book_name) as f:
    file_contents = f.read()

  # Get data
  chars = char_counter(file_contents)
  words = word_counter(file_contents)

  # Print report
  print(f"--- Begin report of books/${book_name} ---")
  print(f"{words} words found in the document")
  print("")
  for i in chars:
    print(f"The '{i}' character was found {chars[i]} times")

main()