import argparse
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
  script_dir = os.path.dirname(__file__)
  parser = argparse.ArgumentParser(description='Process a text file.')
  parser.add_argument('filename', nargs='?', default=os.path.join(script_dir, 'books/frankenstein.txt'), type=str, help='The name of the file to process')
  args = parser.parse_args()

  if not os.path.isfile(args.filename):
    print(f"File {args.filename} does not exist.")
    return

  with open(os.path.join(script_dir, args.filename)) as f:
    file_contents = f.read()

  # Get data
  chars = char_counter(file_contents)
  words = word_counter(file_contents)

  # Print report
  print(f"--- Begin report of books/${args.filename} ---")
  print(f"{words} words found in the document")
  print("")
  for i in chars:
    print(f"The '{i}' character was found {chars[i]} times")

main()