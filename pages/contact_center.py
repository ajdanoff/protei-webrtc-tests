from playwright.async_api import Page


class ContactCenterPage:
    def __init__(self, page: Page):
        self.page = page

    async def wait_for_call_notification(self, call_id: str, timeout=10000):
        await self.page.wait_for_selector(f"[data-call-id='{call_id}']", timeout=timeout)

    async def accept_call(self, call_id: str):
        await self.page.click(f"[data-call-id='{call_id}'] [data-action='accept']")
        await self.page.wait_for_selector(".webrtc-connected")

    async def is_video_stream_active(self, call_id: str) -> bool:
        stream_element = self.page.locator(f"#video-{call_id}")
        return await stream_element.is_visible() and await stream_element.get_attribute("data-streaming") == "true"

    async def get_call_duration(self, call_id: str) -> int:
        duration = await self.page.locator(f"[data-call-id='{call_id}'] .duration").inner_text()
        return int(duration.replace("s", ""))

    async def error_notification(self) -> str:
        return await self.page.locator(".error-alert").inner_text()
