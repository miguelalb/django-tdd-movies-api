import json

import pytest
from rest_framework import status

from movies.models import Movie


@pytest.mark.django_db
def test_add_movie(client):
    """Test adding a movie."""
    movies = Movie.objects.all()
    assert len(movies) == 0

    resp = client.post(
        '/api/movies/',
        {
            'title': 'The Big Lebowski',
            'genre': 'comedy',
            'year': '1998',
        },
        content_type='application/json'
    )
    assert resp.status_code == status.HTTP_201_CREATED
    assert resp.data['title'] == 'The Big Lebowski'

    movies = Movie.objects.all()
    assert len(movies) == 1
