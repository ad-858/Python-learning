characters=["krillin","goku","picollo","gohann"]
a=list(enumerate(characters))
print(a)
for i,j in enumerate(characters):
    print(i,j)
characters=["krillin","goku","picollo","gohann",
"krillin","goku","picollo","gohann",
"krillin","goku","picollo","gohann",
"krillin","goku","picollo","gohann"
]    
character_map={ character:[] for character in characters}
print(character_map)
for i,j in enumerate(characters):
    character_map[j].append(i)
print(character_map)    