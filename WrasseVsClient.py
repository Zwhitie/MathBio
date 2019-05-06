#simulation to simulate the wrasse cleaner relationship
#defecting gives greatest payoff
#cost of defecting is the probability of interation decreases
'''
wrasse payoffs
p1 = nutrients from parasites
p2 = nutrients from mucus from bite
p3 = wrasse eaten
client payoffs
p4 = parasite removal
p5 = nutrients from eating wrasse
p6 = tissue damage from wrasse bite

Strategic_matrix
                        Client
                Coop            Eat
        Clean    p1,p4          p3,p4+p5
Wrasse  Bite     p2,p6          p3,p5

'''
import random

#rand num has min and max inclusive
def get_rand_num(min,max):
    rand_num = random.randint(min,max)
    return rand_num

num_rounds = 10
#pop. wrasse
P_w = 50
#pop. clients
P_c = 80

p1 = 5
#p1 = nutrients from parasites
p2 = 15
#p2 = nutrients from mucus from bite
p3 = -10
#p3 = wrasse eaten
p4 = 5
#p4 = parasite removal
p5 = 10
#p5 = nutrients from eating wrasse
p6 = -5
#p6 = tissue damage from wrasse bite

#after defecting the client will interact with the wrasse again after this many rounds
#forgiveness_rate = 10

wrasse_score = 0
client_score = 0

mutual_coop_count = 0
wrasse_bite_count = 0
wrasse_clean_then_eaten_count = 0
wrasse_eaten_count = 0

for i in range(num_rounds):
    wrasse_action = get_rand_num(1,6)
    client_action = get_rand_num(1,6)
    if wrasse_action == 6:
        wrasse_bite = True
    elif wrasse_action != 6:
        wrasse_bite = False
    if client_action >= 5:
        client_eat = True
    elif client_action < 5:
        client_eat = False
    if not wrasse_bite and not client_eat:
        wrasse_score += p1
        client_score += p4
        mutual_coop_count += 1
    elif wrasse_bite and not client_eat:
        wrasse_score += p2
        client_score += p6
        wrasse_bite_count += 1
    elif not wrasse_bite and client_eat:
        wrasse_score += p3
        client_score += (p4 + p5)
        wrasse_clean_then_eaten_count += 1
    elif wrasse_bite and client_eat:
        wrasse_score += p3
        client_score += p5
        wrasse_eaten_count += 1

print("After " + str(num_rounds) + " rounds of the simulation")
print("Wrasse score: " + str(wrasse_score))
print("Client score: " + str(client_score))
print("\nGame summery")
print("Number of times of mutual cooporation: " + str(mutual_coop_count))
print("Number of times wrasse bit the client: " + str(wrasse_bite_count))
print("Number of times wrasse cleaning a client and then eaten: " + str(wrasse_clean_then_eaten_count))
print("Number of times wrasse eaten by client: " + str(wrasse_eaten_count))
