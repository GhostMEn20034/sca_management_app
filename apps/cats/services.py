import requests


def is_breed_valid(breed_name: str) -> bool:
    """
    Validates a breed name using The Cat API.
    :param breed_name: The name of the breed to validate.

    :returns: True if the breed is valid, False otherwise.
    """
    try:
        response = requests.get("https://api.thecatapi.com/v1/breeds")
        breeds = set(breed["name"] for breed in response.json())
        return breed_name in breeds
    except requests.RequestException:
        return False
