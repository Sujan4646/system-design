"""
Rate Limiter Algorithms Implementation
- Token Bucket
- Sliding Window Counter
"""

import time
import threading
from collections import deque


class TokenBucketRateLimiter:
    """
    Token Bucket Rate Limiter
    Allows bursts up to capacity, refills at refill_rate tokens per second.
    """
    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = float(capacity)
        self.tokens = float(capacity)
        self.refill_rate = refill_rate
        self.last_refill = time.time()
        self.lock = threading.Lock()

    def allow_request(self, tokens: int = 1) -> bool:
        with self.lock:
            now = time.time()
            elapsed = now - self.last_refill
            self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
            self.last_refill = now

            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False


class SlidingWindowLogRateLimiter:
    """
    Sliding Window Log Rate Limiter
    Maintains timestamps of requests within window_seconds.
    """
    def __init__(self, max_requests: int, window_seconds: float):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = deque()
        self.lock = threading.Lock()

    def allow_request(self) -> bool:
        with self.lock:
            now = time.time()
            cutoff = now - self.window_seconds

            while self.requests and self.requests[0] <= cutoff:
                self.requests.popleft()

            if len(self.requests) < self.max_requests:
                self.requests.append(now)
                return True
            return False


if __name__ == "__main__":
    print("Testing TokenBucketRateLimiter (Capacity: 3, Refill: 1 token/sec):")
    limiter = TokenBucketRateLimiter(capacity=3, refill_rate=1.0)
    for i in range(5):
        allowed = limiter.allow_request()
        print(f"Request {i + 1}: {'ALLOWED' if allowed else 'DENIED (429)'}")

    time.sleep(1.1)
    print("\nAfter waiting 1.1s (1 token refilled):")
    print(f"Request 6: {'ALLOWED' if limiter.allow_request() else 'DENIED (429)'}")
