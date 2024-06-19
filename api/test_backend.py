# tests/test_list.py
import requests

def test_list():
    response = requests.get("http://127.0.0.1:5000/list")
    assert response.status_code == 200
    services = response.json()
    assert isinstance(services, dict)

def test_getbyid():
    service_id = "1"  
    response = requests.get(f"http://127.0.0.1:5000/getbyid/{service_id}")
    assert response.status_code == 200
    service = response.json()
    assert service["id"] == service_id

def test_filter():
    payload = {
        "location": "London", 
        "price": ["£", "££"],
        "stars": [3, 4]
    }
    response = requests.post("http://127.0.0.1:5000/filter", json=payload)
    assert response.status_code == 200
    filtered_services = response.json()
    assert isinstance(filtered_services, dict)
    assert "services" in filtered_services
    assert all(service["location"] == "London" for service in filtered_services["services"])
    assert all(service["stars"] == 3 or service["stars"] == 4 for service in filtered_services["services"])
    assert all(service["price"] == "£" or service["price"] == "££" for service in filtered_services["services"])

def test_add():
    payload = {
    "serviceData": {
        "address": "456 Regent Street, London, W1B 2BB",
        "distance": 2.3,
        "email": "citymotors@yahoo.com",
        "id": "2",
        "location": "London",
        "logo": "services/three.png",
        "name": "City Motors",
        "phone": "07770002222",
        "price": "£££",
        "stars": 4
    },
    "bookingId": "2024-06-1918:06Brake Pad Replacement",
    "date": "2024-06-19",
    "repair": "Brake Pad Replacement",
    "cost": 750,
    "time": "18:06"
}
    response = requests.post("http://127.0.0.1:5000/add", json=payload)
    assert response.status_code == 200
    booking_id = response.json()
    assert booking_id == payload["bookingId"]

def test_getbookingbyid():
    booking_id = "2024-06-1918:06Brake Pad Replacement"
    response = requests.get(f"http://127.0.0.1:5000/getbookingbyid/{booking_id}")
    assert response.status_code == 200
    booking = response.json()
    assert booking["bookingId"] == booking_id

def test_getbookings():
    response = requests.get("http://127.0.0.1:5000/getbookings")
    assert response.status_code == 200
    bookings = response.json()
    assert isinstance(bookings, list)

def test_update():
    booking_id = "2024-06-1918:06Brake Pad Replacement" 
    payload ={
    "serviceData": {
        "address": "456 Regent Street, London, W1B 2BB",
        "distance": 2.3,
        "email": "citymotors@yahoo.com",
        "id": "2",
        "location": "London",
        "logo": "services/three.png",
        "name": "City Motors",
        "phone": "07770002222",
        "price": "£££",
        "stars": 4
    },
    "bookingId": "2024-06-1918:06Brake Pad Replacement",
    "date": "2024-06-20",
    "repair": "Oil Change",
    "cost": 100,
    "time": "16:00"
}
    response = requests.post(f"http://127.0.0.1:5000/update/{booking_id}", json=payload)
    assert response.status_code == 200
    updated_booking = response.json()
    assert (booking["date"] == "2024-06-20" for booking in updated_booking)
    assert (booking["time"] == "16:00" for booking in updated_booking)
    assert (booking["repair"] == "Oil Change" for booking in updated_booking)

def test_remove():
    booking_id = "2024-06-1918:06Brake Pad Replacement" 
    response = requests.post(f"http://127.0.0.1:5000/remove/{booking_id}")
    assert response.status_code == 200
    bookings = response.json()
    assert all(booking["bookingId"] != booking_id for booking in bookings)
