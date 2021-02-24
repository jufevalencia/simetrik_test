import os
from collections import defaultdict





def create_dict_of_login(Log_login):
    """
    
    this function is in charge of creating a dictionary with the characters and their position within the groups of three, saving it in list dictionaries.    

    """
    Dict_login = defaultdict(list)
    for login in Log_login:
        for i, n in enumerate(login):
            Dict_login[n].append(i)
            
    return Dict_login


def Find_position(Dict_logins):
    
    """
    
    this function is in charge of calculating the average position of each character by dividing the sum of the positions of the character by the number of times the character has appeared.    

    """
    positions = {}
    for k,v in list(Dict_logins.items()):
        positions[k] = float(sum(v))/float(len(v))
    
    return positions

def fin_the_password(positions):
    
    """
    
     this function is in charge of sorting the dictionary by value, so that the characters with a lower average position appear before those with a higher average position.
     Finally, we concatenate the sorted characters and return the result.

    """
    password = [k for k,v in sorted(list(positions.items()), key=lambda password: password[1])]
    passw =''.join(str(x) for x in password)
    return passw



if __name__ == "__main__":
    Log_Login = [line.strip() for line in open(os.path.join(os.path.dirname(__file__), 'keylog.txt')).readlines()]
    Dict_login = create_dict_of_login(Log_Login)
    Positions = Find_position(Dict_login)
    password = fin_the_password(Positions)
    print(password)
