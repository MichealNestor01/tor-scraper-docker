# sanatiser.py
# includes the code to sanatise the page title

def sanatiseTitle(title):
    for index, char in enumerate(title):
        # check that each character is valid for use as a filename
        if not (char.isalpha() or char.isdigit() or char.isspace()):
            return title[0:index]
    # title does not need sanatising
    return title