from mlproject.distance import  haversine

def test_distance_haversine():
    lat1 = 20
    lat2 = 30
    lon1 = 10
    lon2 =30
    assert  type(haversine(lat1,lat2,lon1,lon2)) == float 