from movies.serializers import MovieSerializer

def test_valid_movie_serializer():
    """Test movie serializer validate data correctly"""
    valid_serializer_data = {
        'title': 'Raising Arizona',
        'genre': 'comedy',
        'year': '1987'
    }
    serializer = MovieSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_movie_serializer():
    """Test movie serializer catches invalid data"""
    invalid_serializer_data = {
        'title': 'Raising Arizona',
        'genre': 'comedy'
    }
    serializer = MovieSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {'year': ['This field is required.']}
