import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.wikipedia.org/")
    page.get_by_role("searchbox", name="Search Wikipedia").click()
    page.get_by_role("searchbox", name="Search Wikipedia").fill("modern infrastructure")
    page.get_by_role("button", name="Search").click()
    page.get_by_role("link", name="Infrastructure", exact=True).first.click()
