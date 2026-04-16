class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p_score(player_name)
        else:
            self.p_score(player_name)

    def score(self):
        result = ""
        if self.p1points == self.p2points:
            if self.p1points <3:
                if self.p1points == 0:
                    result = "Love"
                if self.p1points == 1:
                    result = "Fifteen"
                if self.p1points == 2:
                    result = "Thirty"
                result += "-All"
            else:
                result = "Deuce"

        p1res = ""
        p2res = ""
        if self.p1points > 0 and self.p2points == 0:
            if self.p1points == 1:
                p1res = "Fifteen"
            if self.p1points == 2:
                p1res = "Thirty"
            if self.p1points == 3:
                p1res = "Forty"
            p2res = "Love"
            result = p1res + "-" + p2res

        if self.p2points > 0 and self.p1points == 0:
            if self.p2points == 1:
                p2res = "Fifteen"
            if self.p2points == 2:
                p2res = "Thirty"
            if self.p2points == 3:
                p2res = "Forty"
            p1res = "Love"
            result = p1res + "-" + p2res

        if self.p1points > self.p2points and self.p1points < 4:
            if self.p1points == 2:
                p1res = "Thirty"
            if self.p1points == 3:
                p1res = "Forty"
            if self.p2points == 1:
                p2res = "Fifteen"
            if self.p2points == 2:
                p2res = "Thirty"
            result = p1res + "-" + p2res

        if self.p2points > self.p1points and self.p2points < 4:
            if self.p2points == 2:
                p2res = "Thirty"
            if self.p2points == 3:
                p2res = "Forty"
            if self.p1points == 1:
                p1res = "Fifteen"
            if self.p1points == 2:
                p1res = "Thirty"
            result = p1res + "-" + p2res

        if self.p1points > self.p2points and self.p2points >= 3:
            result = "Advantage player1"

        if self.p2points > self.p1points and self.p1points >= 3:
            result = "Advantage player2"

        if self.p1points >= 4 and (self.p1points - self.p2points) >= 2:
            result = "Win for player1"

        if self.p2points >= 4 and (self.p2points - self.p1points) >= 2:
            result = "Win for player2"
        return result

    # def set_p1_score(self, number):
    #     for i in range(number):
    #         self.p1_score()
    #
    # def set_p2_score(self, number):
    #     for i in range(number):
    #         self.p2_score()

    def p_score(self, name):
        if name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    def build_score(self, p1, p2):
        score_names = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }
        return score_names[p1] + "-" + score_names[p2]
    # def p1_score(self):
    #     self.p1points += 1
    #
    # def p2_score(self):
    #     self.p2points += 1
