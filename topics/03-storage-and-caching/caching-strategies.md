# Caching Strategies & Eviction Policies

Caching stores copies of frequently accessed data in high-speed storage (e.g., Redis, Memcached, RAM) to reduce latency and database load.

---

## 1. Caching Patterns

### Cache-Aside (Lazy Loading)
- Application looks in cache first.
- If cache hit: return cached data.
- If cache miss: read from DB, populate cache, return data.
- **Pros**: Only requested data is cached; resilient to node failure.
- **Cons**: Cache miss penalty; possibility of stale data if DB is updated directly.

### Write-Through
- Application writes to the cache; cache synchronously writes to DB before returning success.
- **Pros**: Data in cache is always up-to-date and consistent with DB.
- **Cons**: Higher write latency due to two writes.

### Write-Behind (Write-Back)
- Application writes to the cache immediately; cache asynchronously writes batches to DB.
- **Pros**: Maximum write speed; absorbs heavy write bursts.
- **Cons**: Risk of data loss if cache fails before flushing to DB.

### Refresh-Ahead
- Cache proactively refreshes keys nearing expiration based on predicted access patterns.

---

## 2. Eviction Policies

- **LRU (Least Recently Used)**: Discards items not accessed for the longest time.
- **LFU (Least Frequently Used)**: Discards items with the lowest access count.
- **FIFO (First In, First Out)**: Evicts oldest cached items regardless of access frequency.
