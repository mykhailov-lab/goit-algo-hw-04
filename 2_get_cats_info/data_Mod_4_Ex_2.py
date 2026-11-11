def get_cats_info(path:str) -> list[dict]:
    new_cat_list= []
    try:
        with open(path, 'r', encoding='utf-8') as cats_list:
            #return file.readlines()
            for i in cats_list:
                clean_lines = i.strip()
                if not clean_lines:
                    continue
                id, name, age = clean_lines.split(",")
                cat_dict = {"id": id, "name": name, "age": age}
                new_cat_list.append(cat_dict)
    except FileNotFoundError:
        return []
    if not cats_list:
        return []
    return (new_cat_list)