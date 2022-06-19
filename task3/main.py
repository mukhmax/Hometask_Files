def file_plus(*files):
    file_list = {}
    for file in files:
        with open(file, encoding='utf-8') as one_file:
            list_ = one_file.readlines()
            file_list[file] = list_
    sorted_file_list = {}
    sorted_files = sorted(file_list.values(), key=len)
    for file in sorted_files:
        for key_ in file_list:
            if file_list[key_] == file:
                sorted_file_list[key_] = file
    for file, text in sorted_file_list.items():
        with open('result.txt', 'a') as result:
            result.write(file+'\n')
            result.write(str(len(text))+'\n')
            for line in text:
                if '\n' in line:
                    result.write(line)
                else:
                    result.write(line+'\n')


file_plus('1.txt', '2.txt', '3.txt')
