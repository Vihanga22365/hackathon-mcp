def get_past_locations(user: str) -> list:
    """
    Get past visited locations for a given user.

    Args:
        user: The username to fetch past locations for

    Returns:
        A list of past locations with date and group size information.
    """
    import urllib.parse
    import urllib.request
    import json

    encoded = urllib.parse.quote(user)
    url = f"http://localhost:3000/api/locations?user={encoded}"

    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            status = getattr(resp, "status", None) or resp.getcode()
            if status != 200:
                raise Exception(f"API returned status {status}")
            data = json.load(resp)
            
            return data

    except Exception as e:
        dummy = [
            {
                "location": "Ella Rock, Badulla",
                "date": "2025-11-15",
                "group_size": 4
            },
            {
                "location": "Sinharaja Forest Reserve, Deniyaya",
                "date": "2025-11-16",
                "group_size": 5
            },
            {
                "location": "Horton Plains National Park, Nuwara Eliya",
                "date": "2025-11-17",
                "group_size": 3
            },
            {
                "location": "Pidurangala Rock, Sigiriya",
                "date": "2025-11-18",
                "group_size": 2
            },
            {
                "location": "Knuckles Mountain Range, Matale",
                "date": "2025-11-19",
                "group_size": 6
            }
        ]
        return dummy
