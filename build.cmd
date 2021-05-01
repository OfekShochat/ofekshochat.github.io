@echo off
c:\Users\o\AppData\Local\Pandoc\pandoc.exe -c mvp.css -s test.md -t html -o out.html --metadata title="%1"