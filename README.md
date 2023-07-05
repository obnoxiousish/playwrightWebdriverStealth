# playwrightWebdriverStealth
Takes a playwright page object and adds a init JS script to hide the webdriver API from websites. This is probably the most common method of detecting playwright.

# Example

    from playwright_webdriver_stealth import add_stealth
    from playwright.sync_api import sync_playwright

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            channel='chrome',
            proxy={
                'server': f'http://{self.hostname}:{self.port}',
                'username': self.username,
                'password': self.password,
            },
            headless=False
        )

        context = browser.new_context()
        page = context.new_page()

        add_stealth(page)