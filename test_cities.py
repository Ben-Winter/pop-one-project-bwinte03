import pytest
from cities import *

import copy

def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    assert type(compute_total_distance(road_map1)) is float
    assert compute_total_distance(road_map1) > 0
    assert compute_total_distance(road_map1)==\
           pytest.approx(9.386+18.496+10.646, 0.01)

    road_map2 = [('Connecticut', 'Hartford', 41.767, -72.677), \
                 ('Delaware', 'Dover', 39.161921, -75.526755), \
                 ('Florida', 'Tallahassee', 30.4518, -84.27277)]
    assert type(compute_total_distance(road_map2)) is float
    assert compute_total_distance(road_map2) > 0
    assert compute_total_distance(road_map2)==\
           pytest.approx(3.861+12.343+16.202, 0.01)

    road_map3 = [('Alaska', 'Juneau', 58.301935, -134.41974), \
                 ('Arizona', 'Phoenix', 33.448457, -112.073844), \
                 ('California', 'Sacramento', 38.555605, -121.468926)]
    assert type(compute_total_distance(road_map3)) is float
    assert compute_total_distance(road_map3) > 0
    assert compute_total_distance(road_map3)==\
           pytest.approx(33.422+10.693+23.614, 0.01)

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
    road_map3 = copy.copy(road_map1)
    road_map4 = copy.copy(road_map1)
    road_map5 = copy.copy(road_map1)

    # Test swap cities within list
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

    # Test swap cities within list - indices reversed
    assert swap_cities(road_map2, 'Denver', 'Phoenix')==\
            ([('Alabama', 'Montgomery', 32.361538, -86.279118), \
              ('Alaska', 'Juneau', 58.301935, -134.41974), \
              ('Colorado', 'Denver', 39.7391667, -104.984167), \
              ('Arkansas', 'Little Rock', 34.736009, -92.331122), \
              ('California', 'Sacramento', 38.555605, -121.468926), \
              ('Arizona', 'Phoenix', 33.448457, -112.073844), \
              ('Connecticut', 'Hartford', 41.767, -72.677), \
              ('Delaware', 'Dover', 39.161921, -75.526755), \
              ('Florida', 'Tallahassee', 30.4518, -84.27277)], pytest.approx(202.411, 0.01))

    # Test swap first and last
    assert swap_cities(road_map3, 'Montgomery', 'Tallahassee')== \
           ([('Florida', 'Tallahassee', 30.4518, -84.27277), \
             ('Alaska', 'Juneau', 58.301935, -134.41974), \
             ('Arizona', 'Phoenix', 33.448457, -112.073844), \
             ('Arkansas', 'Little Rock', 34.736009, -92.331122), \
             ('California', 'Sacramento', 38.555605, -121.468926), \
             ('Colorado', 'Denver', 39.7391667, -104.984167), \
             ('Connecticut', 'Hartford', 41.767, -72.677), \
             ('Delaware', 'Dover', 39.161921, -75.526755), \
             ('Alabama', 'Montgomery', 32.361538, -86.279118)], pytest.approx(208.207, 0.01))

    # Test swap first and last - indices reversed
    assert swap_cities(road_map4, 'Tallahassee', 'Montgomery') == \
           ([('Florida', 'Tallahassee', 30.4518, -84.27277), \
             ('Alaska', 'Juneau', 58.301935, -134.41974), \
             ('Arizona', 'Phoenix', 33.448457, -112.073844), \
             ('Arkansas', 'Little Rock', 34.736009, -92.331122), \
             ('California', 'Sacramento', 38.555605, -121.468926), \
             ('Colorado', 'Denver', 39.7391667, -104.984167), \
             ('Connecticut', 'Hartford', 41.767, -72.677), \
             ('Delaware', 'Dover', 39.161921, -75.526755), \
             ('Alabama', 'Montgomery', 32.361538, -86.279118)], pytest.approx(208.207, 0.01))

    #Test if indices are the same - test 1
    assert swap_cities(road_map5, 'Little Rock', 'Little Rock')== \
           ([('Alabama', 'Montgomery', 32.361538, -86.279118),\
             ('Alaska', 'Juneau', 58.301935, -134.41974), \
             ('Arizona', 'Phoenix', 33.448457, -112.073844), \
             ('Arkansas', 'Little Rock', 34.736009, -92.331122), \
             ('California', 'Sacramento', 38.555605, -121.468926), \
             ('Colorado', 'Denver', 39.7391667, -104.984167), \
             ('Connecticut', 'Hartford', 41.767, -72.677), \
             ('Delaware', 'Dover', 39.161921, -75.526755), \
             ('Florida', 'Tallahassee', 30.4518, -84.27277)], pytest.approx(205.15, 0.01))

    # Test if indices are the same - test 2
    assert swap_cities(road_map5, 'Dover', 'Dover')== \
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

def test_shift_cities():
    road_map1 = [('Alabama', 'Montgomery', 32.361538, -86.279118), \
                 ('Alaska', 'Juneau', 58.301935, -134.41974), \
                 ('Arizona', 'Phoenix', 33.448457, -112.073844), \
                 ('Arkansas', 'Little Rock', 34.736009, -92.331122), \
                 ('California', 'Sacramento', 38.555605, -121.468926), \
                 ('Colorado', 'Denver', 39.7391667, -104.984167), \
                 ('Connecticut', 'Hartford', 41.767, -72.677), \
                 ('Delaware', 'Dover', 39.161921, -75.526755), \
                 ('Florida', 'Tallahassee', 30.4518, -84.27277)]

    # Test shift 1
    assert shift_cities(road_map1)== \
           [('Florida', 'Tallahassee', 30.4518, -84.27277), \
            ('Alabama', 'Montgomery', 32.361538, -86.279118), \
            ('Alaska', 'Juneau', 58.301935, -134.41974), \
            ('Arizona', 'Phoenix', 33.448457, -112.073844), \
            ('Arkansas', 'Little Rock', 34.736009, -92.331122), \
            ('California', 'Sacramento', 38.555605, -121.468926), \
            ('Colorado', 'Denver', 39.7391667, -104.984167), \
            ('Connecticut', 'Hartford', 41.767, -72.677), \
            ('Delaware', 'Dover', 39.161921, -75.526755)]

    # Test shift 2
    assert shift_cities(road_map1)== \
           [('Delaware', 'Dover', 39.161921, -75.526755), \
            ('Florida', 'Tallahassee', 30.4518, -84.27277), \
            ('Alabama', 'Montgomery', 32.361538, -86.279118), \
            ('Alaska', 'Juneau', 58.301935, -134.41974), \
            ('Arizona', 'Phoenix', 33.448457, -112.073844), \
            ('Arkansas', 'Little Rock', 34.736009, -92.331122), \
            ('California', 'Sacramento', 38.555605, -121.468926), \
            ('Colorado', 'Denver', 39.7391667, -104.984167), \
            ('Connecticut', 'Hartford', 41.767, -72.677)]

    # Test shift 3
    assert shift_cities(road_map1)== \
           [('Connecticut', 'Hartford', 41.767, -72.677), \
            ('Delaware', 'Dover', 39.161921, -75.526755), \
            ('Florida', 'Tallahassee', 30.4518, -84.27277), \
            ('Alabama', 'Montgomery', 32.361538, -86.279118),\
            ('Alaska', 'Juneau', 58.301935, -134.41974), \
            ('Arizona', 'Phoenix', 33.448457, -112.073844), \
            ('Arkansas', 'Little Rock', 34.736009, -92.331122), \
            ('California', 'Sacramento', 38.555605, -121.468926), \
            ('Colorado', 'Denver', 39.7391667, -104.984167)]

    '''add your tests'''


