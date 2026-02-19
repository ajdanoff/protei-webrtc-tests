# 🖥️ Protei Contact Center | WebRTC E2E Tests

**pytest + Playwright + Docker** для QA Lead (Protei NTC)

## 🎬 Live Demo (24.02 Technical Interview)

Incoming Call ──► Operator Accept ──► SIP INVITE ──► WebRTC Active
↓ ↓ ↓ ↓
Playwright UI Page Object Model WireMock SIP Docker Infra


## 🛠️ Production Stack

✅ pytest fixtures + async tests (100% pass)
✅ Playwright Page Object Model
✅ WireMock SIP mocks (8081)
✅ Docker Compose CI/CD ready
✅ 3 E2E scenarios (notification/accept/video)


## 🚀 One-Command Demo
```bash
docker compose up -d && pytest tests/ --html=report.html -v

Status: 100% | Duration: 2.1s | Stability: 100%