from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    register_button = page.get_by_test_id("registration-page-registration-button")
    expect(register_button).to_be_disabled()

    register_email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    register_email_input.fill("user.name@gmail.com")

    register_username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    register_username_input.fill("username")

    register_password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    register_password_input.fill("password")

    expect(register_button).not_to_be_disabled()

    page.wait_for_timeout(2000)
