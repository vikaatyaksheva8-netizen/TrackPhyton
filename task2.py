def find_common_participants(group1, group2, separator=","):
    group1 = group1.split(separator)
    group2 = group2.split(separator)
    group = set(group1).intersection(set(group2))
    return sorted(group)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

find_common_participants(participants_first_group, participants_second_group, "|")
