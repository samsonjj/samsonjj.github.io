#!/usr/bin/env python3
import sys
import os
from datetime import datetime

def main():
  if len(sys.argv) == 0:
    print("No arguments supplied")
    exit(1)

  print(sys.argv)

  if len(sys.argv) == 2:
    words = sys.argv[1].split('\w')
  else:
    words = sys.argv[1:]
  
  print('sys.argv[1:]', sys.argv[1:])
  print('words', words)

  title = ' '.join(words)
  fileTitle = '-'.join([x.lower() for x in words])

  print('title', title)

  pwd = os.path.dirname(os.path.abspath(__file__))
  dateString = datetime.now().strftime("%Y-%m-%d")

  print('dateString', dateString)
  with open(os.path.join(pwd, '_posts', dateString + '-' + fileTitle + '.markdown'), 'w+') as f:
    f.write('''---
layout: post
title: {}
---
            '''.format(title))

if __name__ == "__main__":
  main()