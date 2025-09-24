from flask import request, jsonify
from config import Config
import time

rate_limit_store = {}

RATE_LIMIT = Config.RATE_LIMIT       # requests
TIME_WINDOW = Config.TIME_WINDOW     # per 60 seconds

def rate_limiter():
    ip = request.remote_addr or "unknown"
    now = time.time()

    entry = rate_limit_store.get(ip, {"tokens": RATE_LIMIT, "last_refill": now})

    # refill tokens
    elapsed = now - entry["last_refill"]
    refill = (elapsed / TIME_WINDOW) * RATE_LIMIT
    entry["tokens"] = min(RATE_LIMIT, entry["tokens"] + refill)
    entry["last_refill"] = now

    # check tokens
    if entry["tokens"] < 1:
        retry_after = TIME_WINDOW - elapsed
        return True, jsonify({
            "error": "Too Many Requests",
            "retry_after": round(retry_after, 2)
        }), 429

    # consume token
    entry["tokens"] -= 1
    rate_limit_store[ip] = entry
    return False, None