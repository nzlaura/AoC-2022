elf_with_most_calories = 0
elf = 0

elf_calorie_list = []


with open('input.txt') as f:
    content = f.readlines()
lines = [x.strip() for x in content]

for line in lines:
    if line == '':
        elf_with_most_calories = max(elf, elf_with_most_calories)
        elf_calorie_list.append(int(elf))
        elf_calorie_list.sort(reverse=True)
        elf = 0

    else:
        elf = int(elf) + int(line)
print(elf_with_most_calories)
print(sum(elf_calorie_list[:3]))
