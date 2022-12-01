elf_with_most_calories = 0
elf = 0

with open('input.txt') as f:
    content = f.readlines()
# Remove whitespace characters like '\n' at the end of each line
lines = [x.strip() for x in content]

for line in lines:
    if line == '':
        elf_with_most_calories = max(elf, elf_with_most_calories)
        elf = 0
    else:
        elf = int(elf) + int(line)
print(elf_with_most_calories)
