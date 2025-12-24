book_name_list = ["The Great Gatsby", "To Kill a Mockingbird", "Harry Potter", "The Lord of the Rings"]
kwords = "the gret mocingbird"

book_name_list = [book_name.lower() for book_name in book_name_list]

# print(book_name_list)

def compare_trigrams(name, string):
    splitted_name = []
    splitted_string = []
    for i in range(len(name)-2):
        splitted_name.append(name[i:i+3])
    for i in range(len(string)-2):
        splitted_string.append(string[i:i+3])

    matches = 0
    for s_trigrama in splitted_string:
        for n_trigrama in splitted_name:
            if s_trigrama == n_trigrama:
                matches += 1

    # return (splitted_name, splitted_string, matches)
    return matches

def search_by_name(list_of_names, string):
    suitable_names = []
    for name in list_of_names:
        matches = compare_trigrams(name, string)
        if matches >= 4:
            suitable_names.append(name)

    return suitable_names


# print(compare_trigrams(book_name_list[2], kwords))
print(search_by_name(book_name_list, kwords))
