from playwright.sync_api import sync_playwright
import data

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        email = data.email()
        password = data.password()
        browser = browser_type.launch()
        print(browser_type.name, 'test started')
        page = browser.new_page(locale='en-GB')
        page.goto("")
        # Login
        page.click('text=Log in')
        page.type("input[name='email']", email)
        page.type("input[name='password']", password)
        page.click('text=Log in')
        page.wait_for_timeout(3000)
        # Log out
        page.click("xpath=//*[@id='root']/div[2]/div/div/div[2]/div[4]/span/button")
        page.click('text=Log out')
        # Check log out
        user = page.evaluate('() => window.localStorage.getItem("cyber/user/AUTH")')
        if user is None:
            print('User is log out')
        print('Test success')
        browser.close()
    print('All tests success')