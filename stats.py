def num_words (text):
    lst = text.split()
    count = 0
    for word in lst:
        count += 1
    return count

def count_chars (text):
    d = {}
    for i in text:
        letter = i.lower()
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
    return d

def sort_on (dict):
    return dict["num"]

def report (d):
    lst =[]
    for i in d:
        d1 = {}
        d1["char"] = i
        d1["num"] = d[i]
        lst.append(d1)
    lst.sort(reverse=True, key=sort_on)
    return lst
