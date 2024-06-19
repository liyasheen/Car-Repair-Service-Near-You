import re
from playwright.sync_api import Page, expect

#Tests that the homepage is rendered
def test_renders_homepage(page: Page):
    page.goto("http://localhost:3000")
    expect(page.get_by_text("Search for your local repair...")).to_be_visible()

# Tests that the search results are displayed with the correct critera
def test_get_search_results(page: Page):
    page.goto("http://localhost:3000/")
    page.locator("div").filter(has_text=re.compile(r"^Select CityLondonBirminghamManchesterYorkLeedsCoventry$")).get_by_role("combobox").select_option("London")
    page.locator("div").filter(has_text=re.compile(r"^Select CarBMWMercedesVolvoJeepRange RoverFordLexus$")).get_by_role("combobox").select_option("BMW")
    page.get_by_role("button", name="Search").click()
    expect(page.get_by_text("Search results for BMW services in London")).to_be_visible()

# Tests that the user can filter search results and then open a more indepth view of the repair service
def test_repair_service_information(page:Page):
    page.goto("http://localhost:3000/")
    page.locator("div").filter(has_text=re.compile(r"^Select CityLondonBirminghamManchesterYorkLeedsCoventry$")).get_by_role("combobox").select_option("London")
    page.locator("div").filter(has_text=re.compile(r"^Select CarBMWMercedesVolvoJeepRange RoverFordLexus$")).get_by_role("combobox").select_option("BMW")
    page.get_by_role("button", name="Search").click()
    page.locator("label").filter(has_text=re.compile(r"^££$")).locator("span").first.click()
    page.locator("[id=\"\\31 \"]").click()
    expect(page.get_by_text("London Auto Clinic")).to_be_visible()

# tests the button takes you to "My Account" page
def test_my_account_page(page:Page):
    page.goto("http://localhost:3000/")
    page.get_by_role("button").nth(1).click()
    expect(page).to_have_url(re.compile("http://localhost:3000/account"))
    expect(page.get_by_text("My Account")).to_be_visible()

# tests the button takes you to the "My Bookings" page
def test_my_bookings_page(page:Page):
    page.goto("http://localhost:3000/")
    page.get_by_role("button").nth(0).click()
    expect(page).to_have_url(re.compile("http://localhost:3000/bookings"))
    expect(page.get_by_text("My Bookings")).to_be_visible()

# tests the user is able to create a booking and see the booking confirmation page
def test_make_booking (page:Page):
    page.goto("http://localhost:3000/")
    page.locator("div").filter(has_text=re.compile(r"^Select CityLondonBirminghamManchesterYorkLeedsCoventry$")).get_by_role("combobox").select_option("London")
    page.locator("div").filter(has_text=re.compile(r"^Select CarBMWMercedesVolvoJeepRange RoverFordLexus$")).get_by_role("combobox").select_option("BMW")
    page.get_by_role("button", name="Search").click()
    page.locator("[id=\"\\31 \"]").click()
    page.locator("input[type=\"date\"]").fill("2024-06-23")
    page.locator("input[type=\"time\"]").click()
    page.locator("input[type=\"time\"]").fill("10:00")
    page.get_by_role("button", name="MOT £").click()
    page.get_by_role("button", name="Confirm Booking").click()
    expect(page.get_by_text("Booking Confirmed")).to_be_visible()

# tests the user is able to cancel their bookings
def test_cancel_booking (page:Page):
    page.goto("http://localhost:3000/")
    page.get_by_role("button").nth(0).click()
    page.get_by_role("button", name="Upcoming Bookings").click()
    page.get_by_role("button", name="Cancel Booking").nth(0).click()
    expect(page.get_by_text("No upcoming bookings")).to_be_visible()
    

