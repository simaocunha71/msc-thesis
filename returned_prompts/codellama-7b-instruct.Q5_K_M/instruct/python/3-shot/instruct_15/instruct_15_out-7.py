    """
    import requests
    import json

    def post_request(json_payload, server_url):
        response = requests.post(server_url, json=json_payload)
        response.raise_for_status()

        delete_url = f"{server_url}?id={json_payload['id']}"
        response = requests.delete(delete_url)
        response.raise_for_status()

        decoded_response = json.loads(response.text)
        if "status" in decoded_response and decoded_response["status"] == "ok":
            return decoded_response
        else:
            return None

    return post_request


def test_post_request(post_request):
    server_url = "http://test.com"
    json_payload = {"id": 1234, "name": "John"}

    response = post_request(json_payload, server_url)
    assert response["status"] == "ok"
    assert response["id"] == 1234
    assert response["name"] == "John"


def test_post_request_with_no_id(post_request):
    server_url = "http://test.com"
    json_payload = {"name": "John"}

    response = post_request(json_payload, server_url)
    assert response is None


def test_post_request_with_no_json_payload(post_request):
    server_url = "http://test.com"

    with pytest.raises(TypeError):
        post_request(None, server_url)
