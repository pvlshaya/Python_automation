import re, pyperclip

phoneRegex = re.compile(r'''(
((\d\d\d)|(\(\d\d\d\)))?    #area code
(\s|-)    #first seperator
\d\d\d    #first 3 digits
-    #seperator
\d\d\d\d    #last 4 digits
(((ext(\.)?\s)|x)    #extensions word part
(\d{2,5}))?    #extensions number part
)''', re.VERBOSE)

emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+    #name part
@    #@ symbol
[a-zA-Z0-9_.+]+    #domain name part
                        ''', re.VERBOSE)

text = pyperclip.paste()

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNubmer in extractedPhone:
    allPhoneNumbers.append(phoneNubmer[0])

resoults = '\n'.join(allPhoneNumbers) + '\n' +'\n'.join(extractedEmail)
pyperclip.copy(resoults)