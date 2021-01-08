from yatzy_refactorizado import Yatzy
import pytest

# test_chance_scores_sum_of_all_dice  to test_chance
def test_chance():

    assert 15 == Yatzy.chance(1,2,3,4,5)
    assert 14 == Yatzy.chance(1,1,3,3,6)
    assert 22 == Yatzy.chance(5,5,5,6,1)
    assert 18 == Yatzy.chance(5,4,5,1,3)
    assert 19 == Yatzy.chance(6,5,4,1,3)
    assert 17 == Yatzy.chance(2,3,6,5,1)
    assert 16 == Yatzy.chance(1,2,2,5,6)
    assert 23 == Yatzy.chance(6,4,2,5,6)
    assert 28 == Yatzy.chance(5,5,6,6,6)
    assert 21 == Yatzy.chance(6,5,1,3,6)

# test_yatzy_scores_50 to test_yatzy
def test_yatzy():

    assert 50 == Yatzy.yatzy(1,1,1,1,1)
    assert 0 == Yatzy.yatzy(1,1,3,2,2)
    assert 50 == Yatzy.yatzy(2,2,2,2,2)
    assert 0 == Yatzy.yatzy(6,6,6,6,3)
    assert 50 == Yatzy.yatzy(3,3,3,3,3)
    assert 0 == Yatzy.yatzy(4,4,3,5,1)
    assert 50 == Yatzy.yatzy(4,4,4,4,4)
    assert 0 == Yatzy.yatzy(1,2,3,4,5)
    assert 50 == Yatzy.yatzy(5,5,5,5,5)
    assert 0 == Yatzy.yatzy(2,3,4,5,6)
    assert 50 == Yatzy.yatzy(6,6,6,6,6)

# ones to test_ones
def test_ones():

    assert 1 == Yatzy.ones(1,2,3,4,5)
    assert 2 == Yatzy.ones(1,1,2,3,4)
    assert 0 == Yatzy.ones(2,3,4,5,6)
    assert 3 == Yatzy.ones(5,4,1,1,1)
    assert 4 == Yatzy.ones(1,1,1,1,5)
    assert 0 == Yatzy.ones(6,5,4,3,2)
    assert 5 == Yatzy.ones(1,1,1,1,1)
    assert 0 == Yatzy.ones(2,2,2,2,3)
    assert 0 == Yatzy.ones(2,2,5,5,4)
    assert 0 == Yatzy.ones(5,5,4,6,6)
  
# twos to test_twos
def test_twos():
    
    assert 2 == Yatzy.twos(1,2,3,4,5)
    assert 4 == Yatzy.twos(1,2,2,3,4)
    assert 0 == Yatzy.twos(1,3,4,5,6)
    assert 6 == Yatzy.twos(6,2,2,1,2)
    assert 8 == Yatzy.twos(4,2,2,2,2)
    assert 0 == Yatzy.twos(1,1,3,4,5)
    assert 10 == Yatzy.twos(2,2,2,2,2)
    assert 0 == Yatzy.twos(3,4,5,6,1)
    assert 0 == Yatzy.twos(1,1,1,1,1)
    assert 0 == Yatzy.twos(1,6,5,4,3)

#threes to test_threes
def test_threes():

    assert 3 == Yatzy.threes(1,2,3,4,5)
    assert 6 == Yatzy.threes(1,3,3,5,6)
    assert 0 == Yatzy.threes(1,2,4,5,6)
    assert 9 == Yatzy.threes(3,3,3,2,6)
    assert 12 == Yatzy.threes(1,3,3,3,3)
    assert 0 == Yatzy.threes(2,4,5,6,1)
    assert 15 == Yatzy.threes(3,3,3,3,3)
    assert 0 == Yatzy.threes(6,5,4,2,1)
    assert 0 == Yatzy.threes(4,2,1,6,5)
    assert 0 == Yatzy.threes(2,5,4,2,1)

# fours to test_fours  
def test_fours():

    assert 4 == Yatzy.fours(4,1,2,3,5)
    assert 8 == Yatzy.fours(4,4,2,1,1)
    assert 0 == Yatzy.fours(1,2,3,5,6)
    assert 12 == Yatzy.fours(4,4,4,5,5)
    assert 16 == Yatzy.fours(4,4,4,4,5)
    assert 0 == Yatzy.fours(2,3,5,3,2)
    assert 20 == Yatzy.fours(4,4,4,4,4)
    assert 0 == Yatzy.fours(1,1,1,1,1)
    assert 0 == Yatzy.fours(6,6,2,2,5)
    assert 0 == Yatzy.fours(3,5,6,1,2)

#fives to test_fives
def test_fives():

    assert 5 == Yatzy.fives(3,2,4,5,1)
    assert 10 == Yatzy.fives(1,2,4,5,5)
    assert 0 == Yatzy.fives(1,1,1,1,1)
    assert 15 == Yatzy.fives(4,4,5,5,5)
    assert 20 == Yatzy.fives(6,5,5,5,5)
    assert 0 == Yatzy.fives(2,3,4,6,1)
    assert 25 == Yatzy.fives(5,5,5,5,5)
    assert 0 == Yatzy.fives(6,4,3,2,1)
    assert 0 == Yatzy.fives(1,3,6,3,1)
    assert 0 == Yatzy.fives(1,2,3,4,6)

#sixes to test_sixes
def test_sixes():

    assert 6 == Yatzy.sixes(6,1,1,1,2)
    assert 12 == Yatzy.sixes(4,4,6,6,5)
    assert 0 == Yatzy.sixes(1,3,4,5,5)
    assert 18 == Yatzy.sixes(6,3,6,6,2)
    assert 24 == Yatzy.sixes(3,6,6,6,6)
    assert 0 == Yatzy.sixes(1,2,3,4,5)
    assert 30 == Yatzy.sixes(6,6,6,6,6)
    assert 0 == Yatzy.sixes(2,3,4,5,1)
    assert 0 == Yatzy.sixes(5,5,5,4,4)
    assert 0 == Yatzy.sixes(4,4,5,5,1)

# score_pair to test_pair
def test_pair():

    assert 2 == Yatzy.pair(1,1,4,5,6)
    assert 4 == Yatzy.pair(2,5,2,6,1)
    assert 0 == Yatzy.pair(1,1,1,1,1)
    assert 6 == Yatzy.pair(4,2,1,3,3)
    assert 8 == Yatzy.pair(5,4,4,2,1)
    assert 0 == Yatzy.pair(2,2,2,5,3)
    assert 10 == Yatzy.pair(5,5,2,2,2)
    assert 12 == Yatzy.pair(1,3,2,6,6)
    assert 0 == Yatzy.pair(6,5,4,4,4)
    assert 0 == Yatzy.pair(1,2,3,4,5)

#two_pair to test_two_pair
def test_two_pair():
    
    assert 6 == Yatzy.two_pair(1,2,1,2,5)
    assert 0 == Yatzy.two_pair(1,1,1,1,1)
    assert 22 == Yatzy.two_pair(5,5,6,6,1)
    assert 0 == Yatzy.two_pair(1,2,3,4,5)
    assert 18 == Yatzy.two_pair(4,5,3,4,5)
    assert 0 == Yatzy.two_pair(5,4,3,2,1)
    assert 14 == Yatzy.two_pair(3,4,2,4,3)
    assert 0 == Yatzy.two_pair(2,3,4,5,6)
    assert 22 == Yatzy.two_pair(6,5,5,6,1)
    assert 0 == Yatzy.two_pair(6,5,4,3,2)

#three_of_a_kind to test_three_of_a_kind
def test_three_of_a_kind():

    assert 3 == Yatzy.three_of_a_kind(1,1,1,4,5)
    assert 6 == Yatzy.three_of_a_kind(3,8,2,2,2)
    assert 0 == Yatzy.three_of_a_kind(4,4,3,2,1)
    assert 9 == Yatzy.three_of_a_kind(7,3,1,3,3)
    assert 12 == Yatzy.three_of_a_kind(4,2,4,9,4)
    assert 0 == Yatzy.three_of_a_kind(6,5,1,1,2)
    assert 15 == Yatzy.three_of_a_kind(5,5,3,2,5)
    assert 18 == Yatzy.three_of_a_kind(6,3,2,6,6)
    assert 0 == Yatzy.three_of_a_kind(2,2,5,5,1)
    assert 0 == Yatzy.three_of_a_kind(1,1,5,2,2)
  
#four_of_a_kind to test_four_of_a_kind
def test_four_of_a_kind():

    assert 4 == Yatzy.four_of_a_kind(1,1,4,1,1)
    assert 8 == Yatzy.four_of_a_kind(2,2,2,6,2)
    assert 12 == Yatzy.four_of_a_kind(5,3,3,3,3)
    assert 16  == Yatzy.four_of_a_kind(4,4,4,2,4)
    assert 20 == Yatzy.four_of_a_kind(5,5,5,5,1)
    assert 24 == Yatzy.four_of_a_kind(6,3,6,6,6)
    assert 0  == Yatzy.four_of_a_kind(3,3,5,6,2)
    assert 0 == Yatzy.four_of_a_kind(4,3,2,1,5)
    assert 0  == Yatzy.four_of_a_kind(6,5,2,1,3)
    assert 0 == Yatzy.four_of_a_kind(1,3,4,5,2)

#smallStraight to test_smallStraight
def test_smallStraight():

    assert 15 == Yatzy.smallStraight(1,2,3,4,5)
    assert 0 == Yatzy.smallStraight(6,3,5,3,6)
    assert 0 == Yatzy.smallStraight(4,2,6,2,3)
    assert 0 == Yatzy.smallStraight(6,1,4,3,5)
    assert 0 == Yatzy.smallStraight(6,5,3,2,6)
    assert 0 == Yatzy.smallStraight(5,3,1,6,2)
    assert 0 == Yatzy.smallStraight(5,3,6,2,5)
    assert 0 == Yatzy.smallStraight(6,3,1,4,2)

#largeStraight to test_largeStraight
def test_largeStraight():

    assert 0 == Yatzy.largeStraight(1,2,3,4,5)
    assert 20 == Yatzy.largeStraight(2,3,4,5,6)
    assert 0 == Yatzy.largeStraight(1,2,2,4,5)
    assert 0 == Yatzy.largeStraight(6,4,5,4,1)
    assert 0 == Yatzy.largeStraight(6,2,3,4,2)
    assert 0 == Yatzy.largeStraight(5,4,3,2,1)
    assert 0 == Yatzy.largeStraight(6,5,4,3,2)
    assert 0 == Yatzy.largeStraight(6,1,3,4,5)
    assert 0 == Yatzy.largeStraight(3,4,2,1,3)
    assert 0 == Yatzy.largeStraight(1,1,4,3,2)
    assert 0 == Yatzy.largeStraight(5,4,3,2,4)

#fullHouse to test_fullHouse
def test_fullHouse():

    assert 7 == Yatzy.fullHouse(1,1,1,2,2)
    assert 0 == Yatzy.fullHouse(1,2,3,4,5)
    assert 22 == Yatzy.fullHouse(5,5,4,4,4)
    assert 0 == Yatzy.fullHouse(6,5,4,3,2)
    assert 19 == Yatzy.fullHouse(2,2,5,5,5)
    assert 0 == Yatzy.fullHouse(1,2,2,3,1)
    assert 17 == Yatzy.fullHouse(4,3,3,4,3)
    assert 0 == Yatzy.fullHouse(2,2,3,3,1)
    assert 26 == Yatzy.fullHouse(4,4,6,6,6)
    assert 0 == Yatzy.fullHouse(5,5,5,5,5)
