@echo off
COPY C:\Python34\diplom\input.txt C:\Users\hp9\IdeaProjects\LinguisticAnnotationSystem\src\Parsers\mystem-input.txt
COPY C:\Python34\diplom\input.txt C:\Users\hp9\IdeaProjects\LinguisticAnnotationSystem\src\Parsers\text\mystem-input.txt
COPY C:\Python34\diplom\input.txt C:\Users\hp9\IdeaProjects\LinguisticAnnotationSystem\src\Parsers\text\mystem-output.txt
C:\Users\hp9\IdeaProjects\LinguisticAnnotationSystem\src\Parsers\Mystem.exe -ni --format text C:\Users\hp9\IdeaProjects\LinguisticAnnotationSystem\src\Parsers\text\mystem-input.txt C:\Python34\diplom\mout.txt -e cp1251
COPY C:\Users\hp9\IdeaProjects\LinguisticAnnotationSystem\src\Parsers\text\output.gra C:\Python34\diplom\gout.gra
