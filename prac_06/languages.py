"""estimated time 7 min
started at 1:14 pm
finished at 1:24 pm
total time 10 min"""

from programming_language import ProgrammingLanguage
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
languages = [python, ruby, visual_basic]
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
