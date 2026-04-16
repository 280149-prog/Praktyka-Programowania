from time import process_time_ns


class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        """Adding one point to player"""
        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    def equal_score(self):
        """Response to equal score"""
        return {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(self.p1points, "Deuce")

    def endgame_score(self):
        """Response to endgame score"""
        diff = self.p1points - self.p2points
        if diff == 1:
            return "Advantage player1"
        elif diff == -1:
            return "Advantage player2"
        elif diff >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def normal_score(self):
        """Normal score response"""
        score_names = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }
        return score_names[self.p1points] + "-" + score_names[self.p2points]

    def score(self):
        """Main score function"""
        if self.p1points == self.p2points:
            return self.equal_score()

        if self.p1points >= 4 or self.p2points >= 4:
            return self.endgame_score()

        return self.normal_score()

    # def score(self):
    #     result = ""
    #     temp_score = 0
    #     if self.p1points == self.p2points:
    #         result = {
    #             0: "Love-All",
    #             1: "Fifteen-All",
    #             2: "Thirty-All",
    #         }.get(self.p1points, "Deuce")
    #     elif self.p1points >= 4 or self.p2points >= 4:
    #         minus_result = self.p1points - self.p2points
    #         if minus_result == 1:
    #             result = "Advantage player1"
    #         elif minus_result == -1:
    #             result = "Advantage player2"
    #         elif minus_result >= 2:
    #             result = "Win for player1"
    #         else:
    #             result = "Win for player2"
    #     else:
    #         for i in range(1, 3):
    #             if i == 1:
    #                 temp_score = self.p1points
    #             else:
    #                 result += "-"
    #                 temp_score = self.p2points
    #             result += {
    #                 0: "Love",
    #                 1: "Fifteen",
    #                 2: "Thirty",
    #                 3: "Forty",
    #             }[temp_score]
    #     return result