import json





def myRange(start,end,step):
    """ 
      this function is to create our own custom ranges, to make match counts.
    
    """
    i = start
    while i < end:
        yield i
        i += step
    yield end

def Find_number_matches(Player_1, Player_2, Player_3):
     """ 
      this function is to find the number of matches that were played, adding the matches of each player and dividing by 2 which is the number of players that compose a match 
    
     """
     Total = Player_1["games_played"] +Player_2["games_played"]+Player_3["games_played"]
     Total_Matches = Total/2
     return int(Total_Matches)


def Find_minimun_number_matches_by_any_player(Number_Matches):
    """ 
      this function is the one that finds the minimum number of matches played by a participant who loses all his matches. 
    
     """
    Label = ""
    count_odd = 0 
    count_even = 0
    for i in myRange(1, Number_Matches,2):
        
        if i % 2 ==1:
            count_even = count_even+1
    for i in myRange(2, Number_Matches,2):
        if i % 2 ==0:
            count_odd = count_odd+1
        
    Minimun_number_matches = min(count_odd,count_even)
    if Minimun_number_matches == count_odd:
        Label = "Odd"        
    if Minimun_number_matches == count_even:
        Label = "Even"    
    return Minimun_number_matches, Label
    

def Find_Player_With_minimun_matches(Minimun_number_matches,Player_1, Player_2, Player_3):
    """ 
      this function is the one that creates the json file, with the name, the number of matches played and the matches lost by the player who lost the second match. 
    
    """
    Player_1_Bool = Minimun_number_matches in Player_1.values()
    Player_2_Bool = Minimun_number_matches in Player_2.values()
    Player_3_Bool = Minimun_number_matches in Player_3.values()
    
    if (Player_1_Bool == True):
        return Player_1
    if (Player_2_Bool == True):
        return Player_2
    if (Player_3_Bool == True):
        return Player_3


def Create_json_Response(Player_play_second_Match , Label, Number_Matches):
    """ 
        this function is in charge of comparing the minimum number of matches with the matches played by our participants to look for the coincidence and find the player who played the second match.      
    """
    list_matches = []
    if Label =="Odd":
        for i in myRange(2, Number_Matches,2):
            if i % 2 ==0:
                list_matches.append(i)
    elif Label =="Even":
        for i in myRange(1, Number_Matches,2):
            if i % 2 ==1:
                list_matches.append(i)
    
    Player_play_second_Match["Lista_Partidos_Perdidos"] = list_matches
    Player_play_second_Match["El jugador que perdio el segundo partido es: "] = Player_play_second_Match["Name"]
    with open("Response.json", "w") as outfile:  
        json.dump(Player_play_second_Match, outfile) 
        
    
    

         
     



if __name__ == "__main__":
    
    Ana = {"games_played":17, "Name":"Ana"}
    Jose = {"games_played":15, "Name":"Jose"}
    Juan = {"games_played":10, "Name":"Juan"}
    Total_matches = Find_number_matches(Ana, Jose, Juan)
    Minimun_number_matches, Label = Find_minimun_number_matches_by_any_player(Total_matches)
    Player_play_second_Match = Find_Player_With_minimun_matches(Minimun_number_matches,Ana, Jose, Juan)
    Create_json_Response(Player_play_second_Match,Label,Total_matches)
    
    with open('response.json') as json_file:
        data = json.load(json_file)
    
    print(data)