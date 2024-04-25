# 
# RegEx (Regular Expressions) by Rutger Alexander Munoz.
#
#
#
"""

    Copyright: Wednesday 24/April/2024
    By: Rutger Alexander Munoz
    
    Licensed under the MIT License.

    
    Please check the " README.md " and the " LICENSE.txt " Files for more information.

"""
# 
#   These are My Own RegEx's (Regular Expressions).
# Their function is:
# To validate: Any kind of Emails, Usernames with many characters and with different languages, and Passwords with many characters and languages. 
# These RegEx's are advanced, then they cover many cases.
# Is a Library, use it as You want.
#
#
#
#   What is "RegEx"?
# Is a special code used to define a pattern for searching text. It's like a recipe that tells the computer what kind of text to find.
# You can use RegEx to:
# Find specific words or phrases within a large chunk of text
# Extract particular pieces of information, like dates or email addresses
# Check if a text string follows a certain format, like a phone number
# Replace text that matches a pattern with something else
#
#
#
#
# Email RegEx
# import re
"""
    What this Code does?:
    1) String start: " ^ " : Indicates that the match must occur at the beginning of the string.
    2) Body of e-mail address: " [a-zA-Z0-9 .  - _ + ?  # ! & ( %) $]+ " : This pattern matches any combination of upper and lower case letters, digits, and some common
    special characters in email addresses such as dots, hyphens, underscores, plus signs, question marks, number signs, exclamation marks, ampersand signs,
    percentages, dollars.
    3) Symbol " @ " : " @{1} " : This indicates that there must be exactly one arroba symbol in the email address.
    4) Domain: " [a-zA-Z0-9]+ " : This pattern matches any combination of upper and lower case letters, and digits for the email address domain.
    5) Point: " . " : Matches a literal point, which separates the top-level domain (TLD (Top-Level Domain)) from the rest of the domain.
    6) TLD (Top-Level Domain) : " [a-zA-Z]{2,3} " : This pattern matches two or three letters of the alphabet for the top-level domain (TLD).
    7) String End: " $ " : Indicates that the match must end at the end of the string.
"""
# 
# emailRegEx = re.compile("^[a-zA-Z0-9\.\-\_\+\?\#\!\&\(\%\)\$]+@{1}[a-zA-Z0-9]+\.{1}[a-zA-Z]{2,3}$")
#
#  Testing the Code with some random Emails
# print(emailRegEx.search("Myemail#10?@gmail.com"))
# print(emailRegEx.search("Email123%9@gmail.net"))
# print(emailRegEx.search("rutger9&9+23@gmail.com"))
# print(emailRegEx.search("email.games+$@gmail.games"))


# Exercise 2 :
#
# Username RegEx
# Importing the RegEx Library
# import re
# 
"""
    For Korean: \uAC00-\uD7A3
    For Japanese (Hiragana): \u3040-\u309F
    For Japanese (Katakana): \u30A0-\u30FF
    For Chinese (Simplified & Kanjis (Chinese and Japanese Kanjis)): \u4E00-\u9FFF
    For Chinese (Traditional): \u3400-\u4DBF
    For Russian: \u0400-\u04FF  
    
    The " [\s\S]* " Code: Is a common way to match any sequence of characters, including line breaks and blanks.
    [\s\S]: This character group matches any character, either a white space (\s) or any character other than a white space (\S). Together, these two patterns match
    any character, regardless of whether it is a blank or not.
    The " * " Character: The asterisk indicates that the group [ s S] may appear zero or more times. In other words, this part of the regular expression can match any, one
    or multiple repetitions of any character.
    English & Spanish (Spanish with and without Accents): [a-zA-Z], áéíóúÁÉÍÓÚ. 
    
    What this Code does?:
    1) String start:  " ^ " : Indicates that the match must occur at the beginning of the string.
    2) First character allowed: " [a-zA-Z0-9áíííúÁÉÉÉÉÓ\.\-\&\%\#\!\@\*\?\$\~\`\(\{\)\=\}\_\¡
    \uAC00-\uD7A3\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FF\u3400-\u4DBF\u0400-\u04FF] " : Defines the first character of the allowed string. It includes
    upper and lower case letters, digits and a variety of special characters, as well as some specific characters from Spanish, Korean, Japanese, Chinese and Russian.
    3) String Body: " [\s\S]*+ " : This pattern matches any number of characters, including line breaks and blanks, after the first valid character. " \s " matches any blank
    character and " \S " matches any character other than a blank. The " *+ " indicates that this match is "lazy" (lazy), which means it matches as few characters as possible.
    4) String End: " $ " : Indicates that the match must end at the end of the string.
"""
#
# usernameRegEx = re.compile(r"^[a-zA-Z0-9áéíóúÁÉÍÓÚ\.\-\&\%\#\!\@\*\?\¿\$\~\`\(\{\)\=\}\_\¡\uAC00-\uD7A3\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\u3400-\u4DBF\u0400-\u04FF][\s\S]*+$")
#
# Testing the Code without combinations
# print(usernameRegEx.search("뎌ㅏㅊ게")) # Korean
# print(usernameRegEx.search("호ㅓㅕㅑㅐㅣㅠ츄")) # Korean
# print(usernameRegEx.search("きかまもたてつ")) # Japanese
# print(usernameRegEx.search("んやゆみきさぃむ")) # Japanese
# print(usernameRegEx.search("日田人弓竹金")) # Traditional Chinese
# print(usernameRegEx.search("矜襒木木月")) # Traditional Chinese
# print(usernameRegEx.search("表火十山金")) # Simplified Chinese
# print(usernameRegEx.search("品尼婼")) # Simplified Chinese
# print(usernameRegEx.search("фиера")) # Russian
# print(usernameRegEx.search("Вселенная")) # Russian
# print(usernameRegEx.search("Acción")) # Spanish with Accents
# print(usernameRegEx.search("Útil")) # Spanish with Accents
# print(usernameRegEx.search("Mejorar")) # Spanish without accents
# print(usernameRegEx.search("Avanzar")) # Spanish without accents
# print(usernameRegEx.search("Progress")) # English
# print(usernameRegEx.search("Strive")) # English
#
# Testing the Code with combinations with: Numbers, Special Characters, and itself Language
# print(usernameRegEx.search("뎌ㅏㅊ게#15")) # Korean
# print(usernameRegEx.search("호ㅓㅕㅑㅐㅣㅠ츄-1")) # Korean
# print(usernameRegEx.search("きかまもたてつ&ひんやそほ")) # Japanese
# print(usernameRegEx.search("んやゆみきさぃむ%5")) # Japanese
# print(usernameRegEx.search("日田人弓竹金.76")) # Traditional Chinese
# print(usernameRegEx.search("矜襒木木月*9")) # Traditional Chinese
# print(usernameRegEx.search("表火十山金@45.?")) # Simplified Chinese
# print(usernameRegEx.search("品尼婼56-7")) # Simplified Chinese
# print(usernameRegEx.search("фиера(простая)")) # Russian
# print(usernameRegEx.search("Вселенная=100")) # Russian
# print(usernameRegEx.search("Acción+Decisión=Logro")) # Spanish with Accents
# print(usernameRegEx.search("Útil&Eficaz")) # Spanish with Accents
# print(usernameRegEx.search("Mejorar100%")) # Spanish without accents
# print(usernameRegEx.search("Avanzar+Esfuerzo=Felicidad")) # Spanish without accents
# print(usernameRegEx.search("Progress*2")) # English
# print(usernameRegEx.search("Strive=Happiness")) # English
#
# Testing the Code with combinations of Languages
# print(usernameRegEx.search("뎌ㅏㅊ게+Sílaba")) # Korean and Spanish with accents
# print(usernameRegEx.search("호ㅓㅕㅑㅐㅣㅠ츄-为写贤")) # Korean and Simplified Chinese
# print(usernameRegEx.search("きかまもたてつ*молеяро")) # Japanese and Russian
# print(usernameRegEx.search("んやゆみきさぃむ$트롤리")) # Japanese and Korean
# print(usernameRegEx.search("日田人弓竹金_へしんやさ")) # Traditional Chinese and Japanese
# print(usernameRegEx.search("矜襒木木月*Trotar")) # Traditional Chinese and Spanish without accents
# print(usernameRegEx.search("表火十山金#$щлобяц")) # Simplified Chinese and Russian
# print(usernameRegEx.search("品尼婼!Hanger")) # Simplified Chinese and English (British)
# print(usernameRegEx.search("фиера-Camino")) # Russian and Spanish without accents
# print(usernameRegEx.search("Вселенная,Trees")) # Russian and English (British)
# print(usernameRegEx.search("Acción=ㅊ레듀ㅕ")) # Spanish with Accents and Korean
# print(usernameRegEx.search("Útil(ふまわはためけ)")) # Spanish with Accents and Japanese
# print(usernameRegEx.search("Mejorar*様必盃")) # Spanish without accents and Chinese
# print(usernameRegEx.search("Avanzar~かそたひ")) # Spanish without accents and Japanese
# print(usernameRegEx.search("Progress(Прогресс)")) # English (British) and Russian
# print(usernameRegEx.search("Strive+海軍耄迎")) # English (British) and Chinese



# Exercise 3 :
#
# Userpassword RegEx
# Importing the RegEx Library
# import re
#
"""
    For Korean: \uAC00-\uD7A3
    For Japanese (Hiragana): \u3040-\u309F
    For Japanese (Katakana): \u30A0-\u30FF
    For Chinese (Simplified & Kanjis (Chinese and Japanese Kanjis)): \u4E00-\u9FFF
    For Chinese (Traditional): \u3400-\u4DBF
    For Russian: \u0400-\u04FF  
    What this Code does?:
    1) String start: " ^ " : Indicates that the match must occur at the beginning of the string.
    2) First character allowed: " [a-zA-Z0-9áííííúÁÉÉÉÉÉ\-\!\@\#\$\%\&\*\(\)\/\ _\=\+\¡\?\~\[\]\{\}\'\"\,\.\¡
    \uAC00-\uD7A3\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FF\u3400-\u4DBF\u0400-\u04FF] " : Defines the first character of the allowed string. It includes upper and
    lower case letters, digits and a variety of special characters, as well as some specific characters from Spanish, Korean, Japanese, Chinese and Russian, and the
    exclamation mark.
    3) String Body: " [\s\S]*+ " : This pattern matches any number of characters, including line breaks and blanks, after the first valid character. " \s " matches any blank
    character and  \S " matches any character other than a blank. The " *+ " indicates that this match is "lazy" (lazy), which means it matches as few characters as possible.
    4) String End: " $ " : Indicates that the match must end at the end of the string.
"""
#
# userpasswordRegEx = re.compile(r"^[a-zA-Z0-9áéíóúÁÉÍÓÚ\-\!\@\#\$\%\^\&\*\(\)\/\_\=\+\¿\?\`\~\[\]\{\}\'\"\,\.\¡\uAC00-\uD7A3\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\u3400-\u4DBF\u0400-\u04FF][\s\S]*+$")
#
# Testing the Code with some random Passwords
# print(userpasswordRegEx.search("AguaconLimón1459")) # Password 1
# print(userpasswordRegEx.search("Пароль_для_пользователя_1_パスワード")) # Password 2
# print(userpasswordRegEx.search("안녕하세&32^要%^素")) # Password 3
# print(userpasswordRegEx.search("¡Hól@Mund0¿Cóm0_3st4s?_HELLO_WORLD")) # Password 4
# print(userpasswordRegEx.search("T3$tiNg_¡nT3r-c4l4d0")) # Password 5