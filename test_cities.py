import pytest
from cities import *


def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    assert compute_total_distance(road_map1)==\
           pytest.approx(9.386+18.496+10.646, 0.01)

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
    index1 = 2
    index2 = 5
    assert swap_cities(road_map1, index1, index2)==\
           ([('Alabama', 'Montgomery', 32.361538, -86.279118),\
             ('Alaska', 'Juneau', 58.301935, -134.41974),\
             ('Colorado', 'Denver', 39.7391667, -104.984167),\
             ('Arkansas', 'Little Rock', 34.736009, -92.331122),\
             ('California', 'Sacramento', 38.555605, -121.468926),\
             ('Arizona', 'Phoenix', 33.448457, -112.073844),\
             ('Connecticut', 'Hartford', 41.767, -72.677),\
             ('Delaware', 'Dover', 39.161921, -75.526755),\
             ('Florida', 'Tallahassee', 30.4518, -84.27277)], pytest.approx(202.411, 0.01))
    '''add your tests'''
    # add tests for if indexes equal

def test_shift_cities():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    assert shift_cities(road_map1)== \
           [("Minnesota", "Saint Paul", 44.95, -93.094),\
            ("Delaware", "Dover", 39.161921, -75.526755), \
            ("Kentucky", "Frankfort", 38.197274, -84.86311)]
    '''add your tests'''


