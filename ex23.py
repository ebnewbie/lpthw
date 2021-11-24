import sys
script, input_encoding, error = sys.argv
def main(language_file, encoding, errors):
6 line = language_file.readline()
7
8 if line:
9 print_line(line, encoding, errors)
10 return main(language_file, encoding, errors)
11
12
13 def print_line(line, encoding, errors):
14 next_lang = line.strip()
15 raw_bytes = next_lang.encode(encoding, errors=errors)
16 cooked_string = raw_bytes.decode(encoding, errors=errors)
17
18 print(raw_bytes, "<===>", cooked_string)
19
20
21 languages = open("languages.txt", encoding="utf-8")
22
23 main(languages, input_encoding, error)
