import pytest
from cities import *

import copy

def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    assert type(compute_total_distance(road_map1)) is float

    assert type(compute_total_distance(road_map1)) is not int

    assert type(compute_total_distance(road_map1)) is not str

    assert compute_total_distance(road_map1)==\
           pytest.approx(9.386+18.496+10.646, 0.01)

    assert compute_total_distance(road_map1) != 0

    assert 1 < compute_total_distance(road_map1) < 10000

    '''add your further tests'''

def test_swap_cities():
    road_map1 = [('Alabama', 'Montgomery', 32.361538, -86.279118),\
                 ('Alaska', 'Juneau', 58.301935, -134.41974),\
                 ('Arizona', 'Phoenix', 33.448457, -112.073844),\
                 ('Arkansas', 'Little Rock', 34.736009, -92.331122),\
                 ('California', 'Sacramento', 38.555605, -121.468926),\
                 ('Colorado', 'Denver', 39.7391667, -104.984167),\
                 ('Connecticut', 'Hartford', 41.767, -72.677),\
                 ('Delaware', 'Dover', 39.161921, -75.526755),\
                 ('Florida', 'Tallahassee', 30.4518, -84.27277)]

    road_map2 = copy.copy(road_map1)

    assert swap_cities(road_map1, 'Phoenix', 'Denver')==\
           ([('Alabama', 'Montgomery', 32.361538, -86.279118),\
             ('Alaska', 'Juneau', 58.301935, -134.41974),\
             ('Colorado', 'Denver', 39.7391667, -104.984167),\
             ('Arkansas', 'Little Rock', 34.736009, -92.331122),\
             ('California', 'Sacramento', 38.555605, -121.468926),\
             ('Arizona', 'Phoenix', 33.448457, -112.073844),\
             ('Connecticut', 'Hartford', 41.767, -72.677),\
             ('Delaware', 'Dover', 39.161921, -75.526755),\
             ('Florida', 'Tallahassee', 30.4518, -84.27277)], pytest.approx(202.411, 0.01))

    assert len(swap_cities(road_map1, 'Phoenix', 'Denver')) == 2

    assert len(swap_cities(road_map1, 'Phoenix', 'Denver')[0]) == len(road_map1)

    for i in range(0, len(road_map1) - 1):
        assert -90 <= swap_cities(road_map1, 'Phoenix', 'Denver')[0][i][2] <=90

    for i in range(0, len(road_map1) - 1):
        assert -180 <= swap_cities(road_map1, 'Phoenix', 'Denver')[0][i][2] <= 180

    assert swap_cities(road_map2, 'Little Rock', 'Little Rock')== \
           ([('Alabama', 'Montgomery', 32.361538, -86.279118),\
             ('Alaska', 'Juneau', 58.301935, -134.41974), \
             ('Arizona', 'Phoenix', 33.448457, -112.073844), \
             ('Arkansas', 'Little Rock', 34.736009, -92.331122), \
             ('California', 'Sacramento', 38.555605, -121.468926), \
             ('Colorado', 'Denver', 39.7391667, -104.984167), \
             ('Connecticut', 'Hartford', 41.767, -72.677), \
             ('Delaware', 'Dover', 39.161921, -75.526755), \
             ('Florida', 'Tallahassee', 30.4518, -84.27277)], pytest.approx(205.15, 0.01))


    '''add your tests'''
    # add tests for if indexes equal

def test_shift_cities():
    road_map1 = [('Alabama', 'Montgomery', 32.361538, -86.279118),\
                 ('Alaska', 'Juneau', 58.301935, -134.41974),\
                 ('Arizona', 'Phoenix', 33.448457, -112.073844),\
                 ('Arkansas', 'Little Rock', 34.736009, -92.331122),\
                 ('California', 'Sacramento', 38.555605, -121.468926),\
                 ('Colorado', 'Denver', 39.7391667, -104.984167),\
                 ('Connecticut', 'Hartford', 41.767, -72.677),\
                 ('Delaware', 'Dover', 39.161921, -75.526755),\
                 ('Florida', 'Tallahassee', 30.4518, -84.27277)]
    assert shift_cities(road_map1)== \
           [('Florida', 'Tallahassee', 30.4518, -84.27277), \
            ('Alabama', 'Montgomery', 32.361538, -86.279118),\
            ('Alaska', 'Juneau', 58.301935, -134.41974), \
            ('Arizona', 'Phoenix', 33.448457, -112.073844), \
            ('Arkansas', 'Little Rock', 34.736009, -92.331122), \
            ('California', 'Sacramento', 38.555605, -121.468926), \
            ('Colorado', 'Denver', 39.7391667, -104.984167), \
            ('Connecticut', 'Hartford', 41.767, -72.677), \
            ('Delaware', 'Dover', 39.161921, -75.526755)]
    assert len(shift_cities(road_map1)) == len(road_map1)
    '''add your tests'''


