from sys import argv
from glob import glob
import os

outputDir = "./docs/{}"
styleName = argv[1]
ARGS =  "c:\\Users\\o\\AppData\\Local\\Pandoc\\pandoc.exe -c ./docs/css/{}.css -s {} -t html -o {}"

def makecmd(f):
  return ARGS.format(styleName, f, outputDir.format(f[f.find("\\" if os.name == "nt" else "/"):f.find(".")+1] + "html"))

files = glob("writings/*.md")
files += glob("writings/**/*.md")
for f in files:
  print(f)
  os.system(makecmd(f))