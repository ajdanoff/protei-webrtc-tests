import pytest
import asyncio
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_contact_center_loads():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("http://localhost:3000")
        assert await page.title() != ""
        await browser.close()