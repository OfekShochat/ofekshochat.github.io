from sys import argv
from glob import glob
import os
import subprocess

FNULL = open(os.devnull, 'w')

outputDir = "./static/{}"
styleName = argv[1]
PANDOC_PATH = "C:\\Users\\o\\AppData\\Roaming\\npm\\node_modules\\pandoc-bin\\vendor\\pandoc.exe"

ARGS =  PANDOC_PATH + " -c css/{}.css -s {} -t html -o {}"

for i in glob("static/*.html"):
  os.remove(i)

def makecmd(f):
  return ARGS.format(styleName, f, outputDir.format(f[f.find("\\" if os.name == "nt" else "/")+1:f.find(".")+1] + "html"))

files = glob("source/*.md")
files += glob("source/**/*.md")
for f in files:
  cmd = makecmd(f)
  print(f)
  print(" - {}".format(cmd))
  subprocess.check_call(cmd, stdout=FNULL, stderr=FNULL, shell=True)