import requests, csv, datetime

def fetch_orca_prices():
    urls = [
        "https://api.orca.so/v2/solana/whirlpool/list",
        "https://api.orca.so/v1/whirlpool/list"
    ]
    for url in urls:
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                data = r.json()
                pools = data.get("whirlpools", data)
                prices = {}
                for p in pools:
                    if isinstance(p, dict) and "tokenAName" in p and "tokenBName" in p and "price" in p:
                        prices[f"{p['tokenAName']}/{p['tokenBName']}"] = p["price"]
                print(f"[INFO] ✅ Orca OK — {len(prices)} pairs")
                return prices
        except Exception as e:
            print(f"[WARN] Orca fail: {url} → {e}")
    return {}

def fetch_raydium_prices():
    url = "https://api.raydium.io/v2/main/price"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            print(f"[INFO] ✅ Raydium OK — {len(data)} pools")
            return data
    except Exception as e:
        print(f"[WARN] Raydium fail → {e}")
    return {}

def log_combined_spreads():
    orca = fetch_orca_prices()
    ray = fetch_raydium_prices()
    ts = datetime.datetime.utcnow().isoformat()
    rows = []
    for k, v in orca.items():
        rows.append([ts, k, v, "ORCA"])
    for k, v in ray.items():
        rows.append([ts, k, v, "RAYDIUM"])
    with open("data/live_spread_log.csv", "a", newline="") as f:
        csv.writer(f).writerows(rows)
    print(f"[{ts}] ✅ Logged {len(orca)} Orca + {len(ray)} Raydium entries")

if __name__ == "__main__":
    log_combined_spreads()

