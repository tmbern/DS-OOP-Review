'''Player class to record stats for individual players
'''
import numpy as np

class Player:
    '''Dosctring TODO
    THIS IS NOT A VERY GENERALIZABLE MODEL IF YOU KNOW THINGS ABOUT FOOTBALL
    and that's okay
    '''
    def __init__(self, name=None, yards=120, touchdowns=5, safety=1,
                 interceptions=0, field_goals=3):
        self.name = name
        self.yards = yards
        self.touchdowns = touchdowns
        self.safety = safety
        self.interceptions = interceptions
        self.field_goals = field_goals

    def get_points(self):
        '''Gets points scored by the player from stats
        '''
        td_points = 6 * self.touchdowns
        safety_points = 2 * self.safety
        field_goal_points = 3 * self.field_goals

        total_points = td_points + safety_points + field_goal_points
        return total_points


class Quarterback(Player):
    '''Override certain parameters of the default Player class and add some
    functionality unique to quarterbacks
    '''
    def __init__(self, name=None, yards=130, touchdowns=5, completed_passes=20,
                 interceptions=4, safety=None, field_goals=None):
        super().__init__(name=name, yards=yards, touchdowns=touchdowns,
                         safety=safety, interceptions=interceptions)
        self.completed_passes = completed_passes

    def passing_score(self):
        '''This is a random formula... FYI
        '''
        score = self.completed_passes - (2 * self.interceptions)
        return score

# TODO - refine the default player stats and/or make a defensive player default
# with number of tackles, sacks, interceptions etc.

class DefensivePlayer(Player):
    '''Override certain parameters of default Player class and add 
    unique parameters to a defensive player
    '''
    def __init__(self, name=None, touchdowns=0, interceptions=0, safety=0, sacks=0,
                 tackles=0, fumble_recovery=0):
        super().__init__(name=name, touchdowns=touchdowns, interceptions=interceptions,
                         safety=safety)
        self.sacks = sacks
        self.tackles = tackles
        self.fumble_recovery = fumble_recovery

    def defensive_score(self):
        '''This is a random formula for a defensive players performance
        '''

        score = (self.sacks
                + (self.touchdowns * 6)
                + (self.fumble_recovery * 1.5)
                + (self.tackles )
                + (self.safety * 2)
        )
        return score


if __name__ == "__main__":

    offensive_player = Player(name='Trent', yards=100, touchdowns=2, safety=0,
                              interceptions=0, field_goals=0)
    print(offensive_player.name)
    print(offensive_player.get_points())



    quarterback = Quarterback(name='Trent', yards=300, touchdowns=3, completed_passes=22,
                interceptions=1, safety=0, field_goals=0)
    print(quarterback.name)            
    print(quarterback.passing_score())


    defensive_player = DefensivePlayer(name='Trent', touchdowns=1, interceptions=2, safety=1,
                                       fumble_recovery=1, sacks=10)
    print(defensive_player.name)
    print(defensive_player.defensive_score())
