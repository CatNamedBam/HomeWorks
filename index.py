from dataset import users, countries



users_wrong_password = []


for user in users:
    if user['password'].isdigit():
        users_wrong_password.append({'name': user['name'], 'mail': user['mail']})


girls_drivers = []

for user in users:
    friends = user.get('friends', [])
    for friend in friends:
        if friend['sex'] == 'F' and friend.get('cars'):
            girls_drivers.append(friend['name'])



best_occupation = []
max_salary = 0 

for user in users:
    friends = user.get('friends', [])
    for friend in friends:
        if friend['job']['salary'] > max_salary:
            max_salary = friend['job']['salary']
            best_occupation = friend['job'].copy()

            
vip_user = ''
max_friends_total_salary = 0

for user in users:
    friends_total_salary = 0
    friends = user.get('friends', [])
    for friend in friends:
        friends_total_salary += friend['job']['salary']
        if friends_total_salary > max_friends_total_salary:
            max_friends_total_salary = friends_total_salary
            vip_user = user['name']


friends_with_cars = 0
total_flights = 0
for user in users:
    friends = user.get('friends', [])
    for friend in friends:
        if friend.get('cars'):
            friends_with_cars += 1
            total_flights += len(friend.get('flights', []))
avg_flights = round(total_flights / friends_with_cars, 5)
print(avg_flights)



i = 0
while i < len(users):
    need_remove = False
    friends = users[i].get('friends', [])
    for friend in friends:
        flights = friend.get('flights', [])
        for flight in flights:
            if flight['country'] in countries:
                need_remove = True
                break
        if need_remove:
            break
    if need_remove:
        del users[i]
    else:
        i += 1
        