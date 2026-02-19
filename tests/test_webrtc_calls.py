# tests/test_webrtc_calls.py
import pytest
import asyncio
from playwright.async_api import async_playwright


@pytest.mark.smoke
@pytest.mark.asyncio
async def test_incoming_call_notification():
    """✅ Incoming call notification → Accept button"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        page = await browser.new_page()
        await page.goto("http://localhost:3000")

        # Точный селектор + английский текст
        call_notification = page.locator("#incoming-call")
        await call_notification.wait_for(state="visible", timeout=5000)

        assert await call_notification.is_visible()
        assert "Incoming WebRTC call" in await call_notification.inner_text()
        assert "client-123" in await call_notification.inner_text()

        # Accept button
        accept_btn = page.locator("[data-action='accept']")
        assert await accept_btn.is_visible()
        assert await accept_btn.inner_text() == "Accept"

        await browser.close()


@pytest.mark.smoke
@pytest.mark.asyncio
async def test_accept_call_workflow():
    """✅ Click Accept → video stream appears"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=1000)
        page = await browser.new_page()
        await page.goto("http://localhost:3000")

        # Accept call
        accept_btn = page.locator("[data-action='accept']")
        await accept_btn.click()

        # Verify video stream active
        video_stream = page.locator("#video-stream")
        await video_stream.wait_for(state="visible", timeout=3000)
        assert await video_stream.is_visible()
        assert await video_stream.get_attribute("data-streaming") == "true"

        await browser.close()
