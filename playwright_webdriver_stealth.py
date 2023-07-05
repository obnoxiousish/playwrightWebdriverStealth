scriptString = """
navigator.webdriver = false
Object.defineProperty(navigator, 'webdriver', {
get: () => false
})
"""

def add_stealth(page):
    page.add_init_script(scriptString)
    return True