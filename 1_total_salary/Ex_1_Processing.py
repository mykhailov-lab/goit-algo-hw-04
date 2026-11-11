def total_salary (path : str) -> tuple[float, float] :
    if not path:
        return (0,0)
    total_sum = 0
    number_workers = 0
    try:
        with open (path, 'r', encoding='utf-8') as file :
            #return file.readlines()
            for i in file:
                line_file = i.strip()
                if not line_file :
                    continue
                name, salary_str = line_file. split(',')
                total_sum = float(salary_str) + total_sum
                number_workers = number_workers + 1
        if number_workers == 0:
            return (0,0)
        average_salary = total_sum / number_workers
        return (total_sum, average_salary)
    except FileNotFoundError:
            return 0,0