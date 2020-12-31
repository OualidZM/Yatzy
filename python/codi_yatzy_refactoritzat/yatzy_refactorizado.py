class Yatzy:

    @staticmethod
    def chance(*dice):
        points = 0
        for i in dice:
            points += i
        return points

    @staticmethod
    def yatzy(*dice):
        for i in dice[1:]:
            if i != dice[0]:
                return 0
        else:
            if i == dice[0]:
                return 50
        
    @staticmethod
    def ones(*dice):
        points = 0
        for i in dice:
            if i == 1:
                points += 1
        return points

    @staticmethod
    def twos(*dice):
        points = 0
        for i in dice:
            if i == 2:
                points += 2
        return points
    
    @staticmethod
    def threes(*dice):
        points = 0
        for i in dice:
            if i == 3:
                points += 3
        return points

    @staticmethod
    def fours(*dice):
        points = 0
        for i in dice:
            if i == 4:
                points += 4
        return points
    
    @staticmethod
    def fives(*dice):
        points = 0
        for i in dice:
            if i == 5:
                points += 5
        return points
    
    @staticmethod
    def sixes(*dice):
        points = 0
        for i in dice:
            if i == 6:
                points += 6
        return points

    @staticmethod
    def pair(*dice):
        pair = 2
        for i in range(6, 0, -1):
            if dice.count(i) == pair:
                return pair * i
        else:
            return 0

    @staticmethod
    def two_pair(*dice):
        contador = 0
        pair = 2
        listt = []
        while contador < 4:
            for i in dice:
                countt = dice.count(i) == pair
                if countt:
                    listt.append(i)
                    contador +=1
            if contador == 4:
                return sum(listt)
            else:
                return 0

    @staticmethod
    def three_of_a_kind(*dice):
        three = 3
        for i in range(6, 0, -1):
            if dice.count(i) == three:
                return three * i
        else:
            return 0

    @staticmethod
    def four_of_a_kind(*dice):
        four = 4
        for i in range(6, 0, -1):
            if dice.count(i) == four:
                return four * i
        else:
            return 0

    @staticmethod
    def smallStraight(*dice):
        for i in range(len(dice)-1):
            number = dice[i]
            next_number = dice[i+1]
            if number <= next_number:
                return 15
            else:
                return 0

    @staticmethod
    def largeStraight(*dice):
        # for i in dice:
        sor = sorted(dice) == dice
        sor_chk = sor == True
        first = dice[0] == 2
        first_check = first == True
        if sor_chk == sor and first_check == True:
            return 20
        else:
            # first_check == True or first_check == False and sor_chk == False
            if first_check == True and sor_chk == False or first_check == False and sor_chk == False:
                return 0 

    @staticmethod
    def fullHouse(*dice):
        contador = 0
        pair = 2
        three = 3
        # num_rep = 2
        listt = []
        while contador < 5:
            for i in dice:
                count_pair = dice.count(i) == pair
                count_three = dice.count(i) == three
                if count_pair or count_three:
                    listt.append(i)
                    contador +=1
            if contador == 5:
                return sum(listt)
                # pair * i
            else:
                return 0 