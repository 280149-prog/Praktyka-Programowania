class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.p1_name = player1_name
        self.p2_name = player2_name
        self.p1score = 0
        self.p2score = 0

    def won_point(self, n):
        if n == self.p1_name:
            self.p1score += 1
        else:
            self.p2score += 1

    def score(self):
        if (self.p1score < 4 and self.p2score < 4) and (self.p1score + self.p2score < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            score = p[self.p1score]
            if self.p1score == self.p2score:
                return s + "-All"
            else:
                return s + "-" + p[self.p2score]
            #return s + "-All" if (self.p1score == self.p2score) else s + "-" + p[self.p2score]
        else:
            if self.p1score == self.p2score:
                return "Deuce"
            if self.p1score > self.p2score:
                score =self.p1_name
            else:
                score =self.p2_name
            #s = self.p1_name if self.p1score > self.p2score else self.p2_name
            if abs(self.p1score - self.p2score) == 1:
                return "Advantage " + score
            else:
                return "Win for " + score
            # return (
            #     "Advantage " + s
            #     if ((self.p1score - self.p2score) * (self.p1score - self.p2score) == 1)
            #     else "Win for " + s
            # )
