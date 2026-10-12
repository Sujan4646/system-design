# Architecture Case Study: Scalable URL Shortener (TinyURL)

## 1. Requirements
- **Functional**:
  - Given a long URL, generate a short 7-character URL.
  - Redirect short URL to the original long URL with HTTP 301 or 302.
  - Custom alias support (optional).
  - URLs expire after a configurable TTL (e.g., 2 years).
- **Non-Functional**:
  - High availability (99.99%).
  - Real-time redirection with $< 10\text{ ms}$ latency.
  - Read-heavy traffic (typically 100:1 read-to-write ratio).

## 2. Key Generation Strategies
1. **Base62 Encoding on Auto-Increment Counter / Snowflake ID**:
   - $62^7 \approx 3.5 \text{ trillion}$ unique URLs.
   - Deterministic and collision-free.
2. **MD5 / Murmur3 Hash + Collision Resolution**:
   - Hash long URL, take first 7 chars. If collision exists, append salt and rehash.
3. **Key Generation Service (KGS)**:
   - Standalone service pre-generates random 7-character Base62 keys and stores them in DB/memory. Fast $O(1)$ key allocation.

## 3. Reference Implementation
See `url_shortener.py` for a working implementation of Base62 encoding and in-memory key generation service.
