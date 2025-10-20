# Solana Arbitrage & Adaptive Trading Framework

## Quickstart
- Create a Python 3.11 virtualenv and install project dependencies, including `fastapi`, `uvicorn`, `rich`, and `pandas`.
- Populate `.env` with operator credentials (`MAIN_WALLET`, `KEYPAIR_DIR`, API tokens) and confirm `DRY_RUN` mode before production.
- Run `python -m core.summary_dashboard` to verify trade logs and generate `logs/summary_latest.json`.
- Start the adaptive live loop with `python -m core.live_loop`; the auto-tuner and watchdog threads spin up automatically.
- Launch the local dashboard via `uvicorn web.dashboard_server:app --host 0.0.0.0 --port 8080 --reload` and open `http://localhost:8080/?token=<API_AUTH_KEY>`.

## Safety Notes
- Always execute `python -m core.pretrade_validator` before live trading to reclaim dangling nonce funds and confirm RPC health.
- Keep `DRY_RUN=True` until wallet balances, RPC endpoints, and Telegram alerts are fully validated.
- The auto-tuner enforces cooling-off pauses and can request controlled restarts; monitor `logs/system_health.log` for interventions.
- Dashboard controls persist to `logs/control_state.json`; confirm trading is enabled before expecting fills.
- Limit live orders to ≤0.05 SOL until profitability and fee dynamics are observed in production.

## Stage 16–20 Changelog
- **Stage 16** — Added `core/summary_dashboard.py` for Rich CLI analytics, JSON snapshots, and live-loop integration.
- **Stage 17** — Introduced `core/ai_signal_engine.py` with whale, DexScreener, and sentiment fusion plus mood-adjusted spread gating.
- **Stage 18** — Delivered `core/auto_tuner.py` for rolling success analysis, forced cooldowns, and RPC watchdog-driven restarts.
- **Stage 19** — Built `web/dashboard_server.py` FastAPI service with secured endpoints, Plotly UI, and trading toggles.
- **Stage 20** — Hardened deployment workflow, promoted `.env` defaults for mainnet, and tagged release `v2.0-Mainnet`.

## Verification Targets
- `logs/summary_latest.json` updates after every summary refresh.
- `logs/system_health.log` records auto-tuner adjustments and watchdog events.
- `logs/dashboard_server.log` tracks dashboard interactions and control changes.
- Use `python -m core.summary_dashboard` and `python -c "from core.ai_signal_engine import get_market_signal; print(get_market_signal(True))"` as smoke tests before mainnet engagement.
# solana-arb-framework
