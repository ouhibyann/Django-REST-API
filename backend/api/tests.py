import pytest
from django.urls import reverse


# Testing the endpoint
@pytest.mark.django_db
def test_view(client):
    url = reverse('')
    response = client.get(url)
    assert response.status_code == 200


# Testing if the admin page is unauthorized for 'regular' user
@pytest.mark.django_db
def test_unauthorized(client):
    url = reverse('admin/')
    response = client.get(url)
    assert response.status_code == 401


# Testing if the admin page is accessible for admin user
@pytest.mark.django_db
def test_superuser_view(admin_client):
    url = reverse('admin/')
    response = admin_client.get(url)
    assert response.status_code == 200

# Testing the GET and POST method should be provided soon