import importlib
import random
from . import participant as part
import copy

class my_own_player(part.Participant):
    def __init__(self):
        super().__init__('team07', '07')


    # ====================================================================== for initializing your player every round
    def initialize_player(self, string):
        self.initialize_params()
    # ====================================================================== for initializing your player every round


    # ================================================================================= for marble game
    def bet_marbles_strategy(self, playground_marbles):
        my_current_marbles = playground_marbles.get_num_of_my_marbles(self)
        return 1

    def declare_statement_strategy(self, playground_marbles):
        num = playground_marbles._marbles_in_hand
        answer = bool(num % 2)
        return self.set_statement(answer)
    # ================================================================================= for marble game


    # ================================================================================= for glass_stepping_stones game
    def step_toward_goal_strategy(self, playground_glasses):
        from __main__ import stage_map as map_a
        return map_a.steps[self.position]

        #if self.position == 0:
        #    self.temp_list = copy.deepcopy(playground_glasses._players_steps)  # 상대방것도 복사
        #length = len(self.temp_list)
        #data = 20 - length

        #if self.previous_player != 'None' and self.temp_list != []:
        #    if self.position < length - 1:  # 카피 한 것보다 앞에 있으면
        #        print(self.temp_list)
        #        print('chk1')
        #        return self.temp_list[self.position]  # 내가 갔던 곳으로
        #    else:
        #        if self.position == length - 1:
        #            print('chk2')
        #            if self.temp_list[self.position] == 0 or data % 2 == 1:
        #                return 1
        #            else:
        #                return 0
        #        else:
        #            print('chk3')
        #            return random.randint(0, 1)
        #return random.randint(0, 1)
    # ================================================================================= for glass_stepping_stones game


    # ================================================================================= for tug_of_war game
    def gathering_members(self):
        return (0, 0, 5, 5)

    def act_tugging_strategy(self, playground_tug_of_war):
        if playground_tug_of_war.player_condition['Computer'] == False:
            if playground_tug_of_war.player_expression[self.name] in ['best', 'well']:
                return 15
            else:
                return 10
        else:
            if playground_tug_of_war.player_expression['Computer'] in ['best', 'well']:
                return 30
            else:
                if playground_tug_of_war.player_expression[self.name] in ['best', 'well']:
                    return 40 + random.randint(0, 3)
                else:
                    return random.randint(0, 3)
    # ================================================================================= for tug_of_war game