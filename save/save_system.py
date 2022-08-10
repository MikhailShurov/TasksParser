def save(index, content):   # index of line to save, value to save

    file = open('save/saved_links.py', 'r')
    old_data = file.readlines()

    # new_line = ''.join(line[:до '=' + 2] + текущее значение)
    new_line = ''.join(old_data[index-1][:old_data[index-1].find('=')+2] + str(content))

    old_data[index-1] = str(new_line + '\n')

    with open('save/saved_links.py', 'w') as file:
        file.writelines(old_data)

    return 'Successfully saved'
