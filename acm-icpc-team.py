def team(all_indivs, number_of):
    
    compare = [int(all_indivs[a],2) | int(all_indivs[b],2) for a in range(number_of - 1) for b in range(a + 1, number_of)]
    maximum = max(bin(x).count('1') for x in compare)
    print maximum
    
    count =0
    for y in compare:
        if bin(y).count('1') == maximum:
            count += 1
    print count

group_size, subjects = [int(i) for i in raw_input().strip().split()]

persons = []
for _ in range(group_size):
    persons.append(raw_input().strip())

team(persons,group_size)
