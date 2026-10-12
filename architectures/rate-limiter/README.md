# Architecture Case Study: Distributed Rate Limiter

## 1. Requirements
- **Functional**: Limit requests to $N$ per minute per client IP or user ID. Return HTTP 429 (Too Many Requests) when exceeded.
- **Non-Functional**:
  - Extremely low latency ($< 5\text{ ms}$).
  - Minimal memory footprint.
  - High availability in distributed environments.

## 2. Common Algorithms
- **Token Bucket**: Allows burst traffic, refill tokens at constant rate.
- **Leaking Bucket**: Smooths out traffic spikes to fixed rate.
- **Fixed Window Counter**: Prone to double-limit traffic at window boundaries.
- **Sliding Window Log**: Highly accurate, but high memory usage.
- **Sliding Window Counter**: Balances accuracy and low memory usage.

## 3. Reference Implementation
See `rate_limiter.py` in this directory for working Python implementations of Token Bucket and Sliding Window Counter.
