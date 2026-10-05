from playwright.sync_api import sync_playwright, expect


def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com")
        page.wait_for_timeout(2000)

        username = page.get_by_placeholder("Username")
        username.fill("standard_user")
        page.wait_for_timeout(1000)

        password = page.get_by_placeholder("Password")
        password.fill("secret_sauce")
        page.wait_for_timeout(1000)

        page.get_by_role("button", name="Login").click()
        page.wait_for_timeout(2000)

        expect(page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )

        page.wait_for_timeout(3000)

        browser.close()