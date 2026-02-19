import pytest
import pytest_asyncio
from playwright.async_api import async_playwright
import asyncio
import responses

@pytest.fixture(scope="session")
async def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def playwright_instance():
    async with async_playwright() as p:
        yield p

@pytest_asyncio.fixture(scope="function")
async def browser(playwright_instance):
    browser = await playwright_instance.chromium.launch(headless=False)
    page = await browser.new_page()
    await page.goto("http://localhost:3000")
    yield page
    await browser.close()

@pytest.fixture(scope="session")
def wiremock_url():
    return "http://localhost:8080"

@pytest.fixture
def mock_sip_invite():
    with responses.RequestsMock() as rsps:
        rsps.add(
            responses.POST,
            "http://localhost:8080/sip/invite",
            json={"status": "RINGING", "call_id": "123"},
            status=200
        )
        rsps.add(
            responses.POST,
            "http://localhost:8080/sip/ack",
            json={"status": "OK"},
            status=200
        )
        yield rsps
