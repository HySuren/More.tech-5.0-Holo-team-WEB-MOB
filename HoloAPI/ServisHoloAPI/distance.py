import googlemaps

class DistanceMap():
    def geocode_address(location):
        google_maps_auth = googlemaps.Client(key='AIzaSyBhODlVQlOFPlh4K6MIB29D_fCGEl1ACq0')
        geocode_result = google_maps_auth.geocode(location)
        latitude = geocode_result[0]["geometry"]["location"]["lat"]
        longitude = geocode_result[0]["geometry"]["location"]["lng"]

        return (latitude, longitude)

distance_map = DistanceMap()