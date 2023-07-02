# Creates a alphabetised dictionary of data based on a certain category. This will be used to make the search more efficient
def alphabetise(category, dictionary):
    alphabetised_dict = {}
    # This function checks the values associated with a dictionary and adds them one by one (if a list) to the alphabetised dictionary.
    for key, value_dict in dictionary.items():
        if isinstance(value_dict[category], tuple):
            for item in list(value_dict[category]):
                if item[0] not in alphabetised_dict.keys():
                    alphabetised_dict[item[0]] = [item]
                else:
                    if item not in alphabetised_dict[item[0]]:
                        alphabetised_dict[item[0]].append(item)
        else:
            if value_dict[category][0] not in alphabetised_dict.keys():
                 alphabetised_dict[value_dict[category][0]] = [value_dict[category]]
            else:
                 if value_dict[category] not in alphabetised_dict[value_dict[category][0]]:
                    alphabetised_dict[value_dict[category][0]].append(value_dict[category])
    return alphabetised_dict