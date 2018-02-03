#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
from operator import itemgetter

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # +++your code here+++
    f = open(filename, 'rU')
    file_text = f.read()
    f.close()
    t_year = re.findall(r'Popularity in (\d+)', file_text)
    # t = re.findall(r'Popularity in (\d+).<td>(\d+)</td><td>(\w+)</td><td>(\w+)', f.read(), re.DOTALL)
    t_names = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)', file_text)
    l_d = get_names(t_names)
    result = []
    result.extend(t_year)
    for name in l_d:
        result.append(name['name'] + ' ' + name['rank'])
    return '\n'.join(result)


def get_names(t):
    l_dict = []
    for each in t:
        d_male = {}
        d_female = {}
        d_male['rank'] = each[0]
        d_male['name'] = each[1]
        d_female['rank'] = each[0]
        d_female['name'] = each[2]
        l_dict.append(d_male)
        l_dict.append(d_female)
    # print l_dict
    # print sorted(l_dict, key=itemgetter('name'))
    return sorted(l_dict, key=itemgetter('name'))

def write_to_summary(file_name, text):
  f = open(file_name + '.summary', 'w')
  f.write(text)
  f.close()
  return


def main():
        # This command-line parsing code is provided.
        # Make a list of command line arguments, omitting the [0] element
        # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print 'usage: [--summaryfile] file [file ...]'
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    out = extract_names(args[0])
    if summary:
      write_to_summary(args[0], out)
    else:
      print out

if __name__ == '__main__':
    main()
