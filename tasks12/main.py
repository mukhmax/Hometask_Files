from pprint import pprint


def file_reader(file_name: str) -> dict:
    result = {}
    with open(file_name, encoding='utf-8') as recipes:
        heads = ['наименование', 'количество', 'единица']
        for line in recipes:
            dish_name = line.strip()
            result[dish_name] = []
            components_number = recipes.readline()
            for component in range(int(components_number)):
                component = recipes.readline().strip().split(' | ')
                component_dict = dict(zip(heads, component))
                result[dish_name].append(component_dict)
            recipes.readline()
    return result


def get_shop_list_by_dishes(*dishes, person_count):
    result_list = {}
    cook_book_lower = dict((k.lower(), v) for k, v in cook_book.items())
    for dish in dishes:
        if dish.lower() in cook_book_lower:
            for component in cook_book[dish]:
                if component['наименование'] not in result_list:
                    result_list[component['наименование']] = {}
                    result_list[component['наименование']]['единица'] = component['единица']
                    result_list[component['наименование']]['количество'] = int(component['количество']) * person_count
                else:
                    result_list[component['наименование']]['количество'] += int(component['количество']) * person_count
        else:
            print(f'В кулинарной книге нет блюда {dish}\n')
    return result_list


cook_book = file_reader('recipes.txt')
pprint(cook_book, sort_dicts=False)
print()
pprint(get_shop_list_by_dishes('Омлет', 'Фахитос', 'Уха', person_count=2), sort_dicts=False)
