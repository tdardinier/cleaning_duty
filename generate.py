import random as rd
from tabulate import tabulate
from datetime import datetime  
from datetime import timedelta  

n_weeks = 20
names = ["Anne-Sophie", "Li", "Claudia", "Jacob", "Mike", "Kai", "Haishan", "Charlotte", "Michael", "Thibault", "Daniel"]
bathrooms = [[0, 1, 2, 10], [3, 8, 9], [4, 5, 6, 7]]
tasks = ["Toilets", "Kitchen", "Trash (PET, paper)", "Trash (glass, metal)", "Floor"]
first_day = (13, 1, 2020)

# rd.seed(42)

n_other_tasks = len(tasks)
n_bathrooms = len(bathrooms)
n_tasks = n_other_tasks + n_bathrooms
n_persons = len(names)

for i in range(n_bathrooms):
    rd.shuffle(bathrooms[i])

schedule = []

def count():
    # count[person][task] = number of this task, this person
    count = [[0 for _ in range(n_tasks)] for _ in names]
    for week in schedule:
        for i in range(n_tasks):
            count[week[i]][i] += 1
    return count

def get_tasks_mini(person, counter):
    c = counter[person][3:] # Not counting bathrooms
    m = min(c)
    M = max(c)
    assert M - m <= 1 # Invariant
    s = set()
    for i, n in enumerate(c):
        if n == m:
            s.add(i + n_bathrooms)
    return s

def total_number_of_jobs(person, counter):
    return sum(counter[person])

def update(i):
    global schedule
    # print("Update", i)
    week = [-1 for _ in range(n_tasks)]
    persons = set(range(n_persons))
    for (ib, b) in enumerate(bathrooms):
        ind = i % len(b)
        p = b[ind]
        week[ib] = p
        persons.remove(p)
    persons = list(persons)
    rd.shuffle(persons)
    c = count()
    persons.sort(key = lambda p: sum(c[p])) # Priority to people with fewer jobs
    avail_tasks = set(range(n_bathrooms, n_tasks))
    for p in persons[:len(avail_tasks)]:
        s = get_tasks_mini(p, c).intersection(avail_tasks)
        if len(s) == 0:
            # print("Failure", i)
            return False
        task = rd.sample(s, 1)[0]
        avail_tasks.remove(task)
        week[task] = p
    schedule.append(week)
    if i + 1 < n_weeks:
        r = update(i + 1)
        while not r:
            schedule = schedule[:i]
            r = update(i)
    return True

update(0)

weeks = []

def format_date(d):
    def f(x):
        return ("{:02d}".format(x))
    return f(d.day) + "/" + f(d.month)

d = datetime.now()
d.replace(first_day[2], first_day[1], first_day[0])
for i in range(n_weeks):
    d2 = d + timedelta(days=6)
    weeks.append(format_date(d) + " - " + format_date(d2))
    d = d + timedelta(days=7)
    i += 1

pretty_schedule = [[weeks[n]] + [names[i] for i in week] for (n, week) in enumerate(schedule)]

print(tabulate(pretty_schedule, headers=["Weeks"] + ["Bathroom " + str(i + 1) for i in range(n_bathrooms)] + tasks, tablefmt="html"))
