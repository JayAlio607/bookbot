def get_num_unique_char(text_to_catalog):
	char_dict = {}
	for c in text_to_catalog:
		key = c.lower()
		if key in char_dict:
			char_dict[key] += 1
		else:
			char_dict[key] = 1
	return char_dict


def get_num_words(text_to_count):
        word_count = text_to_count.split()
        return len(word_count)

def sort_on(items):
	return items["num"]

def sort_unique_chars(unique_chars):
	list_of_chars = []
	for e in unique_chars:
		list_of_chars.append({"char": e, "num": unique_chars[e]})
	list_of_chars.sort(reverse=True, key=sort_on)
	return list_of_chars
